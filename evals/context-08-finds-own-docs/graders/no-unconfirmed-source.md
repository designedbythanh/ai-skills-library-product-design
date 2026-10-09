---
type: llm
focus:
  source: file
  path: PRODUCT.md
---

PASS if either PRODUCT.md doesn't exist yet, or it does and none of `docs/adr/` or `tokens.json` is listed in its Sources with a Verified date (the designer hasn't confirmed them yet). Listing them as unconfirmed or pending is fine. FAIL if either has a Verified date, or if the ADR's content was copied into PRODUCT.md.
