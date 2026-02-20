---
name: headless-browsing
description: Headless browser automation for web scraping, form submission, price monitoring, and interacting with JavaScript-heavy or bot-protected websites. Use when web_fetch fails (Cloudflare, SPAs, login-required sites), when submitting forms on external websites, when checking prices or tracking packages, or when extracting data from pages that require JavaScript rendering. Combines OpenClaw's built-in browser tool with Firecrawl API as a lightweight alternative.
---

# Headless Browsing

Two tools available, choose based on the task:

## Tool 1: Browser Tool (Full Automation)

Use for: form submission, multi-step flows, clicking, screenshots, complex interactions.

```
browser action=navigate targetUrl="https://example.com" profile="openclaw"
browser action=snapshot profile="openclaw"    # Get page structure (aria tree)
browser action=screenshot profile="openclaw"  # Get visual screenshot
browser action=act request={kind:"click", ref:"e12"} profile="openclaw"
browser action=act request={kind:"type", ref:"e15", text:"hello"} profile="openclaw"
browser action=act request={kind:"press", key:"Enter"} profile="openclaw"
```

### Key patterns

**Navigate + snapshot → find elements → interact:**
1. `navigate` to URL
2. `snapshot` to get element refs (e.g. `ref=e12`)
3. Use `act` with `kind:click/type/press/select` targeting refs
4. `snapshot` again to verify state changes

**Form submission flow:**
1. Navigate to form page
2. Snapshot to find input refs
3. Type into each field using refs
4. Click submit button ref
5. Snapshot to confirm submission

**Always pass `profile="openclaw"`** — this uses the isolated headless browser.

**Pass `targetId` from previous snapshot** to keep the same tab across calls.

### Limitations
- reCAPTCHA/hCaptcha cannot be solved — fall back to email or phone contact
- Cookie consent dialogs: click "Accept" or "Reject All" before proceeding
- Some sites detect headless browsers — try Firecrawl instead

## Tool 2: Firecrawl API (Quick Scraping)

Use for: reading page content, searching, extracting data from bot-protected sites. Faster and cheaper than full browser automation.

**Scrape a page:**
```bash
curl -s https://api.firecrawl.dev/v1/scrape \
  -H "Authorization: Bearer <FIRECRAWL_API_KEY>" \
  -H "Content-Type: application/json" \
  -d '{"url":"URL_HERE"}' | python3 -c "
import sys,json
d=json.load(sys.stdin)
print(d.get('data',{}).get('markdown','')[:5000])"
```

**Search the web:**
```bash
curl -s https://api.firecrawl.dev/v1/search \
  -H "Authorization: Bearer <FIRECRAWL_API_KEY>" \
  -H "Content-Type: application/json" \
  -d '{"query":"QUERY_HERE", "limit": 5}'
```

Response: JSON → `data.markdown` has clean markdown content.

### When Firecrawl beats Browser
- Reading content from Cloudflare-protected sites (amsterdam.nl, Dutch retailers)
- Quick content extraction without needing to interact
- Searching across the web with clean results
- Lower token cost (returns markdown vs full aria tree)

## Decision Guide

| Task | Tool |
|------|------|
| Read page content | Firecrawl (faster) |
| Search the web | Firecrawl |
| Submit a form | Browser |
| Click through multi-step flow | Browser |
| Take screenshot proof | Browser |
| Check prices on e-commerce | Browser (dynamic pricing) or Firecrawl |
| Track packages (PostNL, DHL) | Browser (needs JS) |
| Extract from bot-protected site | Firecrawl first, Browser if that fails |

## Setup

### Browser
- Requires Google Chrome installed on the host
- OpenClaw config: `browser.enabled=true`, `headless=true`, `noSandbox=true`
- Profile name: `openclaw`

### Firecrawl
- API key stored in TOOLS.md or passed directly
- Free tier: 500 credits/month
- No setup needed beyond the API key

## Tips
- For sub-agents: both tools are available. Keep tasks focused (one site per sub-agent).
- For price monitoring: use Browser to navigate, extract price, save to file. Schedule via cron.
- For package tracking: extract tracking codes from emails, then navigate to carrier tracking pages.
- Archive Firecrawl API key in TOOLS.md for reuse across sessions.
