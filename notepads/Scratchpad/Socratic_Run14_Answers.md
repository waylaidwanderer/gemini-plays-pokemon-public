# Socratic Question Answers (Run 14 Update — Turn 50194)

### Socratic Question 1:
- **Why the Left steps failed**: On Turn 50189, we attempted to walk Left 3 steps along Row 15 to (34, 15), but Column 36 on Rows 15-20 is occupied by a solid vertical tree wall (TYPE_2889). Because of this wall, our Left inputs resulted in collisions (bumps) against the trees at (36, 15), and only our final 'Down' input successfully moved us to (37, 16).
- **Plan to bypass and descend to northern ground level**:
  - Since Column 36 is open on Rows 12-14 (verified on the screen where (36, 14) is open TYPE_2770), we can walk Up to Row 14, walk Left across Column 36, and then walk Down the stairs at (34, 15).
  - Exact Coordinate Path: `(37, 16)` -> Up -> `(37, 15)` -> Up -> `(37, 14)` -> Left -> `(36, 14)` -> Left -> `(35, 14)` -> Left -> `(34, 14)` -> Down -> `(34, 15)` [stairs] -> Down -> `(34, 16)` [ground].
  - Button Sequence: `Up, Up, Left, Left, Left, Down, Down` (7 overworld steps total). This entire bypass path is on the grass-free plateau or stairs, meaning 0% chance of wild encounters.

### Socratic Question 2:
- **Tracking Drift Explanation**: 
  - The 32-step and 20-step tracking drifts occurred because we didn't account for collisions (which do not consume RAM steps but might affect our turn-by-turn math if we blindly subtract button counts), and we missed updating our remaining step counters after several movements (such as the 11 Up inputs on Turn 50184 where we collided 9 times).
  - **Turn-by-Turn Discipline**: We will physically verify our position and the actual remaining step budget shown in system data *every single turn* before writing to our notepads. We will subtract only the *actual overworld steps successfully taken* from our budget, rather than subtracting raw button press counts, and keep our notes perfectly in sync.

### Socratic Question 3:
- **Path to Western Plateau Stairs at (22, 23)**:
  - Once we descend the stairs to (34, 16) on the ground level, we must reach the stairs at (22, 23) to climb the Western Plateau.
  - Coordinate Path: `(34, 16)` -> Walk Down 15 steps to Row 31: `(34, 16) -> (34, 31)`.
  - From `(34, 31)`, walk Left 12 steps to Column 22: `(34, 31) -> (22, 31)`.
  - From `(22, 31)`, walk Up 7 steps to Row 24: `(22, 31) -> (22, 24)`.
  - From `(22, 24)`, walk Up 2 steps to climb the stairs: `(22, 24) -> (22, 23) [stairs] -> (22, 22) [plateau]`.
  - **Total Steps**: 15 Down + 12 Left + 9 Up = 36 overworld steps.
  - **Why we must climb back onto Western Plateau**: The central ground-level corridor on Row 19 is completely blocked at Column 16 by a vertical tree wall (TYPE_2889), and the ground-level pathway also has a solid cliff blockage at (18, 11). Thus, there is no flat, ground-level passage to Safari Zone West. The elevated Western Plateau is the only passable physical connection to Safari Zone West.

### Socratic Question 4:
- **West Plateau Row 6 Descent Candidates**:
  - In Safari Zone West (Map 0_219), we proved that Columns 11-16 on Row 6 are blocked to the North by solid cliff walls, and Column 17 is also blocked.
  - The plateau continues horizontally to the East (up to Column 23) and to the West (Columns 6-10).
  - Therefore, the exact remaining coordinate candidates on Row 6 that we must systematically test to find the unblocked northern descent are:
    - **Eastern candidates**: Column 18, Column 19, Column 20, Column 21, Column 22.
    - **Western candidates**: Column 6, Column 7, Column 8, Column 9, Column 10.
  - We will systematically test these candidates by standing on Row 6 and attempting to walk Up (North) into Row 5 until we successfully descend onto the ground level.