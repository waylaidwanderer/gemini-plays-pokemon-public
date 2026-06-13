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

🧱 Overwatch Cleanup: Large obsolete/duplicate planning blocks from Turns 85829-86326 removed successfully to keep context focused and clean.

## Disproven State A 1F Northeast Staircase Strategy (Completed Turn 86844)
- **Result**: Tested and disproven on Turns 86841-86843.
- **Conclusion**: The Northeast staircase at (24, 8)-(25, 9) is 100% solid, closed, and impassable from all directions under active State A.

## Disproven State B 1F Northeast Staircase Strategy (Completed Turn 86912)
- **Result**: Tested and disproven on Turns 86902 and 86910.
- **Conclusion**: The Northeast staircase at (24, 8)-(25, 9) is 100% solid, closed, and impassable from all directions under active State B as well as State A.

## Disproven State A 2F Southeast Room Balcony Strategy (Completed Turn 87662)
- **Concept**: Hypothesized that under active State A, Column 14 Row 16 or 17 is open, allowing us to cross from 2F East South balcony to the isolated 2F Southeast room.
- **Conclusion**: The balcony is 100% solid and blocked on both ends under active State A. The Column 14 balcony crossover is completely solid and blocked.

## State B Northeast Room Dead-End Audit (Completed Turn 87817)
- **Conclusion**: The Northeast room of 2F East is a 100% confirmed dead-end under State B on foot with absolutely zero access to the isolated 2F Southeast room. This hypothesis is conclusively disproven.

- Column 14 Row 16 Test (Turn 87351): Stood at (13, 16) facing Right under active State B, pressed Right. Result: Bump, physically proving that Column 14 Row 16 is solid and impassable under active State B.
- Column 14 Row 17 Test (Turn 87372): Stood at (13, 17) facing Right under active State B, pressed Right. Result: Bump, physically proving that Column 14 Row 17 is solid and impassable under active State B.
- 3F West Statue side interaction (Turn 87532/87537): Stood at (9, 9) facing Right, pressed A. Result: No textbox, physically proving that the statue at (10, 9) on 3F is non-interactive/decorative from the side.

## State B 3F West Column 10 Row 12/13 Crossover Test (Completed Turn 88481)
- **Objective**: Reach Cinnabar Mansion B1F by utilizing the State B 3F West crossover path.
- **Results**:
  - We have systematically tested Column 10 Row 11 (Turn 88452), Column 9 Row 12 (Turn 88455), Column 9 Row 12 from (8, 12) (Turn 88465), and Column 9 Row 13 from (8, 13) (Turn 88473) on foot under active State B. All tests resulted in solid bumps.
  - **Definitive Conclusion**: The 3F West-East crossover is 100% physically blocked and impassable on foot under active State B. There is no walkthrough connection on 3F under State B.

## 🧹 Overworld Cleaning Archive (Turn 87554)
- Overwatch clean up successfully done. Removed transient testing protocol for Row 17 Column 14. Original historical facts safely retained.
- **Turn 88033 Physical Passability Test**:
  - We stood at (24, 3) facing Down under active State B and pressed Down against (24, 4) (labeled TYPE_2889).
  - **Result**: Direct collision bump (0 tiles visited), remaining at (24, 3).
  - **Definitive Conclusion**: (24, 4) is indeed a real, solid collision block of TYPE_2889, NOT a background texture. This definitively disproves the State B Northeast-Southeast walkthrough hypothesis. The Northeast room is a complete dead-end under State B.

## State B 3F West Column 10 Crossover Campaign (Active Turn 89024)
- **The Redesign**: We have identified a severe physical contradiction in our previous plan: Columns 11-14 on 3F are in the eastern wing (3F East), but the vertical dividing wall at Column 10 is solid on Rows 8-15, making Columns 11-14 completely unreachable from 3F West on foot if Column 10 is closed on all rows.
- **Topological Breakthrough Hypothesis**: To resolve this deadlock and reach B1F, we must systematically test whether we can bypass or cross Column 10 on Row 6 or Row 7 on 3F West under active State B (Statue 2 Toggled). If we can walk around the partition on Row 6 or Row 7 on 3F West under active State B, we will immediately unlock access to the eastern wing of 3F (Columns 11-30), where the static Pit Chute at (11, 12) is located, which drops us down to the basement (B1F) to retrieve the Secret Key!
- **Left-Side Corridor Test Plan**: 
  - To enter the northern room of 3F West (Rows 1-5), we must find an opening in the Row 7 horizontal barrier. Columns 5, 6, and 7 on Row 7 are solid under both states. However, Columns 1, 2, 3, and 4 on Row 7 have NEVER been systematically tested on foot.
  - We will walk to the far-left side of 3F West (Columns 1-4) and test walking Up onto Row 7 to locate an open corridor.
  - If Columns 1, 2, 3, or 4 on Row 7 are open, we can enter the northern room, walk east along Row 5, and cross Column 10 on Row 6 or Row 7 into 3F East!
- **Step-by-Step Path**:
  1. We are currently standing at (9, 9) on 3F West under active State B.
  2. Walk south to Row 11, then west to Column 4 and Column 1.
  3. Attempt to walk Up along Column 4 and Column 1 to Row 8.
  4. From Row 8, test walking Up onto Row 7 on Columns 1, 2, 3, and 4.
  5. If an opening is found, enter the northern room, walk to (10, 6) or (10, 7), and cross to 3F East to fall down the pit!