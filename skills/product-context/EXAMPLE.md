# Example: product-context

> Real output from Claude Code (Claude Opus 5.5), run on 2026-09-28 with `claude -p` and v1.3.0 of this plugin loaded. Nothing in this skill has changed since. The output and both files are unedited. The scenario is fictional.
> The prompt doesn't name the skill: Claude recognized the situation and used it on its own.

**What to notice:**
- Two references came without links, so they're marked "Not provided" instead of being listed. Later skills will know to ask for them.
- It spotted a gap nobody mentioned (what else Staff can change) and marked it rather than guessing.
- The decision is recorded with its date and who agreed it, so a later critique can tell it apart from an older spec.

## Prompt

```text
We're starting work on Parcelly, a delivery-tracking web app for small online shops. Set up the shared context for our next feature, Notification settings.

Product: shop owners use Parcelly to track parcels and choose which emails their customers get. Mostly not technical, on a laptop, usually between packing orders.
Roles: Owner can change everything. Staff can see tracking and settings but can't change notification settings.
References: our design system in Figma (I'll add the link later), and Shopify's notification settings as a comparison.
Vocabulary: we say "parcel", not "package" or "shipment". "Customer" is the shop's buyer; "owner" is our user.
Known issues: tracked in Linear, project PAR.
Feature: Notification settings. Goal: let owners choose which emails their customers get. Stage: prototype. Decided: switches save immediately, no Save button (agreed with Mia, product lead, 22 Sep 2026). Open: whether to group the 8 notification types. Worry: owners may not understand what each email actually says.
```

## Output

I set up the shared context in two files:

- `PRODUCT.md` covers Parcelly: who uses it and when, the Owner and Staff roles, the vocabulary to use (parcel, customer, owner), and that known issues live in Linear project PAR.
- `briefs/notification-settings.md` covers the goal, the prototype stage, the decision you agreed with Mia on 22 Sep 2026 (switches save immediately, no Save button), the open question about grouping the 8 notification types, and the worry that owners may not understand what each email says. The Log section is empty; later skills will add to it.

Both references are marked "Not provided" for now. A reference only counts once it links to a specific file or screen, and I didn't want to make up links.

**Still marked "Not provided":**
- **Figma design system:** needs the link to the Figma file.
- **Shopify notification settings:** needs a link to the specific screen you're comparing against.
- **Other Staff permissions:** you said Staff can't change notification settings, but not whether they can change any other settings.

Next: `five-whys-root-cause` or `user-interview-synthesis` for a new problem, `prd-first-draft` if the solution is chosen, or `design-critique-facilitator` if there's a design to review. Carry over: nothing, they read these files.

## `PRODUCT.md` it wrote

```markdown
# Parcelly

## Product and users
- Delivery-tracking web app for small online shops
- Users: shop owners. They track parcels and choose which emails their customers get
- Mostly not technical
- On a laptop
- Usually using it between packing orders, so expect interruptions

## Roles and permissions
- Owner: can change everything
- Staff: can see tracking and settings; cannot change notification settings
- Other permissions for Staff (e.g. other settings): Not provided

## References
- Design system (Figma): Not provided (link to be added)
- Competitor, Shopify notification settings: Not provided (needs a link to the specific screen)

## Vocabulary
- **parcel**: the thing being delivered. Avoid "package" and "shipment"
- **customer**: the shop's buyer, who receives the emails
- **owner**: our user, the shop owner

## Known issues live in
- Linear, project PAR
```

## `briefs/notification-settings.md` it wrote

```markdown
# Notification settings

## Goal
- Let owners choose which emails their customers get

## Stage
- Prototype

## Decided
- Switches save immediately; no Save button · 22 Sep 2026 · Mia (product lead)

## Open
- Whether to group the 8 notification types

## Worries
- Owners may not understand what each email actually says

## Log
```
