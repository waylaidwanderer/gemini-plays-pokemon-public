# Strategy: The Suicune Pursuit
- **Quest Started:** Turn #50620
- **Current Status:** Smashed rocks at (5, 29), (4, 25), and (4, 19). Heading to (8, 16).
- **Next Step:** Smash boulder at (8, 16) -> Reach (14, 10) to trigger Suicune sighting.

# Tile Mechanics
- FLOOR: Standard traversable terrain.
- WALL / BUOY: Impassable terrain.
- WATER: Traversable only with Surf.
- DOOR / WARP_CARPET: Map transition points.
- LEDGE_HOP_DOWN: Allows jumping down (e.g., South) but blocks movement from the opposite direction.
- FLOOR_UP_WALL: Slopes that allow movement in specific directions (e.g., North) but block others (e.g., South).
- COUNTER: Blocks movement; interact from an adjacent tile.
- ROCK (Object): Blocks movement; can be cleared with Rock Smash.

# Lessons Learned
- **Menu Navigation:** The "Switch items?" confirmation box is modal; B button does not close it. Use A on NO to exit.
- **Fly Map:** Starts at current town. Cursor moves smoothly. Relative positions: New Bark (East), Cherrygrove (West), Violet (North), Azalea (South), Goldenrod (West/North), Olivine (West), Cianwood (Far West).
- **Coordinates:** Notepad coordinates (e.g., Cianwood 14, 10) refer to the internal map grid, not the Fly Map cursor position.
- **Suicune Spot:** (14, 10) in Cianwood City. Requires Rock Smash at (4, 19) and (8, 16) to reach. [Verified - Advisor]
- **Annotation Alert:** The screen annotation system incorrectly labels Fly map tiles with overworld coordinates and 'Player' markers. Ignore these labels while on the Fly map.