# Strategy: The Suicune Pursuit
- **Time Check:** Attempting sighting since Turn #50620.
- **Objective:** Trigger Suicune sighting at (14, 10) in northern Cianwood.
- **Eusine Battle Prep:** Lead with Lv64 Calcifer. Sweep with Flamethrower/Thunderpunch.
- **Current Plan (The Southern Surf Loop):**
  1. Currently at (28, 45) on WATER.
  2. Surf South to Row 51 (bypassing Terrace Climbs via eastern coast).
  3. Land at (24, 51) and walk West on Row 51 to (2, 51).
  4. Move North via X=2 corridor to (2, 12) (Clear of all barriers).
  5. Move East on Row 12 to (14, 12), then North to (14, 10) for the sighting.
- **Verification:** X=2 corridor and Row 51 bypass confirmed clear of one-way barriers via Python BFS.

# Tile Mechanics (Global)
- FLOOR: Standard traversable terrain.
- WALL: Impassable terrain.
- BUOY: Impassable terrain (Blocks both Surf and Walk).
- WATER: Traversable only with Surf.
- LEDGE_HOP_DOWN: One-way jump DOWN (South). Blocks North movement.
- FLOOR_UP_WALL (Terrace Climb): One-way jump UP (North). Blocks South movement.
- ROCK (Object): Blocks movement; cleared with Rock Smash.

# Area Notes: Cianwood City
- **Shortcut Tiles:** (5, 29), (4, 25), (8, 16), (9, 17) (Smashed Rocks).
- **Dead Ends:** (11, 15) is a pocket blocked by WALL at (11, 13) and (12, 14).
- **Partition wall:** (29, 49) is a dead end from the North.