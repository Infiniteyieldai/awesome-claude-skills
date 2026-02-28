---
name: writing-e2e-tests
description: Use this skill when writing, running, or debugging end-to-end (e2e) tests for web applications using Playwright. This includes creating test files from scratch, converting manual test steps to automated tests, testing login flows, form submissions, navigation, API mocking, multi-page workflows, and visual regression tests. Invoke when users mention Playwright, e2e tests, browser tests, integration tests, or want to automate testing of a web UI. Also handles Cypress migration and cross-browser test setup.
---

# Writing End-to-End Tests with Playwright

Creates, runs, and debugs end-to-end browser tests using Playwright — the modern standard for web application testing.

## Setup

```bash
# Install Playwright in an existing project
npm init playwright@latest

# Or add to existing project
npm install --save-dev @playwright/test
npx playwright install chromium  # install browsers
```

Configuration goes in `playwright.config.ts` — see `./playwright-config-patterns.md` for common setups.

---

## Writing Tests

### Basic Test Structure

```typescript
// tests/example.spec.ts
import { test, expect } from '@playwright/test';

test.describe('Feature: [Feature Name]', () => {
  test.beforeEach(async ({ page }) => {
    await page.goto('/');
  });

  test('should [expected behavior]', async ({ page }) => {
    // Arrange
    await page.click('[data-testid="button"]');

    // Act
    await page.fill('[data-testid="input"]', 'test value');
    await page.click('[data-testid="submit"]');

    // Assert
    await expect(page.locator('[data-testid="result"]')).toContainText('Success');
  });
});
```

### Selector Strategy (Priority Order)

Use selectors in this order — most reliable to least:

```typescript
// 1. Role-based (best — matches accessibility)
page.getByRole('button', { name: 'Submit' })
page.getByRole('textbox', { name: 'Email' })
page.getByRole('heading', { level: 1 })

// 2. Test IDs (fast, stable)
page.locator('[data-testid="login-form"]')

// 3. Labels
page.getByLabel('Password')

// 4. Text content
page.getByText('Sign in')

// 5. CSS selectors (avoid — brittle)
page.locator('.btn-primary')  // ❌ avoid
```

---

## Common Test Patterns

### Authentication Flow

```typescript
test('user can log in', async ({ page }) => {
  await page.goto('/login');
  await page.getByLabel('Email').fill('test@example.com');
  await page.getByLabel('Password').fill('password123');
  await page.getByRole('button', { name: 'Sign in' }).click();

  // Wait for redirect to dashboard
  await expect(page).toHaveURL('/dashboard');
  await expect(page.getByRole('heading', { name: 'Dashboard' })).toBeVisible();
});
```

### Reusable Auth — Use `storageState`

```typescript
// tests/auth.setup.ts
import { test as setup } from '@playwright/test';

setup('authenticate', async ({ page }) => {
  await page.goto('/login');
  await page.getByLabel('Email').fill(process.env.TEST_EMAIL!);
  await page.getByLabel('Password').fill(process.env.TEST_PASSWORD!);
  await page.getByRole('button', { name: 'Sign in' }).click();
  await page.waitForURL('/dashboard');

  // Save auth state — reused by all tests
  await page.context().storageState({ path: 'playwright/.auth/user.json' });
});
```

```typescript
// playwright.config.ts
export default defineConfig({
  projects: [
    { name: 'setup', testMatch: /auth.setup.ts/ },
    {
      name: 'authenticated',
      dependencies: ['setup'],
      use: { storageState: 'playwright/.auth/user.json' },
    },
  ],
});
```

### Form Validation

```typescript
test('shows error for invalid email', async ({ page }) => {
  await page.goto('/signup');
  await page.getByLabel('Email').fill('not-an-email');
  await page.getByRole('button', { name: 'Create account' }).click();

  await expect(page.getByText('Please enter a valid email')).toBeVisible();
});
```

### API Mocking

```typescript
test('handles API error gracefully', async ({ page }) => {
  // Mock the API to return an error
  await page.route('**/api/users', route => {
    route.fulfill({
      status: 500,
      contentType: 'application/json',
      body: JSON.stringify({ error: 'Internal server error' }),
    });
  });

  await page.goto('/users');
  await expect(page.getByText('Something went wrong')).toBeVisible();
});
```

### File Upload

```typescript
test('can upload a profile picture', async ({ page }) => {
  await page.goto('/profile');

  // Set file input directly
  await page.locator('input[type="file"]').setInputFiles('tests/fixtures/avatar.jpg');

  await expect(page.locator('[data-testid="preview-image"]')).toBeVisible();
});
```

### Waiting Strategies

```typescript
// Wait for specific state — not sleep()
await page.waitForURL('/dashboard');               // URL change
await expect(element).toBeVisible();               // Element appears
await expect(element).not.toBeVisible();           // Element disappears
await page.waitForResponse('**/api/data');         // API response
await page.waitForLoadState('networkidle');        // No pending requests
```

### Keyboard Navigation

```typescript
test('is keyboard accessible', async ({ page }) => {
  await page.goto('/');
  await page.keyboard.press('Tab');  // Focus first element
  await page.keyboard.press('Tab');  // Focus second element
  await page.keyboard.press('Enter'); // Activate focused element

  await expect(page.locator(':focus')).toHaveAttribute('data-testid', 'nav-link');
});
```

---

## Running Tests

```bash
# Run all tests
npx playwright test

# Run specific file
npx playwright test tests/auth.spec.ts

# Run with browser UI (headed)
npx playwright test --headed

# Debug a specific test (opens Inspector)
npx playwright test --debug tests/login.spec.ts

# Show test report
npx playwright show-report
```

---

## Page Object Model

For larger test suites, extract repeated interactions into Page Objects:

```typescript
// tests/pages/LoginPage.ts
import { Page, Locator, expect } from '@playwright/test';

export class LoginPage {
  readonly emailInput: Locator;
  readonly passwordInput: Locator;
  readonly submitButton: Locator;

  constructor(readonly page: Page) {
    this.emailInput = page.getByLabel('Email');
    this.passwordInput = page.getByLabel('Password');
    this.submitButton = page.getByRole('button', { name: 'Sign in' });
  }

  async goto() {
    await this.page.goto('/login');
  }

  async login(email: string, password: string) {
    await this.emailInput.fill(email);
    await this.passwordInput.fill(password);
    await this.submitButton.click();
  }
}

// In tests:
const loginPage = new LoginPage(page);
await loginPage.goto();
await loginPage.login('user@example.com', 'password');
```

---

## Visual Regression Testing

```typescript
test('matches visual snapshot', async ({ page }) => {
  await page.goto('/dashboard');
  await expect(page).toHaveScreenshot('dashboard.png', {
    maxDiffPixelRatio: 0.01,  // 1% pixel difference tolerance
  });
});

// Update snapshots when intentional changes are made:
// npx playwright test --update-snapshots
```

---

## CI/CD Configuration

```yaml
# .github/workflows/e2e.yml
name: E2E Tests
on: [push, pull_request]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with: { node-version: '20' }
      - run: npm ci
      - run: npx playwright install --with-deps chromium
      - run: npx playwright test
        env:
          TEST_EMAIL: ${{ secrets.TEST_EMAIL }}
          TEST_PASSWORD: ${{ secrets.TEST_PASSWORD }}
      - uses: actions/upload-artifact@v4
        if: failure()
        with:
          name: playwright-report
          path: playwright-report/
```

For playwright.config.ts patterns and advanced setups, see `./playwright-config-patterns.md`.
