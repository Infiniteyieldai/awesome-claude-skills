#!/usr/bin/env node
/**
 * list-skills.js
 *
 * Lists all Claude Code skills installed from this portfolio.
 * Shows name, description trigger, and source location.
 *
 * Usage:
 *   node scripts/list-skills.js              # list all installed skills
 *   node scripts/list-skills.js --available  # list skills in this repo (not yet installed)
 *   node scripts/list-skills.js --all        # list both installed and available
 */

import { readdir, readFile, stat, access } from 'fs/promises';
import { join, relative } from 'path';
import { homedir } from 'os';

const SKILLS_DIR = join(homedir(), '.claude', 'skills');

const args        = process.argv.slice(2);
const SHOW_AVAIL  = args.includes('--available') || args.includes('--all');
const SHOW_INST   = !args.includes('--available') || args.includes('--all');

async function isDir(p) {
  try { return (await stat(p)).isDirectory(); } catch { return false; }
}

async function hasSkillMd(dir) {
  try { await access(join(dir, 'SKILL.md')); return true; } catch { return false; }
}

async function parseSkillMeta(skillDir) {
  const skillPath = join(skillDir, 'SKILL.md');
  try {
    const content = await readFile(skillPath, 'utf8');
    const frontmatterMatch = content.match(/^---\n([\s\S]*?)\n---/);
    if (!frontmatterMatch) return { name: '(no frontmatter)', description: '' };

    const fm = frontmatterMatch[1];
    const nameMatch = fm.match(/^name:\s*(.+)$/m);
    const descMatch = fm.match(/^description:\s*(.+)$/m);

    return {
      name: nameMatch?.[1]?.trim() || '(unnamed)',
      description: descMatch?.[1]?.trim() || '(no description)',
    };
  } catch {
    return { name: '(unreadable)', description: '' };
  }
}

function truncate(str, max) {
  return str.length > max ? str.slice(0, max - 1) + '…' : str;
}

async function listSkillsInDir(dir, label) {
  const entries = await readdir(dir).catch(() => []);
  const skills = [];

  for (const entry of entries.sort()) {
    if (entry.startsWith('.')) continue;
    const skillDir = join(dir, entry);
    if (!await isDir(skillDir)) continue;
    if (!await hasSkillMd(skillDir)) continue;

    const meta = await parseSkillMeta(skillDir);
    skills.push({ dir: entry, ...meta });
  }

  if (skills.length === 0) {
    console.log(`  (none found in ${dir})\n`);
    return 0;
  }

  const nameWidth = Math.min(40, Math.max(...skills.map(s => s.dir.length)) + 2);

  console.log(`\n${label} (${skills.length} skills)\n${'─'.repeat(70)}`);
  for (const s of skills) {
    const col1 = s.dir.padEnd(nameWidth);
    const col2 = truncate(s.description, 70 - nameWidth);
    console.log(`  ${col1}${col2}`);
  }

  return skills.length;
}

async function main() {
  console.log('\nClaude Skills Portfolio — Inventory');
  console.log('='.repeat(50));

  let total = 0;

  if (SHOW_INST) {
    console.log(`\nInstalled skills location: ~/${relative(homedir(), SKILLS_DIR)}`);

    // Try to read the manifest for richer info
    try {
      const manifest = JSON.parse(
        await readFile(join(SKILLS_DIR, '.portfolio-manifest.json'), 'utf8')
      );
      console.log(`Last installed: ${new Date(manifest.installed_at).toLocaleString()}`);
      console.log(`Source: ${manifest.source_repo}`);
    } catch { /* no manifest — still list */ }

    total += await listSkillsInDir(SKILLS_DIR, 'Installed Skills');
  }

  if (SHOW_AVAIL) {
    const repoRoot = join(new URL('.', import.meta.url).pathname, '..');
    total += await listSkillsInDir(repoRoot, 'Available in this Repo (not yet installed)');
  }

  console.log(`\nTotal: ${total} skill${total === 1 ? '' : 's'}`);
  console.log('\nUsage tips:');
  console.log('  node scripts/install-skills.js          install all skills globally');
  console.log('  node scripts/install-skills.js --only dev   install only dev skills');
  console.log('  node scripts/list-skills.js --all       see both installed + available\n');
}

main().catch(err => {
  console.error('Error:', err.message);
  process.exit(1);
});
