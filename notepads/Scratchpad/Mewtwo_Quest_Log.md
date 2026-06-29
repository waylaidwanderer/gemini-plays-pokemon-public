# Post-Game Mewtwo Quest Log & Active Routing
- Quest Started: Turn 111394
- Current Status: On foot at (11, 13) on Map 0_228 (1F) on Turn 135820.

## Active Routing Strategy
- **Horizontal Surfing Route (ACTIVE TEST)**: We are currently testing if the central water canal (Columns 8-11) is connected to the western water canal (Columns 1-2) via Rows 4 and/or 5. Specifically, we are testing if (8, 5) or (9, 5) on Row 5 can be surfed onto from the south, or if they are solid blocks. If Row 4 or Row 5 is open, we can surf directly to (1, 4) on the west side and dismount at the B1F stairs at (1, 3)!
- **Backup Ground Floor Backtracking Route**: If the horizontal surfing route is 100% blocked, we will fall back to:
  1. Surf back to (11, 13) (Water Ramp 2).
  2. Dismount Surf onto (11, 13) on foot.
  3. Walk to (17, 15) and descend the stairs to the ground floor at (17, 16).
  4. Walk along the unblocked southern ground floor corridor of Row 17 to (1, 14).
  5. Walk Up to (1, 13) and ascend the wooden staircase to the southwest plateau at (1, 12).
  6. From (1, 12), walk to the Southwest Ladder at (3, 11) and ascend to 2F West.
  7. On 2F West, navigate to Northwest Ladder at (1, 3) via the unblocked 12-step path: Up, Up, Right, Up, Up, Up, Up, Up, Up, Left, Left, Left.
  8. Descend Northwest Ladder at (1, 3) to land on 1F Northwest.
  9. Walk on foot along the northern boundary Row 0 to (1, 3) (B1F stairs) and descend to Mewtwo!

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
## 1F (0_228) Column 8 and Column 9 Row 5 Passability Experiment (Turn 135835)
- **Objective**: Empirically verify if (8, 5) or (9, 5) on Map 0_228 (1F) can be surfed onto from the south, which would allow direct water connection between the central canal and Row 4/5 water leading to the western canal.
- **Hypothesis**: Either (8, 5) or (9, 5) is open water, contrary to our static BFS collision database.
- **Experimental Protocol**:
  1. Surf to (8, 6) in the central canal.
  2. Face Up and press Up to attempt to surf onto (8, 5). Record result.
  3. Surf to (9, 6) in the central canal.
  4. Face Up and press Up to attempt to surf onto (9, 5). Record result.
- **Experimental Results**:
  - **Turn 135832**: Standing at (8, 6) on water, faced Up and pressed Up. Result: BUMP (visited 0 tiles). Conclusively proves (8, 5) is a solid rock wall of TYPE_2889 and is impassable on water.
  - **Turn 135835**: Standing at (9, 6) on water, faced Up and pressed Up. Result: BUMP (visited 0 tiles). Conclusively proves (9, 5) is a solid rock wall of TYPE_2889 and is impassable on water.
- **Experimental Conclusion**: Both (8, 5) and (9, 5) are completely solid rock walls of TYPE_2889. Since Column 10 and 11 on Row 5 are also solid land/rock blockages, there is absolutely no vertical way to cross Row 5 in the central canal on water. Thus, we cannot reach Row 4 on water from the central canal. This definitively disproves the 1F horizontal water canal shortcut hypothesis. The eastern/central canals are 100% separated from the western canal on all water rows on 1F, making the multi-map backtracking route the ONLY topologically connected path to Mewtwo.