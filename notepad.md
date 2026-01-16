# Strategy: The Suicune Pursuit
- **Quest Started:** Turn #50620
- **Goal:** Fly to Cianwood -> Smash boulders at (4, 19) and (8, 16) -> Reach Suicune sighting spot at (14, 10).
- **Execution:** Use ICARUS (Pidgeotto) to Fly to Cianwood City.

# Global Tile Mechanics
- FLOOR: Traversable.
- WALL / BUOY / HEADBUTT_TREE: Impassable.
- WATER: Requires Surf.
- DOOR / WARP_CARPET: Warp point.
- STAIRCASE: Warp point (stairs/elevator).
- COUNTER: Impassable; interact from adjacent tile.
- SMASHABLE_ROCK (Object): Requires Rock Smash.

# Lessons Learned
- **Menu Navigation:** The "Switch items?" confirmation box is modal; B button does not close it. Use A on NO to exit.
- **Fly Map:** Starts at New Bark Town. Sequences: 9L+1U (Cherrygrove), 4L+2U (Azalea), 3L+3U (Olivine), >30L+Down? (Cianwood). Always verify text before A. Cursor wraps East-West.
- **Coordinates:** Notepad coordinates (e.g., Cianwood 14, 10) refer to the internal map grid, not the Fly Map cursor position.
- **Suicune Spot:** (14, 10) in Cianwood City. Requires Rock Smash at (4, 19) and (8, 16) to reach.
- **Tool Logic:** `fly_to_destination` exceeded the 50-button limit (53 buttons). Sequences must be broken into chunks or optimized.
- **Fly Map wrapping:** Hypothesis: Going Right from New Bark might wrap to the West (Cianwood). Testing now.
- **Fly Map Wrap:** Sequence of 50 buttons (mostly Left) from New Bark resulted in landing at Mahogany Town (15, 14). This confirms East-West wrapping and suggests Cianwood requires a more precise South-West path or fewer Left presses to avoid overshooting.
- **Current Status:** In Mahogany Town. Retrying flight to Cianwood.