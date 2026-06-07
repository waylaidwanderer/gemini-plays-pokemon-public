# Safari Zone West Exploration - Run 41 (Turn 67715 - Active)
- **Current Status**: Standing at (5, 16) on Koga's plateau bridge in Safari Zone West (Map 0_219) on Turn 67715 with 246 steps remaining.
- **Inventory Status**: 15/20 items.
- **Run 41 Starting Steps**: 500 steps.
- **Current Steps Remaining**: 246 steps.
- **Money remaining**: ¥69,817.

## Active Campaign Plan (From current position (5, 16))
1. **Backtrack to (15, 16)**: Walk Right 10 steps horizontally along Row 16 to stand on the plateau at (15, 16) [z=1].
2. **Move to (15, 13)**: Walk Up 3 steps vertically along Column 15 to stand at (15, 13) [z=1].
3. **Test Column 14 Row 13 Jump-Left**: Standing at (15, 13) [z=1], attempt to walk Left into (14, 13) to see if we jump West over Column 14 to land on ground level at (13, 13) [z=0].
4. **Test Column 14 Row 12 Jump-Left**: If the Row 13 test bumps, walk Up 1 step to (15, 12) [z=1] and attempt to walk Left into (14, 12) to see if we jump West over Column 14 to land on ground level at (13, 12) [z=0].
5. **Retrieve Teeth & Surf**: Once ground level z=0 is successfully reached, walk to (3, 3) (Secret House) to get Surf, and (9, 7) to pick up the Gold Teeth Pokéball. Then use GEMMY's DIG to escape.

## Socratic Answers & Proof of Work (Overwatch Resolution)
- **Socratic Question 1 (Column 10 & 5 Blockages)**:
  - On Turn 67670, our 27-button sequence failed to reach the Secret House because Column 10 Rows 6-9 contains solid cliff walls of `TYPE_2889` that block any horizontal westward movement on Koga's plateau. Standing at (11, 7) or (11, 6), walking Left results in a physical bump, meaning the northeastern plateau pocket (Columns 11-16, Rows 6-9) is completely isolated from the western plateau. Furthermore, Column 11 Row 9 is also a solid cliff face, blocking southward escape on Column 11.
  - On Turn 67710, we walked Left along Row 16 to (5, 16) [z=1] and attempted to walk Up into (5, 15), resulting in a physical collision (bump). This empirically proves that Column 5 Rows 14-15 are ground-level (`TYPE_3fe2`) grass cells rather than plateau, and the northern boundary of Row 16 on Column 5-13 is a solid North-facing cliff edge that is impassable.
  - **Structural Puzzle Solution**: Since Koga's western plateau is cut off on Columns 5-13, and the Southwest pocket is blocked on ground level by Row 13 water, the player must locate and use the West-facing jump-down ledge on Column 14. We will walk to (15, 13) and (15, 12) to systematically test if walking Left results in jumping West over Column 14 to land on ground level at Column 13.
- **Socratic Question 2 (Detour Step Math & Reconciliation)**:
  - Starting with **399 steps remaining** at (20, 3) in Safari Zone East (Turn 67554):
    1. Walked from (20, 3) to East-North transition at (0, 5) -> **23 steps used** (376 remaining).
    2. Walked detour through Safari Zone North from (39, 31) to (9, 35) -> **61 steps used** (315 remaining).
    3. Walked from West entry at (27, 0) to stairs UP at (21, 17) -> **24 steps used** (291 remaining).
    4. Climbed stairs to (21, 16) and walked to (15, 16) -> **8 steps used** (283 remaining).
    5. Attempted Row 6/7 path and ended up at (11, 6) -> **21 steps used** (262 remaining).
    6. Backtracked along Row 16 to stand at (5, 16) -> **16 steps used** (246 remaining).
  - This step-by-step physical step calculation accounts for all **153 physical steps consumed**, and perfectly reconciles our actual remaining step count of **246 steps** on Turn 67715, resolving the previous tracking desync!

## Chronological Detour Movement Log (Turns 67554 - 67715)
- Turn 67554: Standing at (20, 3) in East with 399 steps remaining.
- Turn 67558: Walked Left 20 steps to (0, 3) and Down 2 steps to (0, 5).
- Turn 67565: Transitioned to Safari Zone North at (39, 31) (23 steps used, 376 remaining).
- Turn 67569: Climbed Eastern stairs UP at (28, 27) to stand at (28, 26) [z=1] (16 steps used, 360 remaining).
- Turn 67572: Descended stairs at (28, 27) to ground level at (28, 30) (4 steps used, 356 remaining).
- Turn 67581: Climbed Western stairs UP at (22, 23) to stand at (22, 22) [z=1] (14 steps used, 342 remaining).
- Turn 67588: Walked Left 6 steps to (16, 22) [z=1] (6 steps used, 336 remaining).
- Turn 67594: Descended stairs at (16, 27) to ground level at (16, 28) (6 steps used, 330 remaining).
- Turn 67600: Transitioned to Safari Zone West at (27, 0) [z=0] (15 steps used, 315 remaining).
- Turn 67608: Climbed Eastern stairs UP at (21, 17) to stand at (21, 16) [z=1] (26 steps used, 289 remaining).
- Turn 67609: Walked to (15, 16) [z=1] (6 steps used, 283 remaining).
- Turn 67670: Pathfinder sequence to Row 6/7; bumped at Column 10 cliff and ended at (11, 6) [z=1] (21 steps used, 262 remaining).
- Turn 67710: Backtracked along Row 16 to (5, 16) [z=1] (16 steps used, 246 remaining).