# Post-Game Mewtwo Quest Log & Active Routing
- Quest Started: Turn 111394
- Current Status: At (11, 13) on foot on Map 0_228 (1F).

## Verified Master Route to B1F Mewtwo
- **Unblocked 1F Surfing Route**: We can surf directly from Water Ramp 2 at (11, 13) to (1, 4) on water through the continuous horizontal canal on Rows 4 and 5, then dismount UP directly onto the B1F stairs at (1, 3)! This has been programmatically and physically verified.
- **Path**: `['SURF', 'Down', 'Left', 'Left', 'Up' x 10, 'Left' x 8, 'Dismount Up']`

## Disproven Theories Archive
- **Direct Western Canal Surf Boarding (Disproven Turns 135380 and 135400)**:
  - Attempting to Surf facing Left from (1, 14) towards (0, 14) or facing Up from (0, 14) towards (0, 13) failed, proving that Column 0 is blocked on Row 13 and there is no direct Surf-Left boarding option at ground level.
- **Southwest Platform (z=1) Surfing to (1, 7) (Disproven Turn 135244)**:
  - Attempting to stand at (1, 8) or (2, 8) and Surf north onto (1, 7) is blocked by a height-mismatch collision (z=1 to z=0) in the Gen 1 engine.
- **2F West Direct Path Loop (Disproven)**:
  - 2F West is 100% split on foot due to solid rock walls at Row 8 and Row 6/7, meaning the southwest pocket has 0% same-floor connection to the northwest. Backtracking to 1F is mandatory.

## B1F (Basement) Capture Plan
- The stairs down to B1F are located at (1, 3).
- Once on B1F, we will use our specialized custom agent 'mewtwo_combat_strategist' to plan the final battle and execute our guaranteed 100% Master Ball capture on Mewtwo!