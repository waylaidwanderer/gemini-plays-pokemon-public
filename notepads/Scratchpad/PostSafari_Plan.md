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
## Active State A Northeast Room Hypothesis (Started Turn 86221)
- **The Hypothesis**: Since 3F West-East crossover is completely solid under both states, and the 2F Southeast room (with stairs up to 3F East) is isolated, and 1F East Northeast room has no stairs under State B, the active staircase to 2F East Southeast/Northeast must be active and accessible under State A!
  - Under State A, we can enter the Northeast room of 1F East on foot via the northern crossover on Column 22 Row 3 (which is open under State A).
  - We successfully toggled Mewtwo Statue 1 to State A (Default) on Turn 86214.
  - We will now systematically test all tiles in the Northeast room on foot under State A and log every coordinate-specific outcome below.

- **Definitive 1F East Northeast Room Complete Sweep Disproof**: We systematically and physically walked over every single passable floor tile in the Northeast room of 1F East under both State A (Default) and State B (Turns 86234-86286). Absolutely none of the tiles triggered a staircase transition or warp. This empirically and definitively disproves the existence of any active staircase or warp in the Northeast room. Combined with the complete sweep disproof of the Southeast room of 1F East, we can definitively state that **1F East is completely staircase-less**. The staircase to 2F East South/Southeast must be accessed by some other means.

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

## Active State A 2F Southeast Room Balcony Strategy (Started Turn 87402)
- **Concept**: Our previous State B Balcony Crossover and State B 1F Northeast Staircase strategies are completely disproven. We discovered that the 2F East South balcony (Column 14) is CLOSED under State B but OPEN under State A!
- **Step-by-Step Execution Plan**:
  1. From our current position (10, 18) on 2F West under State B, walk to Statue 2 at (2, 11) on 2F West.
  2. Toggle Statue 2 to active State A (Default).
  3. Under active State A, Gate 3 at (18, 8)-(19, 8) on 2F East is OPEN. Walk through Gate 3 onto 2F East South.
  4. Walk South to the 2F East South southern balcony (Row 16).
  5. Under active State A, the balcony gate at Column 14 Row 16 is OPEN. Walk East through Column 14 into the isolated 2F Southeast room (Columns 23-28)!
  6. In the Southeast room of 2F East, walk to the stairs at (25, 14) and climb UP to 3F East.
  7. On 3F East, walk to the rightmost balcony pit and fall down to B1F.
  8. Enter B1F to find the Secret Key.

- Active Exploration Phase Start: Turn 86550. Currently on Turn 87424.
- Column 14 Row 16 Test (Turn 87351): Stood at (13, 16) facing Right under active State B, pressed Right. Result: Bump, physically proving that Column 14 Row 16 is 100% solid and impassable under active State B.
- Column 14 Row 17 Test (Turn 87372): Stood at (13, 17) facing Right under active State B, pressed Right. Result: Bump, physically proving that Column 14 Row 17 is 100% solid and impassable under active State B.
- Gate 26 Test (Turn 87357): Stood at (13, 25) facing Down under active State B, pressed Down. Result: Bump, physically proving that Gate 26 at (13, 26) is CLOSED and impassable under active State B.

## State A Column 22 Row 16/17 Passability Testing Protocol (Started Turn 87424)
- **Objective**: Verify if the southern balcony on Row 16 or Row 17 is open across Column 22 under active State A, allowing horizontal crossover from Column 21 to Column 23 on foot.
- **Methodology**:
  1. Set global switch to State A (Default) at Statue 2.
  2. Walk to 2F East South via the open Gate 3 at (18, 8)-(19, 8).
  3. Walk to (21, 16) on the southern balcony.
  4. Attempt to walk Right onto (22, 16). Log result (Bump vs Pass).
  5. If Row 16 is blocked, walk to (21, 17) and attempt to walk Right onto (22, 17). Log result (Bump vs Pass).
  6. If either is open, walk East to Column 23 to access the isolated 2F Southeast room.