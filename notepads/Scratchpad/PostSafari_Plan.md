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

## State B Southeast Room Isolation Verification (Turn 85829 Verification)
- **Hypothesis**: The Southeast room (Columns 25-28) of 1F East is completely isolated on foot from the B1F stairs at (21, 23) under State B.
- **Methodology**: Stood at (25, 21) on Turn 85829 and visually analyzed the surrounding tile map:
  - Column 24 has a solid wall of TYPE_2889 extending vertically on Rows 19-23.
  - Column 24 and 25 have solid rubble of TYPE_2889 at (24, 24), (25, 24), and (25, 25).
  - Therefore, there is no horizontal pathway connecting Column 25 and Column 21 on the south side.
- **Definitive Conclusion**: The Southeast room of 1F East is indeed completely isolated on foot from the rest of 1F. We must backtrack and toggle the switch to State B to cross to 3F East on foot.

## State B Southeast Room Search Verification (Turn 85901 Completed)
- **Definitive Conclusion**: On Turn 85901, we completed 100% of our systematic floor coverage of the entire Southeast room of 1F East under State B (tested Rows 14-26, Columns 24-28). None of the tiles triggered a staircase transition or warp. This empirically and definitively proves that there is no staircase in the Southeast room of 1F East under State B.

## State A Northeast Staircase Verification (Turn 85926 Completed)**:
  - We toggled Statue 1 back to State A (Default) on Turn 85913, navigated back to 1F East Northeast room, and tested walking Up onto (27, 11) from (27, 12).
  - **Result**: Direct collision bump against (27, 11), remaining at (27, 12) on Turn 85926.
  - **Definitive Conclusion**: The Northeast staircase at (27, 11) / (27, 10) remains completely solid, blocked, and impassable under State A as well. There is no staircase on 1F East under any state.

## Cinnabar Mansion Breakthrough Exploration Phase (Turn 79491)
- **Verified Fact**: 2F East South Column 22 is completely solid/rubble under both State A and State B across rows 8-15. This separates Column 21 from Column 23 on these rows.

- **B1F Mapping Protocol**:
  - Once in B1F, we will walk along every passable tile, logging items, statues, and gates.
  - We will record all B1F gates and switch dependencies in `Scratchpad/Mansion_Gate_Matrix` using our structured circuit matrix format.

### 3F East Pit-Mapping Spatial Safety Protocol (Added Turn 79515)
- **The Risk**: Overworld pit tiles (such as TYPE_21ec, visually dark voids) trigger immediate, irreversible map transitions/falls upon step contact. Rushing can result in an accidental fall before mapping is complete.
- **Safety Protocol**:
  1. Once we cross into the eastern wing on 3F East, we will limit all movements near boundaries or unfamiliar areas to **1-tile chunks** (pressing only one directional button at a time).
  2. We will verify the screen and tile labels after every single step.
  3. We will NEVER step blindly onto any tile that has not been confirmed to be a standard floor tile (such as TYPE_3fe2).
  4. We will systematically map the coordinates of all walls, balconies, and pit boundaries from a safe distance before choosing which pit to fall into.

## Socratic Socratic Answers (Turn 79575)
### Socratic Question 1: 3F East Pit Landing & Escape Protocol
- **Historical Note (State B)**: Under State B, we previously analyzed dropping to the 1F south-central pocket. However, physical testing has proved that Column 24 is a solid wall on Rows 19-24 and Gate 4 is closed under State B, meaning the 1F Southeast room is completely isolated on foot from the B1F stairs. Therefore, the State B Pit Drop Route is disproven.

### Socratic Question 3: Basement Switch Architecture (B1F)
- **Mapping Plan**: B1F is completely unmapped. We will walk every walkable corridor on B1F, logging coordinates of all walls, items, and gates.
- **Circuit Matrix Logging**: We will record all basement gates and their status under State A and State B in `Scratchpad/Mansion_Gate_Matrix`.
- **Statue 4 Evaluation**: If we discover a fourth Mewtwo Statue (Statue 4), we will stand adjacent, face it, and interact with 'A' to toggle it. We will then systematically map which gates in B1F open/close, logging the exact turn and proof of work in our matrix.

## Strategic Notes from Overwatch Audit (Turn 80167)
- **1F West Switch Statue 1 Plan**: If we need to find and toggle Statue 1 on 1F West in the future, we must explore the westernmost room (Columns 1-4, typically around (2, 5)), as the statue at (10, 8) has been proven decorative.

## Socratic Strategy & Coordinate Verification (Turn 80913 Audit) - Verified & Updated
- **Analysis of Southeast Room Rows**:
  - The Southeast room is documented to span Rows 9-15 on 2F East (Map 0_214).
  - Physical testing on Turn 76552-76760 has proven that the Southeast room is 100% isolated and cannot be reached on foot on 2F under both State A and State B because Column 22 is completely blocked by solid rubble/walls on Rows 8-15.
  - Socratic Question 1 is fully resolved: the 2F Southeast room is completely unreachable on foot.
