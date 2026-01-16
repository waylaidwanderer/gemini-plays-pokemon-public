# Strategy: The Suicune Pursuit
- **Primary Goal:** Trigger Suicune sighting at (14, 10).
- **Secondary Goal:** Defeat Eusine immediately after sighting.
- **Eusine Roster:** Drowzee (Lv23), Haunter (Lv23), Electrode (Lv25).
- **Battle Strategy:** Leading with Lv64 Calcifer. Use Flamethrower/Thunderpunch to sweep.
- **Navigation Plan:**
  1. Move to (4, 20) [FLOOR_UP_WALL].
  2. Move West to (2, 20).
  3. Walk North to Row 14.
  4. Walk East to (8, 14), then North to Row 12.
  5. Walk East to (14, 12), then North to (14, 10).

# Tile Mechanics
- FLOOR: Standard traversable terrain.
- WALL / BUOY: Impassable terrain.
- WATER: Traversable only with Surf.
- DOOR / WARP_CARPET: Map transition points.
- LEDGE_HOP_DOWN: Allows jumping down (South) but blocks movement from the opposite direction (North).
- FLOOR_UP_WALL: Terrace edges. Hypothesis: Can be walked across horizontally or entered from specific sides. [Testing in progress]
- ROCK (Object): Blocks movement; can be cleared with Rock Smash. Respawns upon map transition.

# Lessons Learned
- **Cianwood Pathing:** (11, 15) leads to a dead-end pocket.
- **Respawn Logic:** Overworld rocks respawn when leaving and re-entering the area.
- **Poke Seer's House:** (5, 17) is a regular interior, not a shortcut.