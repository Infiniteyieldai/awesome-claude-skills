---
name: generating-reports
description: Use this skill when creating structured reports from data, analysis, or research. This includes generating executive summaries, weekly/monthly business reports, technical incident reports, sprint retrospectives, project status reports, and research summaries. Invoke when users want to compile findings into a document, create a report from data or notes, write an executive summary, format a status update, or produce a formatted PDF or Markdown report. Pairs with the analyzing-financial-data and building-dashboards skills.
---

# Generating Reports

Transforms raw data, analysis, or research into polished, structured reports. Outputs Markdown (default), PDF-ready HTML, or directly to Notion/Google Docs via connect-apps.

## Report Types Supported

| Type | Key Sections | Typical Audience |
|------|-------------|-----------------|
| Executive Summary | Highlights, decisions needed, next steps | C-suite, board |
| Business Review | Metrics, trends, variance, outlook | Leadership |
| Technical Incident Report | Timeline, root cause, remediation | Engineering |
| Sprint Retrospective | Completed, missed, blockers, improvements | Dev team |
| Research Summary | Background, findings, implications | Stakeholders |
| Project Status | Progress, risks, milestones, actions | PM, sponsors |

---

## Workflow

### Step 1: Gather Inputs

Ask the user for:
- **Data/content source** — CSV, analysis output, notes, Slack threads
- **Report type** — (see table above)
- **Audience** — determines language complexity and detail level
- **Period** — what time range does this cover?
- **Format** — Markdown, HTML, PDF, or send to Notion/Docs

### Step 2: Structure the Report

Every report shares this skeleton — expand or trim sections per type:

```
1. Header (title, date, author, period)
2. Executive Summary (3-5 bullet highlights)
3. Key Metrics (table of most important numbers)
4. Main Sections (type-specific)
5. Risks / Issues (if any)
6. Action Items (owner, due date)
7. Appendix (raw data, methodology)
```

### Step 3: Write with Audience in Mind

| Audience | Tone | Detail Level | Length |
|----------|------|-------------|--------|
| Executives | Direct, confident | High-level, no jargon | 1 page |
| Leadership | Professional, clear | Summary + supporting data | 2-3 pages |
| Engineering | Technical, precise | Full detail + code | No limit |
| Investors | Positive, forward-looking | Metrics-first | 1-2 pages |

### Step 4: Format and Deliver

```bash
# Convert Markdown to PDF
npx markdown-pdf report.md -o report.pdf

# Or styled HTML → PDF via Playwright
node scripts/export-report-to-pdf.js report.html report.pdf
```

---

## Report Templates

### Executive Summary

```markdown
# [Company/Project] Executive Summary
**Period:** [Month Year] | **Prepared:** [Date] | **Author:** [Name]

---

## Highlights

- ✅ [Most important positive result with specific metric]
- ✅ [Second highlight]
- ⚠️ [Key concern or risk requiring attention]

---

## Key Metrics

| Metric | This Period | Last Period | Change |
|--------|------------|------------|--------|
| Revenue | $X | $X | +X% |
| Users | X,XXX | X,XXX | +X% |
| [Key metric] | X | X | X% |

---

## Decisions Required

1. **[Decision]** — [Context, options, recommendation]
2. **[Decision]** — [Context, options, recommendation]

---

## Next Steps

| Action | Owner | Due |
|--------|-------|-----|
| [Action item] | [Name] | [Date] |
| [Action item] | [Name] | [Date] |
```

---

### Technical Incident Report

```markdown
# Incident Report: [Incident Title]
**Severity:** P[1-4] | **Date:** [Date] | **Duration:** [X hours Y minutes]

---

## Summary

[2-3 sentences: what happened, impact, resolution.]

---

## Impact

- **Users affected:** [Number or %]
- **Services affected:** [List]
- **Revenue impact:** [$ if applicable]
- **Data loss:** [None / Describe if any]

---

## Timeline

| Time (UTC) | Event |
|------------|-------|
| [HH:MM] | Incident detected via [alert/user report] |
| [HH:MM] | On-call engineer paged |
| [HH:MM] | Root cause identified |
| [HH:MM] | Fix deployed |
| [HH:MM] | Service restored |

---

## Root Cause

[Technical explanation of what caused the incident. Be specific.]

## Contributing Factors

- [Factor 1]
- [Factor 2]

---

## Remediation

### Immediate (completed)
- [x] [Action taken during incident]

### Short-term (this sprint)
- [ ] [Preventive measure] — Owner: [Name]

### Long-term (this quarter)
- [ ] [Systemic improvement] — Owner: [Name]

---

## Lessons Learned

**What went well:**
- [Detection was fast because...]
- [Team communication was...]

**What could improve:**
- [Alert was too noisy / too late because...]
- [Runbook didn't cover...]
```

