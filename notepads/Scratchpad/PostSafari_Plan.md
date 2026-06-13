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

## State B 1F East Staircase & B1F Access Model (Active Turn 90003)
- **Objective**: Determine how to access the basement floor (B1F) of Pokémon Mansion.
- **Topological Reality Check**:
  - The eastern shaft is a strictly one-way descending path: 3F East (pit) -> 2F East Southeast (stairs down) -> 1F East Southeast (stairs down) -> B1F (stairs down).
  - Therefore, we cannot climb up the eastern side of the mansion.
  - To reach the start of this descending path on 3F East, we must cross from 3F West via the crossover gate at Column 10 Row 11.
  - Gate 2 on 3F (10, 11) is OPEN under active State B.
  - *Correction / Empirical Proof (Turn 89994/90003)*: We verified that Gate 2 at (10, 11) is CLOSED and solid under active State A AND active State B. Wait, why? The overwatch alert identified that our custom tool `activate_mansion_switch` contained a critical design flaw (pressing UP inside the YES/NO choice box, which shifted the cursor from YES to NO and cancelled the switch activation). Thus, Mewtwo Statue 2 at (2, 11) was NEVER successfully toggled to State B! We have been in active State A (Default) this whole time, which is why Gate 2 remained closed.
- **Current Action Plan**:
  - Walk back to the stairs at (7, 10) on 3F West and descend to 2F West.
  - Walk to Mewtwo Statue 2 at (2, 11) on 2F West.
  - Correctly toggle Statue 2 to State B by manually talking to it from (2, 12) facing UP or (3, 11) facing LEFT, and pressing 'A' to select 'YES' (relying on the default cursor position, without pressing UP).
  - Confirm the gate toggled (e.g. by checking if Gate 6 is open).
  - Walk back to the stairs at (7, 10) and ascend to 3F West.
  - Walk to (9, 11) and cross into 3F East via the now open Gate 2 at (10, 11).
  - Step into the giant balcony drop pit on 3F East to land in the isolated 2F Southeast room, then take the stairs down to 1F Southeast, and then take the stairs down to B1F!
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