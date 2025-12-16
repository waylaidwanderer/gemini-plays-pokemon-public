# Gem's Journey in Pokémon Crystal

## Current Objectives
- **Primary:** Earn the Zephyr Badge in Violet City.
- **Secondary:** Reach Cherrygrove City.
- **Tertiary:** Switch TOPAZ to Lead.

## Game Mechanics & Lessons
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
1. Backtrack South from Mr. Pokemon's House to the Route 30 split (near Cherrygrove).
2. Take the West/North-West path towards Violet City.
3. Watch for trainers on the Violet City path.
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