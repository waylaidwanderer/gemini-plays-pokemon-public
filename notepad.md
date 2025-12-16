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
- **Status:** See Game State for Money, Badges, and Party HP.
- **Party:**
    1. GARNET (Cyndaquil) - Fire.
    2. TOPAZ (Sentret) - Normal.

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
1. Execute complex navigation path North to Route 31 entrance at (6, 0).
   - Path bypasses Youngster (5,23), Row 17 Ledge, Row 11 Ledge, and other trainers.
2. Enter Violet City.
3. Heal at Pokemon Center.

## Route 30 Navigation Details
- **Ledge Bypass (Row 25):** Use gap at x=5.
- **Youngster Bypass:** Go around (5, 23) using x=4.
- **Ledge Bypass (Row 17):** Use x=3.
- **Ledge Bypass (Row 11):** Use x=0 or x=1 (requires moving Left at Row 12).
- **Trainer Bypass:** Avoid (2, 13) and (1, 9) by adjusting X-coordinate.

## Tool Dev Notes
- **Lesson:** Custom Tool Limit is 5. Must delete an existing tool (`delete_tool`) before defining a new one.
- **Lesson:** Ensure input variables in `define_tool` are accessed via `input_data`.