Mt. Moon Tile Semantics & Mechanics (Synthesized Turn 4322):
- Floors are NOT strictly defined by color. Both "Brown Speckles" and "Purple Zig-Zags" can exist on the same elevation. (Proved Turn 4319 by walking freely between them at X=13/14, Y=29).
- Elevation Boundaries (Cliffs): Impassable boundaries between floor types are explicitly marked by black shadow lines on the edges of the tiles (e.g., horizontal black lines at Y=26, X=17).
- Solid Walls: `Obstacle/Cave_Wall_Blue` (light blue rock walls) block movement on the same elevation.
- Stairs/Ladders: `Walkable/Stairs_Up` are horizontal lines. `Warp/Ladder_Down` are square holes with ladders.
- False Positives: The 2x1 wooden structure at (15, 23) is a solid SIGN, NOT stairs. (Exhaustively collision-tested from all 4 cardinal directions and verified blocked on Turn 4308).

LADDER MAPPING REVELATION:
- Ladders do NOT always share the same X,Y coordinates between floors!
  - 1F (25, 15) <-> B1F (25, 15) [1:1]
  - 1F (17, 11) <-> B1F (25, 9) [Offset]
  - B1F (17, 11) <-> B2F (25, 9) [Offset]
  - B1F (13, 27) <-> B2F (15, 27) [Offset]

Active Hypotheses:
- Black cliff lines (shadows) dropping South might act as one-way ledges (jumpable). Testing at (17, 25) moving DOWN to (17, 26).
- Turn 4324: From (13, 29), I walked Left to (12, 29). Then attempted to walk Down to (12, 30). Movement was BLOCKED. (12, 30) is purple, and has a black line on its top edge. This confirms the horizontal cliff boundary at Y=30.
- Testing vertical cliff boundary at X=11/12 by attempting to walk Left from (12, 29) to (11, 29).