---

### Weekly Business Report

```markdown
# Weekly Business Report — Week of [DATE]
**Prepared by:** [Name] | **Distribution:** [Team/Stakeholders]

---

## This Week's Highlights

**Revenue:** $[X] ([▲/▼] [X]% WoW)
**New Users:** [X] ([▲/▼] [X]% WoW)
**Support Tickets:** [X] open / [X] resolved

---

## Progress vs Goals

| Goal | Target | Actual | Status |
|------|--------|--------|--------|
| [Goal 1] | [X] | [X] | ✅/⚠️/❌ |
| [Goal 2] | [X] | [X] | ✅/⚠️/❌ |

---

## Completed This Week

- [Achievement 1]
- [Achievement 2]
- [Achievement 3]

---

## Blocked / At Risk

- **[Item]** — [Blocker description] — [Who can unblock]

---

## Next Week Focus

1. [Priority 1]
2. [Priority 2]
3. [Priority 3]
```

---

### Sprint Retrospective

```markdown
# Sprint [N] Retrospective
**Sprint dates:** [Start] – [End] | **Team:** [Team name]

---

## Sprint Goals vs. Outcomes

| Goal | Completed? | Notes |
|------|-----------|-------|
| [Goal 1] | ✅ Yes | |
| [Goal 2] | ✅ Yes | |
| [Goal 3] | ⚠️ Partial | [What was missed] |

**Velocity:** [X] points planned / [X] delivered ([X]%)

---

## What Went Well 🟢

- [Specific positive]
- [Specific positive]

---

## What Could Improve 🔴

- [Specific problem]
- [Specific problem]

---

## Action Items

| Action | Owner | Done by |
|--------|-------|---------|
| [Action] | [Name] | Sprint [N+1] |
```

---

## PDF Export Script

```javascript
// scripts/export-report-to-pdf.js
import { chromium } from 'playwright';
import { readFile } from 'fs/promises';
import { marked } from 'marked';

const [,, inputFile, outputFile = 'report.pdf'] = process.argv;

const markdown = await readFile(inputFile, 'utf8');
const html = `<!DOCTYPE html>
<html>
<head>
<style>
  body { font-family: system-ui; max-width: 800px; margin: 40px auto; color: #1e293b; }
  h1 { border-bottom: 2px solid #e2e8f0; padding-bottom: 8px; }
  table { width: 100%; border-collapse: collapse; margin: 16px 0; }
  th, td { padding: 8px 12px; border: 1px solid #e2e8f0; text-align: left; }
  th { background: #f8fafc; font-weight: 600; }
  code { background: #f1f5f9; padding: 2px 6px; border-radius: 4px; font-size: 0.9em; }
</style>
</head>
<body>${marked(markdown)}</body>
</html>`;

const browser = await chromium.launch();
const page = await browser.newPage();
await page.setContent(html, { waitUntil: 'networkidle' });
await page.pdf({ path: outputFile, format: 'A4', margin: { top: '40px', bottom: '40px', left: '40px', right: '40px' } });
await browser.close();

console.log(`✅ Report saved to ${outputFile}`);
```

```bash
node scripts/export-report-to-pdf.js report.md report.pdf
```

---

## Delivery Options

| Destination | Method |
|-------------|--------|
| Local file | `report.md` or `report.pdf` |
| Notion | Use connect-apps skill with Notion integration |
| Google Docs | Use connect-apps skill with Google Docs integration |
| Slack | Use connect-apps skill, paste summary in message |
| Email | Use connect-apps skill with Gmail/Outlook integration |
