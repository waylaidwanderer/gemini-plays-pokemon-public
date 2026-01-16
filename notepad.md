# Strategy: The Rock Smash Pivot
- **Current Plan:** Purchase TM08 at Goldenrod Dept. Store 5F (¥1000) -> Teach to GNEISS (replacing Defense Curl) -> Fly to Cianwood -> Smash boulders at (4, 19) and (8, 16) to reach Suicune at (14, 10).
- **Verification:** Route 36 Fisher (44, 9) flag is set but item was missing from bag/PC. Purchase is the confirmed fallback.

# Global Tile Mechanics
- FLOOR: Traversable.
- WALL / BUOY / HEADBUTT_TREE: Impassable.
- WATER: Requires Surf.
- DOOR / WARP_CARPET: Warp point.
- STAIRCASE: Warp point (stairs/elevator).
- COUNTER: Impassable; interact from adjacent tile.
- SMASHABLE_ROCK (Object): Requires Rock Smash.

# Lessons Learned
- **Fisher Dialogue:** "If any rocks are in your way..." is post-gift. flag set even if item gone.
- **Arthur (45, 6):** Only gives Hard Stone on Thursdays.
- **Menu Navigation:** The "Switch items?" confirmation box is modal; B button does not close it. Use A on NO to exit.
- **Fly Map:** Cursor snaps to towns. Relative positions: New Bark (East), Cherrygrove (West of New Bark), Violet (North of Cherrygrove), Azalea (South), Goldenrod (West/North of Azalea), Olivine (West), Cianwood (Far West).
- **Tool Alert:** fly_to_city_v2 was unreliable due to menu logic; deleted. Use manual menu_navigator_refined_v2 for Flying.
- **Coordinates:** Notepad coordinates (e.g., New Bark 14, 10) refer to the World Map/Town Map grid, not the Fly Map cursor position.