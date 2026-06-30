# Post-Game Mewtwo Quest Log & Active Routing
- Quest Started: Turn 111394
- Current Status: Standing at (3, 11) on Map 0_226 (2F West) on Turn 136801.

## Active Routing Strategy
- **Path to B1F Mewtwo via 1F Southwest SURF boarding**:
  - Active Plan: Descend from 2F West at (9, 1) via the ladder to 1F at (7, 1). From (7, 1), navigate to (15, 3), SURF down the water canal to Water Ramp 2 at (11, 13), walk to the 1F Southwest elevated platform at (3, 11), stand facing Left, and attempt to SURF directly onto the western water canal. This will test the Socratic hypothesis that Gen 1 overworld SURF has no Z-level height-mismatch check. If successful, we can surf up to the Northwest landmass (1, 3) and descend to B1F to catch Mewtwo!
## Disproven Theories Archive
- **Direct 1F Horizontal Surfing Route (Disproven Turns 135121-135471)**:
  - Direct water surfing from Water Ramp 2 at (11, 13) to (1, 4) is blocked. Column 7 on Rows 6-7 is blocked by solid rock walls, and Column 6 is blocked across Rows 4-7.
- **Direct Western Canal Surf Boarding (Disproven Turns 135380 and 135400)**:
  - Attempting to Surf facing Left from (1, 14) towards (0, 14) or facing Up from (0, 14) towards (0, 13) failed, proving that Column 0 is blocked on Row 13 and there is no direct Surf-Left boarding option at ground level.

- **2F West Direct Path Loop (Disproven)**:
  - 2F West is 100% split on foot due to solid rock walls at Row 8, Row 6/7, Row 2, Row 0 (blocked at (6,0)), and Column 10 (blocked at (10,1)), meaning the southwest pocket and the northern pocket have 0% same-floor connection to the northwest. Backtracking to 1F is mandatory.
- **2F East (29, 1) Pocket Passability (Disproven Turn 136026)**:
  - **Objective**: Verify if Row 0 at (27, 0) on Map 0_226 is passable on foot.
  - **Experimental Results**: On Turn 136025, starting from (29, 1), we walked Left to (28, 1), Up to (28, 0), and pressed Left against (27, 0). Result: BUMP (visited 0 tiles). This conclusively disproves the passability of (27, 0), proving 2F East (29, 1) is a 100% closed, dead-end pocket on foot.
- **1F Horizontal Surfing Route (Disproven Turn 135945)**:
  - The central water canal (Columns 8-11) does not connect directly to the western water canal (Columns 1-2) via Rows 4 and/or 5. This is 100% blocked by solid rock walls (8, 5) and (9, 5). Systematically verified via physical BUMPs from (8, 6) and (9, 6) facing Up. Row 4 is blocked at Column 13 by (13, 4) solid rock. Row 5 is blocked at Column 13 by (13, 5) solid rock. Thus, the eastern/central water canals are completely separated from the western water canal on all rows of 1F.

## B1F (Basement) Capture Plan
- The stairs down to B1F are located at (1, 3).
- Once on B1F, we will use our specialized custom agent 'mewtwo_combat_strategist' to plan the final battle and execute our guaranteed 100% Master Ball capture on Mewtwo!

## Corrected Socratic Test: 1F Southwest SURF Boarding Experiment
- **Objective**: Verify if the player can initiate SURF from the 1F Southwest elevated platform (Z=1) directly onto the adjacent western water canal (Z=0).
- **Hypothesis**: The Gen 1 overworld SURF script does not check for height/Z-level mismatches during initiation, allowing the player to board the water canal and bypass the isolated blockages.
- **Protocol**:
  1. Stand at (1, 8) on the 1F Southwest elevated platform facing UP towards the water at (1, 7).
  2. Select SURF from the POKéMON menu.
  3. Record result.
- **Historical Context & Previous Flaw**: On Turn 136783, we attempted to Surf while standing at (1, 8). However, because we had just walked Left from (3, 11) via (2, 11) and (1, 11) to (1, 8), our character was facing Left (towards the solid rock wall at (0, 8)) rather than facing Up (towards the water at (1, 7)). This caused the Surf attempt to fail against the wall, which we mistakenly concluded was due to a Z-level height mismatch. In standard Gen 1, overworld Surf has no Z-level height-mismatch check. We must re-verify this by standing at (1, 8) facing UP and executing Surf.
- **Results**: TBD.