# Gem's Journey in Pokémon Crystal

## Current Strategy
- **Primary Goal:** Deliver Kenya to Route 31.
- **Secondary Goal:** Travel to Mahogany Town (Route 42).
- **Tertiary Goal:** Train Party to Level 30+.

## Quest: Deliver Kenya (Route 31)
1.  **Status:** Verifying Recipient.
2.  **Current Plan:**
    - **Step 1:** Check Youngster at (10, 5). (Skipped him earlier).
    - **Step 2:** If Youngster is not him, return to Fisher.
    - **Step 3:** Rewrite mail: "Dark Cave leads to another road" (Title Case).
    - **Step 4:** Retry delivery to Fisher.

## Knowledge Base
- **Fisher (Route 31):** Rejected "DARK CAVE leads to another road." (All Caps). Said "This MAIL isn't for me."
- **Cooltrainer M (Route 31):** Generic dialogue about Dark Cave. Not the recipient.
- **PC Mechanics:** "Move Mail" requires open slot in PC Box.
- **Dark Cave:** Connects Route 31, 45, 46. Needs Flash.

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
- **Mail Delivery Status:**
  - Verified "DARK CAVE" spelling on sign (All Caps).
  - Fisher rejected previous attempts likely due to typo/case.
- **Current Plan:** Give fresh Flower Mail to Kenya.
- **Password:** "DARK CAVE leads to another road" (Exact).
- **Next Step:** Write mail using `write_mail_safe` tool.