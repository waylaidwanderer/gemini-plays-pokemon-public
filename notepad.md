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
- **Mail Management:** Mass delete mail at PC is efficient. "Send to PC?" -> YES to discard.
- **Menu Navigation:** Pressing Start in Mail menu triggers Printer Error. Use B.
- **Tool Safety:** OCR verification is critical. `write_mail_dark_cave` failed.
- **Mail Mechanics:** Kenya must hold nothing to receive mail. "ITEM" menu option appears if holding non-mail item OR nothing.
- **Status:** Mail successfully attached to Kenya.
- **Next Step:** Deliver to Fisher on Route 31.
- **Route:** Violet City -> Route 31 Gate -> Route 31.
- **Note:** Fisher is at (17, 7) on Route 31.
- **Log:** Manual mail writing worked. "DARK CAVE leads to another road." confirmed.