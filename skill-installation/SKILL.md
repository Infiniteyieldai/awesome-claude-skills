---
name: skill-installation
description: Teaches Claude how to install skills from the awesome-claude-skills collection using direct file copy. This skill should be used when the user wants to install a skill from the awesome-claude-skills GitHub repository into their Claude Code environment by manually copying the skill directory, as an alternative to the npx skills CLI.
---

# Skill Installation

This skill guides installation of skills from the [awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) collection into a Claude Code environment using the direct file copy method.

## When to Use This Skill

- The user wants to install a skill from the awesome-claude-skills repository
- The user asks "how do I install a skill" or "how do I add a skill to Claude Code"
- The user wants to install a skill without using the `npx skills` CLI
- The user has cloned the repository locally and wants to copy skills from it
- The user wants to install a skill at the global level or the project level

## Installation Paths

Skills can be installed at two scopes:

| Scope | Path | When to Use |
|-------|------|-------------|
| Global (user-level) | `~/.config/claude-code/skills/` | Available in all Claude Code sessions |
| Project-level | `.agents/skills/` (in the project root) | Available only within that project |

Other agent tools use similar conventions: `.opencode/skills/` and `.codex/skills/`.

## Instructions

### Step 1: Identify the Skill to Install

Browse the available skills in the [awesome-claude-skills repository](https://github.com/ComposioHQ/awesome-claude-skills) or in the locally cloned directory. Each skill is a directory containing a `SKILL.md` file. Confirm the skill name with the user before proceeding.

### Step 2: Install Globally (Claude Code, all projects)

To install a skill so it is available across all Claude Code sessions:

```bash
mkdir -p ~/.config/claude-code/skills/
cp -r /path/to/awesome-claude-skills/skill-name ~/.config/claude-code/skills/
```

For example, to install the `skill-creator` skill:

```bash
mkdir -p ~/.config/claude-code/skills/
cp -r /path/to/awesome-claude-skills/skill-creator ~/.config/claude-code/skills/
```

### Step 3: Install at Project Level (current project only)

To install a skill so it is available only within the current project:

```bash
mkdir -p .agents/skills/
cp -r /path/to/awesome-claude-skills/skill-name .agents/skills/
```

### Step 4: Verify the Installation

After copying, verify the skill's metadata is correct:

```bash
head ~/.config/claude-code/skills/skill-name/SKILL.md
# or for project-level:
head .agents/skills/skill-name/SKILL.md
```

Confirm the YAML frontmatter contains a valid `name` and `description` field.

### Step 5: Activate the Skill

Restart Claude Code for the skill to be picked up:

```bash
claude
```

The skill loads automatically and activates when Claude determines it is relevant to the current task.

## Installing from a Remote Clone

If the user has not already cloned the repository, clone it first:

```bash
git clone https://github.com/ComposioHQ/awesome-claude-skills.git
cd awesome-claude-skills
```

Then run the copy commands above using the cloned path.

## Notes

- Skills in the `composio-skills/` subdirectory require Composio credentials. Refer to the README for setup.
- To install multiple skills at once, repeat the `cp -r` command for each skill.
- The `npx skills` CLI (see the `find-skills` skill) is an alternative installation method that supports searching and installing from GitHub without cloning first.
