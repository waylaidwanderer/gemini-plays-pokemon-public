# Gem's Journey in Pokémon Crystal

## Current Strategy
- **Primary Goal:** Deliver Kenya to Route 31.
- **Secondary Goal:** Travel to Mahogany Town (Route 42).
- **Tertiary Goal:** Train Party to Level 30+.

## Quest: Deliver Kenya (Route 31)
1.  **Status:** Recovering from Tool Failure (Printer Error).
2.  **Issue:** `write_mail_dark_cave` caused unexpected menu navigation and Printer Error.
3.  **Action Plan:**
    - **Step 1:** Clear Error & Exit Menus (Executing B x4).
    - **Step 2:** Check Kenya's held item/mail status.
    - **Step 3:** If mail is incomplete/wrong, remove and retry MANUALLY.
    - **Step 4:** Write "DARK CAVE leads to another road." (With period).
    - **Step 5:** Return to Fisher.

## Knowledge Base
- **Fisher (Route 31):** Wants mail. Rejects if text/item incorrect.
- **PC Mechanics:** "Move Mail" requires open slot in PC Box. Tossing mail frees space.
- **Dark Cave:** Connects Route 31, 45, 46. Requires Flash/Rock Smash/Surf.
- **Bug Catcher Wade:** Route 31. Calls for swarms.

## Tile Mechanics
- **Standard:** FLOOR, GRASS, DIRT.
- **Blockers:** WALL, TREES (Cut), WATER (Surf), WHIRLPOOL (Whirlpool), WATERFALL (Waterfall).
- **Interactables:** HEADBUTT_TREE, CAVE, WARP_CARPET, LADDER.
- **Puzzle:** ICE (Slide until hit).

## Log & Lessons
- **Mail Management:** Mass delete mail at PC is more efficient than "one-in-one-out".
- **Menu Navigation:** Pressing Start in Mail menu causes "Printer Error". Use B to cancel.
- **Mail Removal:** "Send to PC?" -> NO to keep for rewrite, YES to discard.
- **Tool Safety:** OCR verification is critical before assuming tool success.
- **Tool Debug:** `write_mail_dark_cave` caused Printer Error. Likely selected a hidden "PRINT" option or navigated out of bounds. Must fix before reuse.
- **Mail Check:** Failed to GIVE mail because Kenya is already holding one.
- **Action:** Must TAKE old mail first.
  1. Exit Pack (B).
  2. Enter Party Menu.
  3. Kenya -> Take Mail -> Send to PC.
  4. Give fresh Flower Mail.
  5. Write Message.