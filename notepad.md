# Gem's Journey in Pokémon Crystal

## Current Strategy
- **Primary Goal:** Deliver Kenya to Route 31.
- **Secondary Goal:** Travel to Mahogany Town (Route 42).
- **Tertiary Goal:** Train Party to Level 30+.
- **Immediate Action:** Deliver Mail to Sleeping Man.
  1. **Current State:** Standing at (31, 9). Cooltrainer M is at (32, 8).
  2. **Action:** Step `Up` to (31, 8), Face `Right`, Interact `A`.
  3. **Goal:** Initiate dialogue. He should ask for the mail.
  4. **Contingency:**
     - If he accepts: Quest Complete!
     - If he rejects: "This MAIL isn't for me" -> Check Mail Content again.
     - If he says something generic: Verify he is the right NPC.
  5. **Next Step:** Get TM50 (Nightmare) or reward.
- **Route Info:** Staying on the upper path (Row 8/9) to reach Dark Cave area.
- **Mail Status:** Kenya holding mail with message "DARK CAVE leads to another road".

## Party Status
- **Team:** Muscle (41), Garnet (28), Hematite (15), Azurite (13), Lapis (12), Mistral (13), Kenya (10).
- **Inventory:** Contains FLOWER MAIL (3 in Bag).

## Quests
- **Webster's Mail:** Delivering Kenya (Spearow) to Route 31. Recipient is the Sleeping Man (Cooltrainer) near Dark Cave.
- **Gyms:** 6 Badges. Next: Mahogany (Glacier).

## Mechanics Notes
- **Fly Map:** Navigation is list-based via `Up`/`Down`. Order: New Bark -> Cherrygrove -> Violet -> Azalea -> Goldenrod.
- **Menu Cursor:** Remember position! Always reset or verify.

### Reflection (Turn 8681)
- **Execution:** Addressed "Cursor Memory" issues by resetting via Start Menu. Debugged Fly Map navigation step-by-step.
- **Notepad:** Cleaned up obsolete typing logs. Recorded Fly Map list logic.
- **Lesson:** When blind inputs fail, STOP and verify with screen text. Do not assume standard grid navigation.