---
name: mercury-finance
description: Daily finance tracking, subscription auditing, cash position monitoring, and tax compliance via Mercury Banking API. Use when asked about bank balances, transactions, subscriptions, monthly spend, runway, cash flow, or 1099 contractor compliance. Also use for setting up automated daily/weekly finance reports.
---

# Mercury Finance

## Authentication

Bearer token stored in `.secrets/mercury_api_token`. Prefix with `secret-token:` in the Authorization header.

```bash
TOKEN="secret-token:$(cat .secrets/mercury_api_token)"
curl -s -H "Authorization: Bearer $TOKEN" "https://api.mercury.com/api/v1/..."
```

## API Endpoints

### List accounts
```
GET https://api.mercury.com/api/v1/accounts
```
Returns checking, savings, and credit accounts with balances.

### List credit accounts
```
GET https://api.mercury.com/api/v1/credit
```
Returns credit card accounts with current balance (negative = outstanding).

### Get transactions
```
GET https://api.mercury.com/api/v1/account/{id}/transactions?limit=500&start=YYYY-MM-DD&end=YYYY-MM-DD&offset=N
```
- `limit`: max 500
- `start`/`end`: date range filter
- `offset`: pagination

### Transaction fields
- `amount`: negative = debit, positive = credit
- `counterpartyName`: vendor/payee name
- `kind`: `debitCardTransaction`, `creditCardTransaction`, `outgoingPayment`, `incomingPayment`, `other`
- `mercuryCategory`: `Software`, `Restaurants`, `Lodging`, `Fees`, etc.
- `details.electronicRoutingInfo`: bank name, address (for outgoing payments — useful for 1099 compliance)
- `createdAt`: ISO timestamp
- `status`: `sent`, `pending`, `cancelled`

## Workflows

### Daily Finance Report
Pull last 24h transactions across all accounts. Format: total debits, total credits, per-transaction breakdown. Send to designated channel/group.

### Subscription Audit
Pull 60-90 days of transactions. Group by vendor. Identify recurring charges. Flag:
- Duplicate subscriptions (same vendor, multiple charges)
- Price increases (compare current vs previous month)
- Unused tools (ask human to confirm usage)
- High-cost items relative to company runway

### Cash Position
```
Available balance (checking) + savings - credit card outstanding = net position
Monthly burn = sum of last 30 days outflows
Runway = net position / monthly burn
```

### 1099-NEC Compliance (US)
For US-based companies paying US contractors >= $600/year:
1. Filter `outgoingPayment` transactions
2. Check `details.electronicRoutingInfo.address` for US addresses
3. Sum payments per contractor per calendar year
4. Flag anyone >= $600 threshold
5. Deadlines: Feb 28 (paper), Mar 31 (e-file)
6. Contractors need to provide W-9 form (IRS form fw9.pdf)

## Cron Setup

Daily report at 9am:
```json
{
  "name": "Daily Mercury Finance Report",
  "schedule": {"kind": "cron", "expr": "0 9 * * *", "tz": "Europe/Berlin"},
  "sessionTarget": "isolated",
  "payload": {
    "kind": "agentTurn",
    "message": "Pull yesterday's transactions from Mercury API..."
  }
}
```

## Tips
- Credit card transactions are on a separate account (check `/credit` endpoint)
- International transaction fees show as `cardInternationalTransactionFee` kind
- Mercury Credit autopay shows as `other` kind from checking account
- Wire transfers (Anthropic, xAI) show as `other` kind
- Always paginate: use `offset` when `limit` returns full 500
