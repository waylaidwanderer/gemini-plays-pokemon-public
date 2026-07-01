# Post-Game Mewtwo Quest Log & Active Routing
- Current Status: Standing on foot at (16, 1) on Map 0_226 (2F West) on Turn 138561 facing Left. Ready to flee from Dodrio and continue backtracking to Ladder 5.

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
  - We hypothesized that Southwest Ladder 6 at (3, 11) is connected on foot to (1, 3) on 2F West via an odd-coordinate grid corridor. However, our connected components analysis on Turn 138494 proved that Southwest Ladder 6 is in an isolated Component 1 of size 18, and Column 2 has solid rock walls at (2, 9), (2, 12), and (1, 10), (1, 11) are also solid. This completely isolates (3, 11) from (1, 3) on foot, disproving the direct 2F West southwest shortcut.
- **2F East (29, 1) Pocket Passability (Disproven Turn 136026)**:
  - **Objective**: Verify if Row 0 at (27, 0) on Map 0_226 is passable on foot.
  - **Experimental Results**: On Turn 136025, starting from (29, 1), we walked Left to (28, 1), Up to (28, 0), and pressed Left against (27, 0). Result: BUMP (visited 0 tiles). This conclusively disproves the passability of (27, 0), proving 2F East (29, 1) is a 100% closed, dead-end pocket on foot.
- **1F Northwest Column 4 Passability (Disproven Turn 138461)**:
  - Standing on foot at (5, 2) on 1F Northwest and pressing Left against (4, 2) resulted in a direct collision BUMP on Turn 138461. This conclusively disproves the horizontal land crossover on Row 2 of 1F Northwest, proving that 1F Northwest is completely isolated on foot from the eastern landmass.

## 2F West Maze Detour Analysis
- **Discovered Constraint**: Koga's 2F West has solid rock walls on Column 2 on Rows 1-3 (specifically, (2, 1), (2, 2), and (2, 3) are solid rock walls of TYPE_2889). Row 4 is also completely solid from Column 1 to Column 8. This isolates the Northwest Ladder (1, 3) from the immediate northern corridor (Row 1).
- **The True Detour Route**:
  To reach the Northwest Ladder (1, 3) from Ladder 5 at (9, 1), we must execute a complete 82-step detour around the entire 2F West floor:
  1. Walk Left along Row 1 to (3, 1).
  2. Walk Down Column 3 to (3, 3).
  3. Walk Right along Row 3 to (9, 3).
  4. Walk Down Column 9 to (9, 5) to bypass the Column 10-12 mountain block.
  5. Walk Right along Row 5 to (13, 5).
  6. Walk Up Column 13 to (13, 1) to reach Row 1 again.
  7. Walk Right along Row 1 to (18, 1).
  8. Walk Down Column 18 to (18, 3).
  9. Walk Right along Row 3 to (20, 3).
  10. Walk Up Column 20 to (20, 2) to reach Row 2.
  11. Walk Right along Row 2 to (24, 2).
  12. Walk Down Column 24 to (24, 5).
  13. Walk Right to (25, 5) to bypass the eastern blockages.
  14. Walk Down Column 25 to Row 14 at (25, 14).
  15. Walk Left along Row 14 all the way to (2, 14).
  16. Walk Up Column 2 to (2, 13) and Left to (1, 13).
  17. Walk Up Column 1 to (1, 3) [Northwest Ladder] to access B1F!

- **Verification Log**:
  - Turn 138482: Walked Left 1 step to (8, 1) and encountered a wild Chansey (fled).
  - Turn 138485: Walked Left 3 steps to (5, 1) and encountered a wild Dodrio (fled).
  - Turn 138501: Walked Right 3 steps to (6, 3) and encountered a wild Rhydon (fled).
  - Turn 138509: Walked from (13, 1) to (18, 3) on foot successfully.
  - Turn 138511: Walked from (18, 3) to (23, 2) on foot successfully (currently standing at (23, 2)).