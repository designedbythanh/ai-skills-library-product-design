# Example: assumption-reversal

> Real output from Claude Code (Claude Opus 5.5), run on 2026-09-23 with this skill installed. The output is unedited. The scenario is fictional.
> The prompt doesn't name the skill: Claude recognized the situation and used it on its own.

## Prompt

```text
We're redesigning the checkout of a grocery delivery app and I feel stuck in the same ideas. Our current assumptions: (1) users want checkout to be as few steps as possible, (2) users choose the delivery slot at the end, after filling the cart, (3) users know what they want before they open the app. Help me break out of this.
```

## Output

Here's each assumption flipped all the way around. Don't worry yet about whether these ideas are practical. The goal is to see what becomes possible once the assumption is gone.

---

❌ **Assumption 1:** Users want checkout to be as few steps as possible.
✅ **Reversal:** Users *want* a long checkout. Checkout is the part of the trip they enjoy and want to spend time in.

💡 **Design ideas:**
- **Checkout as a walk down the aisles.** Checkout becomes a guided pass through the cart, one category at a time: "Produce: 6 items. Swap the bananas for riper ones? Add herbs for the salmon you picked?" Each step helps the user fix mistakes and finish their meals, so the extra steps are welcome.
- **The "packing table" step.** Before paying, the user arranges how the order will arrive: which bag holds what, "keep eggs on top," "frozen goods together," "put the snacks in a separate bag so the kids don't find them." It turns the handoff to the shopper into a small ritual the user controls.
- **The weekly review.** Checkout ends with a short look at the week: "This order covers 4 dinners, 2 lunches, and no breakfasts. You spent €12 less on snacks than last week." People who plan meals would come back for this.

---

❌ **Assumption 2:** Users choose the delivery slot at the end, after filling the cart.
✅ **Reversal:** Picking the slot is the *first* thing users do, and the time slot shapes everything that goes into the cart.

💡 **Design ideas:**
- **The slot as the start of the order.** Opening the app starts with "When do you want food?" Picking "Thursday 6–8pm" creates a basket tied to that moment. The catalog then adapts: ripeness is matched to the delivery day, and only items in stock for that slot are shown. Nobody finds out at checkout that an item is unavailable.
- **Several slots at once.** Users set up two or three upcoming deliveries ("Tuesday top-up," "Saturday big shop") and drag items between them. Checkout means confirming a delivery, not wrapping up a session.
- **The slot decides the price.** The slot comes first and sets the basket's economics: "Pick the 7am Wednesday van that's already on your street and get free delivery plus 5% off." Choosing when becomes the main decision, and filling the cart becomes the smaller one.

---

❌ **Assumption 3:** Users know what they want before they open the app.
✅ **Reversal:** Users open the app with *no idea* what they want. They're hungry, tired, or bored, and they're hoping the app will decide for them.

💡 **Design ideas:**
- **Start with a question instead of a search bar.** "How many people, how many nights, how much effort?" The app then builds a full, editable cart. Checkout becomes the user editing a proposal, not building a list from zero.
- **Swipe before you shop.** The user swipes through meal cards (keep / skip), and each kept meal adds its ingredients to the cart, merged and de-duplicated. The cart is a result of the choices, not a list the user typed.
- **"Surprise me" as a checkout option.** The user sets a budget and dietary rules, and the shopper picks seasonal items, deals, or something they've never tried. Payment happens before the user knows exactly what's coming, like a meal kit crossed with a mystery box.

---

**What the three reversals have in common:** they all stop treating checkout as the end of a shopping list and start treating it as the moment the user *decides* something: which meals, which time, which trade-offs. Before you pick a direction, it's worth checking which of the original three assumptions your own data actually supports. For example, look at how often slot unavailability at checkout causes people to drop off. That will show which reversal is worth prototyping.

Next, I can run **cross-industry-steal** on the strongest idea (airline seat selection looks like a close structural match to "slot first") or **persona-pretest** to see how a rushed weeknight shopper and a Sunday meal planner would each react to these ideas.
