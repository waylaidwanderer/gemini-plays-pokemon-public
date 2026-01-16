# Strategy: The Suicune Pursuit
- **Time Check:** Attempting sighting since Turn #50620.
- **Objective:** Trigger Suicune sighting at (14, 10) in northern Cianwood.
- **Eusine Battle Prep:** Lead with Lv64 Calcifer.
- **Current Plan (The Grand Loop):**
  1. Move East to (21, 44), then South to (21, 45), then East to (28, 45) (Water).
  2. Surf South to (28, 50), then West on Row 50 to (12, 50) (Terrace Climb).
  3. Move North to (12, 48), then West to (8, 48).
  4. Move North to (8, 46), then West to (2, 46).
  5. Move North via X=2 corridor to (2, 10), then East to (14, 10).
- **Verification:** X=2 corridor and Row 50-51 bypasses confirmed via Python BFS.

# Tile Mechanics (Global)
- FLOOR: Standard traversable terrain.
- WALL / BUOY: Impassable terrain.
- WATER: Traversable only with Surf.
- LEDGE_HOP_DOWN: One-way jump DOWN (South). Blocks North movement.
- FLOOR_UP_WALL (Terrace Climb): One-way jump UP (North). Blocks South movement.
- ROCK (Object): Blocks movement; cleared with Rock Smash. Respawns on map exit.

# Area Notes: Cianwood City
- **Dead Ends:** (11, 15) is a pocket blocked by WALL at (11, 13) and (12, 14).
- **Shortcut Tiles:** (5, 29), (4, 25), (8, 16), (9, 17) (Smashed Rocks).
- **Partition wall:** (29, 49) is a dead end from the North.