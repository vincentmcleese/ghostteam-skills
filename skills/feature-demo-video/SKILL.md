---
name: feature-demo-video
description: Create short branded demo videos (20–40s) for newly shipped website features by capturing real interactions (typing/clicks) with Playwright and rendering an MP4 with Remotion. Use when Ghost Team ships a feature (e.g. /score) and wants a reviewable demo video in AppDiscoverability brand style.
---

# Feature Demo Video (Ghost Team)

Make a **short, branded** demo video for a feature.

Default output: **16:9 1280×720 MP4**, 20–40 seconds.

## Preconditions

- The target URL must be **publicly accessible** (no Vercel Authentication / password gate). If blocked, ask Vincent to make previews public.

## Brand Style (AppDiscoverability)

Use these as defaults:
- **Font:** PP Neue Montreal (bundled in `assets/fonts/`)
- **Brand gradient:** `linear-gradient(90deg, rgb(27,200,140), rgb(20,160,112))`
- **Accent green:** `rgb(27,200,140)`

If you need to refresh tokens, read the source of truth in the app repo:
- `appsdiscoverability/tailwind.config.js` (`backgroundImage.brand-gradient`, `fontFamily.sans`)
- `appsdiscoverability/app/fonts.ts` (font files)

## Workflow (recommended)

### 1) Capture real UI assets (screenshots + optional interaction video)

Use the script:

```bash
node skills/feature-demo-video/scripts/capture_score_screenshots.mjs \
  --baseUrl "https://<vercel-preview>" \
  --outDir "/root/.openclaw/workspace/demo-assets/score"
```

This captures:
- `/score` (full page)
- `/score` with search autocomplete visible
- `/score/[slug]` top section
- `/score/[slug]` CTA section

If you want **live typing + click**, also run:

```bash
node skills/feature-demo-video/scripts/record_score_walkthrough.mjs \
  --baseUrl "https://<vercel-preview>" \
  --outDir "/root/.openclaw/workspace/demo-assets/score"
```

### 2) Render the branded video

Use Remotion (project can live anywhere, e.g. `/root/.openclaw/workspace/remotion-demos`).

- For screenshot-based video, use the template guidance in `references/score-intro-script.md`.
- For interaction-video based demo, overlay the **hook/pitch** text on top of the recording.

## Copy Template (Score intro)

Use Vincent’s structure (hook → pitch → UI layers). See `references/score-intro-script.md`.

## Notes

- Prefer **clarity over flash**: big readable text, slow pans, no tiny UI details.
- Keep the hook stat punchy; optionally add a small citation line ("arXiv:2602.14878").
