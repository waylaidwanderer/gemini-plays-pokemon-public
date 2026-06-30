# Post-Game Mewtwo Quest Log & Active Routing
- Quest Started: Turn 111394
- Current Status: Standing at (8, 1) on Map 0_226 (2F West) on Turn 137167 facing Left.

## Row 5 Column 8 (8, 5) Passability Test Protocol
- **Start Turn**: 137156
- **Start Position**: (9, 1) on Map 0_226 (2F West) on foot
- **Path to Test Position (9, 5)**: ['Left', 'Left', 'Left', 'Left', 'Left', 'Down', 'Down', 'Right', 'Right', 'Right', 'Right', 'Right', 'Down', 'Down']
- **Test Sequence**: From (9, 5), face Left and press 'Left' to step onto (8, 5).
- **Empirical Results**: [Pending]
- **Turn Executed**: [Pending]
- **Conclusive Result**: [Pending]

## Active Routing Strategy
- Currently executing: Verified Master Route to Mewtwo (B1F).
- Currently on Step 7: Walk Left along the northern landmass of 1F Northwest to reach Ladder 5 at (7, 1).

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
- **Hypothesis**: Either (1, 10) or (2, 9) on 2F West is NOT a solid blockage.
- **Results**: Tested and verified solid. Koga's southwest pocket is indeed a closed, isolated pocket on foot.

## Verified Master Route to Mewtwo (B1F)
- **Concept**: Since 2F West is vertically split, we cannot reach (8, 5) from the southwest ladder at (3, 11). Instead, we must take the multi-map route to land on the northern half of 2F West at (9, 1). From there, we can walk on foot directly to (8, 5) and test its passability.
- **Path Steps**:
  1. Take Southwest Ladder 6 at (3, 11) on 2F West DOWN to 1F Southwest.
  2. Walk down the wooden stairs at (1, 13) to the ground floor.
  3. Walk across the southern ground floor to the central staircase at (17, 15) and ascend to the central platform.
  4. Walk to Water Ramp 2 at (11, 13) and use SURF to board the central water canal.
  5. Surf north up the central canal and dismount onto Water Ramp 4 at (15, 3).
  6. Walk Left on the northern landmass of 1F Northwest to reach Ladder 5 at (7, 1).
  7. Climb Ladder 5 UP to 2F West at (9, 1).
  8. From (9, 1) on 2F West, walk on foot to (8, 5) and physically test if we can walk onto it.
  9. If passable, continue walking Left to Northwest Ladder (1, 3), descend to 1F Northwest, and enter B1F!