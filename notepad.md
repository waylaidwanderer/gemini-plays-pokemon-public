# Strategy: The Suicune Pursuit
- **Quest Started:** Turn #50620 (Cianwood City)
- **Status:** Exploring walking route to Suicune (14, 10).
- **Walking Route (Testing):**
  1. Navigate to (4, 20) via (6, 20).
  2. Move West to (2, 20) to reach the left corridor.
  3. Walk North to (2, 14).
  4. Walk East to (8, 14), then North to (8, 12).
  5. Walk East to (14, 12), then North to (14, 10).
- **Alternative:** Surf around the east side (X=23) if walking route is blocked.
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
- **Suicune Spot:** (14, 10) in Cianwood City. 
- **Annotation Alert:** Ignore overworld coordinate labels while on the Fly map.