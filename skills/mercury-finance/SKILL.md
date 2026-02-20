---
name: mercury-finance
description: Ghost Team financial intelligence. Use when asked about bank balances, transactions, subscriptions, monthly spend, runway, cash flow, invoices, bookkeeping, tax compliance, or any finance question. Combines Mercury Banking API (real-time transactions), Gmail (accountant emails, invoices, payment receipts), and Google Drive (financial documents, trackers, engagement letters). Use for automated daily/weekly finance reports, subscription auditing, and 1099 contractor compliance.
---

# Ghost Team Finance Skill

Three data sources for complete financial intelligence:

## 1. Mercury Banking API (Real-time transactions)

Bearer token in `.secrets/mercury_api_token`. Prefix with `secret-token:`.

```bash
TOKEN="secret-token:$(cat .secrets/mercury_api_token)"
curl -s -H "Authorization: Bearer $TOKEN" "https://api.mercury.com/api/v1/..."
```

### Endpoints
- `GET /accounts` — all accounts with balances
- `GET /credit` — credit card accounts
- `GET /account/{id}/transactions?limit=500&start=YYYY-MM-DD&end=YYYY-MM-DD&offset=N`

### Account IDs
- Checking: `251a007a-74a3-11f0-8dd8-7f4bbb7e3366`
- Credit Card: `4bed9028-7556-11f0-9c50-abb64d0f821b`

### Transaction fields
- `amount`: negative = debit, positive = credit
- `counterpartyName`: vendor/payee
- `kind`: `debitCardTransaction`, `creditCardTransaction`, `outgoingPayment`, `incomingPayment`, `other`
- `mercuryCategory`: `Software`, `Restaurants`, `Lodging`, `Fees`, etc.
- `details.electronicRoutingInfo`: bank name, address (for 1099 compliance)
- `status`: `sent`, `pending`, `cancelled`

## 2. Gmail (Accountant, invoices, receipts)

Requires `gog` CLI with `GOG_KEYRING_PASSWORD=openclaw` and `GOG_ACCOUNT=vincent@ghostteam.ai`.

### Key Gmail labels
- `💰 Transactions` — Mercury charge notifications, payment alerts
- `📋 Invoices` — vendor invoices, receipts, billing confirmations
- `✅ James` — agent-processed items
- `⭐ Action Required` — items needing human attention

### Key contacts
- **doola** (accountant/bookkeeper): `dedicatedbookkeeping@doola.com`, `taxes@doola.com`
- **Mercury**: `hello@mercury.com`

### Common searches
```bash
# Accountant emails
gog gmail search "from:doola" --max 10

# Recent invoices
gog gmail search "label:📋-Invoices newer_than:30d" --max 20

# Mercury transaction alerts
gog gmail search "label:💰-Transactions newer_than:7d" --max 20

# Tax-related
gog gmail search "from:doola subject:tax" --max 10

# Specific vendor receipts
gog gmail search "from:billing@apify.com OR from:receipts@webshare.io" --max 10
```

### Reading an email
```bash
gog gmail messages read <message_id>
```

## 3. Google Drive (Financial documents)

### Key folders
| Folder | Drive ID | Contents |
|--------|----------|----------|
| 01. Finance | `1lJkQbnB-kkm8OKBx_syxirZ5ZQnTrYMx` | Revenue/Expense tracker, Loan tracker |
| 00. Ghost Team Finances | `1Uz3Rg7SXUYsqW_mtPysebmWpjpz5_ANB` | Corporate finance docs |
| 04. Finances | `1wetw7qw298qU9v2zjP77IhQqnBmiqv7V` | Client finance folders (Luminar, Magnus, MintHC, Mend, etc.) |
| 01. Legal | `1mFT09UW6WUoobRiLcnGpybklStQpWLsv` | Legal/corporate docs |

### Key documents
| Document | ID | Type |
|----------|-----|------|
| Revenue, Expense & Forecast Tracker | `1nWW5GOzAi5q73VtIT4WwBXgib5UftoW7TluLb1YnxBM` | Google Sheet |
| Vincent Loan Tracker | `10p2IXMOzlYRNkk3mfRiWXH0Zfg3uE5tUc-GbYpX7CdM` | Google Sheet |
| doola Bookkeeping Engagement Letter | `1k5SdJsyAI8reZKikqFyPD5Nx-0tRu4IV` | PDF |

### Common operations
```bash
# List files in a finance folder
gog drive search "'FOLDER_ID' in parents" --max 20

# Read a Google Sheet
gog sheets get <sheetId> "Sheet1!A1:Z100" --json

# Export a Google Doc
gog docs export <docId> --format txt --out /tmp/doc.txt
```

## Workflows

### Daily Finance Report
1. Pull last 24h transactions from Mercury (both checking + credit card)
2. Check Gmail for new invoices/receipts in last 24h
3. Format: total debits, total credits, per-transaction breakdown
4. Send to designated channel/group

### Subscription Audit
1. Pull 60-90 days of Mercury transactions (both accounts)
2. Cross-reference with Gmail invoices for exact amounts
3. Group by vendor, identify recurring charges
4. Flag: duplicates, price increases, unused tools, high-cost items
5. Reference: `references/subscription-tracking.md`

### Cash Position & Runway
```
Net position = checking balance + savings - credit card outstanding
Monthly burn = sum of last 30 days outflows (both accounts)
Runway months = net position / monthly burn
```
Cross-reference with Revenue/Expense Tracker sheet for forecast data.

### 1099-NEC Compliance (US contractors)
1. Filter Mercury `outgoingPayment` transactions
2. Check `details.electronicRoutingInfo.address` for US addresses
3. Sum per contractor per calendar year
4. Flag anyone >= $600 threshold
5. Search Gmail for W-9 forms: `gog gmail search "W-9 OR w9"`
6. Accountant contact for filing: doola (`taxes@doola.com`, $30/form)
7. Deadlines: Feb 28 (paper), Mar 31 (e-file)

### Answering Finance Questions
For any finance question, check all three sources:
1. **Mercury API** for real-time balances and transaction data
2. **Gmail** for context (invoices, receipts, accountant correspondence)
3. **Google Drive** for forecasts, trackers, and documents

## Tips
- Credit card transactions are on a separate account ID
- International transaction fees: `cardInternationalTransactionFee` kind
- Mercury Credit autopay: `other` kind from checking
- Wire transfers (Anthropic, xAI): `other` kind
- Always paginate Mercury: use `offset` when hitting 500 limit
- Gmail labels use emoji: search with `label:💰-Transactions` (URL-encode if needed)
- Set both env vars before any gog command: `GOG_KEYRING_PASSWORD=openclaw GOG_ACCOUNT=vincent@ghostteam.ai`
