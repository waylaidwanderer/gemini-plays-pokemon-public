- VICTORY ROAD 1F EMPIRICAL CONSTRAINTS:
  1. Elevation: DR Blocky = Level 1 (Walkable). DP Speckled = Level 3 (Walkable via stairs).
  2. Walls: Blue Rubble, Chasms, and Level 1 -> Level 3 transitions (without stairs) are SOLID WALLS.
  3. Level 3 to Level 1 transitions facing South act as JUMPABLE LEDGES (e.g., from 2,8 down to 2,9).
  4. X=4 is Blue Rubble EXCEPT at Y=8 where it is Level 1.
  5. To reach West side: Navigate Level 3 East to X=12, then North to (7,6). Take stairs at (7,7) DOWN to Level 1 at (7,8). Walk West on Level 1 along Y=8.
- VICTORY ROAD 1F ELEVATION RULES:
  - DR Blocky = Level 1 (Low) Walkable Floor.
  - DP Speckled = Level 3 (High) Walkable Floor (accessed via stairs).
  - Blue Rubble & Chasms = SOLID WALL.
  - Transitions between DR Blocky and DP Speckled without stairs act as SOLID WALLS.
- 1F EMPIRICAL BLOCKAGES (PERMANENT CONSTRAINTS):
  1. X=12 corridor is blocked Northward at Y=13 by Level 3 floor.
  2. The entire East side (X>=16) is a dead end, blocked Northward at Y=10.
  3. West Area (X=1 to X=4) is blocked Northward at Y=14.
- CURRENT EXPLORATION GOAL:
  1. Warp at (8,17) to reset the entrance boulder to (5,16).
  2. Test if the boulder can be pushed UP the stairs at (5,13) to Level 3.
  3. If yes, push it into the Blue Chasm at (9,12) to bridge the gap to the East side!
- LOWER 2F (DP Speckled) NAV NOTES:
  - Moving South from (3,6) down X=3 leads to a dead end at (3,10). The transition to Y=11 is DR Blocky (Upper 2F) and acts as a solid wall.
  - The path East MUST be taken along Y=6.
  - The Juggler at (4,2) cannot see the player at (4,6) because the Blue Rubble at (4,4) blocks line of sight.
- Update on 2F West Elevation: DP Speckled is HIGH (Level 3) and DR Blocky is LOW (Level 1). You can jump South from DP Speckled to DR Blocky. Y=4 is a solid wall of Blue Rubble. To reach the 3F ladder at (2,0) from (4,5), jump South to the DR Blocky area at Y=6, walk East to the clear corridor at X=9, go North to Y=2, West to X=2, and North to (2,0).
- 2F West Empirical Layout:
  - DR Blocky = Low (Level 1), DP Speckled = High (Level 3).
  - Moving Low -> High (North) is a SOLID WALL (e.g. (2,5) -> (2,4)).
  - Moving High -> Low (South) is a JUMPABLE LEDGE (e.g. (0,8) -> (0,9)).
  - Ladder to 3F is at (1,1) on High ground.
  - To escape the Low pit, head South to Y>=11, East to stairs at (5,10), ascend to High ground, and walk North using the Y=4 High ground bridge.
- 2F West Pathing Fix: The bumps at Y=4 and Y=5 were NOT caused by an invisible elevation wall. They were caused by walking directly into the static Moltres encounter, whose 2x2 sprite occupies (1,4), (2,4), (1,5), and (2,5). The safe path to the 3F ladder at (1,1) is to cross Y=4 at X=4, then move Left along Y=3.