# Post-Game Mewtwo Quest Log & Active Routing
- Quest Started: Turn 111394
- Current Status: On foot at (15, 3) on Map 0_228 (1F Northwest) on Turn 135752.

## Active Routing Strategy
- **Ground Floor Backtracking Route**: Since direct horizontal surfing on Rows 4 and 5 is blocked by solid rock walls at Column 6 and 13, and the eastern and western canals are 100% separated, we must use the multi-map path to B1F:
  1. From (17, 15) (stairs), step Down to the ground floor at (17, 16).
  2. Walk along the unblocked southern ground floor corridor of Row 17 to (1, 14).
  3. Walk Up to (1, 13) and ascend the wooden staircase to the southwest plateau at (1, 12).
  4. From (1, 12), walk to the Southwest Ladder at (3, 11) and ascend to 2F West.
  5. On 2F West, navigate to Northwest Ladder at (1, 3) (or find the appropriate path). Wait, descending Northwest Ladder on 2F West lands us on 1F Northwest on foot, which allows us to walk to the B1F stairs at (1, 3).

## Disproven Theories Archive
- **Direct 1F Horizontal Surfing Route (Disproven Turns 135121-135471)**:
  - Direct water surfing from Water Ramp 2 at (11, 13) to (1, 4) is blocked. Column 7 on Rows 6-7 is blocked by solid rock walls, and Column 6 is blocked across Rows 4-7.
- **Direct Western Canal Surf Boarding (Disproven Turns 135380 and 135400)**:
  - Attempting to Surf facing Left from (1, 14) towards (0, 14) or facing Up from (0, 14) towards (0, 13) failed, proving that Column 0 is blocked on Row 13 and there is no direct Surf-Left boarding option at ground level.
- **Southwest Platform (z=1) Surfing to (1, 7) (Disproven Turn 135244)**:
  - Attempting to stand at (1, 8) or (2, 8) and Surf north onto (1, 7) is blocked by a height-mismatch collision (z=1 to z=0) in the Gen 1 engine.
- **2F West Direct Path Loop (Disproven)**:
  - 2F West is 100% split on foot due to solid rock walls at Row 8, Row 6/7, Row 2, Row 0 (blocked at (6,0)), and Column 10 (blocked at (10,1)), meaning the southwest pocket and the northern pocket have 0% same-floor connection to the northwest. Backtracking to 1F is mandatory.

## B1F (Basement) Capture Plan
- The stairs down to B1F are located at (1, 3).
- Once on B1F, we will use our specialized custom agent 'mewtwo_combat_strategist' to plan the final battle and execute our guaranteed 100% Master Ball capture on Mewtwo!
## 2F West (0_226) (2, 2) and (2, 3) Doorway / Wall Passability Experiment (Turn 135754)
- **Objective**: Empirically verify if (2, 2) or (2, 3) are open doorways on Map 0_226 (2F West) on foot, which would allow direct, unblocked access from Column 3 to Column 1 and the B1F Northwest ladder at (1, 3).
- **Hypothesis**: Either (2, 2) or (2, 3) is a passable tile (contrary to our hardcoded BFS assumptions).
- **Experimental Protocol**:
  1. From our current position (9, 1), walk Left to (3, 1).
  2. Walk Down to (3, 2).
  3. Face Left and attempt to step Left onto (2, 2). Record result.
  4. Walk Down to (3, 3).
  5. Face Left and attempt to step Left onto (2, 3). Record result.
- **Experimental Results**:
  - **Turn 135759**: Standing on foot at (3, 2) facing Left, pressed Left. Result: BUMP (visited 0 tiles). Conclusively proves (2, 2) is a solid rock wall of TYPE_2889 and is impassable on foot.
  - **Turn 135764**: Standing on foot at (3, 3) facing Left, pressed Left. Result: BUMP (visited 0 tiles). Conclusively proves (2, 3) is a solid rock wall of TYPE_2889 and is impassable on foot.
- **Experimental Conclusion**: Both (2, 2) and (2, 3) are completely solid rock walls. This physically disproves the hypothesis that a passable doorway exists across Column 2 on Rows 1-3. Column 2 is 100% solid on Rows 1-3, confirming that the northern area of 2F West is indeed completely isolated on foot from the Northwest Ladder. The multi-map backtrack route is the ONLY valid path to reach Mewtwo.