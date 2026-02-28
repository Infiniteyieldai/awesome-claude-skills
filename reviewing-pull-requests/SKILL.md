---
name: reviewing-pull-requests
description: Use this skill when reviewing a pull request, providing code review feedback, analyzing a diff, or preparing a structured PR review. This includes reviewing code quality, logic correctness, security issues, test coverage, naming conventions, performance concerns, and architectural alignment. Invoke when users share a PR URL, paste a diff, ask for code review, or want feedback on changes before merging. Works with GitHub, GitLab, and raw diffs.
---

# Reviewing Pull Requests

Provides structured, actionable PR reviews covering correctness, security, quality, and maintainability. Produces feedback that is direct, specific, and prioritized.

## Review Philosophy

- **Be specific**: Point to exact lines, not vague concerns
- **Be actionable**: Every comment suggests a fix or asks a clear question
- **Be prioritized**: Distinguish blocking issues from suggestions
- **Be kind**: Critique the code, not the author

---

## Step 1: Fetch the PR

```bash
# GitHub CLI — fetch diff and metadata
gh pr view <PR_NUMBER> --json title,body,additions,deletions,files,baseRefName,headRefName
gh pr diff <PR_NUMBER>

# Or view in browser format
gh pr checkout <PR_NUMBER>  # then review locally
git diff main...HEAD
```

If the user pastes a raw diff, work directly from that.

---

## Step 2: Understand Context

Before reviewing, establish:
1. **What is this PR trying to do?** (read the description)
2. **What is the base branch?** (main, develop, release)
3. **How many files changed?** (scope of change)
4. **Are there linked issues?** (understand the why)

---

## Step 3: Run the Review Checklist

### Correctness
- [ ] Does the logic match the stated intent?
- [ ] Are edge cases handled (null, empty, overflow, negative)?
- [ ] Are error paths handled and surfaced correctly?
- [ ] Are async operations awaited where needed?
- [ ] Are there any obvious off-by-one errors or incorrect conditions?

### Security
- [ ] Are user inputs validated and sanitized?
- [ ] Are there SQL injection, XSS, or command injection risks?
- [ ] Are secrets/tokens ever logged or exposed?
- [ ] Are authorization checks in place (not just authentication)?
- [ ] Are file uploads validated (type, size, path traversal)?

### Tests
- [ ] Do tests cover the happy path?
- [ ] Do tests cover error/edge cases?
- [ ] Are mocks/stubs appropriate (not over-mocked)?
- [ ] Is test coverage proportional to code risk?

### Code Quality
- [ ] Is there duplicated logic that should be extracted?
- [ ] Are names (variables, functions, files) clear and accurate?
- [ ] Are functions focused on a single responsibility?
- [ ] Is complexity justified? (cyclomatic complexity, nesting depth)
- [ ] Are magic numbers/strings given named constants?

### Performance
- [ ] Are there N+1 query patterns?
- [ ] Are expensive operations inside loops?
- [ ] Are large collections handled with pagination/streaming?
- [ ] Are there missing database indexes for new query patterns?

### Maintainability
- [ ] Is the PR small enough to review? (>500 lines is a smell)
- [ ] Are new patterns consistent with the existing codebase?
- [ ] Is documentation updated (README, API docs, comments)?
- [ ] Are deprecation warnings introduced unnecessarily?

---

## Step 4: Structure the Feedback

Use this format for every significant comment:

```
**[BLOCKING | SUGGESTION | QUESTION | NITPICK]** — [File]:[Line]

[Specific observation about the code]

[Explanation of why it matters]

[Concrete suggestion or question]

Example (if helpful):
```code
// suggested fix
```
```

---

## Review Output Format

```markdown
## PR Review: [PR Title]

**Verdict:** ✅ Approve / 🔄 Request Changes / 💬 Comment

**Summary:** [2-3 sentences on what changed and overall quality]

---

### Blocking Issues

These must be resolved before merging.

#### 1. [Issue Title] — `src/auth/middleware.ts:42`

[Observation] [Why it matters] [Suggested fix]

---

### Suggestions

Non-blocking improvements worth considering.

#### 1. [Suggestion Title] — `src/api/users.ts:87`

[Observation and rationale]

---

### Nitpicks

Style/naming preferences, take or leave.

- `src/utils/format.ts:12` — Consider renaming `x` to `userId` for clarity

---

### Positive Callouts

- [Something done well — specific line/pattern]
- [Another strength]

---

### Questions

- `src/db/queries.ts:55` — Is this query ever called without a user context? If so, the default empty array could hide bugs.
```

---

## Severity Levels

| Level | When to Use | Merge? |
|-------|-------------|--------|
| **BLOCKING** | Bug, security issue, data loss risk, broken functionality | No |
| **SUGGESTION** | Better approach exists, worth discussing | Author decides |
| **QUESTION** | Genuinely unclear, need more context | No until answered |
| **NITPICK** | Style preference, minor naming | Yes |

---

## Common Issues by Language

### JavaScript / TypeScript
```typescript
// ❌ Missing await
const user = getUser(id);  // returns Promise, not User

// ❌ Unsafe any
function process(data: any) { ... }

// ❌ Missing error boundary
const data = JSON.parse(input);  // throws on invalid JSON
```

### Python
```python
# ❌ Mutable default argument
def add_item(item, lst=[]):  # shared across calls!

# ❌ Broad exception catch
try: ...
except Exception: pass  # swallows all errors

# ❌ Missing type hints on public functions
def process(data):  # should be def process(data: dict) -> list:
```

### SQL
```sql
-- ❌ N+1 pattern (call inside a loop)
SELECT * FROM orders WHERE user_id = ?  -- called 100 times

-- ❌ SELECT * in production code
SELECT * FROM users  -- returns all columns, breaks on schema change

-- ❌ Missing index for new query
WHERE created_at > ? AND status = ?  -- add composite index
```

---

## Quick Commands

```bash
# View PR files changed
gh pr view <PR> --json files --jq '.files[].path'

# View specific file diff
gh pr diff <PR> -- src/auth/middleware.ts

# Check CI status
gh pr checks <PR>

# List review comments already made
gh api repos/{owner}/{repo}/pulls/{pr}/comments
```

---

## Tips for Large PRs

If the PR is >500 lines, suggest splitting it. If you must review it anyway:
1. Start with the entry points (route handlers, main exports)
2. Trace the data flow through the change
3. Focus blocking issues on security and correctness only
4. Leave style/suggestions for a follow-up
