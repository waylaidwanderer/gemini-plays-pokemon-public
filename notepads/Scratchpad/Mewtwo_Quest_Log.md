# Post-Game Mewtwo Quest Log & Active Routing
- Current Status: Surfing on GEMMY at (9, 11) on Map 0_228 (1F) on Turn 138391. Actively navigating north along the central canal to test Row 5 water passability.

## 1F Water Canal Column 7 and Column 13 Passability Test Log
- **Objective**: Empirically verify water passability at Column 13 Rows 4/5 and Column 7 Rows 6/7 on Map 0_228 (1F) on water.
- **Experimental Results**:
  - **Tile (13, 5)**: Impassable (Bumped on Turn 137432; verified solid rock of TYPE_2889).
  - **Tile (13, 4)**: Impassable (Bumped on Turn 137436; verified solid rock of TYPE_2889).
  - **Tile (7, 7)**: Impassable (Bumped on Turn 137525; verified solid rock of TYPE_2889).
  - **Tile (7, 6)**: Impassable (Bumped on Turn 137530; verified solid rock of TYPE_2889).
- **Status**: Completed and fully disproven on Turn 137530. The water canals are 100% split at Column 13 and Column 7. There is no horizontal water shortcut on 1F. We must use the verified multi-map backtracking route to reach B1F.

## Row 5 Water Passability Testing Plan
- **Objective**: Board water at Water Ramp 2 and surf north along the central canal to physically test if we can cross Row 5 at (8, 5) or (9, 5) on water. If open, this connects the central/eastern canals directly to the western canal on water!
- **Testing Log**:
  - Turn 138373: Prepared to board water at Water Ramp 2 (11, 13).
  - Turn 138395: Stood at (9, 7) surfing. Pressed Up, Up to move to (9, 6) and test (9, 5).
  - Turn 138397: Verified current position is (9, 6) after bumping on the second step. Physical result: BUMP against (9, 5). **Conclusive Proof: (9, 5) is 100% solid rock and impassable on water.**
  - Turn 138404: Stood at (9, 6) surfing. Pressed Left, Up to move to (8, 6) and test (8, 5).
  - Turn 138405: Verified current position is (8, 6) after bumping on the second step. Physical result: BUMP against (8, 5). **Conclusive Proof: (8, 5) is 100% solid rock and impassable on water.**
- **Testing Conclusion**: Both (8, 5) and (9, 5) are 100% solid, impassable rock walls of TYPE_2889. Since Column 10-13 Row 5 and Column 7 Row 6-15 are also solid, there is absolutely no horizontal or vertical water connection between the eastern/central canals and the western canal on 1F. This definitively disproves the 1F water crossover hypothesis, meaning we must use the 2F West odd-coordinate grid corridor to reach the Northwest Ladder (1, 3).

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