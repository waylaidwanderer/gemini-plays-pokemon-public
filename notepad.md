# Strategy: The Suicune Pursuit
- **Time Check:** Attempting sighting since Turn #50620.
- **Objective:** Trigger Suicune sighting at (14, 10) in northern Cianwood.
- **Eusine Battle Prep:** Lead with Lv64 Calcifer. Sweep with Flamethrower/Thunderpunch.
- **Current Plan (Route 41 Southern Bypass):**
  1. Move Right to (29, 45) and transition to Route 41 (0, 45).
  2. Surf South on Route 41 to Row 51.
  3. Move Left to transition back to Cianwood at (29, 51).
  4. Walk West on Row 51 to (2, 51).
  5. Walk North via X=2 corridor to (2, 10).
  6. Walk East to (14, 10) for the sighting.
- **Verification:** BFS confirmed path via Route 41 and X=2 corridor.

# Tile Mechanics (Global)
- FLOOR: Standard traversable terrain.
- WALL / BUOY: Impassable terrain.
- WATER: Traversable only with Surf.
- LEDGE_HOP_DOWN: One-way jump DOWN (South). Blocks North movement.
- FLOOR_UP_WALL (Terrace Climb): One-way jump UP (North). Blocks South movement.
- ROCK (Object): Blocks movement; cleared with Rock Smash.

# Area Notes: Cianwood City
- **Shortcut Tiles:** (5, 29), (4, 25), (8, 16), (9, 17) (Smashed Rocks).
- **Dead Ends:** (11, 15) is a pocket blocked by WALL at (11, 13) and (12, 14).
- **Partition wall:** (29, 49) is a dead end from the North.