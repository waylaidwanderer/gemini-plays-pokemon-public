# Gem's Journey in Pokémon Crystal

## Current Strategy
- **Primary Goal:** Deliver Kenya to Route 31.
- **Secondary Goal:** Travel to Mahogany Town (Route 42).
- **Tertiary Goal:** Train Party to Level 30+.

## Quest: Deliver Kenya (Route 31)
1.  **Status:** Verifying Sign Text for Password.
2.  **Current Plan:**
    - **Step 1:** Read Dark Cave Sign at (31, 5) to confirm EXACT text (case, punctuation).
    - **Step 2:** Rewrite mail on Kenya using `write_mail_safe` with verified text.
    - **Step 3:** Deliver to Fisher at (17, 7).

## Failed Mail Attempts
- "DARK CAVE leads to another road" (Rejected)
- Hypothesis: Text must match sign exactly (Case Sensitive, Punctuation).

## Knowledge Base
- **Fisher (Route 31):** Rejected "DARK CAVE leads to another road." (All Caps). Said "This MAIL isn't for me."
- **Cooltrainer M (Route 31):** Generic dialogue about Dark Cave. Not the recipient.
- **Wade (Route 31):** Called (Turn 9576). Waiting on Route 31 to share something (Berry/Item).
- **PC Mechanics:** "Move Mail" requires open slot in PC Box.
- **Dark Cave:** Connects Route 31, 45, 46. Needs Flash.

## Tile Mechanics
- **Standard:** FLOOR, GRASS, DIRT.
- **Blockers:** WALL, TREES (Cut), WATER (Surf), WHIRLPOOL (Whirlpool), WATERFALL (Waterfall).
- **Interactables:** HEADBUTT_TREE, CAVE, WARP_CARPET, LADDER.
- **Puzzle:** ICE (Slide until hit).

## Mail Mechanics
- **Holding Mail:** Prevents depositing Pokémon. Must be removed first.
- **Removal:** "Move PKMN w/o Mail" in PC strips mail *if* PC Mailbox has space.
- **PC Mailbox Full:** "Send to PC" fails. Mail goes to Bag.
- **Writing:** Pressing Start in Mail menu triggers Printer Error. Use B.
- **Attachment:** Pokémon must hold nothing to receive mail.

## Quest Logic: Kenya Delivery
- **Goal:** Deliver Kenya (Spearow) with specific mail to Fisher (Route 31).
- **Recipient:** Fisher at (17, 7), Route 31.
- **Password:** "DARK CAVE leads to another road" (Verified "DARK CAVE" caps).
- **Plan:**
  1. Get Belladonna (Cut). (Done)
  2. Cut tree at (13, 5).
  3. Read sign at (31, 5) for EXACT punctuation.
  4. Write Mail.
  5. Deliver to Fisher at (17, 7).

## Current Quest: PC Swap
1.  **Deposit:** Hematite (Pinsir). (Mail removed).
2.  **Withdraw:** Belladonna (Oddish).