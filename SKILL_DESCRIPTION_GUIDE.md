# Skill Description Guide — Token Efficiency

## Why Descriptions Matter for Token Efficiency

The `description` field in every `SKILL.md` is the **most critical factor** in Claude's decision to invoke a skill. A vague or generic description causes two types of token waste:

1. **False positives** — Claude invokes the wrong skill, wastes a full round-trip, then has to recover
2. **False negatives** — Claude ignores the skill and generates a response from scratch when the skill would have been faster and more accurate

A precise description that matches the user's actual language eliminates both problems.

## The Rule: Under 1024 Characters, Trigger-Focused

Every description must:
- Be **under 1024 characters** (hard limit)
- Start with **"Use this skill when..."** — not "This skill can..." or "A tool for..."
- Include **trigger keywords** — the exact words users say that should invoke the skill
- List **concrete use cases** — not abstract capabilities
- Be written in **third person** from Claude's perspective: "When would I invoke this?"

## Scoring Rubric

Rate each description on these 4 axes (1-5 each, target: 16+/20):

| Axis | 1 (Poor) | 5 (Excellent) |
|---|---|---|
| **Trigger clarity** | "helps with X" | "Use when user says 'build artifact', 'create React component', 'make a UI'" |
| **Use case specificity** | "various tasks" | "building multi-file React apps, bundling to single HTML for claude.ai" |
| **Keyword coverage** | No trigger words | Lists 5+ natural-language triggers |
| **Brevity** | >1024 chars or padded | <300 chars, every word earns its place |

## Before/After Examples

### artifacts-builder

**Before (generic):**
> Suite of tools for creating elaborate, multi-component claude.ai HTML artifacts using modern frontend technologies.

**After (trigger-focused):**
> Use this skill when the user wants to build a React artifact, create an interactive HTML demo, make a multi-component UI for claude.ai, or bundle a frontend project into a single HTML file. Triggers: "build an artifact", "create a React app", "make an interactive demo", "build a UI component".

---

### changelog-generator

**Before (generic):**
> Generates changelogs from git history.

**After (trigger-focused):**
> Use this skill when the user says "generate a changelog", "write release notes", "summarise git commits", or "what changed in this release". Produces structured changelogs (Keep a Changelog format) from git log output or a list of commits.

---

### competitive-ads-extractor

**Before (generic):**
> Extracts competitive advertising data.

**After (trigger-focused):**
> Use this skill when the user wants to analyse competitor ads, extract ad copy from a URL or screenshot, compare ad strategies, or research what messaging competitors are using. Triggers: "analyse competitor ads", "extract ad copy", "research competitor marketing".

---

### file-organizer

**Before (generic):**
> Organizes files and directories.

**After (trigger-focused):**
> Use this skill when the user asks to clean up a directory, organise files by type or date, rename files in bulk, or sort a messy folder. Triggers: "organise my files", "clean up this directory", "sort files by date", "rename these files".

---

### invoice-organizer

**Before (generic):**
> Helps manage and organize invoices.

**After (trigger-focused):**
> Use this skill when the user wants to parse invoice files, extract invoice data (amount, date, vendor), organise invoices by date or client, or generate an invoice summary. Triggers: "process my invoices", "extract invoice data", "organise invoices", "summarise my bills".

---

## Checklist for Every Skill Description

Before committing a skill description, verify:

- [ ] Starts with "Use this skill when..."
- [ ] Under 1024 characters (check with: `echo -n "your description" | wc -c`)
- [ ] Contains at least 3 explicit trigger phrases in quotes
- [ ] Lists at least 2 concrete use cases
- [ ] Does NOT contain: "helps with", "can be used to", "a tool for", "various", "powerful"
- [ ] Passes the test: "If I read this cold, would I know EXACTLY when to call this skill?"

## Anti-Patterns to Avoid

| Anti-Pattern | Why It's Bad | Fix |
|---|---|---|
| "Helps with X" | Too passive — no trigger signal | "Use when user asks to X" |
| "A powerful tool for..." | Marketing language wastes tokens | Remove all adjectives |
| "Various tasks" | Zero specificity | List the actual tasks |
| "Can also do Y" | Scope creep — keep it focused | Make Y a separate skill |
| Over-long descriptions | Wastes tokens on every invocation | Cut to under 300 chars if possible |
