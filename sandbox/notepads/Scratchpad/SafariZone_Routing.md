# Safari Zone Systematic Routing Framework

## Session Ledger & Step Budget
- Admission: 500 steps (Turn 7795)
- In-Game Verified Milestones:
  - Turn 7883: Exactly 361 / 500 steps remaining (Start menu verified at 4, 17)
  - Turn 7900: Entered Safari Zone Area 1 at (0, 23) (~338 steps remaining)
  - Turn 7921: In battle at (24, 20) (~308 steps remaining)
  - Turn 7951: Current position (14, 24) facing Up (276 steps remaining)

## Area 1 Verified Empirical Topology & Boundaries
- Southern Boundary: Row 25 boundary bushes & statue bases (solid).
- Southern Corridor (Row 24):
  - Cols 0..13: Clear open green lawn (zero wild encounters).
  - Cols 14..25: Tall grass strip (wild encounters possible).
  - Cols 26..28: Clear open green lawn.
- Row 23 Hedge Barrier:
  - Extends along cols 8..16 (solid bush hedge).
  - Solid statue at (6, 23) [Verified Turn 7944].
  - Open lawn gap at (17..18, 23) connecting row 24 directly to row 22 [Verified Turns 7903, 7941].
- Row 22 Open Lawn:
  - Cols 12..15: Open lawn directly in front of western staircase at (12, 21).
  - Col 16: Bush tile at (16, 22) (untested for passability).
  - Col 17: Open lawn directly north of hedge gap.
  - Cols 18..20: Tall grass leading to southern staircase at (20, 21).
- Plateau Bridge System:
  - South Stairs at (20, 21): Ascends to elevated plateau top at (20, 20).
  - Walkable Ridge (cols 21-22 rows 15-18): Connects southern plateau to northern plateau at (21, 14).
  - Northern Plateau (rows 12-14 cols 18-26): Wide elevated plateau directly south of northern lawn (rows 10-11).
  - East Stairs at (24, 15): Descends south to isolated eastern lawn (cols 24-28 rows 16-19).
  - Eastern Boundary (col 28): (28, 15) is confirmed solid tree collision [Verified Turn 7927].

## Active Navigation Strategy: Reaching Area 2
1. Immediate Move (from 14, 24):
   - Advance east 3 steps to (17, 24), step Up 2 times through (17, 23) hedge gap to (17, 22) clear lawn.
2. Empirical Test at (17, 22):
   - Test Left into (16, 22). If passable, advance west to (12, 22) and ascend western staircase at (12, 21).
3. If (16, 22) is solid:
   - Advance east across row 22 to (20, 22), ascend staircase at (20, 21), and cross ridge to northern plateau at (21, 14).
   - At (21, 14): Systematically test row 12 northward into row 11 (cols 20..26) to access northern lawn and Rest House 2 without descending eastern stairs.
4. Northern Sector Progression:
   - Advance west across northern corridor past pond and (6, 4) signpost to exit into Area 2.

- Turn 7953: Reached (17, 24) at the threshold of the hedge opening. Wild Paras appeared. Remaining steps: ~273. Fleeing via RUN.
- Turn 7957: Tested (16, 22); confirmed solid bush hedge. Row 22 does not connect west to (12, 21). Remaining steps: 271. Ascending staircase at (20, 21) to cross plateau bridge north to (21, 14).
- Turn 7960: Reached (21, 14) on northern plateau via col 21 bridge. Remaining steps: 259. Moving Up 2 times to (21, 12) to test northern descent onto row 11 lawn.
- Turn 7963: Reached (26, 12) on the northeast plateau rim directly south of Rest House 2. Testing Right into corner tile (27, 12) to descend onto the cols 27..28 lawn.