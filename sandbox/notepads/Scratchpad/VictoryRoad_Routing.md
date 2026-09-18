# Victory Road Master Routing & Active Testing

## Current Verified State [Turn 24184]:
- Floor reset via ladder (0, 8): Boulder 1 is at (5, 5), Boulder 3 is at (4, 14).
- Switch Plate A at (1, 16) is unpressed; Plateau Barrier at (7, 8)-(7, 9) is currently RAISED.
- Strength is active (cast by Rocky Turn 24160).
- Northwest Chamber entrance at (5, 4): (4, 4) and (6, 4) are rock walls; pushing Boulder 1 north into (5, 3) blocks (5, 4) against rock wall (5, 2). Access to Ladder (1, 1) is via Northern Highway (Rows 0-1) from eastern sector.

## Execution Blueprint & Active Hypotheses:
1. Ride West via Route 22 past Reception Gate to Route 23, surf North to Victory Road 1F.
2. Victory Road 1F:
   - Cast Strength with Rocky (Geodude).
   - Push entrance boulder onto switch (17, 13).
   - Walk across plateau to ladder (1, 1) and ascend to 2F.
3. Victory Road 2F (Transit):
   - Push Boulder 3 onto Switch Plate A at (1, 16) to lower Plateau Barrier at (7, 8)-(7, 9).
   - Return via Row 11 to wooden staircase at (5, 10), ascend to elevated plateau at (5, 9).
   - Walk east across lowered barrier (7, 8)-(7, 9) onto eastern plateau.
   - Walk east and north past Moltres (11, 5) to Column 16 Highway.
   - Ascend Column 16 Highway north to Row 1 Northern Highway.
   - Ascend Northwest ladder at (1, 1) to Victory Road 3F (2, 0).
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
