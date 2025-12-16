# Gem's Journey in Pokémon Crystal

## Current Objectives
- **Primary:** Earn the Zephyr Badge in Violet City.
- **Secondary:** Reach Cherrygrove City.
- **Tertiary:** Switch TOPAZ to Lead.

## Quest Log (Completed)
- Delivered Mystery Egg to Elm.
- Received Pokedex from Oak.
- Defeated Rival Silver.

## Game Mechanics & Lessons
- **Lesson:** ALWAYS verify "Important Events" log before assuming quest state. I backtracked unnecessarily because I forgot I had already done the Mr. Pokemon event.
- **Battle:** Watch "Text History" closely. If "Got away safely!" appears, the battle is over. Do not attempt to run again.
- **Menus:** Wait for visual confirmation (text/cursor) before inputting subsequent menu commands.
- **Running:** Success depends on Speed. If slower, multiple attempts may be needed.

## Tile Mechanics
- **LEDGE_HOP_RIGHT:** One-way jump from Left to Right. Blocks movement from Right to Left.
- **LEDGE_HOP_DOWN:** One-way jump from Up to Down. Blocks movement from Down to Up.
- **WALL:** Impassable.
- **HEADBUTT_TREE/CUT_TREE:** Impassable (unless interacting with specific move).
- **TALL_GRASS:** High encounter rate.
- **WARP_CARPET:** Transports to new map.

## Trainer Card (Gem)
- **ID:** 24_6
- **Money:** ¥3300
- **Badges:** 0
- **Pokedex:** 2 (Cyndaquil, Sentret)
- **Party:**
    1. GARNET (Cyndaquil) Lv7 - Tackle, Leer, Smokescreen.
    2. TOPAZ (Sentret) Lv3 - Tackle.

## Key Items
- Pokegear (Phone, Map)
- Pokedex
- Poke Balls

## Navigation History & World Knowledge
- **New Bark Town:**
    - Elm's Lab: (6,3). Player's House: (13,5).
    - Rival (Silver) stole a Pokemon.
- **Route 29:**
    - Connects New Bark Town (East) to Cherrygrove City (West).
    - **Ledge Maze:** Northern section (Rows 0-7) separate from Southern (Rows 8-18).
    - **Gap:** Found at (43, 14) to bypass ledges heading West.
    - Pokemon: Pidgey, Sentret, Hoppip (Day).
- **Cherrygrove City:** Pokemon Center (29,3), Mart (17,7).
- **Route 30:** North of Cherrygrove. Mr. Pokemon at (17,5).

## Immediate Plan
1. Talk to the man in the Berry House (get Berry?).
2. Exit the house.
3. Continue North on Route 30 to Violet City.

## Tool Dev Notes
- **Lesson:** Ensure input variables in `define_tool` are accessed via `input_data`.
- **Restriction:** `press_buttons` cannot mix directional and action buttons in one list. Use `autopress_buttons: true` tools or single commands.
- **Battle Menu Mistake:** Accessed 'Start' menu during battle to switch Pokemon. This only reorders the party and does not switch the active battler. Must use 'PKMN' option in the Battle Menu to switch.
- **Battle State Confusion:** Battle with Hoothoot ended abruptly without visible text log confirmation, directly transitioning to Start Menu upon input. Confirmed Overworld state via visual inspection of Start Menu.
- **Menu Navigation Correction:** In Turn 593, I attempted to navigate the menu assuming it was open, but I had closed it in Turn 592. Always verify 'Current Screen Text' or visual overlays before assuming a menu is active. 'Down' input resulted in player movement, not cursor movement.
- **Route 30 Layout:** Split into two parallel vertical paths.
    - **Right Path:** Leads to Mr. Pokemon's House (Done).
    - **Left Path:** Leads to Route 31/Violet City (Target).
    - **Action:** Must return to Cherrygrove to access the Left Path.
- **Route 30 Correction:** Reviewed history. I previously visited the Berry House at (7, 39), which is on the Left Path. This confirms the split is accessible from the main Route 30 entrance.
- **Plan:** Re-enter Route 30 and navigate West/North-West to finding the path to Violet City (past the Berry House).
- **Berry House Info:** Man says "Check trees for BERRIES. They just drop right off." No item received directly.