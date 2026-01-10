# Persistence Knowledge
## Tile Mechanics (Global)
- FLOOR: Traversable. Standard walking surface.
- WALL: Impassable.
- LADDER: Floor change (e.g. 1F to B1F).
- WARP_CARPET_DOWN: Map transition.
- COUNTER: Face and press A to interact.
- WATER: Requires SURF.
- LEDGE: Semi-traversable (jump down).
- GRASS: Wild encounter zone.
- HOLE: Fall to floor below.

## Active Quest: Find Granddaughter
- Started: Turn 37715. Timestamp: Friday, January 9, 2026 at 5:17 PM PST.
- Status: Investigating B1F. Sailor at (31, 6) blocks the eastern corridor. Path at (30, 6) is clear.
- Strategy: Bypass sailor at (31, 6) by moving through (30, 7) -> (30, 6) -> (30, 5).
- Target: Explore western corridor at x=28.
- Obstacle: Super Nerd at (26, 9) acts as a wall and blocks the corridor at x=26.
- Failure Log:
    - Attempted (31, 7) to (26, 10) via find_path_v2 (Turns 37919-37940). Reason: Super Nerd at (26, 9) blocks x=26 corridor. Targeting x=28 instead.
- Clues: Gentleman (2, 17) on 1F says she's energetic. Sailor at (31, 6) was looking for his "lazy bum" buddy. Found buddy at (30, 6). Both sailors now on duty.

## Kanto Strategy
- Goal: Collect 8 Kanto badges.
- Target 1: Lt. Surge (Vermilion City).
- MVP: GNEISS (Graveler) Lv 51. Ground-type immunity to Electric.

## Lessons Learned
- XENON (Haunter) is immune to Normal moves.
- Status: Paralysis reduces speed by 75%.
- NPCs may block corridors until specific events/dialogue.
- NPCs update positions after a map transition.
- Super Nerd at (26, 9) acts as a wall and blocks the corridor at x=26.
- Lesson: Keep warp markers (like ladders) permanent for efficient navigation.