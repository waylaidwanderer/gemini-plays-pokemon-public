# Strategic Notes
## Objectives
- **Primary:** Complete Pokedex.
- **Secondary:** Hunt Roaming Beasts (Raikou/Entei).
- **Navigation:** Buy 10 Super Repels (Celadon Dept. Store).

## Celadon Search Log
- **Goal:** Buy 10 Super Repels.
- **2F:** Trainer's Market. Right (Balls) checked - No Repels. Left (Meds) - NEEDS CHECK.
- **3F:** TM Shop.
- **4F:** Gifts (Dolls/Mail).
- **5F:** Drug Store (Vitamins/Battle Items).

## Roamer Hunt
- **Target:** Raikou & Entei.
- **Method:** Route 37 Loop.

# Current Strategy
## Resupply Run
- **Goal:** Buy Super Repels in Celadon.
- **Location:** Celadon Dept. Store (2F).
- **Action:** Select 'SUPER REPEL'.
- **Status:** Moving Cursor Up (x2).
- **Reasoning:** 'navigate_menu' overshot to 'CANCEL'. Using manual inputs to correct.
- **Tool Note:** `navigate_menu` presses buttons twice per request. DO NOT USE for single-step navigation.
- **Fallback:** Saffron Mart.
## Lessons Learned
- **Inventory Checks:** Always scroll through the ENTIRE list of items a clerk sells. Don't assume contents based on the first few items (e.g., Medicine clerk might also sell Repels).
- **Tool Warning:** `navigate_menu` appears to register double inputs (e.g., one 'Up' becomes two 'Up' presses). Use `press_buttons` for precise menu navigation to avoid overshooting.
- **Safety First:** Encountered a state desync (Intermediate States vs Current Screen). Aborted transaction to prevent accidental purchase of expensive items. Backing out fully before retrying.