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
1. Heal at Cherrygrove Pokemon Center.
2. Head North-West to the left path of Route 30.
3. Proceed to Violet City.
- **Route 29 Strategy:**
    - **Solution Found:** Navigate Northern Path (Row 3/4) to X=16, then dip South to Row 6 to bypass Ledges.
    - **Path:** (24,3) -> Down to (24,5) -> West to (21,5) -> Up to (21,4) -> West through gap at (20,4) -> West to (16,4) -> South to (16,6) -> West to Cherrygrove.
- **Route 46:**
    - Accessed via Gatehouse at (27, 1).
    - **DEAD END:** Blocked by ledges at Row 23. Do not return unless exploring Dark Cave later.
- **Route 29 Middle Section:**
    - Contains Fruit Tree and Cooltrainer.
    - Protected by one-way ledges exiting to East and South.
    - Likely accessible only from Route 46 North (later game) or a hidden path I missed.
    - **Action:** Ignore for now, proceed to Cherrygrove.

- **Route 29 Path:** Taking Row 6 West. Jumping ledge at (8,6) to bypass remaining grass.
- **Tool Dev Lesson:** When defining tools, ensure input variables are correctly accessed via `input_data` or the defined schema variable names. JSON parsing within tools requires `import json`.
- **Mart Mechanics:** Use Up/Down to change quantity. Selection wraps around? (Need to verify).
- **Tool Dev Note:** Variable injection in `define_tool` scripts failed for list inputs ('btn_seq'). Needs investigation. `bfs_path` variables were likely never tested. Future tools should assume variables might need different access or debugging.
- **System Restriction:** `press_buttons` blocks mixing directional and action buttons (e.g. `['Down', 'A']`). Use single inputs or define a tool with `autopress_buttons: true` for sequences.
- **Battle Menu Mistake:** Accessed 'Start' menu during battle to switch Pokemon. This only reorders the party and does not switch the active battler. Must use 'PKMN' option in the Battle Menu to switch.
- **Battle State Confusion:** Battle with Hoothoot ended abruptly without visible text log confirmation, directly transitioning to Start Menu upon input. Confirmed Overworld state via visual inspection of Start Menu.
- **Menu Navigation Correction:** In Turn 593, I attempted to navigate the menu assuming it was open, but I had closed it in Turn 592. Always verify 'Current Screen Text' or visual overlays before assuming a menu is active. 'Down' input resulted in player movement, not cursor movement.
- **Tool Idea:** (Implemented) `use_item_sequence` defined in Turn 602.
- **Route 30 Layout:** Split into two parallel vertical paths.
    - **Right Path:** Leads to Mr. Pokemon's House (Done).
    - **Left Path:** Leads to Route 31/Violet City (Target).
    - **Action:** Must return to Cherrygrove to access the Left Path.