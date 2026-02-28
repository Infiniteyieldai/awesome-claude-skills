---
name: analyzing-financial-data
description: Use this skill when analyzing financial data, revenue figures, expense breakdowns, profit and loss statements, balance sheets, or cash flow reports. This includes calculating growth rates, margins, burn rate, runway, MRR/ARR, cohort analysis, financial forecasting, and budget variance analysis. Invoke when users share financial spreadsheets, CSVs with numbers, P&L data, accounting exports, or ask questions like "how are we doing financially", "what's our runway", "analyze this revenue data", or "break down our costs".
---

# Analyzing Financial Data

Performs structured financial analysis on revenue, expenses, P&L statements, and balance sheets. Produces clear summaries, key ratios, trend analysis, and actionable insights.

## Supported Input Formats

- CSV/Excel exports from QuickBooks, Xero, Wave, FreshBooks
- Google Sheets with financial data
- Plain numbers pasted into the conversation
- Structured JSON from accounting APIs
- Bank statement CSVs

---

## Workflow

### Step 1: Understand the Data Structure

Before analyzing, identify:
```
What period does this cover? (monthly, quarterly, annual)
What currency? (USD, GBP, EUR)
What type of data? (P&L, balance sheet, cash flow, revenue)
Is it actuals, budget, or forecast — or a comparison?
```

### Step 2: Load and Validate

```javascript
// scripts/load-financial-data.js
import { readFile } from 'fs/promises';
import { parse } from 'csv-parse/sync';

const raw = await readFile(process.argv[2], 'utf8');
const rows = parse(raw, { columns: true, skip_empty_lines: true });

// Validate: convert string currency to numbers
const cleaned = rows.map(row => ({
  ...row,
  amount: parseFloat(row.amount?.replace(/[$,]/g, '') || '0'),
  date: new Date(row.date),
}));

// Check for parsing errors
const invalid = cleaned.filter(r => isNaN(r.amount));
if (invalid.length > 0) {
  console.error(`⚠️  ${invalid.length} rows with invalid amounts`);
}

console.log(JSON.stringify(cleaned.slice(0, 3), null, 2));
console.log(`Total rows: ${cleaned.length}`);
```

### Step 3: Compute Key Metrics

Always calculate these first:

```javascript
// Key financial metrics
const metrics = {
  totalRevenue: sum(rows, 'revenue'),
  totalExpenses: sum(rows, 'expenses'),
  grossProfit: totalRevenue - cogs,
  grossMargin: (grossProfit / totalRevenue) * 100,
  netProfit: totalRevenue - totalExpenses,
  netMargin: (netProfit / totalRevenue) * 100,
  burnRate: monthlyExpenses - monthlyRevenue,  // if negative cash flow
  runway: cashOnHand / monthlyBurnRate,         // months remaining
};

function sum(rows, field) {
  return rows.reduce((acc, r) => acc + (r[field] || 0), 0);
}
```

### Step 4: Trend Analysis

```javascript
// Month-over-month growth
function momGrowth(current, previous) {
  if (previous === 0) return null;
  return ((current - previous) / previous) * 100;
}

// Group by month and compute growth
const byMonth = groupBy(rows, r => r.date.toISOString().slice(0, 7));
const months = Object.keys(byMonth).sort();
const trends = months.map((month, i) => {
  const revenue = sum(byMonth[month], 'revenue');
  const prevRevenue = i > 0 ? sum(byMonth[months[i-1]], 'revenue') : 0;
  return {
    month,
    revenue,
    growth: momGrowth(revenue, prevRevenue)?.toFixed(1) + '%',
  };
});
```

---

## Common Financial Analyses

### SaaS Metrics

```javascript
// MRR (Monthly Recurring Revenue)
const mrr = subscriptions
  .filter(s => s.status === 'active')
  .reduce((sum, s) => sum + s.monthly_amount, 0);

// ARR
const arr = mrr * 12;

// Churn Rate
const churnRate = (cancelledThisMonth / activeStartOfMonth) * 100;

// Net Revenue Retention (NRR)
const nrr = (startMRR + expansion - contraction - churn) / startMRR * 100;

// Customer Acquisition Cost (CAC)
const cac = totalSalesAndMarketingSpend / newCustomersAcquired;

// LTV (Lifetime Value)
const avgLifetimeMonths = 1 / (churnRate / 100);
const ltv = mrr_per_customer * avgLifetimeMonths;

// LTV:CAC ratio (healthy = >3)
const ltvCacRatio = ltv / cac;
```

