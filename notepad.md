# Gem's Journey in Pokémon Crystal

## Current Strategy
- **Primary Goal:** Deliver Kenya to Route 31.
- **Secondary Goal:** Travel to Mahogany Town (Route 42).
- **Tertiary Goal:** Train Party to Level 30+.
- **Current Action:** Fix Mail Message & Retest.
  1. **Hypothesis:** Quest NPC checks Mail content. "HI" caused failure.
  2. **Plan:** Restore original message ("DARK CAVE leads...").
  3. **Step 1:** Take Mail from Kenya.
  4. **Step 2:** Give Mail back -> Write Message.
  5. **Step 3:** Talk to Cooltrainer (Guard) again.
  6. **Contingency:** If Cooltrainer fails again, check Gatehouse or Cave Interior.

## Reflection (Turn 8837)
- **Immediate:** Addressing Mail Message fix.
- **Hygiene:** Marked "Wrong Recipient" on Fisher. Need to mark Cooltrainer status.
- **Analysis:** "HI" message likely broke the quest trigger. In Gen 2, Mail content is often just data, but specific delivery quests might check flags or require the *original* item state. Restoring the message is the best attempt to "reset" the item state.
- **Error:** Assumed any mail on Kenya would work.
- **Lesson:** Do not alter quest items unless necessary.

## Party Status
- **Team:** Muscle (41), Garnet (28), Hematite (15), Azurite (13), Lapis (12), Mistral (13), Kenya (10).
- **Inventory:** Contains FLOWER MAIL (3 in Bag).

## Quests
- **Webster's Mail:** Delivering Kenya (Spearow) to Route 31. Recipient is likely the Cooltrainer near Dark Cave.

## Mechanics Notes
- **Fly Map:** List-based `Up`/`Down`. New Bark -> Cherrygrove -> Violet -> Azalea -> Goldenrod.
- **Menu Cursor:** Always verify position.