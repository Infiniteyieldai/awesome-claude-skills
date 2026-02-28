---
name: building-dashboards
description: Use this skill when creating interactive data dashboards, charts, or visualization UIs from CSV files, JSON data, or database queries. This includes building bar charts, line graphs, pie charts, KPI cards, time series visualizations, and multi-panel dashboards. Invoke when users want to visualize data, create a metrics dashboard, build a chart from a spreadsheet, display KPIs, or turn raw numbers into visual insights. Uses Chart.js, Recharts, or Observable Plot depending on context.
---

# Building Data Dashboards

Creates interactive charts and dashboards from CSV, JSON, or database data. Outputs self-contained HTML files or React components depending on the user's stack.

## Output Formats

| Format | When to Use |
|--------|-------------|
| Self-contained HTML | Standalone file, no framework needed |
| React component (Recharts) | Next.js, React, or Vite projects |
| Observable notebook | Data exploration and analysis |
| Claude artifact | Quick visualization in claude.ai |

---

## Self-Contained HTML Dashboard

Best for: Shareable files, non-technical stakeholders, quick demos.

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <title>[Dashboard Title]</title>
  <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
  <style>
    * { margin: 0; padding: 0; box-sizing: border-box; }
    body { font-family: system-ui, sans-serif; background: #f8fafc; padding: 24px; }
    h1 { font-size: 1.5rem; color: #1e293b; margin-bottom: 8px; }
    .subtitle { color: #64748b; margin-bottom: 24px; font-size: 0.9rem; }
    .grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 16px; margin-bottom: 24px; }
    .kpi { background: white; border-radius: 8px; padding: 20px; box-shadow: 0 1px 3px rgba(0,0,0,0.1); }
    .kpi-label { font-size: 0.8rem; color: #64748b; text-transform: uppercase; letter-spacing: 0.05em; }
    .kpi-value { font-size: 2rem; font-weight: 700; color: #1e293b; margin: 4px 0; }
    .kpi-trend { font-size: 0.85rem; }
    .kpi-trend.up { color: #16a34a; }
    .kpi-trend.down { color: #dc2626; }
    .chart-card { background: white; border-radius: 8px; padding: 20px; box-shadow: 0 1px 3px rgba(0,0,0,0.1); margin-bottom: 16px; }
    .chart-title { font-size: 1rem; font-weight: 600; color: #1e293b; margin-bottom: 16px; }
  </style>
</head>
<body>
  <h1>[Dashboard Title]</h1>
  <p class="subtitle">Updated [DATE] · Data source: [SOURCE]</p>

  <!-- KPI Cards -->
  <div class="grid">
    <div class="kpi">
      <div class="kpi-label">Total Revenue</div>
      <div class="kpi-value">$124K</div>
      <div class="kpi-trend up">▲ 12% vs last month</div>
    </div>
    <div class="kpi">
      <div class="kpi-label">Active Users</div>
      <div class="kpi-value">3,847</div>
      <div class="kpi-trend up">▲ 8% vs last month</div>
    </div>
    <div class="kpi">
      <div class="kpi-label">Churn Rate</div>
      <div class="kpi-value">2.1%</div>
      <div class="kpi-trend down">▼ 0.3% vs last month</div>
    </div>
    <div class="kpi">
      <div class="kpi-label">Net Margin</div>
      <div class="kpi-value">18%</div>
      <div class="kpi-trend up">▲ 2% vs last month</div>
    </div>
  </div>

  <!-- Charts -->
  <div class="chart-card">
    <div class="chart-title">Monthly Revenue</div>
    <canvas id="revenueChart" height="100"></canvas>
  </div>

  <div class="chart-card">
    <div class="chart-title">Revenue by Category</div>
    <canvas id="categoryChart" height="120"></canvas>
  </div>

  <script>
    // ── Revenue Line Chart ────────────────────────────────────
    new Chart(document.getElementById('revenueChart'), {
      type: 'line',
      data: {
        labels: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
        datasets: [{
          label: 'Revenue ($)',
          data: [85000, 92000, 98000, 105000, 118000, 124000],
          borderColor: '#6366f1',
          backgroundColor: 'rgba(99, 102, 241, 0.1)',
          borderWidth: 2,
          fill: true,
          tension: 0.3,
          pointRadius: 4,
        }]
      },
      options: {
        responsive: true,
        plugins: { legend: { display: false } },
        scales: {
          y: {
            ticks: {
              callback: v => '$' + (v/1000).toFixed(0) + 'K'
            }
          }
        }
      }
    });

    // ── Category Doughnut Chart ───────────────────────────────
    new Chart(document.getElementById('categoryChart'), {
      type: 'doughnut',
      data: {
        labels: ['Product A', 'Product B', 'Services', 'Subscriptions'],
        datasets: [{
          data: [45000, 32000, 28000, 19000],
          backgroundColor: ['#6366f1', '#06b6d4', '#10b981', '#f59e0b'],
        }]
      },
      options: {
        responsive: true,
        plugins: {
          legend: { position: 'right' },
          tooltip: {
            callbacks: {
              label: ctx => ` $${ctx.raw.toLocaleString()}`
            }
          }
        }
      }
    });
  </script>
</body>
</html>
```

---

## React + Recharts Component

Best for: Next.js, React, or Vite apps where the dashboard is part of the product.

```bash
npm install recharts
```

```tsx
// components/RevenueDashboard.tsx
import {
  LineChart, Line, BarChart, Bar,
  XAxis, YAxis, CartesianGrid, Tooltip, Legend,
  ResponsiveContainer, PieChart, Pie, Cell
} from 'recharts';

const COLORS = ['#6366f1', '#06b6d4', '#10b981', '#f59e0b'];

interface KPICardProps {
  label: string;
  value: string;
  trend: string;
  positive: boolean;
}

function KPICard({ label, value, trend, positive }: KPICardProps) {
  return (
    <div className="bg-white rounded-lg p-5 shadow-sm">
      <p className="text-xs text-gray-500 uppercase tracking-wider">{label}</p>
      <p className="text-3xl font-bold text-gray-900 my-1">{value}</p>
      <p className={`text-sm ${positive ? 'text-green-600' : 'text-red-600'}`}>
        {positive ? '▲' : '▼'} {trend}
      </p>
    </div>
  );
}

export function RevenueDashboard({ data }: { data: MonthlyData[] }) {
  return (
    <div className="p-6 bg-gray-50 min-h-screen">
      <h1 className="text-2xl font-bold text-gray-900 mb-1">Revenue Dashboard</h1>
      <p className="text-gray-500 text-sm mb-6">Updated today</p>

      {/* KPI Grid */}
      <div className="grid grid-cols-2 md:grid-cols-4 gap-4 mb-6">
        <KPICard label="MRR" value="$124K" trend="12% vs last month" positive />
        <KPICard label="Active Users" value="3,847" trend="8% vs last month" positive />
        <KPICard label="Churn" value="2.1%" trend="0.3% vs last month" positive={false} />
        <KPICard label="Net Margin" value="18%" trend="2% vs last month" positive />
      </div>

      {/* Line Chart */}
      <div className="bg-white rounded-lg p-5 shadow-sm mb-4">
        <h2 className="font-semibold text-gray-900 mb-4">Monthly Revenue</h2>
        <ResponsiveContainer width="100%" height={250}>
          <LineChart data={data}>
            <CartesianGrid strokeDasharray="3 3" stroke="#f1f5f9" />
            <XAxis dataKey="month" tick={{ fontSize: 12 }} />
            <YAxis tickFormatter={v => `$${(v/1000).toFixed(0)}K`} tick={{ fontSize: 12 }} />
            <Tooltip formatter={(v: number) => [`$${v.toLocaleString()}`, 'Revenue']} />
            <Line
              type="monotone"
              dataKey="revenue"
              stroke="#6366f1"
              strokeWidth={2}
              dot={{ r: 4 }}
              activeDot={{ r: 6 }}
            />
          </LineChart>
        </ResponsiveContainer>
      </div>
    </div>
  );
}
```

---

## Chart Type Selection Guide

| Data Type | Best Chart | When NOT to Use |
|-----------|-----------|----------------|
| Trend over time | Line chart | When comparing many categories |
| Comparing categories | Bar chart | More than 8-10 categories |
| Part-to-whole | Donut/Pie | More than 5 segments |
| Distribution | Histogram | Small datasets (<20 points) |
| Correlation | Scatter plot | Ordinal/categorical data |
| KPI vs target | Gauge / progress bar | Complex multi-metric views |
| Heatmap | Calendar/grid heatmap | Non-time-based data |

---

## Data Loading Pattern

```javascript
// scripts/prepare-dashboard-data.js
import { readFile } from 'fs/promises';
import { parse } from 'csv-parse/sync';

const raw = await readFile(process.argv[2] || 'data.csv', 'utf8');
const rows = parse(raw, { columns: true, skip_empty_lines: true });

// Normalize currency fields
const cleaned = rows.map(r => ({
  month: r.month,
  revenue: parseFloat(r.revenue?.replace(/[$,]/g, '') || 0),
  expenses: parseFloat(r.expenses?.replace(/[$,]/g, '') || 0),
  users: parseInt(r.users || 0, 10),
}));

// Output as JSON for use in HTML template
console.log(JSON.stringify(cleaned, null, 2));
```

---

## Accessibility Checklist

- [ ] All charts have text alternatives (`aria-label` on canvas)
- [ ] Color is not the only differentiator (use patterns or labels too)
- [ ] Interactive elements are keyboard navigable
- [ ] Sufficient color contrast (4.5:1 minimum)
- [ ] Data table alternative provided for screen readers
