#!/usr/bin/env python3
"""Generate a phone-friendly PDF of the Complete Claude Capabilities Guide."""

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm, cm
from reportlab.lib.colors import HexColor, white, black
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    PageBreak, KeepTogether, HRFlowable
)
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import os

OUTPUT = "/home/user/awesome-claude-skills/Claude-Capabilities-Guide.pdf"

# Colours
DARK = HexColor("#1a1a2e")
ACCENT = HexColor("#d97757")
BLUE = HexColor("#6a9bcc")
GREEN = HexColor("#788c5d")
LIGHT_BG = HexColor("#f8f7f4")
MID_GRAY = HexColor("#666666")
LIGHT_GRAY = HexColor("#e8e6dc")
TABLE_HEAD_BG = HexColor("#2d2d44")
TABLE_ALT_BG = HexColor("#f2f1ed")

styles = getSampleStyleSheet()

# Custom styles
title_style = ParagraphStyle(
    "CustomTitle", parent=styles["Title"],
    fontSize=26, leading=32, textColor=DARK,
    spaceAfter=6, alignment=TA_CENTER,
    fontName="Helvetica-Bold"
)

subtitle_style = ParagraphStyle(
    "CustomSubtitle", parent=styles["Normal"],
    fontSize=11, leading=14, textColor=MID_GRAY,
    spaceAfter=20, alignment=TA_CENTER,
    fontName="Helvetica"
)

h1_style = ParagraphStyle(
    "H1", parent=styles["Heading1"],
    fontSize=18, leading=22, textColor=DARK,
    spaceBefore=20, spaceAfter=8,
    fontName="Helvetica-Bold",
    borderColor=ACCENT, borderWidth=0,
    borderPadding=0
)

h2_style = ParagraphStyle(
    "H2", parent=styles["Heading2"],
    fontSize=14, leading=18, textColor=ACCENT,
    spaceBefore=14, spaceAfter=6,
    fontName="Helvetica-Bold"
)

h3_style = ParagraphStyle(
    "H3", parent=styles["Heading3"],
    fontSize=11, leading=14, textColor=BLUE,
    spaceBefore=10, spaceAfter=4,
    fontName="Helvetica-Bold"
)

body_style = ParagraphStyle(
    "CustomBody", parent=styles["Normal"],
    fontSize=9, leading=13, textColor=DARK,
    spaceAfter=4, fontName="Helvetica"
)

bullet_style = ParagraphStyle(
    "Bullet", parent=body_style,
    leftIndent=12, bulletIndent=4,
    spaceAfter=2, fontSize=9, leading=12
)

small_style = ParagraphStyle(
    "Small", parent=body_style,
    fontSize=8, leading=11, textColor=MID_GRAY
)

table_head_style = ParagraphStyle(
    "TableHead", parent=body_style,
    fontSize=8, leading=11, textColor=white,
    fontName="Helvetica-Bold"
)

table_cell_style = ParagraphStyle(
    "TableCell", parent=body_style,
    fontSize=8, leading=11, textColor=DARK
)

table_cell_bold = ParagraphStyle(
    "TableCellBold", parent=table_cell_style,
    fontName="Helvetica-Bold"
)


def heading_bar(text, color=ACCENT):
    """Create a section heading with a coloured bar."""
    return [
        HRFlowable(width="100%", thickness=2, color=color, spaceAfter=2),
        Paragraph(text, h1_style),
        Spacer(1, 4),
    ]


def make_table(headers, rows, col_widths=None):
    """Create a styled table."""
    w = col_widths or [None] * len(headers)
    data = [[Paragraph(h, table_head_style) for h in headers]]
    for row in rows:
        data.append([Paragraph(str(c), table_cell_style) for c in row])

    t = Table(data, colWidths=col_widths, repeatRows=1)
    style_cmds = [
        ("BACKGROUND", (0, 0), (-1, 0), TABLE_HEAD_BG),
        ("TEXTCOLOR", (0, 0), (-1, 0), white),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("FONTSIZE", (0, 0), (-1, -1), 8),
        ("TOPPADDING", (0, 0), (-1, -1), 4),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
        ("LEFTPADDING", (0, 0), (-1, -1), 6),
        ("RIGHTPADDING", (0, 0), (-1, -1), 6),
        ("GRID", (0, 0), (-1, -1), 0.5, LIGHT_GRAY),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
    ]
    # Alternate row colours
    for i in range(1, len(data)):
        if i % 2 == 0:
            style_cmds.append(("BACKGROUND", (0, i), (-1, i), TABLE_ALT_BG))
    t.setStyle(TableStyle(style_cmds))
    return t


