# Safari Zone Master Routing & Step Ledger (Session 8 / Session 9)

## Session 8 Reconnaissance Summary
- Session 8 Traversal: 500 steps consumed [Concluded Turn 9710 with PA chime].
- Current Turn: 9715
- Current Position: (4, 0) in Safari Zone Gatehouse.
- Session 8 Expiration: Completed. Dismissing dialogue to purchase Session 9 admission.

## Ground Truth & Area 3 Connectivity (Verified Turns 9533–9691)
- Area 3 Entrance: (26, 0) from Area 2.
- East Corridor (cols 25..28 rows 0..23):
  - Row 0..1 northern boundary is blocked by 2x2 trees across cols 22..25 and 28..29.
  - Column 24 is a continuous solid bush hedge from row 2 through row 13.
  - Western access from East Corridor exists via:
    1. Row 18: South Plateau Eastern Staircase at (21, 17) [Ascends to elevated bridge].
    2. Row 23: Ground lawn corridor across cols 19..26 [Connects west to central lawn and cols 10..15 bypass].
  - Row 14 connects west into Gold Teeth Cove (cols 18..23 rows 6..13, enclosed cul-de-sac; Gold Teeth collected Turn 8235).
  - East boundary at (29, 22..23) warps to Center Area at (0, 11).
- Southern Plateau Bridge:
  - Spans cols 6..21 across rows 16..18.
  - Eastern Staircase at (21, 17); Western Staircase at (6, 19).
  - Descends at (6, 19) to ground level tall grass at (6, 20).
- Western Sector & Rest House 4:
  - From (6, 20), row 20 connects west to Western Corridor (cols 1..2).
  - Column 1 is clean lawn from row 16 to row 23.
  - Water pond occupies cols 3..9 rows 10..13.
  - Rest House 4 is at cols 10..13 rows 10..11.
  - Rest House 4 basin is an enclosed cul-de-sac: blocked east by cliff at col 14, and west by water shoreline at (9, 11..13) (Turn 9626: tile 9, 12 is water collision).
- Unvisited Candidate Target Sectors:
  1. Southwest Sector: Rows 24..28 across cols 2..15 (unvisited; cols 0..6 rows 25..27 viewed from 1, 23 showed open lawn).
  2. Northwest Sector: Rows 0..9 across cols 0..9 (unvisited; item ball at 9, 7 sighted from Northern Plateau).

## Session 9 Direct Traversal Strategy & Step Budget Ledger
- Initial Budget: 500 steps (¥500 admission).
- Stage 1: Gatehouse to Area 1 (Center Area traversal): ~90 steps.
- Stage 2: Area 1 traversal (via South Plateau, Pond Bypass, North Bridge, and Row 3 Canopy Corridor to Area 2 gate): ~110 steps.
- Stage 3: Area 2 traversal (via Eastern Plateau descent, Central Lawn, Western Plateau Bridge to Area 3 gate): ~100 steps.
- Stage 4: Arrive in Area 3 at (26, 0) with ~200 steps remaining.

## Area 3 Search Hierarchy & Hard Step Allocation
- Target Sector 1 (Primary): Northwest Sector (cols 0..9 rows 0..9).
  - Allocation: 140 steps maximum.
  - Route: From (26, 0), descend East Corridor to (21, 18), cross Southern Plateau Bridge west to (6, 19), descend stairs to (6, 20), walk west to col 1 corridor (1, 20), head north along col 1 past the pond (rows 14..15) directly into the Northwest Sector (cols 0..6 rows 0..9).
  - Landmark: The Secret House (source of HM03 Surf) and item ball at (9, 7).
- Target Sector 2 (Secondary / Fallback): Southwest Sector (cols 0..15 rows 24..28).
  - Allocation: Remaining ~60 steps if Northwest Sector is confirmed fully exhausted/blocked.
  - Pivot Trigger: If Northwest corridor is completely blocked by physical barriers before row 5, immediately reverse south along col 1 to explore rows 24..28.
