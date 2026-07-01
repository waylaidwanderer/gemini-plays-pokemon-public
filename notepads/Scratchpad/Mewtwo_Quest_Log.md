# Post-Game Mewtwo Quest Log & Active Routing
- Current Status: On foot at (5, 2) on Map 0_228 (1F) on Turn 138461 facing Left. Completed physical passability test of Column 4 at (4, 2). Heading to Ladder 5 at (7, 1) Northwest.

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

## 1F Northwest Column 4 Passability Testing Plan
- **Objective**: Empirically verify on foot whether Column 4 on 1F Northwest is actually open and passable, or if it is blocked as our historical database claims.
- **Hypothesis**: The "Column 4 blockage" on 1F Northwest is actually map-level data pollution from 2F West's rock pillars. Column 4 on 1F is completely open, meaning 1F Northwest is fully connected on foot to the B1F descent at (1, 3).
- **Experimental Protocol**:
  1. We are currently standing at (11, 2) on foot on Map 0_228.
  2. We will walk Left along Row 2 towards Column 4.
  3. We will record the exact Turn, coordinates, and visual/physical results of each movement step.
  4. If we successfully cross Column 4 and reach (3, 2), we will have conclusively proven Column 4 is open and unblocked!
- **Testing Log**:
  - Turn 138454: Prepared to begin the physical passability test of Column 4 from (11, 2).
  - Turn 138457: Stood at (11, 2) on foot. Pressed Left 4 times. Arrived at (7, 2) on Turn 138458.
  - Turn 138459: Stood at (7, 2) on foot. Pressed Left 3 times to move to (5, 2) and physically test (4, 2) on foot.
  - Turn 138461: Arrived at (5, 2) facing Left. The movement was aborted at step 3 because of a physical collision. Visited exactly 2 tiles (7,2 -> 6,2 -> 5,2) and bumped on the 3rd step.
  - **Conclusive Proof**: Column 4 at Row 2 (4, 2) is 100% solid, impassable rock wall of TYPE_2889. This confirms that 1F Northwest is indeed completely separated from the eastern landmass on foot at ground level. There is no map-level data pollution; the Column 4 blockage is real on 1F. We must ascend Ladder 5 at (7, 1) Northwest to find our way to Mewtwo via 2F West.

## 2F West Pillar Grid Grid-Coordinate Analysis
- **Core Principle**: Vanilla Cerulean Cave 2F is designed as a grid of 1x1 rock pillars placed at even-even coordinates (where both X and Y are even, such as (2, 2), (4, 4), (12, 6), etc.). Every odd-numbered row and odd-numbered column consists of completely open, unblocked walkable space.
- **Unblocked Path to Mewtwo B1F stairs**:
  1. We will dismount at Water Ramp 4 at (15, 3) and walk to Ladder 5 at (7, 1) Northwest on 1F, which warps us to (9, 1) on 2F West.
  2. From (9, 1) on 2F West, we can walk Left to (3, 1) along Row 1 (odd row):
     - Path: (9, 1) -> (8, 1) -> (7, 1) -> (6, 1) -> (5, 1) -> (4, 1) -> (3, 1).
     - Since Row 1 is an odd row, there are no pillars on it.
  3. From (3, 1), we can walk Down along Column 3 (odd column) to reach Row 3:
     - Path: (3, 1) -> (3, 2) -> (3, 3).
     - Since Column 3 is an odd column, there are no pillars on it.
  4. From (3, 3), we can walk Left along Row 3 (odd row) to reach the Northwest Ladder at (1, 3):
     - Path: (3, 3) -> (2, 3) -> (1, 3).
     - Since Row 3 is an odd row, there are no pillars on it, and (1, 3) connects directly to B1F Mewtwo!
- **Verification Log**: We will log each step on 2F West to prove this grid layout and unlock Mewtwo's room!