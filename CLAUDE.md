# Claude Code Skills Portfolio

This repository is a curated collection of Claude Code skills. When working inside this directory, the following skills are available to Claude at the project level.

## Quick Setup (Global Install)

To make all skills available across every project on this machine:

```bash
node scripts/install-skills.js
```

Then restart Claude Code. Skills will be available everywhere.

**Options:**
```bash
node scripts/install-skills.js --dry-run          # preview what will be installed
node scripts/install-skills.js --only dev         # install only development skills
node scripts/install-skills.js --only biz         # install only business/data skills
node scripts/install-skills.js --only creative    # install only creative/design skills
node scripts/install-skills.js --only docs        # install only document skills (pdf, docx, xlsx, pptx)
node scripts/install-skills.js --only comms       # install communication + automation skills
node scripts/install-skills.js --composio         # also install 832 Composio SaaS skills
node scripts/install-skills.js --uninstall        # remove all portfolio skills
node scripts/list-skills.js                       # see all installed skills
```

---

## Available Skills

All skills in this repo are structured as `<skill-name>/SKILL.md`. When working here, you can invoke any of them by name or description.

### Development & Engineering
| Skill | Invoke when... |
|-------|---------------|
| `generating-openapi-specs` | Generating or validating OpenAPI/Swagger specs from code |
| `writing-e2e-tests` | Writing Playwright end-to-end browser tests |
| `reviewing-pull-requests` | Reviewing a PR diff or GitHub pull request |
| `debugging-with-traces` | Analyzing a stack trace, Sentry issue, or crash log |
| `changelog-generator` | Generating changelogs from git commit history |
| `langsmith-fetch` | Fetching LangSmith/LangChain execution traces |
| `mcp-builder` | Creating a new MCP (Model Context Protocol) server |
| `webapp-testing` | Testing a local web app with Playwright |
| `developer-growth-analysis` | Analyzing Claude Code chat history for coding patterns |

### Business, Data & Finance
| Skill | Invoke when... |
|-------|---------------|
| `analyzing-financial-data` | Analyzing P&L, revenue, expenses, burn rate, SaaS metrics |
| `building-dashboards` | Creating Chart.js or Recharts dashboards from CSV/JSON |
| `generating-reports` | Producing executive summaries, incident reports, retros |
| `orchestrating-saas-workflows` | Automating multi-step workflows across 2+ SaaS apps |
| `competitive-ads-extractor` | Extracting competitor ad copy from ad libraries |
| `content-research-writer` | Writing research-backed articles, blog posts, essays |
| `lead-research-assistant` | Researching and qualifying sales leads |
| `twitter-algorithm-optimizer` | Optimizing tweets for reach and engagement |
| `invoice-organizer` | Organizing invoices and receipts for tax preparation |
| `tailored-resume-generator` | Creating job-specific tailored resumes |

### Creative & Design
| Skill | Invoke when... |
|-------|---------------|
| `artifacts-builder` | Building multi-component React/Tailwind HTML artifacts |
| `brand-guidelines` | Applying Anthropic brand colors and typography |
| `canvas-design` | Creating PNG/PDF visual art and design layouts |
| `theme-factory` | Applying color and font themes to artifacts or slides |
| `slack-gif-creator` | Creating optimized animated GIFs for Slack |
| `image-enhancer` | Enhancing image/screenshot quality and resolution |

### Document Processing
| Skill | Invoke when... |
|-------|---------------|
| `pdf` (in `document-skills/pdf/`) | Processing, extracting, merging, or creating PDF files |
| `docx` (in `document-skills/docx/`) | Creating or editing Word documents |
| `pptx` (in `document-skills/pptx/`) | Creating or editing PowerPoint presentations |
| `xlsx` (in `document-skills/xlsx/`) | Working with Excel/spreadsheet files |

### Communication & Automation
| Skill | Invoke when... |
|-------|---------------|
| `internal-comms` | Writing internal memos, announcements, all-hands |
| `connect` | Connecting Claude to external apps via Composio |
| `connect-apps` | Using Gmail, Slack, GitHub, Notion via Composio |
| `orchestrating-saas-workflows` | Running multi-app automation sequences |
| `meeting-insights-analyzer` | Analyzing meeting transcripts for action items |
| `skill-share` | Creating and publishing new skills to Slack |

### Utilities
| Skill | Invoke when... |
|-------|---------------|
| `file-organizer` | Organizing files and folders intelligently |
| `raffle-winner-picker` | Selecting random winners from a list or spreadsheet |
| `video-downloader` | Downloading YouTube or other videos with yt-dlp |
| `domain-name-brainstormer` | Generating and checking domain name availability |

### Meta / Skill Creation
| Skill | Invoke when... |
|-------|---------------|
| `skill-creator` | Creating a new Claude Code skill from scratch |

---

## Skill Standards

All skills follow the [skill-builder](https://github.com/Infiniteyieldai/skill-builder) conventions:
- Names in gerund form: `reviewing-pull-requests`, not `pr-reviewer`
- Description starts with "Use this skill when..."
- Max 1024 chars in description, max 64 chars in name
- No `allowed-tools`, `model`, or `tools` in YAML frontmatter
- Scripts use Node.js ESM (no Python)
- SKILL.md under 500 lines (progressive disclosure to reference files)

## Adding New Skills

1. Create a new directory: `<gerund-name>/SKILL.md`
2. Follow the template in [skill-builder/templates/skill-template.md](https://github.com/Infiniteyieldai/skill-builder/blob/main/templates/skill-template.md)
3. For API-wrapping skills: use `api-skill-template.md`
4. For multi-step workflows: use `workflow-skill-template.md`
5. Run `node scripts/install-skills.js` to make it available globally
6. Update `CATALOG.md` with the new skill

## Repository Map

```
awesome-claude-skills/
├── CATALOG.md                    ← unified skill index
├── CLAUDE.md                     ← this file
├── scripts/
│   ├── install-skills.js         ← global installer
│   └── list-skills.js            ← inventory viewer
├── <skill-name>/
│   ├── SKILL.md                  ← skill definition
│   └── *.md                      ← optional reference files
├── document-skills/
│   ├── pdf/ docx/ pptx/ xlsx/    ← sub-skills
└── composio-skills/              ← 832 Composio SaaS skills (install with --composio)
```
