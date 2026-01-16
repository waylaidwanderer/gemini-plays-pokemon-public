# Strategy: The Suicune Pursuit
- **Quest Started:** Turn #50620 (Cianwood City)
- **Status:** Rocks respawned after traveling. Need to smash (5, 29) to access the left corridor.
- **Walking Route to Suicune (14, 10):**
  1. Navigate to (6, 29).
  2. Smash rock at (5, 29).
  3. Move to (2, 30) via (4, 29) -> (4, 30) -> (3, 30).
  4. Walk North to (2, 14).
  5. Walk East to (8, 14), then North to (8, 12).
  6. Walk East to (14, 12), then North to (14, 10).
- **Note:** Be prepared for Eusine battle immediately after Suicune bolts.

# Tile Mechanics (Verified)
- FLOOR: Standard traversable terrain.
- WALL / BUOY: Impassable terrain.
- WATER: Traversable only with Surf.
- DOOR / WARP_CARPET: Map transition points.
- LEDGE_HOP_DOWN: Allows jumping down (South) but blocks movement from the opposite direction (North).
- FLOOR_UP_WALL: Terrace edges. Can be walked onto and across.
- COUNTER: Blocks movement; interact from an adjacent tile.
- ROCK (Object): Blocks movement; can be cleared with Rock Smash. Respawns upon map transition.

# Lessons Learned
- **Cianwood Pathing:** (11, 15) leads to a dead-end pocket. Use the far-left corridor (X=0-2) instead.
- **Respawn Logic:** Overworld rocks respawn when leaving and re-entering the area.
- **Menu Navigation:** The 'Switch items?' confirmation box is modal; B button does not close it. Use A on NO to exit.
- **Fly Map:** Cursor positions: New Bark (East), Cherrygrove (West), Violet (North), Azalea (South), Goldenrod (West/North), Olivine (West), Cianwood (Far West).
- **Suicune Spot:** (14, 10) in Cianwood City. Requires Rock Smash at (5, 29) to reach via walking. [Verified]
- **Annotation Alert:** Ignore overworld coordinate labels while on the Fly map.