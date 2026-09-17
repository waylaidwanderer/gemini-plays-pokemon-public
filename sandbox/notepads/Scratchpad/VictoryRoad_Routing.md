# Victory Road Master Routing & Active Testing

## Current Verified State [Turn 23978]:
- Player is inside Victory Road 1F at (15, 12) on foot with Strength actively enabled.
- Boulder 1 has been successfully maneuvered onto (17, 12) directly North of Switch Plate 1 at (17, 13).
- Next immediate step: Walk Up to (15, 11), Right twice to (17, 11), and push South to depress Switch Plate 1 at (17, 13) and lower Plateau Barrier Block at (9, 12).

## Execution Blueprint & Active Hypotheses:
1. Ride West via Route 22 past Reception Gate to Route 23, surf North to Victory Road 1F.
2. Victory Road 1F:
   - Cast Strength with Rocky (Geodude).
   - Push entrance boulder onto switch (17, 13).
   - Walk across plateau to ladder (1, 1) and ascend to 2F.
3. Victory Road 2F (Transit):
   - Walk north via Western Highway (cols 2-3) through doorway (5, 4) to Northwest ladder (1, 1).
   - Ascend ladder (1, 1) to 3F (2, 0).
4. Victory Road 3F:
   - Walk to (6, 1), east along Northern Highway (Row 1) to Column 20, south to Row 6 (17, 6).
   - Ascend wooden staircase (17, 5) to terrace (17, 4).
   - Walk west across terrace to Col 10, south to Row 10, west to (5, 10), north to Row 8, west to (1, 8).
   - Descend wooden staircase (1, 9) into Southwest Basin at (1, 10).
   - Walk south to Row 16, east along Row 16 Highway to (21, 16), and up to (21, 15).
   - Cast Strength with Rocky.
   - Push Boulder (22, 15) East into Pit Hole (23, 15).
   - Step East into Pit Hole (23, 15) to fall to 2F!
5. Victory Road 2F (Final Clear - Verified Routing & Mechanics):
   - Land at (22, 16) with fallen boulder at (23, 16).
   - Cast Strength with Rocky.
   - Note on boulder geometry: Player lands at (22, 16) west of boulder (23, 16).
     To push boulder WEST toward Switch Plate B at (9, 16), player must position EAST of the boulder.
     Test bypass: test whether Row 17 (south of boulder at 22..24, 17) or Row 15 allows walking east to (24, 16).
     If Row 16 is single-tile and non-bypassable locally, verify if there is an alternate path or if pushing boulder initiates from a specific orientation.
   - Once positioned at (24, 16), push fallen boulder WEST along Row 16 onto Switch Plate B at (9, 16).
   - Switch Plate B depresses, lowering the barrier at (23, 14).
   - Ascend wooden stairs (21, 15) to Row 14, walk east past lowered barrier (23, 14), and climb Exit Ladder (25, 14) to INDIGO PLATEAU!
