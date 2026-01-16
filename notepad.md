# Active Strategy: The Suicune Pursuit
- **Goal:** Trigger Suicune sighting at (14, 10) in northern Cianwood.
- **Battle Prep:** Lead with Lv64 Calcifer to sweep Eusine's team (Drowzee, Haunter, Electrode).
- **Plan (The X=2 Expressway):**
  1. Currently at (17, 45). Move Right to (18, 45).
  2. Move Down to (18, 46) then South to (18, 50).
  3. Move West on Row 50 to (12, 50), then North to (12, 48), then West to (8, 48).
  4. Move North to (8, 46), then West to (2, 46).
  5. Move North via X=2 corridor to (2, 10).
  6. Move East on Row 10 to (14, 10) for the sighting.
- **Verification:** X=18 and Row 50-51 bypass confirmed clear of one-way barriers via Python BFS. X=2 corridor is clear of all barriers.

# Progress Tracking
- **Sighting Pursuit Start:** Turn #50620.
- **Key Discovery:** Cianwood's cliffs are one-way (North only). The Grand Loop via X=18/Row 50 is required.
- **Acquired:** Rock Smash (GNEISS).
- **Smashed Rocks:** (5, 29), (4, 25), (8, 16), (9, 17).

# Tile Mechanics (Verified)
- FLOOR: Standard terrain.
- WALL / BUOY: Impassable terrain.
- WATER: Traversable only with Surf.
- LEDGE_HOP_DOWN: One-way jump DOWN (South). Blocks North.
- FLOOR_UP_WALL (Terrace): One-way jump UP (North). Blocks South.
- ROCK (Object): Blocks movement; cleared with Rock Smash.

# Area Notes: Cianwood City
- **Dead Ends:** (11, 15) is a pocket blocked by walls at Row 13.
- **Navigation:** X=2 is the only land corridor reaching Row 10 from the south. X=4 is blocked by a wall at (4, 23).