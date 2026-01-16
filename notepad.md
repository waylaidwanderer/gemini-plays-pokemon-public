# Strategy: The Suicune Pursuit
- **Objective:** Trigger Suicune sighting at (14, 10) in northern Cianwood.
- **Eusine Battle Prep:** Drowzee (Lv23), Haunter (Lv23), Electrode (Lv25). Strategy: Lead with Lv64 Calcifer. Sweep with Flamethrower/Thunderpunch.
- **Current Plan (North Bypass via X=2):**
  1. From (6, 29), move South to (6, 34) to bypass the X=5 wall.
  2. Move West to (2, 34) and enter the X=2 corridor.
  3. Move North to (2, 10) and then East to (14, 10) for the Suicune sighting.
- **Smashed Rocks:** (5, 29), (4, 25), (4, 19), (9, 17), (8, 16). They respawn on map exit.
- **Alternative (Northern Wall Check):** Check if (12, 15) or (11, 15) are mislabeled rocks.
- **Contingency:** If walking paths fail, use Surf around the east side buoy gap at (23, 7). Landing spot: (16, 10).

# Tile Mechanics (Verified)
- FLOOR: Standard traversable terrain.
- WALL / BUOY: Impassable terrain.
- WATER: Traversable only with Surf.
- DOOR / WARP_CARPET: Map transition points.
- LEDGE_HOP_DOWN: One-way jump down (South). Blocks North.
- FLOOR_UP_WALL: Terrace edges. (6, 46) blocks Down movement from (6, 45).
- ROCK (Object): Blocks movement; cleared with Rock Smash. Respawns upon map transition.

# Lessons Learned
- **Cianwood Pathing:** (11, 15) is a dead-end pocket. (6, 46) blocks South movement from (6, 45).
- **Advisor Advice:** "Forget the South Bypass; the path is strictly north."
- **Time Check:** Attempting sighting since Turn #50620. Commit to X=2 corridor by Turn #50900.
- **Movement Discovery:** (6, 34) blocks South movement from (6, 33). Terrace edges (FLOOR_UP_WALL) appear to be one-way barriers (allowing North, blocking South).
- **Refined Path to Suicune (The X=2 Corridor):**
  1. From (6, 33), move North to (6, 29).
  2. Move West through smashed rock (5, 29) to (4, 29).
  3. Move North to (4, 22).
  4. Move West through the gap in the X=3 wall at (3, 22) to (2, 22).
  5. Move North to (2, 10).
  6. Move East to (14, 10) for the sighting.
- **Verification:** (3, 22) is confirmed FLOOR in Mental Map. X=3 wall exists from Y=23 to Y=29.