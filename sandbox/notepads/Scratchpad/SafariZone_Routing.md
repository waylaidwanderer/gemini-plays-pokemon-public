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
- Step Budget: ~250 steps remaining (plenty for Area 1 -> Area 2 -> Area 3 -> HM03).
## Western Sector & Northern Bridge Verification (Turn 7992)
- Western Boundary:
  - Statues at (0, 7), (1, 6), (0, 6), (1, 3), (0, 3) form solid western barrier.
  - Row 6 is completely impassable from col 0 to col 9 (statues at cols 0-1, bushes at cols 2-9).
  - Ground level row 7 cannot bypass row 6 westward.
- Northern Bridge at (12, 7):
  - Wooden staircase at (12, 7) facing south onto (12, 8).
  - Ascends onto the northern elevated plateau to bridge OVER the row 6 hedge.
  - Connects to northern sector and Area 2 corridor.
- Step Budget: 207 steps remaining. Moving east to (9, 7) -> (12, 8) -> ascend (12, 7).
## Northern Corridor & Area 2 Gate (Turn 8005)
- Signpost at (6, 4): 'TRAINER TIPS / The remaining time declines only while you walk!' [Read Turn 8004].
- Northern Gate to Area 2: Open gateway at cols 0..1 rows 4..5 between statue gateposts at (1, 3) and (1, 6).
- Step Budget: 160 steps remaining. Advancing west along row 5 into Area 2.
## Area 2 (North) Arrival (Turn 8007)
- Map Transition Detected: Entered Safari Zone Area 2 at (39, 31) from Area 1 western gate.
- Gate Topology: Enters facing Left between statues at (39, 28..29) and (39, 32..33).
- Step Budget: 149 steps remaining. Wide open green corridor running west.

## Area 2 Active Routing Framework & Hypotheses
- Current Baseline: (27, 31), 137 steps remaining.
- Landmarks Identified:
  - Eastern Entrance Gate: (39, 30..31) between statues.
  - Southern Corridor: Rows 28..33 across cols 25..39. Clear lawn at cols 28..39, tall grass patch at cols 20..27.
  - Northern Staircase: Located at (28, 27) facing south onto (28, 28). Ascends north onto plateau.
- Area 3 Transition Hypothesis:
  - Generation 1 Safari Zone Area 2 connects west/southwest into Area 3 (West Area).
  - Primary path: Follow southern corridor west along rows 30-31 toward western map border (col 0).
  - Target: Transition into Area 3 with ~110+ steps remaining to claim HM03 Surf (Secret House) and Gold Teeth.
