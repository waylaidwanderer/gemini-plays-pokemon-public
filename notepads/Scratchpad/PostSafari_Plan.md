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
- **State A Northeast Staircase Verification (Turn 85926 Completed)**:
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
- **Verification Logs**:
  - Turn 86841: Stood at (25, 10) facing Up, pressed Up against (25, 9). Result: BUMP.
  - Turn 86842: Stood at (24, 10) facing Up, pressed Up against (24, 9). Result: BUMP.
  - Turn 86843: Stood at (23, 9) facing Right, pressed Right against (24, 9). Result: BUMP.
  - Turn 86844: Stood at (26, 9) facing Left, pressed Left against (25, 9). Result: BUMP.
- **Conclusion**: The Northeast staircase at (24, 8)-(25, 9) is 100% solid, closed, and impassable from all directions under active State A.

## Disproven State B 1F Northeast Staircase Strategy (Completed Turn 86912)
- **Result**: Tested and disproven on Turns 86902 and 86910.
- **Verification Logs**:
  - Turn 86902: Stood at (25, 10) facing Up, pressed Up against (25, 9). Result: BUMP.
  - Turn 86910: Stood at (24, 10) facing Up, pressed Up against (24, 9). Result: BUMP.
- **Conclusion**: The Northeast staircase at (24, 8)-(25, 9) is 100% solid, closed, and impassable from all directions under active State B as well as State A.

## Disproven State A 2F Southeast Room Balcony Strategy (Completed Turn 87662)
- **Concept**: Hypothesized that under active State A, Column 14 Row 16 or 17 is open, allowing us to cross from 2F East South balcony to the isolated 2F Southeast room.
- **Physical Test Results (State A)**:
  - Turn 87632: Stood at (13, 16) facing Right under active State A, pressed Right. Result: BUMP against (14, 16).
  - Turn 87640: Stood at (13, 17) facing Right under active State A, pressed Right. Result: BUMP against (14, 17).
  - Turn 87475: Stood at (21, 15) facing Down under active State A, pressed Down. Result: BUMP against (21, 16).
  - Turn 87478: Stood at (21, 15) facing Right under active State A, pressed Right. Result: BUMP against (22, 15).
- **Conclusion**: The balcony is 100% solid and blocked on both ends under active State A. The Column 14 balcony crossover is completely solid and blocked.

## State B Northeast Room Dead-End Audit (Completed Turn 87817)
- **Concept**: Test whether the Northeast room of 2F East (Columns 23-28, Rows 2-7) provides foot access to the isolated 2F Southeast room via a gate on Row 8 Column 24 under State B.
- **Physical Test & Audit**:
  - We navigated to (23, 3) inside the Northeast room on Turn 87807.
  - Visual analysis of `<CurrentScreen>` on Turn 87817 reveals that Rows 6 and 7 across Columns 23 to 27 are completely filled with solid rubble tiles (`TYPE_2889`).
  - (23, 6), (24, 6), (25, 6), (26, 6), (27, 6) are 100% solid.
  - (23, 7), (24, 7), (25, 7), (26, 7), (27, 7) are 100% solid.
  - Therefore, we physically cannot stand on Row 7 on Columns 23-27 to test any coordinates on Row 8 on foot.
  - The only open, walkable path on Row 7 is Column 28, where (28, 7) is a standard open floor tile (`TYPE_3fe2`).
  - However, Column 28 Row 8 has already been proven solid under State B on Turn 83391 (resulting in a direct collision bump).
  - **Conclusion**: The Northeast room of 2F East is a 100% confirmed dead-end under State B on foot with absolutely zero access to the isolated 2F Southeast room. This hypothesis is conclusively disproven.

- Column 14 Row 16 Test (Turn 87351): Stood at (13, 16) facing Right under active State B, pressed Right. Result: Bump, physically proving that Column 14 Row 16 is 100% solid and impassable under active State B.
- Column 14 Row 17 Test (Turn 87372): Stood at (13, 17) facing Right under active State B, pressed Right. Result: Bump, physically proving that Column 14 Row 17 is 100% solid and impassable under active State B.
- 3F West Statue side interaction (Turn 87532/87537): Stood at (9, 9) facing Right, pressed A. Result: No textbox, physically proving that the statue at (10, 9) on 3F is non-interactive/decorative from the side.

## State B 2F East South Gate 13 Pit Drop Route (Turn 88242 Plan)
- Active Exploration Phase: Turn 88274.
- **Objective**: Reach Cinnabar Mansion B1F by utilizing the intended vanilla State B route via the 2F East South Pit.
- **The Turn 79849 False-Positive Analysis**:
  - Our previous log states: "Gate 13 (12, 13) is closed under both State A and State B (Verified CLOSED on Turn 79849 under State B)."
  - **The Flaw**: On Turn 79310, we toggled the switch to State A to test Gate 2 on 3F. We then climbed the stairs to 3F West and fell through the pit at (11, 12) without ever returning to 2F West to toggle back to State B!
  - Therefore, on Turn 79849, the mansion was actually in active **State A**, not State B!
  - Our bump against Gate 13 at (12, 13) was because we were in State A (where Gate 13 is indeed CLOSED).
  - In vanilla Pokémon Red/Blue, Gate 13 at (12, 13) is **OPEN under active State B**.
- **The True Route**:
  1. We are currently backtracking to 2F West at (2, 12).
  2. Toggle Mewtwo Statue 2 at (2, 11) to active **State B**.
  3. Walk to (12, 12) on 2F East South (accessible on foot under State B via the open Row 10 crossover at (9, 10)).
  4. Test the passability of Gate 13 at (12, 13) on foot under active State B.
  5. If open, walk south to Row 16 and drop down the pit at (15, 16)-(17, 16).
  6. Land on 1F next to the B1F basement stairs at (21, 23).
  7. Descend the stairs to B1F and retrieve the Secret Key!

- **Step-by-Step Execution Route**:
  1. Walk to 2F West at (2, 12) via the open Row 10 corridor: Left 19 steps to (2, 10), then Down 2 steps to (2, 12).
  2. Press Up to toggle Mewtwo Statue 2 at (2, 11) to State B.
  3. Walk to (12, 12) via the open Row 10 corridor: Up 2 steps to (2, 10), Right 10 steps to (12, 10), then Down 2 steps to (12, 12).
  4. Press Down to walk through the open Gate 13 at (12, 13).
  5. Walk south to Row 16 and drop down the pit at (15, 16)-(17, 16).
  6. Land on 1F and descend to B1F!

## 🧹 Overworld Cleaning Archive (Turn 87554)
- Overwatch clean up successfully done. Removed transient testing protocol for Row 17 Column 14. Original historical facts safely retained.
- **Turn 88033 Physical Passability Test**:
  - We stood at (24, 3) facing Down under active State B and pressed Down against (24, 4) (labeled TYPE_2889).
  - **Result**: Direct collision bump (0 tiles visited), remaining at (24, 3).
  - **Definitive Conclusion**: (24, 4) is indeed a real, solid collision block of TYPE_2889, NOT a background texture. This definitively disproves the State B Northeast-Southeast walkthrough hypothesis. The Northeast room is a complete dead-end under State B.
  - **Active Plan Change (Turn 88038)**:
    - We must return the mansion to **State A** (Default) by toggling Mewtwo Statue 2 at (2, 11) on 2F West.
    - Under State A, we can climb the stairs to 3F West, walk east past the Mewtwo Statue at (10, 9) to 3F East (which is connected on foot under State A), and fall down the right side of the 3F East pit to land next to the B1F basement stairs on 1F East South.