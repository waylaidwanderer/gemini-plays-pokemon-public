# Current Strategy
- **Primary Goal:** Reach Blackthorn City via Ice Path.
- **Current Status:** In Ice Path 1F at (5, 16).
- **Mechanics:** 
  - **Ice Tiles:** Player slides until hitting an obstacle or non-ice tile.
  - **Ledges:** `FLOOR_UP_WALL` allows jumping South.
- **Navigation:**
  - Entrance: (4, 19).
  - **Path Discovery:**
    - The area West of x=5 is walled off at Row 16.
    - **New Hypothesis:** Access to the West Corridor (x=0) is via the South.
    - I can reach the South area (Row 22) by jumping the ledges at Row 18 (x=7-12).
    - From Row 22, I can walk West to x=0 and then North.
  - **Plan:**
    1. Walk to `(7, 17)`.
    2. Jump Ledge South to `(7, 19)`.
    3. Walk South to Row 22, then West to x=0.
    4. Head North up the corridor.

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