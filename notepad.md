# Strategy: The Suicune Pursuit
- **Quest Started:** Turn #50620 (Cianwood City)
- **Status:** Rocks respawned. Need to smash (4, 19) to access the left corridor.
- **Walking Route to Suicune (14, 10):**
  1. Navigate to (5, 19) and smash rock at (4, 19).
  2. Move to (2, 19) via (4, 19) -> (3, 19) [WALL?] -> NO, check Row 20.
  3. Path: (4, 19) -> (4, 20) [Slope] -> (3, 20) -> (2, 20).
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
- FLOOR_UP_WALL: Terrace edges/slopes. Can be walked onto and across.
- ROCK (Object): Blocks movement; can be cleared with Rock Smash. Respawns upon map transition.

# Lessons Learned
- **Cianwood Pathing:** (11, 15) leads to a dead-end pocket. Use the far-left corridor (X=0-2) instead.
- **Respawn Logic:** Overworld rocks respawn when leaving and re-entering the area.
- **Fly Map:** Cursor positions: New Bark (East), Cherrygrove (West), Violet (North), Azalea (South), Goldenrod (West/North), Olivine (West), Cianwood (Far West).
- **Suicune Spot:** (14, 10) in Cianwood City. 
- **Annotation Alert:** Ignore overworld coordinate labels while on the Fly map.