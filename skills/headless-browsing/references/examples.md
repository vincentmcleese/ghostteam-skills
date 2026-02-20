# Real-World Examples

## 1. Submit a quote request form (dakisolatie installer)
```
1. browser navigate targetUrl="https://devriesisolatie.nl/offerte-aanvragen/" profile="openclaw"
2. browser snapshot profile="openclaw"  → find form input refs
3. browser act {kind:"type", ref:"e15", text:"Vincent McLeese"}
4. browser act {kind:"type", ref:"e18", text:"mcleesevj@gmail.com"}
5. browser act {kind:"type", ref:"e21", text:"+31 6 22317491"}
6. browser act {kind:"type", ref:"e24", text:"Bovenwoning uit 1929, schuin dak..."}
7. browser act {kind:"click", ref:"e30"}  → submit button
8. browser snapshot  → verify confirmation message
```

## 2. Track a PostNL package
```
1. browser navigate targetUrl="https://postnl.nl/tracktrace/?B=3SYQUH6496157&P=1032BN&D=NL&T=C" profile="openclaw"
2. browser snapshot profile="openclaw"  → read delivery status from aria tree
   Look for: heading with "Time of delivery" or status text
```

## 3. Check Amazon price
```
1. browser navigate targetUrl="https://www.amazon.nl/dp/PRODUCT_ID" profile="openclaw"
2. browser snapshot profile="openclaw"  → find price element
   Look for: text containing "€" near "priceblock" or "price" refs
```

## 4. Scrape a Dutch government site (Firecrawl)
```bash
# amsterdam.nl blocks direct fetch but Firecrawl gets through
curl -s https://api.firecrawl.dev/v1/scrape \
  -H "Authorization: Bearer $FIRECRAWL_KEY" \
  -H "Content-Type: application/json" \
  -d '{"url":"https://duurzaamwonen.amsterdam/subsidies-en-leningen"}'
```

## 5. Find installers/services (Firecrawl search)
```bash
curl -s https://api.firecrawl.dev/v1/search \
  -H "Authorization: Bearer $FIRECRAWL_KEY" \
  -H "Content-Type: application/json" \
  -d '{"query":"dakisolatie offerte amsterdam noord", "limit": 5}'
```

## 6. Handle cookie consent
```
1. browser snapshot  → look for dialog with "Accept" or "Reject All"
2. browser act {kind:"click", ref:"e213"}  → click Accept/Reject
3. browser snapshot  → proceed with actual task
```
