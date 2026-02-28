---
name: debugging-with-traces
description: Use this skill when analyzing error traces, stack traces, crash reports, or exception logs to identify root causes and suggest fixes. This includes debugging Sentry issues, interpreting Node.js/Python/Go stack traces, analyzing LangSmith execution traces, diagnosing unhandled promise rejections, memory leaks, timeout errors, and production incidents. Invoke when users share an error trace, paste a stack trace, show a Sentry issue, or describe a crash that needs root cause analysis.
---

# Debugging with Error Traces

Analyzes error traces, stack traces, and crash reports to identify root causes and produce actionable fixes.

## Input Formats Supported

- **Sentry issues** — paste the issue URL or full event JSON
- **Node.js stack traces** — `Error: ... at Object.<anonymous> (file.js:42:10)`
- **Python tracebacks** — `Traceback (most recent call last): ...`
- **Go panic output** — `goroutine 1 [running]: ...`
- **LangSmith traces** — execution JSON from the langsmith-fetch skill
- **Browser console errors** — including minified traces with sourcemaps
- **Docker/container logs** — log lines with timestamps and container IDs

---

## Workflow

### Step 1: Parse the Trace

Identify:
1. **Error type** — `TypeError`, `SegmentationFault`, `HTTPError`, `TimeoutError`, etc.
2. **Error message** — the human-readable description
3. **Origin frame** — the *first* frame in YOUR code (not node_modules, not runtime internals)
4. **Call chain** — what sequence of calls led to the error

```bash
# For Node.js traces with source maps
npx source-map-explorer dist/bundle.js

# For minified browser errors, find the source map
curl https://app.example.com/static/js/main.abc123.js.map > main.js.map
```

### Step 2: Locate the Origin Frame

The most important frame is the **first frame in application code** (skip library internals):

```
Error: Cannot read properties of undefined (reading 'id')
    at getOrderItems (src/services/orders.js:87:23)   ← THIS FRAME
    at processOrder (src/controllers/orders.js:45:18)
    at Layer.handle (node_modules/express/lib/router/layer.js:95:5)
    at next (node_modules/express/lib/router/route.js:137:13)
```

→ The bug is at `src/services/orders.js:87` — not in Express.

### Step 3: Reproduce Locally

```bash
# Reproduce with the exact inputs from the trace
node --inspect src/services/orders.js
# or add temporary logging around the origin frame
```

### Step 4: Identify Root Cause Pattern

Match the error to a known pattern (see patterns below) and trace backwards to find WHY the precondition was violated.

### Step 5: Propose the Fix

Always provide:
1. **Root cause** — one sentence explaining WHY it happened
2. **Fix** — the minimal code change
3. **Prevention** — how to stop this class of error recurring

---

## Common Error Patterns

### Null/Undefined Access

```javascript
// Error: Cannot read properties of undefined (reading 'id')
// Root cause: `order` is undefined because the DB query returned null

// ❌ Before
const id = order.id;

// ✅ Fix
if (!order) {
  throw new Error(`Order not found: ${orderId}`);
}
const id = order.id;

// ✅ Or with optional chaining (if null is OK)
const id = order?.id;
```

### Unhandled Promise Rejection

```javascript
// Error: UnhandledPromiseRejection: Error: ECONNREFUSED
// Root cause: async function not wrapped in try/catch, rejection not propagated

// ❌ Before
app.get('/users', (req, res) => {
  fetchUsers().then(users => res.json(users));  // no catch!
});

// ✅ Fix
app.get('/users', async (req, res, next) => {
  try {
    const users = await fetchUsers();
    res.json(users);
  } catch (err) {
    next(err);  // pass to Express error handler
  }
});
```

### Race Condition

```javascript
// Symptom: Intermittent failures, "object already in use" errors
// Root cause: Two operations modifying shared state concurrently

// ❌ Before — read-modify-write without locking
const balance = await getBalance(userId);
await setBalance(userId, balance - amount);

// ✅ Fix — atomic update in DB
await db.query(
  'UPDATE accounts SET balance = balance - $1 WHERE id = $2 AND balance >= $1',
  [amount, userId]
);
```

