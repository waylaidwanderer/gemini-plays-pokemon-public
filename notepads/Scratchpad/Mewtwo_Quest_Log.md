# Post-Game Mewtwo Quest Log & Active Routing
- Current Status: Surfing at (9, 6) on Map 0_228 (1F) on Turn 138178 facing Left.

## 1F Water Canal Column 7 and Column 13 Passability Test Log
- **Objective**: Empirically verify water passability at Column 13 Rows 4/5 and Column 7 Rows 6/7 on Map 0_228 (1F) on water.
- **Experimental Results**:
  - **Tile (13, 5)**: Impassable (Bumped on Turn 137432; verified solid rock of TYPE_2889).
  - **Tile (13, 4)**: Impassable (Bumped on Turn 137436; verified solid rock of TYPE_2889).
  - **Tile (7, 7)**: Impassable (Bumped on Turn 137525; verified solid rock of TYPE_2889).
  - **Tile (7, 6)**: Impassable (Bumped on Turn 137530; verified solid rock of TYPE_2889).
- **Status**: Completed and fully disproven on Turn 137530. The water canals are 100% split at Column 13 and Column 7. There is no horizontal water shortcut on 1F. We must use the verified multi-map backtracking route to reach B1F.

## Verified Master Route to Mewtwo (B1F)
- **Concept**: Since 2F West (3, 11) is completely isolated on foot from (1, 3) due to Row 8 blockages (proven on Turn 137988 via BFS), and 1F Northwest (7, 1) is isolated on foot from (1, 3) due to the (4, 1) blockage, the only unblocked route to Mewtwo requires taking Ladder 5 at (7, 1) on 1F up to (9, 1) on 2F West and navigating the 80-step loop around 2F to reach Northwest Ladder (1, 3).
- **Backtracking Route Steps**:
  1. Descend Southwest Ladder 6 at (3, 11) on 2F West to 1F Southwest at (3, 11).
  2. Walk on foot from (3, 11) to Water Ramp 2 at (11, 13).
  3. Surf from Water Ramp 2 at (11, 13) to Water Ramp 4 at (15, 3).
  4. Walk on foot from (15, 3) to Ladder 5 at (7, 1).
  5. Climb up Ladder 5 to (9, 1) on 2F West.
  6. Navigate the 80-step on-foot loop on 2F to reach Northwest Ladder (1, 3).
  7. Descend Northwest Ladder at (1, 3) to 1F Northwest.
  8. Take the adjacent stairs down to B1F to capture Mewtwo!

## Disproven Theories Archive
- **Direct 1F Horizontal Surfing Route (Disproven Turns 135121-135471)**:
  - Direct water surfing from Water Ramp 2 at (11, 13) to (1, 4) is blocked. Column 7 on Rows 6-7 is blocked by solid rock walls, and Column 6 is blocked across Rows 4-7.
- **Direct Western Canal Surf Boarding (Disproven Turns 135380 and 135400)**:
  - Attempting to Surf facing Left from (1, 14) towards (0, 14) or facing Up from (0, 14) towards (0, 13) failed, proving that Column 0 is blocked on Row 13 and there is no direct Surf-Left boarding option at ground level.

- **Direct Connection Finding (Turn 137593 Socratic Challenge)**:
  - We have been operating under the assumption that 2F West is horizontally split. However, vanilla Cerulean Cave 2F is a perfect grid of 1x1 pillars at even-even coordinates (X and Y both even). Every odd-numbered row and odd-numbered column is fully open.
  - This implies a direct on-foot connection between Southwest Ladder 6 at (3, 11) and Northwest Ladder (1, 3) must exist on 2F West! Specifically, walking up Column 11 or other odd columns should connect the south to the north.
  - We will systematically test the passability of these lanes to find the unblocked route! We start by walking north to Row 9 and then east.
  - Let's establish a dedicated testing scratchpad 'Scratchpad/2F_West_Pillar_Grid_Test' to log our physical testing and findings.
- **2F East (29, 1) Pocket Passability (Disproven Turn 136026)**:
  - **Objective**: Verify if Row 0 at (27, 0) on Map 0_226 is passable on foot.
  - **Experimental Results**: On Turn 136025, starting from (29, 1), we walked Left to (28, 1), Up to (28, 0), and pressed Left against (27, 0). Result: BUMP (visited 0 tiles). This conclusively disproves the passability of (27, 0), proving 2F East (29, 1) is a 100% closed, dead-end pocket on foot.

## Verified 1F Surfing Backtracking Route (3, 11) to (7, 1) Steps:
- **Phase 1: Southwest Ladder (3, 11) on 1F to Water Ramp 2 (11, 13) [Completed]**
  - Path: `['Down', 'Left', 'Left', 'Down', 'Down', 'Down', 'Down', 'Right', 'Down', 'Right', 'Right', 'Right', 'Right', 'Right', 'Right', 'Right', 'Right', 'Right', 'Right', 'Right', 'Right', 'Right', 'Up', 'Right', 'Right', 'Up', 'Up', 'Left', 'Left', 'Up', 'Up', 'Left', 'Left', 'Left', 'Left', 'Down']`
  - Ended at: (11, 13) on foot facing Down.

- **Phase 2: Surf from Water Ramp 2 (11, 13) to Water Ramp 4 (15, 3) [Active]**
  - Action: Select GEMMY (BLASTOISE) and use SURF.
  - Path on Water: `['Down', 'Left', 'Left', 'Up', 'Up', 'Up', 'Up', 'Up', 'Up', 'Up', 'Up', 'Right', 'Right', 'Right', 'Right', 'Right', 'Up', 'Up', 'Right', 'Up']`
  - Dismounts onto foot at (15, 3) automatically when moving into (15, 3).

- **Phase 3: Walk from Water Ramp 4 (15, 3) to Ladder 5 (7, 1) Northwest**
  - Path on Foot: `['Up', 'Up', 'Left', 'Left', 'Left', 'Left', 'Left', 'Left', 'Left', 'Left']`
  - Arrives at: (7, 1) (Ladder 5), which leads up to 2F West at (9, 1).

## 1F Water Canal Row 4 and 5 Systematic Re-Testing Protocol (Turn 138130)
- **Objective**: Re-test the water canal crossover at Rows 4 and 5 on Map 0_228 (specifically around Columns 12 and 13) on Surf to find the unblocked water path to the northwest quadrant, as the current deadlock implies a logical mapping impossibility.
- **Protocol & Results**:
  1. Descend Ladder 5 at (9, 1) on 2F West to arrive at 1F Northwest at (7, 1). [Completed on Turn 138137]
  2. Walk on foot to Water Ramp 4 at (15, 3). [Completed on Turn 138146]
  3. Use SURF to enter the water. [Completed on Turn 138149]
  4. Surf to (14, 4) and attempt to move Left onto (13, 4).
     - *Result (Turn 138153)*: BUMP! Labeled as (13, 4) TYPE_2889. Conclusively proves (13, 4) is solid rock and impassable on water.
  5. Surf to (14, 5) and attempt to move Left onto (13, 5).
     - *Result (Turn 138159)*: BUMP! Labeled as (13, 5) TYPE_2889. Conclusively proves (13, 5) is solid rock and impassable on water.
  6. Surf to (14, 6) or other Rows to find any other potential horizontal crossovers.