def build_pdf():
    doc = SimpleDocTemplate(
        OUTPUT,
        pagesize=A4,
        topMargin=1.5 * cm,
        bottomMargin=1.5 * cm,
        leftMargin=1.5 * cm,
        rightMargin=1.5 * cm,
        title="Complete Claude Capabilities Guide",
        author="Claude"
    )

    story = []
    avail_width = doc.width

    # ─── COVER ───
    story.append(Spacer(1, 60))
    story.append(Paragraph("Complete Claude<br/>Capabilities Guide", title_style))
    story.append(Spacer(1, 8))
    story.append(Paragraph(
        "Everything Claude can do for you — skills, built-in tools, workflows, "
        "and hidden features — in one reference.",
        subtitle_style
    ))
    story.append(Spacer(1, 12))
    story.append(HRFlowable(width="40%", thickness=2, color=ACCENT, hAlign="CENTER"))
    story.append(Spacer(1, 12))

    # TOC
    toc_items = [
        "1. Quick Lookup: \"I want to...\"",
        "2. Built-In Core Tools",
        "3. Skills: Documents",
        "4. Skills: Development & Code",
        "5. Skills: Business & Marketing",
        "6. Skills: Communication & Writing",
        "7. Skills: Creative & Media",
        "8. Skills: Productivity & Organisation",
        "9. Skills: Integrations & Connections",
        "10. Git & GitHub",
        "11. Multi-Agent System",
        "12. Slash Commands",
        "13. Keyboard Shortcuts",
        "14. Power-User Features",
        "15. Community Skills",
        "16. Tips for Maximum Efficiency",
    ]
    for item in toc_items:
        story.append(Paragraph(item, ParagraphStyle(
            "TOC", parent=body_style, fontSize=10, leading=16,
            textColor=DARK, alignment=TA_CENTER
        )))
    story.append(PageBreak())

    # ═══════════════════════════════════════
    # 1. QUICK LOOKUP
    # ═══════════════════════════════════════
    story.extend(heading_bar("1. Quick Lookup: \"I want to...\""))

    story.append(Paragraph("Documents & Files", h2_style))
    story.append(make_table(
        ["I want to...", "Use this"],
        [
            ["Create/edit a Word document", "docx skill"],
            ["Create/edit a PDF", "pdf skill"],
            ["Create/edit a PowerPoint", "pptx skill"],
            ["Create/edit an Excel spreadsheet", "xlsx skill"],
            ["Fill in a PDF form", "pdf skill (form filling)"],
            ["Merge multiple PDFs", "pdf skill (merge)"],
            ["Extract text/tables from a PDF", "pdf skill (pdfplumber)"],
            ["Organise my messy files", "file-organizer skill"],
            ["Organise invoices for tax", "invoice-organizer skill"],
        ],
        col_widths=[avail_width * 0.55, avail_width * 0.45]
    ))

    story.append(Paragraph("Writing & Content", h2_style))
    story.append(make_table(
        ["I want to...", "Use this"],
        [
            ["Write a blog post / article", "content-research-writer"],
            ["Write team updates", "internal-comms"],
            ["Generate release notes", "changelog-generator"],
            ["Tailor my CV for a job", "tailored-resume-generator"],
            ["Research a topic with citations", "content-research-writer"],
        ],
        col_widths=[avail_width * 0.55, avail_width * 0.45]
    ))

    story.append(Paragraph("Design & Creative", h2_style))
    story.append(make_table(
        ["I want to...", "Use this"],
        [
            ["Create a poster / visual art", "canvas-design"],
            ["Apply a professional theme", "theme-factory (10 themes)"],
            ["Apply Anthropic brand styling", "brand-guidelines"],
            ["Make a GIF for Slack", "slack-gif-creator"],
            ["Enhance/upscale an image", "image-enhancer"],
            ["Download a YouTube video", "video-downloader"],
            ["Build interactive web component", "artifacts-builder"],
        ],
        col_widths=[avail_width * 0.55, avail_width * 0.45]
    ))

    story.append(Paragraph("Business & Marketing", h2_style))
    story.append(make_table(
        ["I want to...", "Use this"],
        [
            ["Find sales leads", "lead-research-assistant"],
            ["Analyse competitor ads", "competitive-ads-extractor"],
            ["Brainstorm domain names", "domain-name-brainstormer"],
            ["Analyse meeting recordings", "meeting-insights-analyzer"],
        ],
        col_widths=[avail_width * 0.55, avail_width * 0.45]
    ))

    story.append(Paragraph("Development & Code", h2_style))
    story.append(make_table(
        ["I want to...", "Use this"],
        [
            ["Read / understand code", "Read, Grep, Glob tools"],
            ["Edit / refactor code", "Edit tool"],
            ["Run commands / scripts", "Bash tool"],
            ["Test a web app in browser", "webapp-testing"],
            ["Build an MCP server", "mcp-builder"],
            ["Debug LangChain agent", "langsmith-fetch"],
            ["Create a new Claude skill", "skill-creator"],
        ],
        col_widths=[avail_width * 0.55, avail_width * 0.45]
    ))

    story.append(Paragraph("Integrations (1000+ Apps)", h2_style))
    story.append(make_table(
        ["I want to...", "Use this"],
        [
            ["Send an email", "connect (Gmail, Outlook, SendGrid)"],
            ["Post a Slack message", "connect (Slack)"],
            ["Create a GitHub issue", "connect or gh CLI"],
            ["Update a Notion page", "connect (Notion)"],
            ["Post to social media", "connect (Twitter, LinkedIn)"],
            ["Query a database", "connect (PostgreSQL, Airtable)"],
        ],
        col_widths=[avail_width * 0.55, avail_width * 0.45]
    ))

    story.append(Paragraph("Other", h2_style))
    story.append(make_table(
        ["I want to...", "Use this"],
        [
            ["Pick raffle winners", "raffle-winner-picker"],
            ["Search the web", "WebSearch tool (built-in)"],
            ["Analyse a web page", "WebFetch tool (built-in)"],
            ["Edit a Jupyter notebook", "NotebookEdit tool (built-in)"],
        ],
        col_widths=[avail_width * 0.55, avail_width * 0.45]
    ))

    story.append(PageBreak())

    # ═══════════════════════════════════════
    # 2. BUILT-IN CORE TOOLS
    # ═══════════════════════════════════════
    story.extend(heading_bar("2. Built-In Core Tools", BLUE))
    story.append(Paragraph(
        "These are always available — no skills or setup needed.", body_style
    ))

    story.append(Paragraph("File Operations", h2_style))
    story.append(make_table(
        ["Tool", "What It Does"],
        [
            ["Read", "Read any file: code, images, PDFs, Jupyter notebooks"],
            ["Write", "Create a new file from scratch"],
            ["Edit", "Surgically edit specific parts of existing files"],
            ["Glob", "Find files by name pattern (e.g. **/*.ts)"],
            ["Grep", "Search file contents with regex patterns"],
        ],
        col_widths=[avail_width * 0.2, avail_width * 0.8]
    ))

    story.append(Paragraph("Execution", h2_style))
    story.append(make_table(
        ["Tool", "What It Does"],
        [
            ["Bash", "Run any shell command (tests, builds, installs, git)"],
            ["Background", "Run long commands without blocking your chat"],
        ],
        col_widths=[avail_width * 0.2, avail_width * 0.8]
    ))

    story.append(Paragraph("Web & Research", h2_style))
    story.append(make_table(
        ["Tool", "What It Does"],
        [
            ["WebSearch", "Search the internet for current information"],
            ["WebFetch", "Fetch and analyse a specific URL"],
            ["Chrome", "Full browser automation (--chrome flag)"],
        ],
        col_widths=[avail_width * 0.2, avail_width * 0.8]
    ))

    story.append(Paragraph("Interaction & Tracking", h2_style))
    story.append(make_table(
        ["Tool", "What It Does"],
        [
            ["AskUserQuestion", "Ask you clarifying questions during work"],
            ["TodoWrite", "Track multi-step tasks with progress"],
            ["NotebookEdit", "Edit Jupyter notebook cells"],
        ],
        col_widths=[avail_width * 0.2, avail_width * 0.8]
    ))

    story.append(Paragraph("Multi-Agent", h2_style))
    story.append(make_table(
        ["Agent", "What It Does"],
        [
            ["Explore", "Fast, parallel codebase research"],
            ["Plan", "Architect a solution before implementing"],
            ["General", "Handle complex multi-step sub-tasks"],
            ["Bash", "Run commands in isolated context"],
        ],
        col_widths=[avail_width * 0.2, avail_width * 0.8]
    ))

    story.append(Paragraph("Visual / Image", h2_style))
    story.append(make_table(
        ["Capability", "How"],
        [
            ["Read images", "View and analyse screenshots, photos, diagrams"],
            ["Clipboard paste", "Ctrl+V to paste images directly"],
            ["Read PDFs", "Analyse PDF documents page by page"],
        ],
        col_widths=[avail_width * 0.2, avail_width * 0.8]
    ))

    story.append(PageBreak())

    # ═══════════════════════════════════════
    # 3. SKILLS: DOCUMENTS
    # ═══════════════════════════════════════
    story.extend(heading_bar("3. Skills: Document Processing", GREEN))

    for name, desc, bullets in [
        ("docx — Word Documents", "Create, edit, and analyse .docx files with tracked changes, comments, and formatting.", [
            "Extract text preserving structure (via pandoc)",
            "Create new documents with headers, tables, formatting",
            "Edit existing documents preserving all formatting",
            "Tracked changes workflow (redlining)",
            "Add review comments",
            "Convert DOCX to PDF/JPEG",
            "Prereqs: pandoc, docx npm, LibreOffice",
        ]),
        ("pdf — PDF Documents", "Full PDF manipulation: extract, create, merge, split, fill forms, OCR.", [
            "Extract text and tables (pdfplumber)",
            "Create new PDFs (reportlab)",
            "Merge multiple PDFs into one",
            "Split PDFs by page ranges",
            "Fill PDF forms programmatically",
            "OCR scanned documents (pytesseract)",
            "Add watermarks, password protection",
            "Prereqs: pypdf, pdfplumber, reportlab",
        ]),
        ("pptx — PowerPoint Presentations", "Create, edit, and template presentations with full layout support.", [
            "Create from scratch (HTML to PPTX workflow)",
            "Edit slides preserving formatting",
            "Work with slide masters and layouts",
            "Add speaker notes and comments",
            "Convert to PDF/JPEG thumbnails",
            "Template-based rearrangement",
            "Prereqs: markitdown, pptxgenjs, LibreOffice",
        ]),
        ("xlsx — Excel Spreadsheets", "Create, edit, and analyse spreadsheets with formulas and data analysis.", [
            "Create with formulas (never hardcoded values)",
            "Data analysis with pandas",
            "Cell formatting, colours, number formats",
            "Multiple sheets per workbook",
            "Formula recalculation via LibreOffice",
            "Financial model standards",
            "Prereqs: openpyxl, pandas, LibreOffice",
        ]),
    ]:
        story.append(Paragraph(name, h2_style))
        story.append(Paragraph(desc, body_style))
        for b in bullets:
            story.append(Paragraph(f"• {b}", bullet_style))
        story.append(Spacer(1, 4))

    story.append(PageBreak())

    # ═══════════════════════════════════════
    # 4. SKILLS: DEVELOPMENT
    # ═══════════════════════════════════════
    story.extend(heading_bar("4. Skills: Development & Code"))

    for name, desc, bullets in [
        ("artifacts-builder", "Build complex interactive HTML artifacts with React 18, TypeScript, Tailwind, shadcn/ui.", [
            "40+ pre-installed shadcn/ui components",
            "Bundles into single HTML file",
            "Design guidance to avoid generic aesthetics",
            "Best for: Interactive dashboards, UI prototypes",
        ]),
        ("changelog-generator", "Scan git history and produce customer-friendly release notes.", [
            "Categorises: features, fixes, improvements, breaking changes",
            "Filters out internal noise (refactoring, tests)",
            "Best for: Release notes, app store descriptions",
        ]),
        ("developer-growth-analysis", "Analyse your Claude Code chat history to identify coding patterns and growth areas.", [
            "Reads last 24-48 hours of history",
            "Detects improvement areas, curates learning resources",
            "Sends personalised report to Slack",
            "Best for: Weekly self-assessment, skill gaps",
        ]),
        ("langsmith-fetch", "Fetch and analyse execution traces from LangSmith Studio.", [
            "Debug agent behaviour, errors, tool calls",
            "Monitor token usage and performance",
            "Multiple output formats (pretty, JSON, raw)",
            "Best for: Debugging LangChain/LangGraph agents",
        ]),
        ("mcp-builder", "Guided creation of MCP servers for connecting Claude to external APIs.", [
            "4-phase workflow: Research, Implement, Review, Evaluate",
            "Agent-centric design principles",
            "Python (FastMCP) and TypeScript guides",
            "Best for: Building MCP integrations",
        ]),
        ("webapp-testing", "Test web apps in a real browser using Playwright.", [
            "Screenshots, DOM inspection, console logs",
            "Server lifecycle management",
            "Best for: UI verification, frontend debugging",
        ]),
    ]:
        story.append(Paragraph(name, h2_style))
        story.append(Paragraph(desc, body_style))
        for b in bullets:
            story.append(Paragraph(f"• {b}", bullet_style))
        story.append(Spacer(1, 4))

    story.append(PageBreak())

    # ═══════════════════════════════════════
    # 5. SKILLS: BUSINESS & MARKETING
    # ═══════════════════════════════════════
    story.extend(heading_bar("5. Skills: Business & Marketing", BLUE))

    for name, desc, bullets in [
        ("brand-guidelines", "Apply Anthropic's official brand colours and typography.", [
            "Official colour palette and font pairing (Poppins + Lora)",
            "Smart font application and accent cycling",
            "Best for: Anthropic-branded materials",
        ]),
        ("competitive-ads-extractor", "Extract and analyse competitor ads from ad libraries.", [
            "Facebook Ad Library, LinkedIn, and more",
            "Captures screenshots, analyses messaging themes",
            "Best for: Campaign planning, competitive research",
        ]),
        ("domain-name-brainstormer", "Generate creative domain names and check availability.", [
            "10-15 options per session across 9 TLDs",
            "Brandability analysis and pricing context",
            "Best for: New projects, product launches",
        ]),
        ("internal-comms", "Write internal communications using company-specific templates.", [
            "3P updates, newsletters, FAQs, status reports",
            "Adapts to your company's style",
            "Best for: Team updates, leadership reports",
        ]),
        ("lead-research-assistant", "Find and qualify sales leads with outreach strategies.", [
            "Scores leads 1-10, provides decision-maker info",
            "LinkedIn URLs, conversation starters",
            "CRM-ready export format",
            "Best for: Sales prospecting, account lists",
        ]),
    ]:
        story.append(Paragraph(name, h2_style))
        story.append(Paragraph(desc, body_style))
        for b in bullets:
            story.append(Paragraph(f"• {b}", bullet_style))
        story.append(Spacer(1, 4))

    # ═══════════════════════════════════════
    # 6. SKILLS: COMMUNICATION & WRITING
    # ═══════════════════════════════════════
    story.extend(heading_bar("6. Skills: Communication & Writing", GREEN))

    for name, desc, bullets in [
        ("content-research-writer", "Write high-quality content with research, citations, and feedback.", [
            "Collaborative outlining and structuring",
            "Citations in inline, numbered, or footnote format",
            "Hook improvement and voice preservation",
            "Best for: Blog posts, articles, newsletters, case studies",
        ]),
        ("meeting-insights-analyzer", "Analyse meeting transcripts for behavioural patterns.", [
            "Conflict avoidance and speaking ratio detection",
            "Filler word tracking, active listening indicators",
            "Trend tracking across multiple meetings",
            "Best for: Communication coaching, leadership development",
            "Needs: Transcript in .txt, .md, .vtt, .srt, or .docx",
        ]),
    ]:
        story.append(Paragraph(name, h2_style))
        story.append(Paragraph(desc, body_style))
        for b in bullets:
            story.append(Paragraph(f"• {b}", bullet_style))
        story.append(Spacer(1, 4))

    story.append(PageBreak())

    # ═══════════════════════════════════════
    # 7. SKILLS: CREATIVE & MEDIA
    # ═══════════════════════════════════════
    story.extend(heading_bar("7. Skills: Creative & Media"))

    for name, desc, bullets in [
        ("canvas-design", "Create visual art in PNG/PDF using design philosophy.", [
            "Two-step: design manifesto then visual output",
            "Museum/magazine quality, bundled fonts",
            "Best for: Posters, artwork, branded graphics",
        ]),
        ("image-enhancer", "Improve image quality: resolution, sharpness, clarity.", [
            "Reduces noise and compression artefacts",
            "Optimises for web, print, or social media",
            "Best for: Screenshot cleanup, image upscaling",
        ]),
        ("slack-gif-creator", "Create animated GIFs optimised for Slack.", [
            "12 animation primitives (shake, bounce, spin, pulse, etc.)",
            "Size validators (2MB messages, 64KB emoji)",
            "Best for: Slack GIFs, custom reaction emojis",
        ]),
        ("theme-factory", "Apply professional themes to any artifact.", [
            "10 pre-set themes: Ocean Depths, Sunset Boulevard, Forest Canopy, Modern Minimalist, Golden Hour, Arctic Frost, Desert Rose, Tech Innovation, Botanical Garden, Midnight Galaxy",
            "Custom theme generation on-the-fly",
            "Best for: Slides, docs, reports, HTML pages",
        ]),
        ("video-downloader", "Download videos from YouTube and other platforms.", [
            "Quality: best/1080p/720p/480p/360p",
            "Formats: mp4, webm, mkv, mp3 (audio-only)",
            "Best for: Offline viewing, audio extraction",
        ]),
    ]:
        story.append(Paragraph(name, h2_style))
        story.append(Paragraph(desc, body_style))
        for b in bullets:
            story.append(Paragraph(f"• {b}", bullet_style))
        story.append(Spacer(1, 4))

    # ═══════════════════════════════════════
    # 8. SKILLS: PRODUCTIVITY
    # ═══════════════════════════════════════
    story.extend(heading_bar("8. Skills: Productivity & Organisation", BLUE))

    for name, desc, bullets in [
        ("file-organizer", "Intelligently organise files, find duplicates, suggest structure.", [
            "MD5 duplicate detection, context-aware decisions",
            "Provides plan before executing moves",
            "Best for: Downloads cleanup, project organisation",
        ]),
        ("invoice-organizer", "Organise invoices and receipts for tax preparation.", [
            "Extracts vendor, date, amount from PDFs/images",
            "Renames: YYYY-MM-DD Vendor - Invoice - Product.pdf",
            "CSV export for accountants",
            "Best for: Tax prep, expense management",
        ]),
        ("raffle-winner-picker", "Fair random selection with cryptographic randomness.", [
            "Accepts CSV, Excel, Google Sheets, plain lists",
            "Multiple winners, exclusions, weighted selection",
            "Best for: Giveaways, raffles, team assignments",
        ]),
        ("tailored-resume-generator", "Tailor resumes to specific job descriptions.", [
            "ATS optimisation with keyword incorporation",
            "Gap analysis and interview prep tips",
            "Best for: Job applications, career transitions",
        ]),
    ]:
        story.append(Paragraph(name, h2_style))
        story.append(Paragraph(desc, body_style))
        for b in bullets:
            story.append(Paragraph(f"• {b}", bullet_style))
        story.append(Spacer(1, 4))

    story.append(PageBreak())

    # ═══════════════════════════════════════
    # 9. SKILLS: INTEGRATIONS
    # ═══════════════════════════════════════
    story.extend(heading_bar("9. Skills: Integrations & Connections", GREEN))

    story.append(Paragraph("connect / connect-apps", h2_style))
    story.append(Paragraph(
        "Connect Claude to 1000+ apps via Composio. Takes real actions — sends actual "
        "emails, creates actual issues, posts actual messages.", body_style
    ))

    story.append(make_table(
        ["Category", "Apps"],
        [
            ["Email", "Gmail, Outlook, SendGrid"],
            ["Chat", "Slack, Discord, Teams, Telegram"],
            ["Dev", "GitHub, GitLab, Jira, Linear"],
            ["Docs", "Notion, Google Docs, Confluence"],
            ["Data", "Sheets, Airtable, PostgreSQL"],
            ["CRM", "HubSpot, Salesforce, Pipedrive"],
            ["Storage", "Drive, Dropbox, S3"],
            ["Social", "Twitter, LinkedIn, Reddit"],
        ],
        col_widths=[avail_width * 0.2, avail_width * 0.8]
    ))
    story.append(Paragraph("Setup: Free API key from platform.composio.dev", small_style))
    story.append(Spacer(1, 8))

    story.append(Paragraph("skill-share", h2_style))
    story.append(Paragraph(
        "Create and package Claude skills, then automatically share them on Slack for "
        "team discovery and collaboration.", body_style
    ))

    # ═══════════════════════════════════════
    # 10. GIT & GITHUB
    # ═══════════════════════════════════════
    story.extend(heading_bar("10. Git & GitHub"))

    story.append(make_table(
        ["Action", "How"],
        [
            ["View status / diff / log", "git commands via Bash"],
            ["Create / switch branches", "git checkout -b, git switch"],
            ["Stage and commit", "git add, git commit"],
            ["Push / pull", "git push, git pull"],
            ["Create a Pull Request", "gh pr create (GitHub CLI)"],
            ["View PR comments", "gh api repos/.../pulls/N/comments"],
            ["View issues", "gh issue view N"],
            ["Rebase / merge", "git rebase, git merge"],
            ["View blame / history", "git blame, git log --follow"],
            ["Parallel branches", "Git worktree support"],
        ],
        col_widths=[avail_width * 0.35, avail_width * 0.65]
    ))

    story.append(PageBreak())

    # ═══════════════════════════════════════
    # 11. MULTI-AGENT SYSTEM
    # ═══════════════════════════════════════
    story.extend(heading_bar("11. Multi-Agent System", BLUE))

    story.append(Paragraph(
        "Claude can spawn specialised sub-agents for parallel or isolated work:", body_style
    ))

    story.append(make_table(
        ["Agent", "Capability", "Best For"],
        [
            ["Explore", "Fast, read-only research", "Finding files, understanding code"],
            ["Plan", "Read-only architecture", "Designing solutions before building"],
            ["General", "Full multi-step tasks", "Complex research, multi-file ops"],
            ["Bash", "Isolated command execution", "Test suites, build commands"],
        ],
        col_widths=[avail_width * 0.15, avail_width * 0.4, avail_width * 0.45]
    ))

    story.append(Spacer(1, 8))
    story.append(Paragraph("Key Patterns", h3_style))
    for b in [
        "Parallel research: Launch multiple agents simultaneously",
        "Plan then implement: Explore safely before changing code",
        "Background work: Agents run while you continue chatting",
        "Context isolation: Keep large operations out of main conversation",
    ]:
        story.append(Paragraph(f"• {b}", bullet_style))

    # ═══════════════════════════════════════
    # 12. SLASH COMMANDS
    # ═══════════════════════════════════════
    story.extend(heading_bar("12. Slash Commands", GREEN))

    story.append(make_table(
        ["Command", "What It Does"],
        [
            ["/help", "Show help and usage info"],
            ["/clear", "Clear conversation history"],
            ["/compact", "Compress conversation to free context"],
            ["/context", "Visual breakdown of context usage"],
            ["/cost", "Show token usage and costs"],
            ["/model", "Change AI model (Sonnet/Opus/Haiku)"],
            ["/continue", "Resume most recent session"],
            ["/resume", "Open session picker"],
            ["/rewind", "Undo recent edits and conversation"],
            ["/rename", "Name current session"],
            ["/fork-session", "Branch from current point"],
            ["/init", "Initialise project with CLAUDE.md"],
            ["/memory", "Edit CLAUDE.md memory files"],
            ["/mcp", "Manage MCP server connections"],
            ["/hooks", "Configure automation hooks"],
            ["/agents", "Create and manage subagents"],
            ["/config", "Open settings"],
            ["/status", "Version, model, account info"],
            ["/export", "Export conversation to file"],
            ["/copy", "Copy last response to clipboard"],
            ["/stats", "Usage stats and streaks"],
            ["/vim", "Enable vim-style editing"],
            ["/fast", "Toggle fast mode"],
            ["/plan", "Enter plan mode (read-only)"],
            ["/debug", "Troubleshoot current session"],
            ["/doctor", "Check installation health"],
            ["/todos", "List current TODO items"],
            ["/theme", "Change colour theme"],
        ],
        col_widths=[avail_width * 0.25, avail_width * 0.75]
    ))

    story.append(PageBreak())

    # ═══════════════════════════════════════
    # 13. KEYBOARD SHORTCUTS
    # ═══════════════════════════════════════
    story.extend(heading_bar("13. Keyboard Shortcuts"))

    story.append(Paragraph("Essential", h2_style))
    story.append(make_table(
        ["Shortcut", "Action"],
        [
            ["Ctrl+C", "Cancel / interrupt"],
            ["Ctrl+V / Cmd+V", "Paste image from clipboard"],
            ["Ctrl+O", "Toggle verbose output (see reasoning)"],
            ["Ctrl+T", "Toggle task list view"],
            ["Ctrl+B", "Move running task to background"],
            ["Ctrl+G", "Open prompt in text editor"],
            ["Ctrl+R", "Reverse search command history"],
            ["Shift+Tab", "Cycle permission modes"],
            ["Esc+Esc", "Rewind / summarise"],
            ["Alt+P", "Switch models"],
            ["Alt+T", "Toggle extended thinking"],
            ["Shift+Enter", "New line in input"],
            ["!command", "Run bash command directly"],
        ],
        col_widths=[avail_width * 0.3, avail_width * 0.7]
    ))

    story.append(Paragraph("Editing", h2_style))
    story.append(make_table(
        ["Shortcut", "Action"],
        [
            ["Ctrl+K", "Delete to end of line"],
            ["Ctrl+U", "Delete entire line"],
            ["Ctrl+Y", "Paste deleted text"],
            ["Alt+B / Alt+F", "Move back / forward one word"],
        ],
        col_widths=[avail_width * 0.3, avail_width * 0.7]
    ))

    # ═══════════════════════════════════════
    # 14. POWER-USER FEATURES
    # ═══════════════════════════════════════
    story.extend(heading_bar("14. Power-User Features", BLUE))

    story.append(make_table(
        ["Feature", "How"],
        [
            ["Paste screenshots", "Ctrl+V to paste images for analysis"],
            ["Pipe data in", "cat file | claude -p \"analyse this\""],
            ["Background tasks", "Ctrl+B moves long ops to background"],
            ["Vim mode", "/vim enables vim-style editing"],
            ["Session naming", "/rename my-feature for easy finding"],
            ["Visual context map", "/context shows context usage"],
            ["Plan mode", "/plan for safe read-only exploration"],
            ["Budget limits", "--max-budget-usd 5 caps session spend"],
            ["JSON output", "--json-schema for validated output"],
            ["Headless mode", "claude -p \"task\" for CI/CD"],
            ["Effort control", "/model to adjust reasoning depth"],
            ["Fallback model", "--fallback-model auto-switches"],
            ["PR linking", "--from-pr 123 ties session to PR"],
            ["Git worktrees", "Parallel sessions on branches"],
            ["Agent teams", "Multiple agents on shared task list"],
            ["Custom keybindings", "~/.claude/keybindings.json"],
            ["Checkpoint rewind", "Auto-snapshots before every edit"],
            ["Chrome automation", "--chrome for browser control"],
            ["Subagent memory", "Agents learn across conversations"],
        ],
        col_widths=[avail_width * 0.3, avail_width * 0.7]
    ))

    story.append(PageBreak())

    # ═══════════════════════════════════════
    # 15. COMMUNITY SKILLS
    # ═══════════════════════════════════════
    story.extend(heading_bar("15. External / Community Skills", GREEN))
    story.append(Paragraph(
        "These are maintained in separate repositories and installed separately:", body_style
    ))

    story.append(Paragraph("Development", h3_style))
    story.append(make_table(
        ["Skill", "What It Does"],
        [
            ["AWS Skills", "CDK best practices, cost optimisation, serverless"],
            ["D3.js Visualization", "D3 charts and interactive visualisations"],
            ["FFUF Web Fuzzing", "Web fuzzer for vulnerability analysis"],
            ["iOS Simulator", "Test and debug iOS apps"],
            ["Playwright Automation", "Browser testing automation"],
            ["Prompt Engineering", "Prompt techniques and best practices"],
            ["PyPICT Testing", "Pairwise combinatorial test design"],
            ["Software Architecture", "Clean Architecture, SOLID patterns"],
            ["Subagent-Driven Dev", "Parallel subagents with code review"],
            ["Test-Driven Dev", "TDD workflow"],
            ["Git Worktrees", "Isolated worktrees with safety checks"],
        ],
        col_widths=[avail_width * 0.35, avail_width * 0.65]
    ))

    story.append(Paragraph("Data, Communication, Creative", h3_style))
    story.append(make_table(
        ["Skill", "What It Does"],
        [
            ["CSV Data Summarizer", "Auto-analyse CSVs with visualisations"],
            ["PostgreSQL", "Safe read-only SQL queries"],
            ["Root Cause Tracing", "Trace errors to original trigger"],
            ["Article Extractor", "Extract articles from web pages"],
            ["Brainstorming", "Structured idea development"],
            ["NotebookLM", "Source-grounded answers from documents"],
            ["YouTube Transcript", "Fetch and summarise video transcripts"],
            ["Imagen", "Gemini image generation"],
            ["Markdown to EPUB", "Convert to professional EPUB ebooks"],
        ],
        col_widths=[avail_width * 0.35, avail_width * 0.65]
    ))

    story.append(Paragraph("Productivity & Security", h3_style))
    story.append(make_table(
        ["Skill", "What It Does"],
        [
            ["Kaizen", "Continuous improvement methodology"],
            ["n8n Skills", "Operate n8n workflows"],
            ["Tapestry", "Interlink documents into knowledge networks"],
            ["Computer Forensics", "Digital forensics analysis"],
            ["Metadata Extraction", "File metadata for forensic purposes"],
            ["Threat Hunting", "Hunt threats with Sigma rules"],
            ["Git Pushing", "Automate git operations"],
            ["Test Fixing", "Detect failing tests, propose fixes"],
        ],
        col_widths=[avail_width * 0.35, avail_width * 0.65]
    ))

    story.append(PageBreak())

    # ═══════════════════════════════════════
    # 16. TIPS
    # ═══════════════════════════════════════
    story.extend(heading_bar("16. Tips for Maximum Efficiency"))

    tips = [
        ("<b>Be outcome-focused:</b> Say \"I need a pitch deck for investors\" — not \"use the pptx skill\". Claude will pick the right tools automatically.",),
        ("<b>Mention constraints:</b> \"It needs to be a PDF\", \"Under 2MB\", \"ATS-friendly\" — this narrows the recommendation instantly.",),
        ("<b>Mention the audience:</b> \"For my team\" vs \"for a customer\" changes which approach is best.",),
        ("<b>Stack capabilities:</b> Claude will automatically combine skills. E.g. research + write + format + theme for a branded report.",),
        ("<b>Use plan mode first:</b> For complex tasks, say \"plan this first\" so Claude explores safely before changing anything.",),
        ("<b>Paste screenshots:</b> Ctrl+V to show Claude exactly what you're looking at.",),
        ("<b>Name sessions:</b> /rename project-x so you can resume later with /resume.",),
        ("<b>Ask \"what else can you do?\":</b> Claude will suggest relevant capabilities you haven't considered.",),
    ]

    for i, (tip,) in enumerate(tips, 1):
        story.append(Paragraph(f"{i}. {tip}", ParagraphStyle(
            "Tip", parent=body_style, fontSize=10, leading=14,
            spaceBefore=6, spaceAfter=2
        )))

    story.append(Spacer(1, 30))
    story.append(HRFlowable(width="40%", thickness=2, color=ACCENT, hAlign="CENTER"))
    story.append(Spacer(1, 10))
    story.append(Paragraph(
        "Just describe what you want — Claude will match it to the right capability.",
        ParagraphStyle("Closing", parent=subtitle_style, fontSize=11, textColor=DARK)
    ))

    # Build
    doc.build(story)
    print(f"PDF generated: {OUTPUT}")
    print(f"Size: {os.path.getsize(OUTPUT) / 1024:.0f} KB")


if __name__ == "__main__":
    build_pdf()
