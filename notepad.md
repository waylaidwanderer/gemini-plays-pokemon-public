# Current Strategy
- **Primary Goal:** Reach Blackthorn City via Ice Path.
- **Current Status:** In Ice Path 1F at (18, 20). Standing on ICE.
- **Mechanics:** 
  - **Ice Tiles:** Player slides until hitting an obstacle or non-ice tile.
  - **Ledges:** `FLOOR_UP_WALL` at (20, 24) is a collision wall, NOT a ledge.
- **Navigation:**
  - Entrance: (4, 19).
  - **Path Discovery:**
    - South-East area is a dead end. Escape route found.
    - **Escape Route:**
      1. (20, 23) -> Up to (20, 22). (Done)
      2. Slide Left to (18, 22). (Done)
      3. Slide Up to (18, 20). (Done)
      4. Slide Left to (14, 20).
      5. Slide Up to (14, 16).
      6. Slide Left to (13, 16) [Floor].
    - This leads to the **West Path** (x=0 to 13).
  - **Plan:** Execute Escape Route steps 4-6 to reach safe ground at (13, 16).

# Tile Mechanics
- **FLOOR:** Walkable.
- **WALL:** Impassable.
- **WATER:** Surfable.
- **HEADBUTT_TREE:** Interactable/Obstacle.

# Key Log
- **Turn 16261:** Surfing on Route 44 (35,9).
- **Turn 16240:** Defeated Psychic Phil.
- **Turn 16222:** Confirmed Suicune not in Pokedex.
- **Route 44 Update:** North/East bank of 2nd lake (Zach's island) is a DEAD END (Ledges block Eastward travel).
- **Correction:** Path to Blackthorn must be via the South Path, accessible from the 1st lake (likely landing South at x=27).
- **Next Step:** Backtrack to 1st lake and explore South bank.
- **Turn 16312:** Defeated Cooltrainer Cybil. Proceeding East on South Path to Blackthorn City.
- **Turn 16322:** Defeated Cooltrainer Allen at (37,15).
- **Turn 16327:** At (44,4). Path blocked by ledges. Looping South to (44,14) then East to (49,14) to use the gap.
- **Turn 16328:** Entered Ice Path 1F at (4,19).
- **Observation:** Spotted an Item Ball at (32, 23) in the eastern ice area, currently separated by a wall.
- **Observation:** Spotted another Item Ball at (35, 9) in the far North-East, currently unreachable from the low ground.
- **Correction:** The "South-East Path" was a dead end.
- **Hypothesis:** The way forward is likely jumping the ledge at (18, 24) to access the southern rows (25+).