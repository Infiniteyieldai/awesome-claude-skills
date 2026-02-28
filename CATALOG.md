# Claude Skills Catalog

A unified, navigable index of every skill in this portfolio — organized by category with trigger keywords, status indicators, and installation notes.

> **Quick navigation:** [Creative & Design](#creative--design) · [Document Processing](#document-processing) · [Development & Engineering](#development--engineering) · [Business & Marketing](#business--marketing) · [Productivity & Organization](#productivity--organization) · [Communication](#communication) · [Automation & Integration](#automation--integration) · [Career & HR](#career--hr) · [Utilities](#utilities) · [Meta / Skill Creation](#meta--skill-creation) · [Composio SaaS Skills (832)](#composio-saas-automations) · [Community Skills](#community-skills)

---

## Status Key

| Symbol | Meaning |
|--------|---------|
| ✅ | Complete — well-formed name, description, and instructions |
| ⚠️ | Needs attention — missing SKILL.md at root, placeholder description, or outdated format |
| 🆕 | Planned — identified gap, skill not yet created |

---

## Installation

**Personal (all projects):**
```bash
# Copy any skill directory to:
~/.claude/skills/<skill-name>/
```

**Project-specific:**
```bash
# Copy any skill directory to:
.claude/skills/<skill-name>/
```

**Via CLI (claude-code-templates):**
```bash
npx claude-code-templates@latest
# then select: Skills → install individual skill or bundle
```

---

## Creative & Design

Skills for generating visual artifacts, applying brand guidelines, and creating media.

| Skill | Name | Trigger Keywords | Status |
|-------|------|-----------------|--------|
| [artifacts-builder](./artifacts-builder/) | `artifacts-builder` | React, Tailwind, shadcn/ui, HTML artifact, multi-component, UI prototype | ✅ |
| [brand-guidelines](./brand-guidelines/) | `brand-guidelines` | Anthropic brand, brand colors, Poppins, Lora, typography, brand identity | ✅ |
| [canvas-design](./canvas-design/) | `canvas-design` | PNG, PDF, visual art, design, illustration, layout, graphic | ✅ |
| [theme-factory](./theme-factory/) | `theme-factory` | theme, fonts, colors, styling, slides, docs, dark mode, design system | ✅ |
| [slack-gif-creator](./slack-gif-creator/) | `slack-gif-creator` | GIF, Slack, animated, reaction gif, 128KB, optimize | ✅ |
| [image-enhancer](./image-enhancer/) | `image-enhancer` | image quality, screenshot, enhance, resolution, upscale, sharpen | ✅ |

---

## Document Processing

Skills for creating, reading, transforming, and manipulating documents.

| Skill | Name | Trigger Keywords | Status |
|-------|------|-----------------|--------|
| [document-skills/pdf](./document-skills/pdf/) | `pdf` | PDF, extract text, merge, split, rotate, watermark, OCR, pypdf, pdfplumber, reportlab | ✅ |
| [document-skills/docx](./document-skills/docx/) | `docx` | Word document, .docx, OOXML, docx-js, create Word, edit document | ✅ |
| [document-skills/pptx](./document-skills/pptx/) | `pptx` | PowerPoint, presentation, .pptx, slides, html2pptx | ✅ |
| [document-skills/xlsx](./document-skills/xlsx/) | `xlsx` | Excel, spreadsheet, .xlsx, workbook, formula, cells | ✅ |
| *(root)* | — | — | ⚠️ No root SKILL.md — navigate to sub-skills above |

---

## Development & Engineering

Skills for software development workflows, debugging, testing, and infrastructure.

| Skill | Name | Trigger Keywords | Status |
|-------|------|-----------------|--------|
| [changelog-generator](./changelog-generator/) | `changelog-generator` | changelog, release notes, git commits, version history, CHANGELOG.md | ✅ |
| [langsmith-fetch](./langsmith-fetch/) | `langsmith-fetch` | LangSmith, LangChain, LangGraph, trace, execution log, debug agent | ✅ |
| [mcp-builder](./mcp-builder/) | `mcp-builder` | MCP server, Model Context Protocol, build MCP, tool server, create MCP | ✅ |
| [webapp-testing](./webapp-testing/) | `webapp-testing` | Playwright, web testing, browser automation, e2e, test local app, screenshot | ✅ |
| [developer-growth-analysis](./developer-growth-analysis/) | `developer-growth-analysis` | coding patterns, Claude Code history, developer metrics, growth, productivity | ✅ |
| — | `generating-openapi-specs` | OpenAPI, Swagger, API spec, REST schema, endpoint documentation | 🆕 |
| — | `writing-e2e-tests` | Playwright, Cypress, end-to-end, e2e test, browser test, integration test | 🆕 |
| — | `reviewing-pull-requests` | PR review, code review, pull request, diff, feedback, GitHub review | 🆕 |
| — | `debugging-with-traces` | Sentry, error trace, stack trace, debug, exception, crash report | 🆕 |

---

## Business & Marketing

Skills for competitive intelligence, content, lead generation, and social media.

| Skill | Name | Trigger Keywords | Status |
|-------|------|-----------------|--------|
| [competitive-ads-extractor](./competitive-ads-extractor/) | `competitive-ads-extractor` | competitor ads, Facebook ad library, LinkedIn ads, ad analysis, ad copy | ✅ |
| [content-research-writer](./content-research-writer/) | `content-research-writer` | write article, content, research, citations, blog post, essay, SEO | ✅ |
| [lead-research-assistant](./lead-research-assistant/) | `lead-research-assistant` | leads, prospects, qualify leads, ICP, sales research, outreach | ✅ |
| [twitter-algorithm-optimizer](./twitter-algorithm-optimizer/) | `twitter-algorithm-optimizer` | tweet, Twitter, X, engagement, algorithm, reach, impressions, viral | ✅ |
| — | `analyzing-financial-data` | revenue, expenses, P&L, balance sheet, financial analysis, forecast | 🆕 |
| — | `building-dashboards` | dashboard, visualization, chart, metrics, KPI, analytics UI | 🆕 |
| — | `generating-reports` | report, data summary, executive summary, insights, export PDF | 🆕 |

---

## Productivity & Organization

Skills for managing files, meetings, and financial records.

| Skill | Name | Trigger Keywords | Status |
|-------|------|-----------------|--------|
| [file-organizer](./file-organizer/) | `file-organizer` | organize files, sort files, rename, folder structure, clean up, directory | ✅ |
| [meeting-insights-analyzer](./meeting-insights-analyzer/) | `meeting-insights-analyzer` | meeting transcript, recording, action items, meeting notes, Zoom, Otter | ✅ |
| [invoice-organizer](./invoice-organizer/) | `invoice-organizer` | invoices, receipts, taxes, expense, accounting, organize documents, tax prep | ✅ |

---

## Communication

Skills for drafting internal and external written communications.

| Skill | Name | Trigger Keywords | Status |
|-------|------|-----------------|--------|
| [internal-comms](./internal-comms/) | `internal-comms` | internal communication, announcement, memo, all-hands, company update, Slack message | ✅ |

---

## Automation & Integration

Skills for connecting Claude to external apps and SaaS services.

| Skill | Name | Trigger Keywords | Status |
|-------|------|-----------------|--------|
| [connect](./connect/) | `connect` | connect app, send email, create issue, post message, Composio, automate | ✅ |
| [connect-apps](./connect-apps/) | `connect-apps` | Gmail, Slack, GitHub, Notion, Google Sheets, external app, OAuth | ✅ |
| [connect-apps-plugin](./connect-apps-plugin/) | — | Plugin format (not a skill) — uses `/connect-apps:setup` command | ⚠️ |
| [skill-share](./skill-share/) | `skill-share` | share skill, publish skill, Slack notification, skill distribution, community | ✅ |
| — | `orchestrating-saas-workflows` | workflow automation, chain actions, multi-step, Zapier-like, trigger pipeline | 🆕 |

> **Composio skills:** 832 individual SaaS app automations live in [composio-skills/](./composio-skills/). See [Composio SaaS Automations](#composio-saas-automations) section.

---

## Career & HR

Skills for job searching, resume writing, and career development.

| Skill | Name | Trigger Keywords | Status |
|-------|------|-----------------|--------|
| [tailored-resume-generator](./tailored-resume-generator/) | `tailored-resume-generator` | resume, job application, CV, cover letter, job description, tailor | ✅ |

---

## Utilities

General-purpose utility skills.

| Skill | Name | Trigger Keywords | Status |
|-------|------|-----------------|--------|
| [domain-name-brainstormer](./domain-name-brainstormer/) | `domain-name-brainstormer` | domain name, .com availability, startup name, brand name, domain check | ✅ |
| [raffle-winner-picker](./raffle-winner-picker/) | `raffle-winner-picker` | raffle, giveaway, winner, random selection, lottery, contest, Google Sheets | ✅ |
| [video-downloader](./video-downloader/) | `youtube-downloader` | download video, YouTube, yt-dlp, mp4, audio extract, video quality | ✅ |

---

## Meta / Skill Creation

Skills for building, improving, and distributing other skills.

| Skill | Name | Trigger Keywords | Status |
|-------|------|-----------------|--------|
| [skill-creator](./skill-creator/) | `skill-creator` | create skill, new skill, build skill, SKILL.md, skill template | ✅ |
| [template-skill](./template-skill/) | `template-skill` | — | ⚠️ Placeholder description — do not install as-is |
| *(skill-builder repo)* | `skill-builder` | create skill, edit skill, convert sub-agent, skill metadata, gerund naming | ✅ |

> **skill-builder** lives in the separate [skill-builder](https://github.com/Infiniteyieldai/skill-builder) repo. Install from `~/.claude/skills/skill-builder/`.

---

## Composio SaaS Automations

**832 skills** in [composio-skills/](./composio-skills/) — one per SaaS app action, all powered by Composio's Rube MCP.

### Prerequisites
1. Get a free API key at [platform.composio.dev](https://platform.composio.dev)
2. Install the connect-apps-plugin: `claude --plugin-dir ./connect-apps-plugin`
3. Run `/connect-apps:setup` and paste your key

### Categories (sample)

| Category | Apps Covered |
|----------|-------------|
| Productivity | Notion, Airtable, Google Docs, Sheets, Calendar |
| Communication | Gmail, Outlook, Slack, Discord, Teams, Zoom |
| Dev Tools | GitHub, GitLab, Jira, Linear, Sentry |
| CRM / Sales | HubSpot, Salesforce, Apollo, Pipedrive |
| Cloud | AWS, GCP, Azure |
| Design | Figma, Canva, Adobe |
| Finance | Stripe, QuickBooks, Xero |
| Marketing | Mailchimp, Klaviyo, HubSpot, Intercom |
| Data | Supabase, MongoDB, PostgreSQL, Snowflake |

> Browse all 832 skills: `ls composio-skills/`

---

## Community Skills

Skills maintained externally and linked from this catalog. See [README.md](./README.md) for the full curated list.

### By Category

| Category | Notable Skills |
|----------|---------------|
| Document Processing | pdf, docx, xlsx, pptx (above), pandoc, markdown |
| Development | git workflows, Docker, Terraform, AWS Lambda, CI/CD |
| Data Analysis | CSV/xsv, SQL, Jupyter, pandas, dbt |
| Business/Marketing | SEO, email campaigns, social scheduling |
| Communication | Slack bots, email templates, meeting notes |
| Creative/Media | Image generation, video editing, Remotion |
| Productivity | Calendar management, task tracking, note-taking |
| Collaboration | GitHub PRs, Notion pages, Confluence docs |
| Security | Security audits, dependency scanning, secret detection |

---

## Planned Skills (Roadmap)

Skills identified as high-value gaps to build next. See [CONTRIBUTING.md](./CONTRIBUTING.md) to contribute.

### Phase 2 — Development
- `generating-openapi-specs` — Generate OpenAPI 3.x specs from existing code/routes
- `writing-e2e-tests` — Playwright patterns for testing web applications
- `reviewing-pull-requests` — Structured PR review with actionable feedback
- `debugging-with-traces` — Sentry/error trace analysis and fix suggestions

### Phase 2 — Business & Data
- `analyzing-financial-data` — P&L, balance sheet, forecast analysis
- `building-dashboards` — Chart.js/Recharts visualization from CSV/JSON
- `generating-reports` — Structured data to formatted PDF/Markdown reports

### Phase 2 — Creative & Media
- `creating-video-content` — Remotion-based programmatic video generation
- `designing-presentations` — Full slide deck generation from outline

### Phase 2 — Automation
- `orchestrating-saas-workflows` — Multi-step Composio workflow chaining

---

## Standards Reference

All skills in this portfolio follow the [skill-builder](https://github.com/Infiniteyieldai/skill-builder) standards:

| Rule | Requirement |
|------|------------|
| Name format | Gerund form: `processing-pdfs` not `pdf-processor` |
| Name length | Max 64 characters |
| Description | Starts with "Use this skill when..." |
| Description length | Max 1024 characters |
| Voice | Third person |
| Forbidden YAML fields | `allowed-tools`, `model`, `tools` |
| Scripts | Node.js ESM (`.js`) preferred over Python |
| File naming | Intention-revealing names, not `helpers.md` or `utils.md` |
| SKILL.md length | Under 500 lines — use progressive disclosure |

---

*Last updated: 2026-02-28 | Maintained by Infiniteyieldai*
