---
max_turns: 20
timeout_seconds: 600
allowed_tools: [Skill, Bash, Read]
---

I'd like a design critique of the Notifications settings page in Parcelly, a delivery-tracking app for small online shops. It's built; here's the relevant CSS:

```css
body { background: #ffffff; color: #1f2937; }
.switch[aria-checked="true"]  { background: #2563eb; }
.switch[aria-checked="false"] { background: #e5e7eb; }
.hint { color: #9ca3af; font-size: 13px; }
```

Layout: page title, a one-line intro, then a list of 8 notification types (Order shipped, Out for delivery, Delivery delayed, Delivered, Failed attempt, Returned, Review request, Weekly summary). Each row has a label, a one-line hint in `.hint`, and a switch that saves immediately.

Goal: let a shop owner choose which emails their customers get. Users: small shop owners, not technical, mostly on a laptop. Stage: built.
Decided: switches save immediately, no Save button.
Open: whether to group the 8 types.
My concern: I'm not sure owners understand what each notification actually sends.
Compare with: our guidelines, which say "off" switches use #e5e7eb and hints use #9ca3af.
