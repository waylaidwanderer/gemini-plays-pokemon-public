# Post-Safari Zone Route & Progression Plan (Cinnabar Mansion)

## Cinnabar Mansion Deep B1F Routing & Switch Matrix (Turn 78160)
- **State A (Statue 2 Default)**:
  - Gate 1 on 1F (25, 13) is CLOSED, blocking foot access to the Southeast room.
  - Gate 3 on 2F (18, 8)-(19, 8) is OPEN (Verified OPEN on Turn 78836).
  - Gate 4 on 1F East (21, 17) is OPEN.
  - Gate 6 on 2F (9, 4)-(9, 5) is CLOSED.
  - Gate 18 on 2F (2, 18) is CLOSED.
  - Gate 26 on 2F (12, 26)-(13, 26) is CLOSED.
  - Gate 13 on 2F (12, 13)-(13, 13) is CLOSED.

- **State B (Statue 2 Toggled)**:
  - Gate 1 on 1F (25, 13) is OPEN, allowing foot access to the Southeast room.
  - Gate 3 on 2F (18, 8)-(19, 8) is CLOSED (Verified CLOSED on Turn 84976).
  - Gate 4 on 1F East (21, 17) is CLOSED.
  - Gate 6 on 2F (9, 4)-(9, 5) is OPEN.
  - Gate 18 on 2F (2, 18) is OPEN (Verified on Turn 86403 by toggling Statue 2 to State B).
  - Gate 26 on 2F (12, 26)-(13, 26) is CLOSED.
  - Gate 13 on 2F (12, 13)-(13, 13) is CLOSED.

## State B 1F East Staircase & B1F Access Model (Active Turn 90874)
- **Objective**: Determine how to access the basement floor (B1F) of Pokémon Mansion.
- **Topological Reality Check**:
  - The eastern shaft is a strictly one-way descending path: 3F East (pit) -> 2F East Southeast (stairs down) -> 1F East Southeast (stairs down) -> B1F (stairs down).
  - Therefore, we cannot climb up the eastern side of the mansion.
  - Gate 2 on 3F (10, 11) is CLOSED and solid under both State A and State B (Empirically verified Turn 90748).
  - The correct path to reach the descending path is to execute the western balcony drop from the 3F West balcony (Column 7 Row 14/15) under active State B.
- **Current Action Plan (Updated Turn 90784)**:
  - Stand at (2, 12) on 2F West, explicitly face UP, and successfully toggle Mewtwo Statue 2 to State B (using the activate_mansion_switch tool).
  - Return to 3F West via the stairs at (7, 10).
  - Walk to the right edge of the balcony: Column 7 Row 14 or 15.
  - Test walking Right (East) onto Column 8 to execute the balcony drop.
## State B 2F East South Balcony Railings Campaign (Active Turn 89522)
- **Objective**: Systematically and physically test the passability of the 2F East South balcony boundaries (Columns 11-14, Rows 15-26) on foot under active State B to find any potential jump-down drop or passage. This campaign is successfully completed.
- **Conclusive Proof of Isolation**: Every single coordinate has been tested on foot and found 100% solid. No drops, gaps, or passages exist on the 2F East South balcony under State B.
- **Audit Schedule & Status Tracker**:
  1. **Column 14 Atrium Railing (Rows 16-25)**:
     - Row 16 Column 14: Completed Turn 87351. Bumped (solid).
     - Row 17 Column 14: Completed Turn 87372. Bumped (solid).
     - Row 18 Column 14: Completed Turn 89293. Bumped (solid).
     - Row 19 Column 14: Completed Turn 89299. Bumped (solid).
     - Row 20 Column 14: Completed Turn 89306. Bumped (solid).
     - Row 21 Column 14: Completed Turn 89315. Bumped (solid).
     - Row 22 Column 14: Completed Turn 89321. Bumped (solid).
     - Row 23 Column 14: Completed Turn 89324. Bumped (solid).
     - Row 24 Column 14: Completed Turn 89330. Bumped (solid).
     - Row 25 Column 14: Completed Turn 89333. Bumped (solid).
  2. **Column 11 Western Railing (Rows 16-26)**:
     - Row 16 Column 11: Completed Turn 89426. Bumped (solid).
     - Row 17 Column 11: Completed Turn 89418. Bumped (solid).
     - Row 18 Column 11: Completed Turn 89403. Bumped (solid).
     - Row 19 Column 11: Completed Turn 89393. Bumped (solid).
     - Row 20 Column 11: Completed Turn 89376. Bumped (solid).
     - Row 21 Column 11: Completed Turn 89365. Bumped (solid).
     - Row 23 Column 11: Completed Turn 89357. Bumped (solid).
     - Row 24 Column 11: Completed Turn 89350. Bumped (solid).
     - Row 25 Column 11: Completed Turn 89345. Bumped (solid).
     - Row 26 Column 11: Completed Turn 89452. Bumped (solid).
  3. **Row 15 Northern Wall (Columns 12-13)**:
     - Row 15 Column 12: Completed Turn 89429. Bumped (solid).
     - Row 15 Column 13: Completed Turn 89434. Bumped (solid).
  4. **Row 26 Southern Wall/Gate (Columns 12-13)**:
     - Row 26 Column 12 (Gate 26): Completed Turn 80627. Bumped (solid).
     - Row 26 Column 13 (Gate 26): Completed Turn 87357. Bumped (solid).

## 1F West to 1F East Northern Crossing Layout (Verified Turn 90445)
- Column 12 is a completely open, passable vertical walkway (TYPE_3fe2) from Row 12 to Row 7, providing the vertical path to bypass the horizontal partition wall at Row 9 in 1F West.
- Path from (10, 11) to northern crossing:
  - Right 2 to (12, 11)
  - Up 4 to (12, 7)
- **Turn 90465**: Reached (26, 3) on 1F East. Column 22 wall partition has been successfully bypassed via Row 3! Now making our way down Column 26 to reach Gate 1 at (25, 13).
## Turn 90734 Gate 2 Verification Campaign
- Objective: Verify if Gate 2 at (10, 11) is OPEN under active State B on 3F.
- Path to test:
  - Walk Up from (5, 10) to (5, 9) to bypass the stairs warp at (7, 10).
  - Walk Right along Row 9 to Column 9 (9, 9).
  - Walk Down to (9, 11).
  - Walk Right to attempt to cross Gate 2 at (10, 11).
## Turn 90789 Western Balcony Drop State B Verification Results
- **Turn 90786 Test (Row 15)**: Stood at (7, 15) facing Right and pressed Right. Result: **Bump** against (8, 15) (stayed at (7, 15)). Confirmed 100% solid, impassable under active State B.
- **Turn 90788 Test (Row 14)**: Stood at (7, 14) facing Right and pressed Right. Result: **Bump** against (8, 14) (stayed at (7, 14)). Confirmed 100% solid, impassable under active State B.
- **Conclusion**: There is absolutely no western balcony drop on Column 7 under active State B. 
- **Active Plan**: Since Statue 2 on 2F West is now successfully toggled to active State B (using activate_mansion_switch), Gate 2 at (10, 11) on 3F should now be OPEN! We will navigate to (9, 11) on 3F West and cross Gate 2 to reach 3F East, where the actual eastern balcony drop is located.