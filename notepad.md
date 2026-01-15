# Tile Mechanics
- FLOOR_UP_WALL: Blocks SOUTH. Allows NORTH. Verified: Down at (24, 45) failed (Turn 49602).
- LEDGE_HOP_DOWN: Blocks NORTH. Found at Row 15 (X=3-17).
- ROCK: Smashable rocks act as WALLs.
- Vertical Walls: X=3, 5, 9, 11, 17, 20.

# Suicune Quest (Cianwood)
## Strategy: The Sea Route (East Bypass)
Reach (14, 10) by surfing around the internal maze via the eastern sea.
1. Move East to (23, 33).
2. Surf from (23, 33) into (24, 33).
3. Surf North to Row 11, passing through buoy gap at (23, 15).
4. Surf West along Row 11 to land at (16, 11) or (15, 11).
5. Walk to Suicune at (14, 10).
- Current Step: Initiating Surf at (23, 33).

# Progress Notes
- Blocked: All land routes (X=12, X=6, X=4) are blocked by internal walls or FLOOR_UP_WALL ledges.
- Verified: (23, 15) is a clear gap in the Row 15 buoy wall.
- Verified: Row 11 is a clear horizontal path from the sea (X=24) to the plateau (X=16).
- Verified: (16, 11) is a landing point on the northern plateau.
- Verified: (16, 10) is a FLOOR_UP_WALL ledge that allows passage NORTH to Suicune.