### P&L Summary

```markdown
## P&L Summary — [Period]

| Category | Amount | % of Revenue |
|----------|--------|-------------|
| Revenue | $X,XXX | 100% |
| Cost of Goods (COGS) | $(X,XXX) | XX% |
| **Gross Profit** | **$X,XXX** | **XX%** |
| Operating Expenses | $(X,XXX) | XX% |
| **Operating Profit (EBITDA)** | **$X,XXX** | **XX%** |
| Taxes | $(XXX) | X% |
| **Net Profit** | **$X,XXX** | **XX%** |

**Key Ratios:**
- Gross Margin: XX% (industry avg: XX%)
- Operating Margin: XX%
- Net Margin: XX%
```

### Runway Calculation

```javascript
// Given: cash on hand, monthly expenses, monthly revenue
const netBurn = monthlyExpenses - monthlyRevenue;  // per month

if (netBurn <= 0) {
  console.log('✅ Cash flow positive — no runway concern');
} else {
  const runwayMonths = cashOnHand / netBurn;
  const runwayDate = new Date();
  runwayDate.setMonth(runwayDate.getMonth() + runwayMonths);

  console.log(`Runway: ${runwayMonths.toFixed(1)} months (until ${runwayDate.toDateString()})`);
  console.log(`Monthly burn: $${netBurn.toLocaleString()}`);

  if (runwayMonths < 6) console.log('⚠️  Less than 6 months runway — fundraise now');
  if (runwayMonths < 3) console.log('🚨 Critical — less than 3 months runway');
}
```

### Budget vs. Actual Variance

```javascript
// Variance analysis
const variance = categories.map(cat => ({
  category: cat.name,
  budget: cat.budget,
  actual: cat.actual,
  variance: cat.actual - cat.budget,
  variancePct: ((cat.actual - cat.budget) / cat.budget * 100).toFixed(1) + '%',
  flag: Math.abs((cat.actual - cat.budget) / cat.budget) > 0.1 ? '⚠️' : '✅',
}));
```

---

## Output Format

```markdown
## Financial Analysis: [Period]

### Executive Summary
[3-4 bullet points on the most important findings]

### Revenue
- Total: $X,XXX (▲ XX% MoM)
- Top source: [Category] ($X,XXX, XX%)
- [Any notable trend or concern]

### Expenses
- Total: $X,XXX
- Largest categories: [1st], [2nd], [3rd]
- [Any unusual items]

### Profitability
- Gross Margin: XX% [⚠️ below/✅ above industry avg of XX%]
- Net Margin: XX%

### Key Metrics
| Metric | Value | Benchmark | Status |
|--------|-------|-----------|--------|
| Gross Margin | XX% | >60% | ✅/⚠️ |
| Runway | X months | >12 months | ✅/⚠️ |
| MoM Growth | XX% | — | — |

### Action Items
1. [Most urgent financial action]
2. [Second priority]
3. [Third priority]
```

---

## Quick Formulas Reference

| Metric | Formula |
|--------|---------|
| Gross Margin | (Revenue - COGS) / Revenue × 100 |
| Net Margin | Net Income / Revenue × 100 |
| Burn Rate | Monthly Expenses - Monthly Revenue |
| Runway | Cash / Monthly Burn Rate |
| MoM Growth | (This Month - Last Month) / Last Month × 100 |
| YoY Growth | (This Year - Last Year) / Last Year × 100 |
| CAC | Sales + Marketing Spend / New Customers |
| LTV | ARPU / Churn Rate |
| LTV:CAC | LTV / CAC (healthy = >3) |
| Churn Rate | Lost Customers / Starting Customers × 100 |
| NRR | (Start MRR + Expansion - Contraction - Churn) / Start MRR × 100 |
