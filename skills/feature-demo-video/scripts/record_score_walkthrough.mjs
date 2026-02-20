#!/usr/bin/env node
import { chromium } from 'playwright';

const args = process.argv.slice(2);
const getArg = (name, fallback) => {
  const i = args.indexOf(name);
  if (i === -1) return fallback;
  return args[i + 1] ?? fallback;
};

const baseUrl = getArg('--baseUrl', null);
const outDir = getArg('--outDir', '/tmp/score-demo-assets');

if (!baseUrl) {
  console.error('Missing --baseUrl (e.g. https://appsdiscoverability-git-....vercel.app)');
  process.exit(1);
}

// NOTE: Playwright records video per-page to a directory and outputs .webm.
const browser = await chromium.launch({ headless: true });
const context = await browser.newContext({
  viewport: { width: 1280, height: 720 },
  recordVideo: { dir: outDir, size: { width: 1280, height: 720 } },
});
const page = await context.newPage();

await page.goto(`${baseUrl}/score`, { waitUntil: 'networkidle', timeout: 60000 });
await page.waitForTimeout(1200);

// Type in search
const input = page.locator('input[type="text"], input[type="search"], input[placeholder*="earch" i]').first();
await input.click();
await page.keyboard.type('image', { delay: 80 });
await page.waitForTimeout(900);

// Click first result/app
const links = await page.locator('a[href^="/score/"]').all();
if (links.length > 0) {
  await links[0].click();
  await page.waitForTimeout(1800);
  await page.mouse.wheel(0, 900);
  await page.waitForTimeout(900);
}

await context.close();
await browser.close();

// Try to rename the last recorded video to a stable filename
// Playwright stores the path on page.video() while the page is alive;
// since we already closed, we just inform the user to find the newest .webm.
console.log(`Recorded a walkthrough video (.webm) into: ${outDir}`);
console.log('Tip: pick the newest .webm file in that folder and feed it into Remotion as an overlay/background.');
