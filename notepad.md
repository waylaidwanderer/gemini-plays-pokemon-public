# Gem's Pokémon Crystal Knowledge Base

## Tile Mechanics (Verified Traversability)
- FLOOR: Traversable.
- WALL: Impassable.
- WATER: Traversable with SURF.
- TALL_GRASS / grass: Traversable.
- DOOR / WARP / CAVE: Entry points.
- LADDER / STAIRCASE: Moves between floors.
- COUNTER: Impassable. Interact from front.
- MART_SHELF: Impassable. Interaction untested.
- LEDGE_HOP_DOWN: One-way North to South.
- FLOOR_LEFT_WALL / FLOOR_RIGHT_WALL / FLOOR_UP_WALL: Impassable.
- OBJECTS (NPCs/Items): Impassable.
- WARP_CARPET_DOWN: Exit point.
- PC / BOOKSHELF: Impassable.

## Battle Strategy & History
- **Erika Strategy:** Lv 42-46 team. Swept with Calcifer (Fire).
- **Gym Trainers Defeated:** Jo & Zoe, Tanya, Michelle, Julia.

## Economy & Shopping
- **Celadon Dept Store Exploration (Started Turn 41740):**
    - 1F: Directory checked.
    - 2F: Fully explored. Stocked up on healing items.
    - 3F: Arrived Turn 41804. TM Shop inventory: TM10, TM11, TM17, TM18, TM37.
- **Long Term Shopping Plan:**
    - 4F (Wiseman Gifts): Purchase Evolution Stones.
    - 5F (Drugstore): Stat boosters.
    - Rooftop: Vending machines (Fresh Water, Soda Pop, Lemonade). Give to thirsty girl for TMs.

## Celadon City Investigation
- **Secret Wing Access:** Reached via back door at (16,3).
- **Mansion Roof House:** Pharmacist (3,2) tells "terrifying tale" ONLY at night.
- **Gym Access:** Path behind southern hedges (Cut tree at 28,35). Follow path west to (5,35), then north through the gap in the ledge at (5,33). Warp at (10, 29).

## Kanto Secrets & NPC Schedules
- **Daisy Oak (Pallet Town):** Has tea every day from 3:00 PM to 4:00 PM. (Source: Chad)

## Strategy for Remaining Kanto Journey
- **Objective:** Defeat Janine (Fuchsia), Blaine (Cinnabar/Seafoam), Blue (Viridian).
- **Strategic Plan for Kanto Badges:**
    1. Celadon (Rainbow) - COMPLETED.
    2. Fuchsia (Soul) - Next target. Use Cycling Road or Route 12-15.
    3. Cinnabar/Seafoam (Volcano) - After Fuchsia. Use Surf from Pallet or Fuchsia.
    4. Viridian (Earth) - Final badge. Blue is the leader.
- **Rematches:** Alan (Route 36) wants a battle.

## General Lessons & Error Log
- **NPC Interaction:** Face the counter tile in front of NPCs (Nurses, Clerks, etc.) then press A.
- **Ledges:** Hop down south only.
- **Celadon Pillars:** Col 12 and Col 36 block horizontal movement.
- **Tool Maintenance:** Ensure tool logic includes all traversable types. Fix immediately when missing types are identified.
- **Inventory Sync:** Calcifer is Lv 62. 2x IRON and 1x RARE CANDY used successfully. Bag slots cleared.

## Reflection Turn 41829
- **Immediate Execution:** No deferred tasks.
- **Notepad Hygiene:** Reorganized and removed redundant logs. Added start turn for 3F.
- **Map Hygiene:** Updated markers on 3F. Deleted incorrect 2F markers.
- **Automation Strategy:** Fixed find_reachable_unseen_tiles logic. Created strategic_planner_v2.
- **Goal Clarity:** Goals are concrete outcomes. Methods in notepad.
- **Error Analysis:** Distilled lesson on marker map_id formatting. Fixed root hypothesis on 3F TM stock. Verified Calcifer's stats.