### Memory Leak

```javascript
// Symptom: Process memory grows indefinitely
// Common causes: Event listeners never removed, closures holding references

// Diagnosis:
// 1. Take heap snapshot: node --inspect app.js → Chrome DevTools → Memory
// 2. Look for growing collections: Map, Set, arrays that are never cleared
// 3. Check for event listeners: emitter.listenerCount('event')

// ❌ Leak — listener added in a loop, never removed
setInterval(() => {
  emitter.on('data', handler);  // adds a new listener every tick!
}, 1000);

// ✅ Fix
emitter.on('data', handler);  // add once, outside the interval
```

### Timeout / Slow Query

```javascript
// Error: Error: Query timeout after 5000ms
// Root cause: Missing index, N+1 query, or long-running transaction

// Diagnosis:
// 1. EXPLAIN ANALYZE the slow query
// 2. Check for missing indexes
// 3. Look for queries inside loops

// ❌ N+1 pattern
const orders = await db.query('SELECT * FROM orders');
for (const order of orders) {
  order.items = await db.query('SELECT * FROM items WHERE order_id = $1', [order.id]);
}

// ✅ Fix — single JOIN query
const orders = await db.query(`
  SELECT o.*, json_agg(i.*) as items
  FROM orders o
  LEFT JOIN items i ON i.order_id = o.id
  GROUP BY o.id
`);
```

---

## Sentry-Specific Workflow

When given a Sentry issue URL or event:

```bash
# Fetch full event via Sentry API (if API token available)
curl -H "Authorization: Bearer $SENTRY_TOKEN" \
  "https://sentry.io/api/0/projects/{org}/{project}/events/{event_id}/" | jq .

# Or use the langsmith-fetch skill for LangSmith traces
```

Key fields to extract from Sentry event:
- `exception.values[0].type` — error class
- `exception.values[0].value` — error message
- `exception.values[0].stacktrace.frames` — call stack (last frame = origin)
- `contexts.runtime` — Node/Python version
- `contexts.os` — OS info
- `user` — which user triggered it
- `request` — URL, method, headers, data
- `extra` — any additional context logged

---

## Python Traceback Analysis

```python
# Traceback (most recent call last):
#   File "app/routes/users.py", line 45, in get_user
#     user = db.session.get(User, user_id)
#   File "venv/lib/python3.11/sqlalchemy/orm/session.py", line 3555, in get
#     ...
# sqlalchemy.exc.DetachedInstanceError: Instance is not bound to a Session

# Root cause: Accessing lazy-loaded relationship after session closed
# Fix: Load relationship eagerly or keep session open
from sqlalchemy.orm import joinedload

user = db.session.query(User).options(
    joinedload(User.orders)
).get(user_id)
```

---

## Go Panic Analysis

```go
// goroutine 1 [running]:
// main.processRequest(0xc0000b4000)
//         /app/main.go:87 +0x1a4
// panic: runtime error: index out of range [3] with length 3

// Root cause: Slice index 3 on a length-3 slice (valid indices: 0, 1, 2)
// Fix: Bounds check before indexing
if idx >= len(items) {
    return fmt.Errorf("index %d out of range (len %d)", idx, len(items))
}
```

---

## Output Format

```markdown
## Debug Analysis: [Error Type]

**Root Cause:** [One sentence: WHY this error occurred, not just what happened]

**Origin:** `[file]:[line]` — [what the code is doing there]

**Call Chain:**
1. [Request/event entry point]
2. [Intermediate function]
3. → [Origin frame where error occurs]

**Fix:**
```[language]
// Before
[buggy code]

// After
[fixed code]
```

**Prevention:**
- [How to stop this class of error: validation, testing, type safety]
- [Monitoring recommendation if applicable]

**Reproduction:**
```bash
[Command or curl to reproduce locally]
```
```