- **Definitive 3F Crossover Passability Audit (Updated Turn 81543)**:
  - We have previously concluded that 3F West is completely blocked from 3F East under both State A and State B.
  - However, our previous testing under State B (Turn 81045) was flawed because we stood on a solid wall tile (8, 12) and tried to walk Right onto (9, 12), resulting in a bump. In Gen 1, attempting to walk from an already solid tile always results in a collision.
  - On Turn 81534, we tested walking Down from the open tile (9, 11) onto (9, 12) under State B (Statue 2 Toggled). Result: **Bump**, remaining at (9, 11). This empirically proves that (9, 12) is indeed 100% solid and impassable under State B.
  - On Turn 81538, we tested walking Right from the open tile (9, 11) onto (10, 11) under State B (Statue 2 Toggled). Result: **Bump**, remaining at (9, 11). This empirically proves that (10, 11) is indeed 100% solid and impassable under State B.
  - Since Column 10 is completely solid rubble/walls on Rows 8-15, and Row 12 Column 9 is solid rubble/wall under State B, the 3F West-East crossover is 100% physically blocked and impassable on foot under BOTH State A and State B. There is no walkthrough connection on 3F.

## State B Northeast Room Complete Sweep Disproof (Turn 86172 Completed)
- **Definitive Conclusion**: On Turn 86172, we completed 100% of our systematic floor coverage of the entire Northeast room of 1F East under State B (tested Rows 1-11, Columns 23-28 on all walkable tiles). Absolutely none of the tiles triggered a staircase transition or warp, and (27, 11) is a solid, closed rubble wall when approached from the proper southern direction at (27, 12). This empirically and definitively disproves the existence of any active staircase or warp in the Northeast room of 1F East under State B.

## 3F West Gate & Balcony Complete Audit (Turn 86326)
- **Turn 86316 Gate (8, 8) Test**: Stood at (8, 9) facing Up under State A and pressed Up. Result: BUMP against (8, 8), proving the gate is CLOSED and impassable under State A.
- **Turn 86323 Balcony (2, 16) Test**: Stood at (2, 16) facing Down under State A and pressed Down. Result: BUMP against (2, 17), proving Column 2 Row 17 is solid and impassable under State A.
- **Turn 86325 Balcony (1, 16) Test**: Stood at (1, 16) facing Down under State A and pressed Down. Result: BUMP against (1, 17), proving Column 1 Row 17 is solid and impassable under State A.
- **Definitive 3F West Balcony Disproof**: All balcony drop directions on 3F West are 100% solid and blocked under both State A and State B. There is no drop-off to 2F East South from the 3F West balcony. We must find another crossover method.

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

## State A 1F East Direct On-Foot Route (Turn 88560 Plan)
- Active Exploration Phase Start: Turn 88593.
- **Objective**: Access the B1F basement by testing the direct on-foot route under active State A on 1F East.
- **Topological Hypothesis**:
  - Under active State A, Gate 4 at (21, 17) is OPEN.
  - The northern horizontal crossover on Row 6 is open on 1F, allowing foot crossing from 1F West to 1F East.
  - We walk horizontally from 1F West to Column 21 Row 6 on 1F East, and walk Down Column 21.
  - Since Row 13 has been proven completely solid across Columns 13 to 22 (Turn 83750, 79215-79227), we will restrict our passability testing strictly to Column 11 and Column 12 on Row 13 to verify if any vertical on-foot pathway to the southern half exists under active State A.
  - If we find an opening on Column 11 or Column 12 Row 13, we will navigate through it to the southern half, walk to (21, 17) (Gate 4, which is OPEN under State A), and descend the B1F stairs at (21, 23).
  - If Columns 11 and 12 are both blocked, then B1F is 100% unreachable on foot under active State A, and we must utilize the 3F West balcony drop under State B.
- **Step-by-Step Execution Route**:
  1. We are currently at (17, 10) on 1F East under State A.
  2. Walk Down 2 steps to (17, 12).
  3. Walk Left 3 steps to (14, 12).
  4. Physically test the passability of Column 13 Row 12, Column 13 Row 11, and Column 13 Row 10 to see if we can get past Column 13 to reach Column 12.
  5. If we cannot cross Column 13, walk back to Row 6 and transition to 1F West, then walk down Column 12/11 from 1F West to test Column 11 and 12 Row 13.

## 🧹 Overworld Cleaning Archive (Turn 87554)
- Overwatch clean up successfully done. Removed transient testing protocol for Row 17 Column 14. Original historical facts safely retained.
- **Turn 88033 Physical Passability Test**:
  - We stood at (24, 3) facing Down under active State B and pressed Down against (24, 4) (labeled TYPE_2889).
  - **Result**: Direct collision bump (0 tiles visited), remaining at (24, 3).
  - **Definitive Conclusion**: (24, 4) is indeed a real, solid collision block of TYPE_2889, NOT a background texture. This definitively disproves the State B Northeast-Southeast walkthrough hypothesis. The Northeast room is a complete dead-end under State B.