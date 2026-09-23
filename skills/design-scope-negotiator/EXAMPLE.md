# Example: design-scope-negotiator

> Real output from Claude Code (Claude Opus 5.5), run on 2026-09-23 with this skill installed. The output is unedited. The scenario is fictional.
> The prompt doesn't name the skill: Claude recognized the situation and used it on its own.

## Prompt

```text
We need to cut scope and I need help deciding what goes.
Feature: new client portal for our invoicing app (clients can view and pay their invoices online).
Hard deadline: October 30 (announced at a partner event).
Current design scope: invoice list with filters; invoice detail page; online card payment; bank transfer instructions; download PDF; payment history; client profile editing; dark mode; multi-language (FR/EN/ES); custom branding (freelancer's logo and colors); comment thread on each invoice; email notifications when a new invoice is available.
Constraint: one of our two engineers is leaving in two weeks, so we lost about 40% of our capacity.
Must-have outcome: a client can receive an invoice link and pay it online.
```

## Output

Everything I need is in your brief, so here's the scope pass. My main suggestion is to treat the Oct 30 release as a **"pay by link" page** rather than a full client portal. A client clicks a link, sees the invoice and pays. Nobody logs in, so you don't have to build accounts, passwords or password resets.

**Timeline assumption:** today is Sep 23, so you have about 5 weeks. That's roughly 2 weeks with both engineers and 3 weeks with one, or about 7 engineer-weeks in total. After the departure you're at half headcount, not 60%, so the last three weeks will feel tighter than "40%" suggests.

### 🚢 Ship (must have)
| Item | Effort | Impact if cut | Reason to keep |
|---|---|---|---|
| Online card payment | L | High | This is the must-have outcome. Use a hosted checkout (e.g. Stripe Checkout) instead of a custom payment form. It covers card-data compliance, 3D Secure and translated payment screens. The real work is the webhook that marks the invoice paid in your app, so plan for that. |
| Invoice detail page (via secure link) | M | High | This is where the link lands. Access it with a long, unguessable token instead of a login. |
| Email notification: **reduced to** a "Pay online" link | S | High | "Receive a link" is half the must-have. If your app already emails invoices, add the link to that email. The full notification system is deferred. |
| Bank transfer instructions | S | High | This is mostly fixed text (bank details and payment reference). It gives clients a way to pay when a card fails or when they pay large invoices by transfer. Very cheap for the value. |
| Download PDF | S | Medium | Likely S because the app already generates PDFs. Accounts payable teams need the PDF for their records, and without it you'll get support requests. |
| Custom branding: **reduced to** logo and business name | S | High | Clients are paying through a page they've never seen. Showing the freelancer's logo and name builds trust and keeps the page from looking like phishing. Custom colors are deferred. |

### 🔜 Fast follow (November)
| Item | Effort | Impact if cut | Reason to defer |
|---|---|---|---|
| Invoice list (no filters at first) | M | Medium | The link opens a single invoice, so the must-have doesn't need a list. A list also needs a way for clients to see all their invoices, which the link can't give them. |
| Payment history | S–M | Low | Build it on top of the invoice list. Receipts from the payment provider cover this gap for now. |
| Multi-language (FR/EN/ES) | M | Medium–High | Write the code so text can be translated later, but ship one language first. The hosted checkout already shows its payment screens in the client's language. ⚠️ See the risk below. |
| Full email notifications and custom brand colors | M | Low | These are the rest of the two items reduced above. The link in the existing email covers launch. |

### 🗑️ Cut (revisit later based on demand)
| Item | Effort | Impact if cut | Reason to cut |
|---|---|---|---|
| Dark mode | M | Low | Clients will spend about 2 minutes on this page to pay. Dark mode doesn't help anyone get paid. |
| Client profile editing | M | Low | This only makes sense with accounts, and the link-based approach skips accounts. Freelancers can keep editing client details in the app. |
| Comment thread per invoice | L | Low | It needs notifications, moderation and a new data model. Email already handles questions about invoices. |
| List filters | S–M | Low | Filters only matter once a client has many invoices. |

### Scope summary
**Original: 12 · Shipping: 6 (2 of them reduced) · Deferred: 3 (plus the rest of the 2 reduced items) · Cut: 3 (plus filters, taken from the list item)**

### Risks to flag
1. **The departing engineer's handover.** Have the engineer who is staying own the payment integration from day one, with the departing engineer pairing on it. Payments is the part you can't afford to have nobody understand on Nov 1. Give the departing engineer self-contained work: the PDF download, the bank transfer section and the email link.
2. **Language is a decision you need to make now.** If most of your freelancers bill French or Spanish clients, an English-only launch could hurt payment rates. Pick the launch language based on your customer data this week. If two languages are essential, move them into Ship and give up the logo branding in exchange.
3. **What gets announced at the partner event.** Present it as "clients can now pay invoices online," not "new client portal." If the announcement promises a portal, people will expect to log in and see all their invoices, and that isn't in this release.
4. **Hidden work in payments.** Marking invoices paid, handling partial or failed payments, refunds, and preventing a double payment when a link is clicked twice all need to be finished by about Oct 23. That leaves a week to test with real money before the event.
5. **Link security.** Anyone who has the link can see the invoice. Make tokens long enough that they can't be guessed, let freelancers revoke them, and don't put sensitive client data on the page beyond what's on the invoice.
