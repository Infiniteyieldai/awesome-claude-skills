# Complete Claude Capabilities Guide

Everything Claude can do for you -- skills, built-in tools, workflows, and hidden features -- in one place. Describe what you need and match it to the right capability.

---

## Table of Contents

1. [How to Use This Guide](#how-to-use-this-guide)
2. [Quick Lookup: "I want to..."](#quick-lookup-i-want-to)
3. [Built-In Core Tools](#built-in-core-tools)
4. [Skills Reference](#skills-reference)
5. [Web & Research](#web--research)
6. [Git & GitHub](#git--github)
7. [Multi-Agent System](#multi-agent-system)
8. [Automation & Hooks](#automation--hooks)
9. [MCP Integrations](#mcp-integrations)
10. [Slash Commands](#slash-commands)
11. [Keyboard Shortcuts](#keyboard-shortcuts)
12. [Hidden / Power-User Features](#hidden--power-user-features)
13. [External / Community Skills](#external--community-skills)

---

## How to Use This Guide

**You don't need to memorise any of this.** Just describe what you want in plain language and Claude will pick the right tool, skill, or combination. This document exists so you can browse what's possible and get ideas.

**Pattern:** "I want to [outcome]" -> Look up the matching section -> Ask Claude to do it.

---

## Quick Lookup: "I want to..."

### Documents & Files
| I want to... | Use this |
|---|---|
| Create/edit a Word document | **docx** skill |
| Create/edit a PDF | **pdf** skill |
| Create/edit a PowerPoint | **pptx** skill |
| Create/edit an Excel spreadsheet | **xlsx** skill |
| Fill in a PDF form | **pdf** skill (form filling) |
| Merge multiple PDFs | **pdf** skill (merge) |
| Extract text/tables from a PDF | **pdf** skill (pdfplumber) |
| Organise my messy files | **file-organizer** skill |
| Organise invoices/receipts for tax | **invoice-organizer** skill |

### Writing & Content
| I want to... | Use this |
|---|---|
| Write a blog post / article | **content-research-writer** skill |
| Write internal team updates | **internal-comms** skill |
| Generate release notes from commits | **changelog-generator** skill |
| Tailor my CV/resume for a job | **tailored-resume-generator** skill |
| Research a topic with citations | **content-research-writer** skill |

### Design & Creative
| I want to... | Use this |
|---|---|
| Create a poster / visual art | **canvas-design** skill |
| Apply a professional theme to slides/docs | **theme-factory** skill (10 pre-set themes) |
| Apply Anthropic brand styling | **brand-guidelines** skill |
| Make an animated GIF for Slack | **slack-gif-creator** skill |
| Enhance/upscale an image | **image-enhancer** skill |
| Download a YouTube video | **video-downloader** skill |
| Build an interactive web component | **artifacts-builder** skill |

### Business & Marketing
| I want to... | Use this |
|---|---|
| Find sales leads for my product | **lead-research-assistant** skill |
| Analyse competitor ads | **competitive-ads-extractor** skill |
| Brainstorm domain names | **domain-name-brainstormer** skill |
| Analyse my meeting recordings | **meeting-insights-analyzer** skill |

### Development & Code
| I want to... | Use this |
|---|---|
| Read / understand code | Built-in **Read**, **Grep**, **Glob** tools |
| Edit / refactor code | Built-in **Edit** tool |
| Run commands / scripts | Built-in **Bash** tool |
| Run tests | Built-in **Bash** tool |
| Test a web app in a browser | **webapp-testing** skill |
| Build an MCP server | **mcp-builder** skill |
| Debug a LangChain/LangGraph agent | **langsmith-fetch** skill |
| Create a new Claude skill | **skill-creator** skill |
| Analyse my coding growth | **developer-growth-analysis** skill |

### Integrations & Actions
| I want to... | Use this |
|---|---|
| Send an email | **connect** / **connect-apps** (Gmail, Outlook, SendGrid) |
| Post a Slack message | **connect** / **connect-apps** |
| Create a GitHub issue | **connect** / **connect-apps** or built-in **gh** CLI |
| Update a Notion page | **connect** / **connect-apps** |
| Post to social media | **connect** / **connect-apps** (Twitter, LinkedIn) |
| Query a database | **connect** / **connect-apps** (PostgreSQL, Airtable) |

### Other
| I want to... | Use this |
|---|---|
| Pick raffle/giveaway winners | **raffle-winner-picker** skill |
| Share a skill with my team | **skill-share** skill |
| Search the web for current info | Built-in **WebSearch** tool |
| Fetch & analyse a web page | Built-in **WebFetch** tool |
| Work with a Jupyter notebook | Built-in **NotebookEdit** tool |

---

## Built-In Core Tools

These are always available -- no skills or setup needed.

### File Operations

| Tool | What It Does | Example |
|---|---|---|
| **Read** | Read any file (code, images, PDFs, notebooks) | "Read my config file" |
| **Write** | Create a new file from scratch | "Create a Python script that..." |
| **Edit** | Surgically edit specific parts of existing files | "Change the function name from X to Y" |
| **Glob** | Find files by pattern | "Find all TypeScript files in src/" |
| **Grep** | Search file contents with regex | "Find everywhere we call `fetchUser`" |

### Execution

| Tool | What It Does | Example |
|---|---|---|
| **Bash** | Run any shell command | "Run the tests", "Install dependencies" |
| **Background tasks** | Run long commands without blocking | "Start the dev server in the background" |

### Web

| Tool | What It Does | Example |
|---|---|---|
| **WebSearch** | Search the internet for current information | "What's the latest version of React?" |
| **WebFetch** | Fetch and analyse a specific URL | "Read this documentation page" |

### Interaction

| Tool | What It Does | Example |
|---|---|---|
| **AskUserQuestion** | Ask you clarifying questions | (Used automatically when Claude needs input) |
| **TodoWrite** | Track multi-step tasks with progress | (Used automatically for complex tasks) |
| **NotebookEdit** | Edit Jupyter notebook cells | "Add a new code cell to my notebook" |

### Multi-Agent

| Tool | What It Does | Example |
|---|---|---|
| **Task** (Explore agent) | Fast, parallel codebase research | "Find how authentication works in this codebase" |
| **Task** (Plan agent) | Architect a solution before implementing | "Plan how to add user roles" |
| **Task** (General agent) | Handle complex multi-step sub-tasks | "Research and summarise all API endpoints" |
| **Task** (Bash agent) | Run commands in isolated context | "Run the full test suite and report results" |

### Image & Visual

| Capability | What It Does | Example |
|---|---|---|
| **Read images** | View and analyse screenshots, photos, diagrams | "What's in this screenshot?" |
| **Clipboard paste** | Paste images directly with Ctrl+V | Paste a UI mockup for review |
| **Read PDFs** | Analyse PDF documents page by page | "Summarise this 50-page report" |

---

## Skills Reference

### Document Processing

#### docx (Word Documents)
- **Create** new .docx files with formatting, headers, tables
- **Edit** existing documents preserving all formatting
- **Track changes** with insertions/deletions (redlining)
- **Add comments** for review workflows
- **Convert** DOCX to PDF/JPEG for visual review
- **Extract text** preserving structure
- **Prereqs:** pandoc, docx npm package, LibreOffice

#### pdf (PDF Documents)
- **Extract** text, tables, metadata, images from PDFs
- **Create** new PDFs with reportlab
- **Merge** multiple PDFs into one
- **Split** PDFs by page ranges
- **Fill forms** programmatically
- **OCR** scanned documents
- **Add** watermarks and password protection
- **Prereqs:** pypdf, pdfplumber, reportlab, pytesseract

#### pptx (PowerPoint Presentations)
- **Create** presentations from scratch (HTML to PPTX workflow)
- **Edit** existing slides preserving formatting
- **Template** support with slide masters and layouts
- **Speaker notes** and comments
- **Convert** to PDF/JPEG thumbnails
- **Rearrange** slides with rearrange.py
- **Prereqs:** markitdown, pptxgenjs, playwright, LibreOffice

#### xlsx (Excel Spreadsheets)
- **Create** spreadsheets with formulas (never hardcoded values)
- **Analyse** data with pandas
- **Format** cells, colours, number formats
- **Multiple sheets** in one workbook
- **Recalculate** formulas via LibreOffice
- **Financial model** standards (colour coding, formatting)
- **Prereqs:** openpyxl, pandas, LibreOffice

---

### Development & Code

#### artifacts-builder
- Builds complex interactive HTML artifacts with React 18, TypeScript, Tailwind, shadcn/ui
- 40+ pre-installed components
- Bundles into single HTML file
- **Best for:** Interactive dashboards, complex UI prototypes, multi-component web tools

#### changelog-generator
- Scans git history and produces customer-friendly release notes
- Categorises: features, fixes, improvements, breaking changes, security
- Filters out internal noise (refactoring, tests)
- **Best for:** Release notes, app store descriptions, product update emails

#### developer-growth-analysis
- Reads your Claude Code chat history (last 24-48 hours)
- Identifies patterns, gaps, and improvement areas
- Curates learning resources from HackerNews
- Sends report to Slack DMs
- **Best for:** Weekly self-assessment, skill gap identification

#### langsmith-fetch
- Fetches execution traces from LangSmith Studio
- Analyses agent behaviour, errors, tool calls, memory
- Multiple output formats
- **Best for:** Debugging LangChain/LangGraph agents
- **Prereqs:** langsmith-fetch CLI, LANGSMITH_API_KEY env var

#### mcp-builder
- 4-phase guide: Research, Implement, Review, Evaluate
- Agent-centric design principles
- Python (FastMCP) and TypeScript (MCP SDK) guides
- **Best for:** Building MCP servers that connect Claude to external APIs

#### webapp-testing
- Playwright-based browser automation
- Screenshots, DOM inspection, console logs
- Server lifecycle management
- **Best for:** Testing web apps after code changes, capturing screenshots, debugging UI

---

### Business & Marketing

#### brand-guidelines
- Anthropic's official colours (Dark, Light, Orange, Blue, Green, grays)
- Typography: Poppins (headings) + Lora (body)
- Accent colour cycling
- **Best for:** Anthropic-branded materials, consistent visual identity

#### competitive-ads-extractor
- Extracts ads from Facebook Ad Library, LinkedIn, etc.
- Captures screenshots, analyses messaging and trends
- Categorises by theme, audience, format
- **Best for:** Competitive research, campaign planning, ad inspiration

#### domain-name-brainstormer
- Generates 10-15 creative domain options per session
- Checks availability across 9 TLDs (.com, .io, .dev, .ai, .app, .co, .xyz, .design, .tech)
- Brandability analysis and pricing context
- **Best for:** New projects, product launches, rebranding

#### internal-comms
- Templates for 3P updates, newsletters, FAQs, status reports, incident reports
- Adapts to company-specific communication styles
- **Best for:** Team updates, leadership reports, any internal communication

#### lead-research-assistant
- Analyses your product/service value proposition
- Finds target companies by industry, size, tech stack, pain points
- Scores leads 1-10, provides outreach strategies
- Decision-maker info and LinkedIn URLs
- CRM-ready export format
- **Best for:** Sales prospecting, building target account lists, outreach planning

---

### Communication & Writing

#### content-research-writer
- Collaborative outlining and structuring
- Research with proper citations (inline, numbered, footnote)
- Hook improvement and voice preservation
- Section-by-section feedback during writing
- **Best for:** Blog posts, articles, newsletters, case studies, thought leadership

#### meeting-insights-analyzer
- Conflict avoidance detection
- Speaking ratio analysis
- Filler word tracking
- Active listening and leadership evaluation
- Trend tracking across multiple meetings
- **Best for:** Communication coaching, performance reviews, leadership development
- **Needs:** Transcript in .txt, .md, .vtt, .srt, or .docx

---

### Creative & Media

#### canvas-design
- Two-step process: design philosophy manifesto then visual output
- Museum/magazine quality PNG and PDF output
- Bundled fonts from canvas-fonts directory
- **Best for:** Posters, artwork, branded graphics, visual compositions

#### image-enhancer
- Resolution enhancement, sharpness improvement, noise reduction
- Optimises for web, print, or social media
- Batch processing with original backup
- **Best for:** Screenshot cleanup, image upscaling, print preparation

#### slack-gif-creator
- Slack-optimised (2MB messages, 64KB emoji)
- 12 animation primitives (shake, bounce, spin, pulse, fade, zoom, explode, wiggle, slide, flip, morph, move)
- Size and dimension validators
- **Best for:** Slack channel GIFs, custom reaction emojis, team animations

#### theme-factory
- **10 pre-set themes:** Ocean Depths, Sunset Boulevard, Forest Canopy, Modern Minimalist, Golden Hour, Arctic Frost, Desert Rose, Tech Innovation, Botanical Garden, Midnight Galaxy
- Custom theme generation on-the-fly
- Applies to slides, docs, reports, HTML pages
- **Best for:** Consistent professional styling across any artifact

#### video-downloader
- YouTube and other platforms
- Quality: best, 1080p, 720p, 480p, 360p
- Formats: mp4, webm, mkv, mp3 (audio-only)
- **Best for:** Downloading videos for offline use, audio extraction

---

### Productivity & Organisation

#### file-organizer
- Analyses folder structure, finds duplicates (MD5)
- Suggests logical organisation schemes
- Automates cleanup with conflict handling
- **Best for:** Downloads cleanup, project organisation, duplicate removal

#### invoice-organizer
- Reads PDFs, images, bank statements
- Extracts vendor, date, amount, description
- Renames: `YYYY-MM-DD Vendor - Invoice - Product.pdf`
- Organises by vendor, category, time period, or tax category
- CSV export for accountants
- **Best for:** Tax preparation, expense management, bookkeeping

#### raffle-winner-picker
- Cryptographically secure random selection
- Accepts CSV, Excel, Google Sheets, plain lists
- Multiple winners, exclusions, weighted selection, runner-ups
- **Best for:** Giveaways, raffles, contests, random team assignments

#### tailored-resume-generator
- Analyses job description keywords and priorities
- Maps your experience to requirements
- ATS optimisation with keyword incorporation
- Gap analysis and interview prep tips
- **Best for:** Job applications, career transitions, maximising callbacks

---

### Integrations & Connections

#### connect / connect-apps
- **1000+ apps** via Composio
- **Email:** Gmail, Outlook, SendGrid
- **Chat:** Slack, Discord, Teams, Telegram
- **Dev:** GitHub, GitLab, Jira, Linear
- **Docs:** Notion, Google Docs, Confluence
- **Data:** Sheets, Airtable, PostgreSQL
- **CRM:** HubSpot, Salesforce, Pipedrive
- **Storage:** Drive, Dropbox, S3
- **Social:** Twitter, LinkedIn, Reddit
- Takes real actions (not just generates text about them)
- **Setup:** Free API key from platform.composio.dev

#### skill-share
- Creates and packages skills with proper structure
- Automatically posts to Slack for team discovery
- **Best for:** Distributing custom skills across a team

---

### Meta / Skill Development

#### skill-creator
- 6-phase guide for building new skills
- Script management, reference material organisation
- SKILL.md best practices and validation
- **Best for:** Creating new Claude skills from scratch

#### template-skill
- Blank starter template with correct directory structure
- **Best for:** Starting point for a new skill

---

## Web & Research

### What Claude Can Do Online

| Capability | How | Example |
|---|---|---|
| **Search the web** | WebSearch tool | "What's the latest Next.js version?" |
| **Read any URL** | WebFetch tool | "Summarise this documentation page" |
| **Automate a browser** | Chrome integration (`--chrome` flag) | "Fill in this form and submit" |
| **Capture screenshots** | Chrome / Playwright | "Screenshot my app's homepage" |
| **Read console logs** | Chrome integration | "Check for JavaScript errors on my site" |

---

## Git & GitHub

### Built-In Git Capabilities

| Action | How |
|---|---|
| View status, diff, log | `git status`, `git diff`, `git log` via Bash |
| Create / switch branches | `git checkout -b`, `git switch` |
| Stage and commit | `git add`, `git commit` |
| Push / pull | `git push`, `git pull` |
| Create a PR | `gh pr create` via GitHub CLI |
| View PR comments | `gh api repos/owner/repo/pulls/N/comments` |
| View issues | `gh issue view N` |
| Rebase / merge | `git rebase`, `git merge` |
| Stash changes | `git stash` |
| View blame / history | `git blame`, `git log --follow` |
| Work across branches | Git worktree support for parallel sessions |

### GitHub-Specific Features
- PR status shown in footer (green/yellow/red)
- Link sessions to PRs with `--from-pr`
- Create PRs with title, body, labels
- Comment on existing PRs and issues

---

## Multi-Agent System

Claude can spawn specialised sub-agents for parallel or isolated work:

| Agent Type | What It Does | Best For |
|---|---|---|
| **Explore** | Fast, read-only codebase research | Finding files, understanding code, searching patterns |
| **Plan** | Read-only architectural planning | Designing solutions before implementing |
| **General-purpose** | Full multi-step tasks with all tools | Complex research, multi-file operations |
| **Bash** | Isolated command execution | Running test suites, build commands |

### Key Patterns
- **Parallel research:** Launch multiple Explore agents simultaneously for faster answers
- **Plan then implement:** Use Plan agent first, then implement based on the plan
- **Background work:** Run agents in background while continuing to chat
- **Context isolation:** Keep large operations out of the main conversation

---

## Automation & Hooks

Hooks let you automate actions in response to Claude events:

| Hook Event | When It Fires | Example Use |
|---|---|---|
| **SessionStart** | Session begins/resumes | Run setup scripts, load environment |
| **UserPromptSubmit** | Before processing your message | Validate inputs, inject context |
| **PreToolUse** | Before any tool runs | Block edits to protected files |
| **PostToolUse** | After a tool succeeds | Auto-format code after edits |
| **Stop** | When Claude finishes responding | Run linters, send notifications |
| **Notification** | When Claude needs your input | Desktop notification alerts |

### Hook Types
- **Command hooks** -- run shell scripts (exit 0 = allow, exit 2 = block)
- **Prompt-based hooks** -- use Claude for yes/no decisions
- **Agent-based hooks** -- use a subagent with full tool access

---

## MCP Integrations

MCP (Model Context Protocol) connects Claude to external tools and services:

- **What it does:** Adds custom tools beyond the built-ins
- **Where to configure:** `~/.claude/mcp.json` (user) or `.claude/mcp.json` (project)
- **Server types:** Local (stdio), Remote HTTP, Remote SSE
- **Auth:** OAuth handled automatically
- **Tool search:** Loads tools on demand to save context space
- **Access resources:** `@server:resource` syntax

### Common MCP Servers
- Database connectors (PostgreSQL, MySQL, SQLite)
- API integrations (Stripe, Twilio, etc.)
- File system extensions
- Custom business logic

---

## Slash Commands

| Command | What It Does |
|---|---|
| `/help` | Show help and usage info |
| `/clear` | Clear conversation history |
| `/compact` | Compress conversation to free up context |
| `/context` | Visual breakdown of what's using context space |
| `/cost` | Show token usage and costs |
| `/model` | Change AI model (Sonnet, Opus, Haiku) |
| `/continue` | Resume most recent session |
| `/resume` | Open session picker to resume any session |
| `/rewind` | Undo recent edits and conversation |
| `/rename <name>` | Name current session for easy finding |
| `/fork-session` | Branch conversation from current point |
| `/init` | Initialise project with CLAUDE.md |
| `/memory` | Edit CLAUDE.md memory files |
| `/mcp` | Manage MCP server connections |
| `/hooks` | Configure automation hooks |
| `/agents` | Create and manage custom subagents |
| `/config` | Open settings interface |
| `/status` | Show version, model, account info |
| `/export` | Export conversation to file or clipboard |
| `/copy` | Copy last response to clipboard |
| `/stats` | View usage stats and streaks |
| `/vim` | Enable vim-style editing |
| `/fast` | Toggle fast mode (faster responses) |
| `/plan` | Enter plan mode (read-only exploration) |
| `/debug` | Troubleshoot current session |
| `/doctor` | Check installation health |
| `/todos` | List current TODO items |
| `/theme` | Change colour theme |
| `/tasks` | List background tasks |
| `/desktop` | Hand off to Desktop app |
| `/teleport` | Resume a web session in terminal |

---

## Keyboard Shortcuts

### Essential
| Shortcut | Action |
|---|---|
| `Ctrl+C` | Cancel / interrupt |
| `Ctrl+V` / `Cmd+V` | Paste image from clipboard |
| `Ctrl+O` | Toggle verbose output (see Claude's reasoning) |
| `Ctrl+T` | Toggle task list view |
| `Ctrl+B` | Move running task to background |
| `Ctrl+G` | Open prompt in text editor |
| `Ctrl+R` | Reverse search command history |
| `Shift+Tab` | Cycle permission modes |
| `Esc+Esc` | Rewind / summarise from a point |
| `Alt+P` | Switch models |
| `Alt+T` | Toggle extended thinking |
| `Shift+Enter` | New line in input (multi-line) |
| `!command` | Run bash command directly |

### Editing
| Shortcut | Action |
|---|---|
| `Ctrl+K` | Delete to end of line |
| `Ctrl+U` | Delete entire line |
| `Ctrl+Y` | Paste deleted text |
| `Alt+B` / `Alt+F` | Move back/forward one word |

---

## Hidden / Power-User Features

Things you might not know Claude can do:

| Feature | How |
|---|---|
| **Paste screenshots** | `Ctrl+V` to paste an image from clipboard for analysis |
| **Pipe data in** | `cat file.csv \| claude -p "analyse this data"` |
| **Background tasks** | `Ctrl+B` moves long operations to background |
| **Vim mode** | `/vim` enables vim-style text editing |
| **Session naming** | `/rename my-feature` for easy session finding |
| **Visual context map** | `/context` shows what's using your context window |
| **Plan mode** | `/plan` for safe, read-only exploration before changes |
| **Budget limits** | `--max-budget-usd 5` caps spending on a session |
| **JSON output** | `--json-schema '{...}'` for structured, validated output |
| **Headless mode** | `claude -p "task" --output-format json` for CI/CD |
| **Effort control** | `/model` to adjust reasoning depth (low/medium/high) |
| **Fallback model** | `--fallback-model sonnet` auto-switches if overloaded |
| **PR linking** | `--from-pr 123` resumes sessions tied to a PR |
| **Git worktrees** | Parallel sessions on different branches simultaneously |
| **Agent teams** | Multiple independent agents coordinating on a shared task list |
| **Custom keybindings** | Edit `~/.claude/keybindings.json` for custom shortcuts |
| **Checkpoint rewind** | Automatic snapshots before every edit, rewind anytime |
| **Chrome automation** | `--chrome` flag for full browser control |
| **MCP tool search** | Tools loaded on-demand to save context space |
| **Subagent memory** | Subagents learn and remember across conversations |

---

## External / Community Skills

Maintained in separate repositories (install separately):

### Development
| Skill | What It Does |
|---|---|
| AWS Skills | CDK best practices, cost optimisation, serverless patterns |
| D3.js Visualization | D3 charts and interactive data visualisations |
| FFUF Web Fuzzing | Web fuzzer for vulnerability analysis |
| iOS Simulator | Test and debug iOS apps in Simulator |
| Move Code Quality | Move language quality checklist analysis |
| Playwright Automation | Model-invoked browser testing |
| Prompt Engineering | Prompt engineering techniques and best practices |
| PyPICT Testing | Pairwise combinatorial test case design |
| Reddit Fetch | Fetch Reddit content when WebFetch is blocked |
| Skill Seekers | Convert documentation sites into Claude skills |
| Software Architecture | Clean Architecture, SOLID, design patterns |
| Subagent-Driven Dev | Parallel subagents with code review checkpoints |
| Test-Driven Dev | TDD workflow before writing implementation |
| Git Worktrees | Isolated git worktrees with safety checks |
| Finishing Dev Branch | Guided workflow for completing branch work |

### Data & Analysis
| Skill | What It Does |
|---|---|
| CSV Data Summarizer | Auto-analyse CSVs with visualisations |
| PostgreSQL | Safe read-only SQL queries |
| Root Cause Tracing | Trace errors back to original trigger |

### Communication
| Skill | What It Does |
|---|---|
| Article Extractor | Extract article text and metadata from web pages |
| Brainstorming | Structured idea development through questioning |
| Family History Research | Genealogy and research planning |
| NotebookLM Integration | Source-grounded answers from uploaded documents |
| YouTube Transcript | Fetch and summarise video transcripts |

### Creative
| Skill | What It Does |
|---|---|
| Imagen | Google Gemini image generation for mockups/icons |
| Markdown to EPUB | Convert markdown to professional EPUB ebooks |
| Claude Code Terminal Title | Dynamic terminal titles describing current work |

### Productivity
| Skill | What It Does |
|---|---|
| Kaizen | Continuous improvement with Lean/Kaizen methodology |
| n8n Skills | Understand and operate n8n workflows |
| Ship-Learn-Next | Iterate on what to build/learn based on feedback |
| Tapestry | Interlink documents into knowledge networks |

### Collaboration
| Skill | What It Does |
|---|---|
| Git Pushing | Automate git operations |
| Review Implementing | Evaluate implementation plans against specs |
| Test Fixing | Detect failing tests and propose fixes |

### Security
| Skill | What It Does |
|---|---|
| Computer Forensics | Digital forensics analysis and investigation |
| File Deletion | Secure file deletion and data sanitisation |
| Metadata Extraction | Extract file metadata for forensic purposes |
| Threat Hunting (Sigma) | Hunt threats using Sigma detection rules |

---

## How to Get the Most Out of Claude

1. **Be outcome-focused:** Say "I need a pitch deck for investors" not "use the pptx skill"
2. **Mention constraints:** "It needs to be a PDF", "Under 2MB", "ATS-friendly"
3. **Mention the audience:** "For my team", "For a client", "For a job application"
4. **Stack capabilities:** Claude will automatically combine skills (e.g., research + write + format + theme)
5. **Use plan mode first:** For complex tasks, say "plan this first" so Claude explores before changing anything
6. **Paste screenshots:** `Ctrl+V` to show Claude what you're looking at
7. **Name your sessions:** `/rename project-x` so you can resume later with `/resume`
8. **Ask "what else can you do?":** Claude will suggest relevant capabilities you haven't considered
