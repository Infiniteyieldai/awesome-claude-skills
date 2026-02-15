# Awesome Claude Skills - Comprehensive Reference

A complete reference of every skill in this repository: what it does, when to use it, and what it needs.

---

## Table of Contents

- [Document Processing](#document-processing)
- [Development & Code Tools](#development--code-tools)
- [Business & Marketing](#business--marketing)
- [Communication & Writing](#communication--writing)
- [Creative & Media](#creative--media)
- [Productivity & Organization](#productivity--organization)
- [Integrations & Connections](#integrations--connections)
- [Meta / Skill Development](#meta--skill-development)
- [External / Community Skills](#external--community-skills)

---

## Document Processing

### docx - Word Document Manipulation

**What it does:** Creates, edits, and analyzes Microsoft Word documents with full support for tracked changes, comments, and formatting preservation.

**Key capabilities:**
- Extract text from .docx files via pandoc (converts to markdown preserving tracked changes)
- Access raw XML for complex formatting operations
- Create new Word documents using docx-js
- Edit existing documents with Python's Document library
- Redlining workflow with tracked changes (insertions/deletions)
- Convert DOCX to PDF or JPEG for visual review
- Minimal, precise edits that preserve original content and formatting

**When to use:** Creating contracts, editing reports, working with legal documents, adding tracked changes for review, commenting on drafts, any task involving .docx files.

**Prerequisites:** pandoc, docx npm package, LibreOffice, Poppler, defusedxml

---

### pdf - PDF Processing Toolkit

**What it does:** Comprehensive PDF manipulation for extracting text/tables, creating new PDFs, merging/splitting documents, handling forms, and more.

**Key capabilities:**
- Text extraction with pdfplumber
- Table extraction and conversion to Excel/pandas DataFrames
- Create new PDFs with reportlab
- Merge multiple PDFs into one
- Split PDFs by page ranges
- Extract metadata and images
- Page rotation and watermark addition
- OCR for scanned PDFs (pytesseract)
- Password protection
- PDF form filling

**When to use:** Extracting data from invoices, filling tax forms, merging reports, splitting large documents, creating formatted PDF reports, processing scanned documents.

**Prerequisites:** pypdf, pdfplumber, reportlab, pytesseract, pdf2image, pdftotext, qpdf

---

### pptx - PowerPoint Presentation Builder

**What it does:** Creates, edits, and analyzes PowerPoint presentations with full layout, slide master, speaker notes, and template support.

**Key capabilities:**
- Extract text from presentations via markitdown
- Access raw XML for advanced OOXML operations
- Create presentations from scratch using html2pptx workflow
- Edit existing slides while preserving formatting
- Work with layouts and slide masters
- Add speaker notes and comments
- Convert PPTX to PDF or JPEG thumbnails
- Generate thumbnail grids for overview
- Template-based presentations with rearrange.py
- Text replacement with formatting preservation

**When to use:** Building pitch decks, editing sales presentations, creating training materials, generating reports as slides, applying templates to existing decks.

**Prerequisites:** markitdown, pptxgenjs, playwright, sharp, LibreOffice, Poppler, defusedxml

---

### xlsx - Excel Spreadsheet Engine

**What it does:** Creates, edits, and analyzes spreadsheets with full formula support, formatting, data analysis, and visualization.

**Key capabilities:**
- Data analysis with pandas
- Create Excel files with openpyxl (formulas, formatting, multiple sheets)
- Critical rule: always use formulas, never hardcode calculated values
- Formula recalculation via recalc.py script
- Financial model standards (color coding, number formatting)
- Cell formatting and styling
- Multiple sheet management
- Formula verification and error prevention
- Text extraction and table reading

**When to use:** Building financial models, analyzing datasets, creating formatted reports, working with existing spreadsheets, any task involving .xlsx/.csv/.tsv files.

**Prerequisites:** LibreOffice (formula recalculation), openpyxl, pandas, recalc.py script

---

## Development & Code Tools

### artifacts-builder - Interactive HTML Artifact Creator

**What it does:** Builds elaborate, multi-component HTML artifacts for Claude.ai using React 18, TypeScript, Vite, Tailwind CSS, and shadcn/ui (40+ components pre-installed).

**Key capabilities:**
- Initialize frontend repos with `scripts/init-artifact.sh`
- Develop with React 18 + TypeScript + Vite + Tailwind CSS
- 40+ shadcn/ui components ready to use
- Bundle everything into a single HTML file with `scripts/bundle-artifact.sh`
- Path aliases configured (@/)
- Design guidance to avoid generic "AI slop" aesthetics

**When to use:** Creating complex interactive web artifacts that need state management, routing, or component libraries -- not for simple single-file HTML snippets.

**Prerequisites:** Node 18+, bash shell, Parcel for bundling

---

### changelog-generator - Automated Release Notes

**What it does:** Scans git history and transforms technical commits into clear, customer-friendly changelogs and release notes.

**Key capabilities:**
- Scan git history for time periods or version ranges
- Categorize changes: features, improvements, bug fixes, breaking changes, security
- Translate developer jargon into user-friendly language
- Filter out noise (refactoring, tests, internal tooling)
- Format with clean, professional structure
- Apply brand voice and changelog style guidelines

**When to use:** Preparing release notes, weekly/monthly product updates, app store submissions, customer-facing documentation of changes.

**Prerequisites:** Git repository access, commit history, optional CHANGELOG_STYLE.md

---

### developer-growth-analysis - Coding Pattern Analyzer

**What it does:** Analyzes your recent Claude Code chat history to identify coding patterns, development gaps, and improvement areas, then sends a personalized growth report to Slack.

**Key capabilities:**
- Reads chat history from ~/.claude/history.jsonl (past 24-48 hours)
- Analyzes development patterns (projects, technologies, challenges)
- Detects 3-5 prioritized improvement areas
- Searches HackerNews for curated learning resources
- Generates comprehensive personalized report
- Sends formatted report to Slack DMs

**When to use:** Weekly self-assessment, identifying skill gaps, discovering learning resources, preparing for performance reviews, tracking improvement over time.

**Prerequisites:** ~/.claude/history.jsonl, Slack connection via Rube, HackerNews access

---

### langsmith-fetch - LangChain/LangGraph Debugger

**What it does:** Fetches and analyzes execution traces from LangSmith Studio to debug LangChain and LangGraph agents.

**Key capabilities:**
- Fetch execution traces from LangSmith
- Analyze agent behavior, errors, and execution flow
- Inspect tool calls and memory operations
- Monitor token usage and performance
- Time-based filtering of traces
- Multiple output formats (pretty, JSON, raw)
- Concurrent trace fetching
- Export debug sessions

**When to use:** Debugging agent failures, investigating unexpected behavior, analyzing tool call sequences, checking memory operations, performance profiling.

**Prerequisites:** langsmith-fetch CLI installed, LANGSMITH_API_KEY and LANGSMITH_PROJECT environment variables

---

### mcp-builder - MCP Server Development Guide

**What it does:** Guides the creation of high-quality MCP (Model Context Protocol) servers that enable LLMs to interact with external services through well-designed tools.

**Key capabilities:**
- 4-phase workflow: Research, Implementation, Review, Evaluation
- Agent-centric design principles (tools model workflows, not just API endpoints)
- Error message design that guides agents to self-correct
- Input/output optimization for LLM context windows
- Language-specific guides for Python (FastMCP) and TypeScript (MCP SDK)
- Evaluation framework for testing tool effectiveness
- Quality checklist for review

**When to use:** Building MCP servers, integrating external APIs with LLMs, creating tools for Claude or other agents.

**Prerequisites:** MCP protocol knowledge, Python or TypeScript SDK, target API documentation

---

### webapp-testing - Playwright Web App Tester

**What it does:** Tests and interacts with local web applications using Playwright for verifying frontend functionality, debugging UI behavior, and capturing screenshots.

**Key capabilities:**
- Playwright-based browser automation and testing
- Static HTML testing (file:// URLs) and dynamic server testing
- Element discovery and CSS/XPath selector identification
- DOM inspection and full-page screenshots
- Server lifecycle management with with_server.py
- Multiple server support simultaneously
- Browser console log capture
- Network state waiting (networkidle)

**When to use:** Verifying UI after code changes, debugging frontend issues, automated browser testing, capturing screenshots for documentation, testing web apps end-to-end.

**Prerequisites:** Playwright, Python, with_server.py helper script

---

## Business & Marketing

### brand-guidelines - Anthropic Brand Identity

**What it does:** Applies Anthropic's official brand colors, typography, and design standards to any artifact for consistent visual identity.

**Key capabilities:**
- Official color palette (Dark #141413, Light #faf9f5, Orange #d97757, Blue #6a9bcc, Green #788c5d, grays)
- Typography: Poppins for headings, Lora for body text (Arial/Georgia fallback)
- Smart font application based on point size
- Shape and accent color cycling (orange, blue, green)
- Automatic fallback for unavailable fonts

**When to use:** Creating branded presentations, designing materials with Anthropic's look and feel, applying consistent visual identity to any output.

**Prerequisites:** System fonts or fallbacks, python-pptx for PowerPoint styling

---

### competitive-ads-extractor - Ad Intelligence Tool

**What it does:** Extracts and analyzes competitor ads from ad libraries (Facebook, LinkedIn, etc.) to understand what messaging and creative approaches are working.

**Key capabilities:**
- Extract ads from Facebook Ad Library, LinkedIn, and other platforms
- Capture screenshots of all ads found
- Analyze messaging themes, problems highlighted, value propositions
- Categorize ads by theme, audience, or format
- Identify common successful patterns and trends
- Detect visual and copy trends across campaigns

**When to use:** Competitive research, planning ad campaigns, understanding market positioning, finding creative inspiration, identifying what messaging resonates.

**Prerequisites:** Access to ad library platforms, screenshot capability

---

### domain-name-brainstormer - Domain Name Generator

**What it does:** Generates creative domain name ideas for projects and checks real-time availability across multiple TLDs.

**Key capabilities:**
- Understands project context to generate relevant names
- Produces 10-15 creative domain options per session
- Checks availability across .com, .io, .dev, .ai, .app, .co, .xyz, .design, .tech
- Provides brandability insights and analysis
- Suggests variations when top picks are taken
- Shows pricing context for different TLDs

**When to use:** Starting new projects, launching products, personal branding, rebranding, finding available alternatives to taken names.

**Prerequisites:** WHOIS or registrar API access for availability checking

---

### internal-comms - Internal Communications Writer

**What it does:** Helps write all types of internal communications using company-specific formats and templates.

**Key capabilities:**
- 3P updates (Progress, Plans, Problems)
- Company newsletter templates
- FAQ response formatting
- Status report and leadership update templates
- Project update and incident report formats
- Company-specific communication style adaptation

**When to use:** Writing team updates, leadership reports, company newsletters, FAQs, incident reports, project status updates, or any internal communication.

**Prerequisites:** Company communication guidelines (stored in examples/ directory)

---

### lead-research-assistant - Sales Lead Finder

**What it does:** Identifies and qualifies high-quality leads by analyzing your product, searching for target companies, and providing actionable outreach strategies.

**Key capabilities:**
- Analyzes your product/service and value proposition
- Identifies target companies by industry, size, location, tech stack, growth stage, pain points
- Prioritizes leads with fit scores (1-10)
- Provides personalized outreach strategies per lead
- Enriches data with decision-maker information
- Suggests conversation starters and LinkedIn URLs
- Formats results for CRM import

**When to use:** Finding potential customers, building target account lists, planning sales outreach, identifying partnerships, business development research.

**Prerequisites:** Web search capabilities, company research access

---

## Communication & Writing

### content-research-writer - Research-Backed Content Creator

**What it does:** Assists in writing high-quality content by conducting research, adding citations, improving hooks, and providing section-by-section feedback throughout the writing process.

**Key capabilities:**
- Collaborative outlining and structuring
- Research assistance with proper citations (inline, numbered, footnote)
- Hook improvement for compelling introductions
- Section-by-section feedback during writing
- Voice preservation (maintains your writing style)
- Iterative refinement and final polish

**When to use:** Writing blog posts, articles, newsletters, educational content, case studies, technical documentation, thought leadership pieces.

**Prerequisites:** Topic knowledge, writing samples (optional), research sources

---

### meeting-insights-analyzer - Meeting Behavior Analyst

**What it does:** Analyzes meeting transcripts to uncover behavioral patterns, communication insights, and actionable feedback for professional development.

**Key capabilities:**
- Identifies recurring behavior patterns
- Detects conflict avoidance tendencies
- Speaking ratio analysis (who talks how much)
- Filler word tracking ("um", "like", "you know")
- Active listening indicators
- Leadership and facilitation evaluation
- Trend tracking across multiple meetings
- Specific timestamped examples
- Actionable improvement suggestions

**When to use:** Improving communication skills, preparing for performance reviews, coaching team members, leadership development, tracking speaking habits over time.

**Prerequisites:** Meeting transcripts in .txt, .md, .vtt, .srt, or .docx format (speaker labels and timestamps preferred)

---

## Creative & Media

### canvas-design - Visual Art Creator

**What it does:** Creates beautiful visual art in PNG and PDF format using a two-step design philosophy approach -- first creating a design manifesto, then rendering the visual output.

**Key capabilities:**
- Two-step process: Design Philosophy (.md) then Canvas Creation (.pdf/.png)
- Creates visual design manifestos expressing aesthetic movements
- Minimal text, strong visual hierarchy, expert craftsmanship
- Fonts from bundled canvas-fonts directory
- Museum/magazine quality output
- Proper margins, no overlaps, professional composition
- Original designs (no copying existing artists)

**When to use:** Creating posters, artwork, visual designs, static visual pieces, branded graphics, artistic compositions.

**Prerequisites:** canvas-fonts directory, PDF/PNG generation capability

---

### image-enhancer - Image Quality Improver

**What it does:** Improves image and screenshot quality by enhancing resolution, sharpness, and clarity for professional use.

**Key capabilities:**
- Analyzes image quality (resolution, sharpness, compression artifacts)
- Enhances resolution intelligently
- Improves sharpness and detail
- Reduces compression artifacts and noise
- Optimizes for target use case (web, print, social media)
- Batch processing
- Preserves originals as backup

**When to use:** Improving screenshot quality, enhancing images for blogs/presentations, upscaling low-resolution images, sharpening blurry photos, preparing images for print.

**Prerequisites:** Image processing libraries (PIL, imageio)

---

### slack-gif-creator - Slack Animation Builder

**What it does:** Creates animated GIFs optimized for Slack's constraints with composable animation primitives and validators.

**Key capabilities:**
- Slack-specific size constraints (2MB messages, 64KB emoji)
- Dimension validation (480x480 messages, 128x128 emoji)
- 12 animation primitives: shake, bounce, spin, pulse, fade, zoom, explode, wiggle, slide, flip, morph, move
- GIF builder with optimization
- Easing functions for smooth motion
- Frame composition and effects
- Size reduction strategies

**When to use:** Creating animated GIFs for Slack channels, making custom reaction emojis, generating celebratory or fun animations for team communication.

**Prerequisites:** PIL (Pillow), imageio, numpy

---

### theme-factory - Professional Theme Applicator

**What it does:** Applies professional font and color themes to any artifact -- slides, docs, reports, HTML pages -- with 10 pre-set themes or custom theme generation.

**Available themes:**
1. **Ocean Depths** - Deep sea blues, calm and authoritative
2. **Sunset Boulevard** - Warm oranges and reds, energetic
3. **Forest Canopy** - Natural greens, organic and grounded
4. **Modern Minimalist** - Clean blacks/whites, sleek and focused
5. **Golden Hour** - Warm golds, premium and inviting
6. **Arctic Frost** - Cool icy blues, crisp and modern
7. **Desert Rose** - Sandy pinks, warm and sophisticated
8. **Tech Innovation** - Electric blues/purples, futuristic
9. **Botanical Garden** - Lush greens/florals, fresh and natural
10. **Midnight Galaxy** - Deep purples/stars, dramatic and bold

**When to use:** Styling presentations, theming slide decks, creating cohesive visual identity across documents, applying consistent branding to artifacts.

**Prerequisites:** theme-showcase.pdf for preview, themes/ directory

---

### video-downloader - YouTube/Video Downloader

**What it does:** Downloads videos from YouTube and other platforms with customizable quality and format options.

**Key capabilities:**
- Quality selection: best, 1080p, 720p, 480p, 360p, worst
- Format options: mp4, webm, mkv
- Audio-only downloads as MP3
- Custom output directory
- Automatic filename from video title
- Uses yt-dlp under the hood (auto-installed)
- Default output to /mnt/user-data/outputs/

**When to use:** Downloading videos for offline viewing, extracting audio from videos, saving content for editing or archival.

**Prerequisites:** yt-dlp (auto-installed), Python

---

## Productivity & Organization

### file-organizer - Smart File Sorter

**What it does:** Intelligently organizes files and folders by understanding context, finding duplicates, and suggesting better organizational structures.

**Key capabilities:**
- Analyzes current folder structure and contents
- Finds duplicate files using MD5 hashing
- Suggests logical organization schemes
- Automates cleanup and file moves
- Identifies old files for archiving
- Context-aware decisions (understands file relationships)
- Handles filename conflicts
- Provides organization plans before executing

**When to use:** Cleaning up Downloads folder, organizing project files, finding and removing duplicates, restructuring messy directories, archiving old projects.

**Prerequisites:** Bash tools (find, ls, du, md5), file system access

---

### invoice-organizer - Tax-Ready Receipt Manager

**What it does:** Reads messy invoice/receipt files, extracts key information, renames consistently, and sorts into tax-ready folder structures.

**Key capabilities:**
- Reads invoices from PDFs, images, documents
- Extracts: vendor, invoice number, date, amount, description, payment method
- Renames consistently: `YYYY-MM-DD Vendor - Invoice - Product.pdf`
- Organizes by vendor, category, time period, or tax category
- Handles PDFs, JPGs, PNGs, screenshots, bank statements
- Preserves original files
- Generates CSV export for accountants
- Creates tax-ready folder structure

**When to use:** Tax preparation, organizing business expenses, managing receipts, setting up automated filing, reconciling expenses with accounts.

**Prerequisites:** PDF text extraction, image OCR, file system access

---

### raffle-winner-picker - Fair Random Selector

**What it does:** Picks random winners from lists, spreadsheets, or Google Sheets using cryptographically secure randomness for verifiable fairness.

**Key capabilities:**
- Cryptographically random selection (not pseudo-random)
- Accepts CSV, Excel, Google Sheets, or plain lists
- Multiple winner selection
- Duplicate prevention
- Transparent results with timestamps
- Exclusion list support
- Weighted selection support
- Runner-up selection

**When to use:** Social media giveaways, event raffles, contest winners, random participant selection, team assignments, fair random distributions.

**Prerequisites:** Input data as CSV, Excel, Google Sheets, or plain list

---

### tailored-resume-generator - Job-Targeted Resume Builder

**What it does:** Analyzes job descriptions and generates tailored resumes that highlight the most relevant experience, skills, and achievements for each specific role.

**Key capabilities:**
- Job description analysis (extracts requirements, keywords, priorities)
- Maps candidate experience to job requirements
- Optimizes resume structure (summary, skills, experience, education)
- ATS optimization with keyword incorporation
- Quantifies achievements with metrics
- Gap analysis between experience and requirements
- Interview preparation tips
- Cover letter hook suggestions
- Multiple output formats (Markdown, plain text, Word/PDF guidance)

**When to use:** Applying for specific positions, career transitions, tailoring resumes per industry, optimizing for ATS systems, maximizing interview callback rates.

**Prerequisites:** Job description text and candidate background/experience information

---

## Integrations & Connections

### connect - Universal App Connector

**What it does:** Connects Claude to any external app so it can take real actions -- send actual emails, create actual issues, post actual messages -- across 1000+ services.

**Supported services include:**
- **Email:** Gmail, Outlook, SendGrid
- **Chat:** Slack, Discord, Teams, Telegram
- **Dev:** GitHub, GitLab, Jira, Linear
- **Docs:** Notion, Google Docs, Confluence
- **Data:** Google Sheets, Airtable, PostgreSQL
- **CRM:** HubSpot, Salesforce, Pipedrive
- **Storage:** Google Drive, Dropbox, S3
- **Social:** Twitter, LinkedIn, Reddit

**Key capabilities:**
- OAuth handled automatically (one-time setup)
- Framework support: Claude Agent SDK, OpenAI Agents, Vercel AI, LangChain
- Real actions, not just text generation about actions

**When to use:** Whenever Claude needs to interact with external services -- sending messages, creating tickets, updating databases, posting content.

**Prerequisites:** Free API key from platform.composio.dev, COMPOSIO_API_KEY environment variable

---

### connect-apps - Composio Plugin for Claude Code

**What it does:** Plugin that enables Claude Code to perform real actions across 1000+ apps using the Composio Tool Router.

**Supported categories:**
- Email, Chat, Dev tools, Docs, Data, CRM, Storage, Social (same as connect)

**Key capabilities:**
- Plugin-based installation for Claude Code
- Composio Tool Router integration
- Setup wizard via `/connect-apps:setup`
- Automatic auth handling

**When to use:** When using Claude Code and you need it to interact with external apps directly from the CLI.

**Prerequisites:** `/plugin install composio-toolrouter`, API key from platform.composio.dev

---

### skill-share - Team Skill Distributor

**What it does:** Creates new Claude skills and automatically shares them on Slack for team collaboration and discovery.

**Key capabilities:**
- Creates properly structured skill directories
- Generates SKILL.md with YAML frontmatter
- Validates skill structure, metadata, and naming conventions
- Packages skills as distributable zip files
- Automatically posts to Slack channels via Rube
- Ensures metadata completeness

**When to use:** Creating and distributing skills across teams, building internal skill libraries, collaborative skill development.

**Prerequisites:** Slack workspace connection via Rube, write access to skill directories

---

## Meta / Skill Development

### skill-creator - Skill Development Guide

**What it does:** Provides a comprehensive 6-phase guide for creating effective Claude Skills that extend capabilities with specialized knowledge, workflows, or tool integrations.

**Key capabilities:**
- Understanding skill anatomy (SKILL.md + resources)
- 6-phase creation process
- Script management for deterministic code
- Reference material and asset organization
- SKILL.md writing best practices
- Progressive disclosure design patterns
- Skill validation and packaging
- Iteration workflow guidance

**When to use:** Creating new skills, updating existing skills, learning skill architecture, packaging workflows for reuse.

**Prerequisites:** Understanding of SKILL.md format

---

### template-skill - New Skill Starter Template

**What it does:** Provides a blank template with the correct directory structure and SKILL.md format for creating new skills.

**When to use:** Starting a brand new skill from scratch. Copy this directory and customize.

---

## External / Community Skills

These skills are maintained in separate repositories and referenced in the README:

| Skill | What It Does | Author |
|-------|-------------|--------|
| **Markdown to EPUB Converter** | Converts markdown/chat summaries into EPUB ebooks | @smerchek |
| **AWS Skills** | AWS CDK best practices, cost optimization, serverless patterns | @zxkane |
| **Claude Code Terminal Title** | Dynamic terminal window titles describing current work | @bluzername |
| **D3.js Visualization** | D3 charts and interactive data visualizations | @chrisvoncsefalvay |
| **FFUF Web Fuzzing** | Web fuzzer integration for vulnerability analysis | @jthack |
| **Finishing a Development Branch** | Guided workflow for completing dev branch work | @obra |
| **iOS Simulator** | Interact with iOS Simulator for testing/debugging | @conorluddy |
| **Move Code Quality** | Analyzes Move language packages against quality checklist | @1NickPappas |
| **Playwright Browser Automation** | Model-invoked Playwright automation for testing | @lackeyjb |
| **Prompt Engineering** | Teaches prompt engineering techniques and Anthropic best practices | NeoLabHQ |
| **PyPICT Testing** | Pairwise combinatorial test case design | @omkamal |
| **Reddit Fetch** | Fetches Reddit content via Gemini CLI when WebFetch is blocked | @ykdojo |
| **Skill Seekers** | Converts documentation websites into Claude skills | @yusufkaraaslan |
| **Software Architecture** | Clean Architecture, SOLID, and design pattern implementation | NeoLabHQ |
| **Subagent-Driven Development** | Dispatches subagents for parallel dev with code review checkpoints | NeoLabHQ |
| **Test-Driven Development** | TDD workflow before writing implementation code | @obra |
| **Using Git Worktrees** | Creates isolated git worktrees with safety verification | @obra |
| **CSV Data Summarizer** | Auto-analyzes CSVs with visualizations | @coffeefuelbump |
| **PostgreSQL** | Safe read-only SQL queries with multi-connection support | @sanjay3290 |
| **Root Cause Tracing** | Traces errors back to original trigger | @obra |
| **Article Extractor** | Extracts full article text and metadata from web pages | @michalparkola |
| **Brainstorming** | Structured idea development through questioning | @obra |
| **Family History Research** | Genealogy and family history research planning | @emaynard |
| **NotebookLM Integration** | Chat with NotebookLM for source-grounded answers | @PleasePrompto |
| **Imagen** | Google Gemini image generation for mockups/icons | @sanjay3290 |
| **YouTube Transcript** | Fetch and summarize YouTube video transcripts | @michalparkola |
| **Kaizen** | Continuous improvement methodology with Lean/Kaizen philosophy | NeoLabHQ |
| **n8n Skills** | Understand and operate n8n workflows | @haunchen |
| **Ship-Learn-Next** | Iterate on what to build/learn based on feedback loops | @michalparkola |
| **Tapestry** | Interlink and summarize documents into knowledge networks | @michalparkola |
| **Git Pushing** | Automate git operations and repo interactions | @mhattingpete |
| **Review Implementing** | Evaluate code implementation plans against specs | @mhattingpete |
| **Test Fixing** | Detect failing tests and propose fixes | @mhattingpete |
| **Computer Forensics** | Digital forensics analysis and investigation | @mhattingpete |
| **File Deletion** | Secure file deletion and data sanitization | @mhattingpete |
| **Metadata Extraction** | Extract and analyze file metadata for forensics | @mhattingpete |
| **Threat Hunting with Sigma Rules** | Hunt threats using Sigma detection rules | @jthack |
