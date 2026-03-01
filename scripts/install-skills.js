#!/usr/bin/env node
/**
 * install-skills.js
 *
 * Installs all Claude Code skills from this portfolio into ~/.claude/skills/
 * so every Claude Code project on this machine can use them.
 *
 * Usage:
 *   node scripts/install-skills.js              # install all skills
 *   node scripts/install-skills.js --dry-run    # preview without writing
 *   node scripts/install-skills.js --only dev   # install a category (dev/biz/creative/utils/meta)
 *   node scripts/install-skills.js --composio   # also install the 832 Composio skills
 *   node scripts/install-skills.js --uninstall  # remove all portfolio skills from ~/.claude/skills/
 */

import { cp, mkdir, readdir, rm, stat, access, writeFile } from 'fs/promises';
import { join, resolve, dirname, relative } from 'path';
import { homedir } from 'os';
import { fileURLToPath } from 'url';

const __dirname = dirname(fileURLToPath(import.meta.url));
const REPO_ROOT  = resolve(__dirname, '..');
const SKILLS_DIR = join(homedir(), '.claude', 'skills');

// ── Configuration ─────────────────────────────────────────────────────────────

// Directories that are NOT skills (skip them)
const NON_SKILL_DIRS = new Set([
  'composio-skills',      // 832 Composio skills — install with --composio flag
  'connect-apps-plugin',  // Plugin format (uses claude --plugin-dir), not a skill
  'template-skill',       // Placeholder boilerplate — not ready to install
  'scripts',              // This script
  '.git',
]);

// Sibling repos to also install (relative to the parent of REPO_ROOT)
const SIBLING_SKILLS = [
  { repo: 'skill-builder', name: 'skill-builder' },
];

// Skill categories for --only filtering
const CATEGORIES = {
  dev:      ['generating-openapi-specs', 'writing-e2e-tests', 'reviewing-pull-requests',
             'debugging-with-traces', 'changelog-generator', 'langsmith-fetch',
             'mcp-builder', 'webapp-testing', 'developer-growth-analysis'],
  biz:      ['analyzing-financial-data', 'building-dashboards', 'generating-reports',
             'orchestrating-saas-workflows', 'competitive-ads-extractor',
             'content-research-writer', 'lead-research-assistant',
             'twitter-algorithm-optimizer', 'invoice-organizer', 'domain-name-brainstormer',
             'tailored-resume-generator'],
  creative: ['artifacts-builder', 'brand-guidelines', 'canvas-design', 'theme-factory',
             'slack-gif-creator', 'image-enhancer', 'video-downloader'],
  docs:     ['pdf', 'docx', 'pptx', 'xlsx'],  // sub-skills from document-skills/
  comms:    ['internal-comms', 'connect', 'connect-apps', 'skill-share',
             'meeting-insights-analyzer'],
  utils:    ['file-organizer', 'raffle-winner-picker'],
  meta:     ['skill-creator'],
};

// ── Helpers ───────────────────────────────────────────────────────────────────

const args    = process.argv.slice(2);
const DRY_RUN = args.includes('--dry-run');
const UNINSTALL = args.includes('--uninstall');
const COMPOSIO  = args.includes('--composio');
const ONLY_IDX  = args.indexOf('--only');
const ONLY_CAT  = ONLY_IDX !== -1 ? args[ONLY_IDX + 1] : null;

async function hasSkillMd(dir) {
  try { await access(join(dir, 'SKILL.md')); return true; } catch { return false; }
}

async function isDir(p) {
  try { return (await stat(p)).isDirectory(); } catch { return false; }
}

function isCategoryMatch(name) {
  if (!ONLY_CAT) return true;
  const cat = CATEGORIES[ONLY_CAT];
  if (!cat) {
    console.error(`Unknown category: ${ONLY_CAT}. Valid: ${Object.keys(CATEGORIES).join(', ')}`);
    process.exit(1);
  }
  return cat.includes(name);
}

function log(msg)  { console.log(msg); }
function ok(msg)   { console.log(`  ✅ ${msg}`); }
function skip(msg) { console.log(`  ⏭️  ${msg}`); }
function warn(msg) { console.log(`  ⚠️  ${msg}`); }

// ── Core ──────────────────────────────────────────────────────────────────────

async function installSkill(srcDir, skillName) {
  const destDir = join(SKILLS_DIR, skillName);

  if (UNINSTALL) {
    try {
      await rm(destDir, { recursive: true, force: true });
      ok(`Removed ${skillName}`);
    } catch (err) {
      warn(`Could not remove ${skillName}: ${err.message}`);
    }
    return;
  }

  if (DRY_RUN) {
    ok(`[dry-run] Would install ${skillName}`);
    return;
  }

  await mkdir(destDir, { recursive: true });
  await cp(srcDir, destDir, { recursive: true, force: true });
  ok(skillName);
}

