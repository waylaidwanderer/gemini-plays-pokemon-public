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

## Active Navigation Strategy: Exploring Western Plateau Corridor
1. From (20, 20), advance west along open plateau corridor across rows 18-20 (cols 19..16 and beyond).
2. Follow western plateau towards western sector and northern corridor to access Area 2.
3. Maintain linear progression without looping back to south stairs.

- Turn 7953: Reached (17, 24) at the threshold of the hedge opening. Wild Paras appeared. Remaining steps: ~273. Fleeing via RUN.
- Turn 7957: Tested (16, 22); confirmed solid bush hedge. Row 22 does not connect west to (12, 21). Remaining steps: 271. Ascending staircase at (20, 21) to cross plateau bridge north to (21, 14).
- Turn 7960: Reached (21, 14) on northern plateau via col 21 bridge. Remaining steps: 259. Moving Up 2 times to (21, 12) to test northern descent onto row 11 lawn.
- Turn 7963: Reached (26, 12) on the northeast plateau rim directly south of Rest House 2. Testing Right into corner tile (27, 12) to descend onto the cols 27..28 lawn.
## Critical Breakthrough (Turn 7976)
- Eastern Plateau Confirmed Impassable North & East:
  - (27, 12) tested Turn 7971; 0 tiles moved (solid cliff corner).
  - Row 12 cliff face blocks north passage to row 11.
  - Staircase at (24, 15) only leads south to the dead-end eastern lawn (cols 24-28).
  - CONCLUSION: Eastern plateau bridge (20, 21 -> 24, 15) does NOT lead to Area 2!
- The True Route to Area 2:
  - Signpost at (5, 23): "CENTER AREA / NORTH: AREA 2".
  - Western Staircase at (12, 21) is accessed from the west sector (row 24 cols 0..13).
  - On Turns 7631-7647: Ascended (12, 21), crossed western plateau, descended to middle sector, crossed northern elevated area, and reached northern lawn at (21, 10) / Rest House 2 at (25, 9) / corridor to Area 2 at (6, 4)!
  - Hedge at (16, 22) separates east and west lawn.
- Execution Plan:
  1. Retrace steps from (26, 12) west to (21, 14) and south across ridge to (20, 21).
  2. Descend staircase at (20, 21) to (20, 22), return west through gap (17, 23) to row 24.
  3. Advance west along row 24 to access the western staircase at (12, 21).
  4. Ascend (12, 21) and follow the western plateau system north into Area 2.
- Step Budget: ~250 steps remaining (plenty for Area 1 -> Area 2 -> Area 3 -> HM03).