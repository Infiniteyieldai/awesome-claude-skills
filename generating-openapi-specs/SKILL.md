---
name: generating-openapi-specs
description: Use this skill when generating, validating, or improving OpenAPI 3.x specifications from existing code, routes, or API descriptions. This includes extracting endpoints from Express, FastAPI, Rails, or Django code, writing OpenAPI YAML/JSON from scratch, converting Swagger 2.0 to OpenAPI 3.x, adding missing schema definitions, generating example requests/responses, and linting specs with Spectral. Invoke when users mention OpenAPI, Swagger, API spec, REST documentation, endpoint schema, or want to document their API.
---

# Generating OpenAPI Specifications

Generates, validates, and improves OpenAPI 3.x specifications from source code, route definitions, or natural-language API descriptions.

## What This Skill Produces

- A valid `openapi.yaml` or `openapi.json` file
- Schema definitions for all request/response bodies
- Example values for every field
- Spectral lint report (zero errors)

## Supported Frameworks

| Framework | Language | How Routes Are Detected |
|-----------|----------|------------------------|
| Express.js | Node.js | `app.get/post/put/delete(path, handler)` |
| FastAPI | Python | `@app.get/post()` decorators |
| Rails | Ruby | `routes.rb` and controller actions |
| Django REST | Python | `urlpatterns` + serializers |
| Hono | TypeScript | `app.get/post()` chains |
| Gin | Go | `r.GET/POST()` calls |

For detailed framework patterns, see `./framework-extraction-patterns.md`.

---

## Workflow

### Step 1: Discover Existing Routes

Scan the codebase for route definitions:

```bash
# Express.js
grep -rn "app\.\(get\|post\|put\|patch\|delete\)" src/ --include="*.js" --include="*.ts"

# FastAPI
grep -rn "@app\.\(get\|post\|put\|delete\)" . --include="*.py"

# Rails
cat config/routes.rb
```

### Step 2: Extract Schema from Code

For each route, extract:
- HTTP method + path
- Path parameters (`:id`, `{userId}`)
- Query parameters
- Request body shape (from validation schemas, TypeScript types, Pydantic models, ActiveRecord)
- Response shape (from serializers, return type annotations, example responses)

### Step 3: Build the OpenAPI Document

Start with the skeleton:

```yaml
openapi: 3.1.0
info:
  title: [API Name]
  version: 1.0.0
  description: [API description]
servers:
  - url: https://api.example.com/v1
    description: Production
  - url: http://localhost:3000
    description: Local development
paths: {}
components:
  schemas: {}
  securitySchemes: {}
```

Then populate `paths` for each route (see `./openapi-path-patterns.md`).

### Step 4: Add Schemas to components

Extract all repeated shapes into `components/schemas`:

```yaml
components:
  schemas:
    User:
      type: object
      required: [id, email]
      properties:
        id:
          type: string
          format: uuid
          example: "550e8400-e29b-41d4-a716-446655440000"
        email:
          type: string
          format: email
          example: "user@example.com"
        createdAt:
          type: string
          format: date-time
```

### Step 5: Lint with Spectral

```bash
npx @stoplight/spectral-cli lint openapi.yaml
```

Fix all errors before delivering. Common issues:
- Missing `operationId` on each endpoint
- Missing `responses` (at minimum 200 and 4xx)
- Unreferenced schemas in `components`
- Missing `description` on parameters

### Step 6: Generate Examples

Add `example` values to every schema property — makes the spec useful for mocking:

```yaml
properties:
  name:
    type: string
    example: "Widget Pro"
  price:
    type: number
    format: float
    example: 29.99
```

---

## Common Path Patterns

```yaml
paths:
  /users:
    get:
      operationId: listUsers
      summary: List all users
      parameters:
        - name: limit
          in: query
          schema:
            type: integer
            default: 20
            maximum: 100
      responses:
        '200':
          description: List of users
          content:
            application/json:
              schema:
                type: object
                properties:
                  data:
                    type: array
                    items:
                      $ref: '#/components/schemas/User'
                  total:
                    type: integer
        '401':
          $ref: '#/components/responses/Unauthorized'

  /users/{id}:
    get:
      operationId: getUser
      summary: Get a user by ID
      parameters:
        - name: id
          in: path
          required: true
          schema:
            type: string
            format: uuid
      responses:
        '200':
          description: The user
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/User'
        '404':
          $ref: '#/components/responses/NotFound'
```

---

## Reusable Response Components

Always add these to `components/responses`:

```yaml
components:
  responses:
    Unauthorized:
      description: Authentication required
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/Error'
    NotFound:
      description: Resource not found
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/Error'
    ValidationError:
      description: Invalid request body
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/ValidationError'
  schemas:
    Error:
      type: object
      properties:
        error:
          type: string
        message:
          type: string
    ValidationError:
      type: object
      properties:
        errors:
          type: array
          items:
            type: object
            properties:
              field:
                type: string
              message:
                type: string
```

---

## Security Schemes

```yaml
components:
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer
      bearerFormat: JWT
    ApiKeyAuth:
      type: apiKey
      in: header
      name: X-API-Key

security:
  - BearerAuth: []   # Apply globally, override per-endpoint if needed
```

---

## Delivery

Save as:
- `openapi.yaml` — primary format (human-readable)
- `openapi.json` — alternative (for tools that prefer JSON)

Run final validation:
```bash
npx @stoplight/spectral-cli lint openapi.yaml --ruleset @stoplight/spectral-oas
echo "Spec is valid: $?"
```

For framework-specific extraction patterns, see `./framework-extraction-patterns.md`.
For advanced path and schema patterns, see `./openapi-path-patterns.md`.
