# Framework-Specific Route Extraction Patterns

Reference for extracting API routes and schemas from different web frameworks.

## Express.js / Node.js

### Route Detection
```bash
# Find all route definitions
grep -rn "router\.\(get\|post\|put\|patch\|delete\)\|app\.\(get\|post\|put\|patch\|delete\)" \
  src/ --include="*.js" --include="*.ts" | grep -v node_modules
```

### Schema Extraction
Look for Joi, Zod, or express-validator schemas near route handlers:
```javascript
// Zod example — extract shape directly to OpenAPI
const CreateUserSchema = z.object({
  email: z.string().email(),
  name: z.string().min(1).max(100),
  role: z.enum(['admin', 'user']).default('user'),
});
```

### TypeScript Types → OpenAPI
```typescript
interface User {
  id: string;          // → type: string
  email: string;       // → type: string, format: email
  age?: number;        // → type: integer (optional)
  role: 'admin'|'user' // → type: string, enum: [admin, user]
}
```

---

## FastAPI / Python

### Route Detection
```bash
grep -rn "@\(app\|router\)\.\(get\|post\|put\|patch\|delete\)" . --include="*.py"
```

### Pydantic Models → OpenAPI
FastAPI auto-generates OpenAPI from Pydantic. Export it:
```bash
# If the app is running:
curl http://localhost:8000/openapi.json > openapi.json

# Or programmatically:
python -c "from main import app; import json; print(json.dumps(app.openapi(), indent=2))" > openapi.json
```

Then enhance with missing descriptions and examples.

---

## Rails

### Route Extraction
```bash
rails routes --expanded 2>/dev/null | head -100
# or
cat config/routes.rb
```

### Serializer → Schema
```ruby
# ActiveModel::Serializer
class UserSerializer < ActiveModel::Serializer
  attributes :id, :email, :name, :created_at
end
# → OpenAPI: User { id: string, email: string, name: string, created_at: date-time }
```

---

## Django REST Framework

### URL Patterns
```bash
python manage.py show_urls 2>/dev/null
# or parse urls.py files
grep -rn "path\|re_path" */urls.py
```

### Serializer → Schema
```python
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'username', 'date_joined']
# → OpenAPI User schema with those fields
```

### Auto-export with drf-spectacular
```bash
pip install drf-spectacular
python manage.py spectacular --file openapi.yaml
```

---

## Go (Gin / Echo)

### Route Detection
```bash
grep -rn "r\.\(GET\|POST\|PUT\|PATCH\|DELETE\)\|e\.\(GET\|POST\)" . --include="*.go"
```

### Struct → Schema
```go
type User struct {
    ID        string    `json:"id" example:"550e8400-..."`
    Email     string    `json:"email" example:"user@example.com"`
    CreatedAt time.Time `json:"created_at"`
}
// Use swaggo/swag annotations for automatic OpenAPI generation
```

---

## Auto-Generation Tools

| Tool | Language | Command |
|------|----------|---------|
| `drf-spectacular` | Python/Django | `python manage.py spectacular --file openapi.yaml` |
| `swaggo/swag` | Go | `swag init` |
| FastAPI built-in | Python | `GET /openapi.json` |
| `ts-rest` | TypeScript | Built-in contract → OpenAPI |
| `zod-openapi` | TypeScript/Zod | `createDocument({ schemas })` |

When auto-generation is available, export first then enhance with descriptions and examples.
