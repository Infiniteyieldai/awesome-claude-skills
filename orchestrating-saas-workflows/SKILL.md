---
name: orchestrating-saas-workflows
description: Use this skill when automating multi-step workflows that span multiple SaaS applications. This includes creating cross-platform pipelines like "create a GitHub issue AND notify Slack", syncing data between services like Airtable to Google Sheets, triggering sequences across apps when events occur, building approval workflows, and chaining Composio actions together. Invoke when users describe a workflow involving 2+ apps, say "when X happens do Y in another app", want to automate a repetitive multi-app process, or need to connect actions across tools like Notion, Slack, GitHub, Gmail, Sheets, Jira, or HubSpot. Requires Composio setup.
---

# Orchestrating Multi-App SaaS Workflows

Builds and executes multi-step automation workflows that coordinate actions across multiple SaaS apps using Composio integrations.

## Prerequisites

Composio must be configured. Run `/connect-apps:setup` if not yet done.
For setup details, see `./composio-setup-guide.md`.

---

## Workflow Design Pattern

Every automation follows this structure:

```
TRIGGER → CONDITION (optional) → ACTIONS → CONFIRMATION
```

1. **Trigger** — What starts the workflow? (user command, event, schedule)
2. **Condition** — Any IF/THEN logic? (status check, filter, threshold)
3. **Actions** — Sequence of cross-app operations
4. **Confirmation** — Report what was done, ask to retry if something failed

---

## Step 1: Understand the Workflow

Ask the user:
- What starts this workflow? (manual trigger, event, on a schedule)
- What apps are involved?
- Is there conditional logic? ("only if the status is X")
- What should happen if a step fails?
- Should each step wait for confirmation, or run fully automated?

---

## Step 2: Map the Workflow

Diagram the flow before executing:

```
Example: Bug Report → GitHub Issue → Slack Notification

1. User reports bug in conversation
   ↓
2. CREATE GitHub issue
   - Title: [bug title]
   - Body: [description + steps to repro]
   - Labels: ["bug"]
   - Assignee: [from-rotation]
   ↓
3. SEND Slack message to #bugs
   - "🐛 New bug filed: [issue title]"
   - Link to GitHub issue
   ↓
4. CONFIRM to user: "Issue #[N] created and #bugs notified"
```

---

## Step 3: Execute Sequentially

Execute steps one at a time, confirm each before proceeding:

```
Step 1/3: Creating GitHub issue...
✅ Issue #247 created: https://github.com/org/repo/issues/247

Step 2/3: Notifying #bugs on Slack...
✅ Message sent to #bugs

Step 3/3: Done! Bug reported and team notified.
```

For destructive or irreversible steps (sending emails, posting publicly), always confirm with the user first.

---

## Common Workflow Templates

### Bug Report → GitHub + Slack

```
1. Create GitHub issue (title, body, labels, assignee)
2. Post to #bugs Slack: issue title + link
3. Add comment to issue with Slack thread link
```

**Trigger phrases:** "file a bug", "report an issue", "log this bug"

---

### Meeting Notes → Notion + Action Items

```
1. Create Notion page in [team workspace]
   - Title: "Meeting Notes — [Date]"
   - Content: formatted transcript/summary
2. Extract action items from notes
3. Create tasks in Notion database for each action item
   - Assign to relevant people
   - Set due dates
4. Post summary to #team-updates Slack
```

**Trigger phrases:** "save these meeting notes", "log this meeting", "create action items from this"

---

### Lead Research → HubSpot + Slack

```
1. Research lead (company, role, LinkedIn, news)
2. Create/update HubSpot contact with gathered info
   - Company, title, email, LinkedIn URL
   - Notes: key talking points from research
3. Notify assigned sales rep via Slack DM:
   "New lead researched: [Name] at [Company] — [1 sentence summary]"
```

**Trigger phrases:** "research this lead", "add to CRM", "prep for this meeting"

---

### Content Published → Social Promotion

```
1. User provides: blog post URL + key points
2. Draft tweet thread (3-5 tweets) from key points
3. Draft LinkedIn post (longer, professional tone)
4. Post to Twitter/X (or draft for approval)
5. Post to LinkedIn (or draft for approval)
6. Post preview link to #marketing Slack
```

**Trigger phrases:** "promote this post", "share this blog", "social media distribution"

---

### Spreadsheet Update → Email Digest

```
1. Read new/changed rows from Google Sheet (since last run)
2. Format changes into a digest email
3. Send email via Gmail to [distribution list]
4. Log run timestamp back to the sheet
```

**Trigger phrases:** "send the sheet digest", "email the updates", "notify team about sheet changes"

---

### Customer Feedback → Jira + Intercom

```
1. Receive customer feedback (pasted or from Intercom)
2. Classify: bug / feature request / question
3. If bug or feature: create Jira ticket
   - Title: [auto-generated from feedback]
   - Priority: based on impact language
   - Link: customer ID in description
4. Reply to customer via Intercom:
   "Thanks for the feedback! We've logged this as [bug/feature] #[JIRA-N]"
```

**Trigger phrases:** "log this customer feedback", "triage this support ticket", "create a ticket from this"

---

## Error Handling Protocol

When a step fails:

```
Step 2/3 failed: Could not post to Slack
Error: Channel #bugs not found

Options:
a) Retry with different channel (#engineering)
b) Skip Slack notification and continue
c) Abort workflow

What would you like to do?
```

Never silently skip failed steps — always surface the error and ask.

---

## Building Reusable Workflows

For workflows users run repeatedly, save as a named workflow:

```markdown
# Saved Workflow: "Bug Report"
Trigger: User says "file a bug" or "report an issue"
Steps:
1. Prompt for: title, description, severity, assignee
2. Create GitHub issue with labels
3. Notify #bugs on Slack
4. Confirm with issue link
```

Store in `.claude/skills/orchestrating-saas-workflows/saved-workflows/` as separate `.md` files named after the workflow.

---

## Supported App Combinations

| Source App | Destination Apps | Common Pattern |
|-----------|-----------------|----------------|
| GitHub | Slack, Jira, Notion, Linear | Issue tracking + notifications |
| Gmail | Notion, Sheets, Slack, HubSpot | Email → CRM / knowledge base |
| Google Sheets | Slack, Gmail, Notion, Airtable | Data update notifications |
| Slack | GitHub, Jira, Notion, HubSpot | Message → task/ticket |
| Intercom | Jira, HubSpot, Slack, Gmail | Support → CRM + engineering |
| HubSpot | Slack, Gmail, Sheets | CRM events → notifications |
| Notion | Slack, GitHub, Gmail | Knowledge → action |
| Linear | Slack, GitHub, Notion | Sprint → updates |

---

## Confirmation Output Format

At the end of every workflow:

```markdown
## Workflow Complete ✅

**[Workflow Name]** — executed [N] steps in [X]s

| Step | App | Action | Result |
|------|-----|--------|--------|
| 1 | GitHub | Create issue | #247 created |
| 2 | Slack | Post message | Sent to #bugs |

**Links:**
- GitHub issue: https://github.com/org/repo/issues/247
- Slack thread: https://team.slack.com/archives/CXXX/p1234567890
```