async function collectSkills() {
  const skills = [];
  const entries = await readdir(REPO_ROOT);

  for (const entry of entries.sort()) {
    if (NON_SKILL_DIRS.has(entry)) continue;
    if (entry.startsWith('.')) continue;

    const entryPath = join(REPO_ROOT, entry);
    if (!await isDir(entryPath)) continue;

    // Direct skill (has SKILL.md at its root)
    if (await hasSkillMd(entryPath)) {
      skills.push({ src: entryPath, name: entry, origin: entry });
      continue;
    }

    // Sub-skill collection (e.g. document-skills/pdf/)
    const subEntries = await readdir(entryPath);
    for (const sub of subEntries.sort()) {
      const subPath = join(entryPath, sub);
      if (!await isDir(subPath)) continue;
      if (await hasSkillMd(subPath)) {
        skills.push({ src: subPath, name: sub, origin: `${entry}/${sub}` });
      }
    }
  }

  // Always include sibling repo skills (e.g. skill-builder)
  const parentDir = resolve(REPO_ROOT, '..');
  for (const sibling of SIBLING_SKILLS) {
    const sibDir = join(parentDir, sibling.repo);
    if (await isDir(sibDir) && await hasSkillMd(sibDir)) {
      skills.push({ src: sibDir, name: sibling.name, origin: `../${sibling.repo}` });
    }
  }

  // Optionally include the 832 Composio skills
  if (COMPOSIO) {
    const composioDir = join(REPO_ROOT, 'composio-skills');
    if (await isDir(composioDir)) {
      const apps = await readdir(composioDir);
      for (const app of apps.sort()) {
        const appPath = join(composioDir, app);
        if (!await isDir(appPath)) continue;
        if (await hasSkillMd(appPath)) {
          skills.push({ src: appPath, name: `composio-${app}`, origin: `composio-skills/${app}` });
        }
      }
    }
  }

  return skills;
}

// ── Entry Point ───────────────────────────────────────────────────────────────

async function main() {
  const mode = UNINSTALL ? 'Uninstalling' : DRY_RUN ? 'Previewing (dry run)' : 'Installing';
  log(`\nClaude Skills Portfolio — ${mode}`);
  log('='.repeat(50));
  log(`Source : ${relative(homedir(), REPO_ROOT) || REPO_ROOT}`);
  log(`Target : ${relative(homedir(), SKILLS_DIR)}`);
  if (ONLY_CAT) log(`Category filter: ${ONLY_CAT}`);
  if (COMPOSIO)  log(`Including Composio skills (+832)`);
  log('');

  if (!DRY_RUN && !UNINSTALL) {
    await mkdir(SKILLS_DIR, { recursive: true });
  }

  const skills = await collectSkills();
  const filtered = skills.filter(s => isCategoryMatch(s.name));

  if (filtered.length === 0) {
    warn('No skills matched the filter.');
    process.exit(0);
  }

  let count = 0;
  for (const skill of filtered) {
    await installSkill(skill.src, skill.name);
    count++;
  }

  log('');
  if (UNINSTALL) {
    log(`Removed ${count} skill${count === 1 ? '' : 's'} from ${SKILLS_DIR}`);
  } else if (DRY_RUN) {
    log(`Would install ${count} skill${count === 1 ? '' : 's'} — rerun without --dry-run to apply.`);
  } else {
    log(`Installed ${count} skill${count === 1 ? '' : 's'} to ${SKILLS_DIR}`);
    log('');
    log('Next steps:');
    log('  1. Restart Claude Code (or start a new session)');
    log('  2. Skills are now available in every project');
    log('  3. Try: "review this pull request" or "generate an OpenAPI spec"');
    log('  4. Run `node scripts/list-skills.js` to see all installed skills');
    log('');

    // Write an install manifest so list-skills.js can reference it
    const manifest = {
      installed_at: new Date().toISOString(),
      source_repo: REPO_ROOT,
      skill_count: count,
      skills: filtered.map(s => ({ name: s.name, origin: s.origin })),
    };
    await writeFile(
      join(SKILLS_DIR, '.portfolio-manifest.json'),
      JSON.stringify(manifest, null, 2)
    );
  }
}

main().catch(err => {
  console.error('\nError:', err.message);
  process.exit(1);
});
