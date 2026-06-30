# Post-Game Mewtwo Quest Log & Active Routing
- Quest Started: Turn 111394
- Current Status: Standing at (11, 13) on Map 0_228 (1F) on Turn 136917 facing Down.

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

## Active Socratic Test: 2F West (2, 10) Passability Audit
- **Objective**: Empirically verify the passability of (1, 10) and (2, 9) on Map 0_226 (2F West) on foot.
- **Hypothesis**: Either (1, 10) or (2, 9) on 2F West is NOT a solid blockage. Since 1F has no water access in this southwest pocket, and 2F West has been reported as vertically split on foot, one of our recorded 'verified blockages' must be a false positive. Testing both coordinates on foot will satisfy the Burden of Proof and reveal the true, connected path to the Northwest Ladder (1, 3).
- **Results**:
  - Tested (2, 9) on Turn 136869: Pressed UP from (2, 10) facing UP. Result: BUMP, confirming (2, 9) is a solid rock wall of TYPE_2889 and is impassable on foot.
  - Tested (1, 10) on Turn 136871: Pressed LEFT from (2, 10) facing LEFT. Result: BUMP, confirming (1, 10) is a solid rock wall of TYPE_2889 and is impassable on foot.
- **Conclusion**: Both blockages at (2, 9) and (1, 10) on 2F West are 100% solid and impassable on foot. This proves that Koga's southwest pocket is indeed a closed, isolated pocket on foot, and no direct walkthrough path exists to (1, 3) from the southwest. We must explore the eastern side of 2F West to find the connection.

## Verified Master Route to Mewtwo (B1F)
- **Concept**: Since 1F Southwest has no water access and 2F West southwest pocket is isolated, we must utilize the center and northern water canals of 1F.
- **Path Steps**:
  1. Walk to Southwest Ladder at (3, 11) on 1F Southwest.
  2. Walk to the wooden stairs at (1, 13) and descend to the ground floor.
  3. Walk across the southern unblocked ground corridor to reach the central platform stairs at (17, 15).
  4. Walk to Water Ramp 2 at (11, 13).
  5. Board the water canal using Surf from (11, 13).
  6. Surf north and dismount onto the northern landmass at Water Ramp 4 at (15, 3).
  7. Walk Left along the northern landmass of 1F Northwest to reach Ladder 5 at (7, 1).
  8. Ascend Ladder 5 to reach 2F West at (9, 1).
  9. Walk Left on 2F West along Row 1 to Column 3 (3, 1) and test Column 2's passability to reach the Northwest Ladder (1, 3) which connects directly to the B1F stairs.