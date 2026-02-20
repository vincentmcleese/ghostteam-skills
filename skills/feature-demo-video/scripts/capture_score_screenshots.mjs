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

const browser = await chromium.launch({ headless: true });
const page = await browser.newPage({ viewport: { width: 1280, height: 900 } });

const shot = async (path, opts = {}) => {
  await page.screenshot({ path: `${outDir}/${path}`, ...opts });
  console.log(`Saved ${outDir}/${path}`);
};

// 1) /score
await page.goto(`${baseUrl}/score`, { waitUntil: 'networkidle', timeout: 60000 });
await page.waitForTimeout(1500);
await shot('score.png', { fullPage: true });

// 2) autocomplete
const input = page.locator('input[type="text"], input[type="search"], input[placeholder*="earch" i]').first();
await input.click();
await input.fill('image');
await page.waitForTimeout(1200);
await shot('score-autocomplete.png');

// 3) click an app
const links = await page.locator('a[href^="/score/"]').all();
if (links.length === 0) {
  console.warn('No /score/* links found on page.');
} else {
  await links[0].click();
  await page.waitForTimeout(2000);
  await shot('profile-top.png');
  await page.evaluate(() => window.scrollTo(0, document.body.scrollHeight));
  await page.waitForTimeout(1000);
  await shot('profile-cta.png');
}

await browser.close();
