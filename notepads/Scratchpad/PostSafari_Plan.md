# Post-Safari Zone Route & Progression Plan (Cinnabar Mansion)

## Cinnabar Mansion Deep B1F Routing & Switch Matrix (Turn 78160)
- **Active Exploration Mission**: Locate and retrieve the Secret Key on B1F.
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
  - Gate 18 on 2F (2, 18) is CLOSED?
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

## State A Northeast Room Systematic Exploration Logs
- Turn 86234: Successfully entered the Northeast room of 1F East at (23, 3) under State A.
- Turn 86241: Completed Row 1 sweep (Columns 23-28). Verified all are standard floor tiles with no staircases or warps.
- Turn 86246: Completed Row 2 sweep (Columns 23-27). Verified all are standard floor tiles with no staircases or warps.
- Turn 86249: Completed Row 3 sweep (Columns 23-27). Verified all are standard floor tiles with no staircases or warps.
- Turn 86253: Completed Row 4 sweep (Columns 26-27). Verified all are standard floor tiles with no staircases or warps.
- Turn 86255: Completed Row 5 sweep (Columns 23-27). Verified all are standard floor tiles with no staircases or warps.
- Turn 86258: Completed Row 6 sweep (Columns 23-28). Verified all are standard floor tiles with no staircases or warps.
- Turn 86259: Completed Row 7 sweep (Columns 23-28). Verified all are standard floor tiles with no staircases or warps.
- Turn 86263: Completed Row 8 sweep (Columns 23, 26, 27). Verified all are standard floor tiles with no staircases or warps.
- Turn 86273: Completed Row 9 sweep (Columns 23, 26, 27). Verified all are standard floor tiles with no staircases or warps.
- Turn 86282: Completed Row 10 sweep (Columns 23-26). Verified all are standard floor tiles with no staircases or warps.
- Turn 86286: Completed Row 11 sweep (Columns 23-26). Verified all are standard floor tiles with no staircases or warps.
- **Definitive 1F East Northeast Room Complete Sweep Disproof**: We have now systematically and physically walked over every single passable floor tile in the Northeast room of 1F East under both State A (Default) and State B. Absolutely none of the tiles triggered a staircase transition or warp. This empirically and definitively disproves the existence of any active staircase or warp in the Northeast room. Combined with the complete sweep disproof of the Southeast room of 1F East, we can definitively state that **1F East is completely staircase-less**. The staircase to 2F East South/Southeast must be accessed by some other means.

## 3F West Gate & Balcony Complete Audit (Turn 86326)
- **Turn 86316 Gate (8, 8) Test**: Stood at (8, 9) facing Up under State A and pressed Up. Result: BUMP against (8, 8), proving the gate is CLOSED and impassable under State A.
- **Turn 86323 Balcony (2, 16) Test**: Stood at (2, 16) facing Down under State A and pressed Down. Result: BUMP against (2, 17), proving Column 2 Row 17 is solid and impassable under State A.
- **Turn 86325 Balcony (1, 16) Test**: Stood at (1, 16) facing Down under State A and pressed Down. Result: BUMP against (1, 17), proving Column 1 Row 17 is solid and impassable under State A.
- **Definitive 3F West Balcony Disproof**: All balcony drop directions on 3F West are 100% solid and blocked under both State A and State B. There is no drop-off to 2F East South from the 3F West balcony. We must find another crossover method.
- **Active State A 3F Crossover Plan (Started Turn 86327)**: Since 1F East is completely staircase-less, and 3F West balcony has no drops, we will revisit the 3F West-East crossover under State A. Historically on Turn 85285-85287, we successfully interacted with the Mewtwo Statue at (10, 9) on 3F and navigated past it to (12, 7) under State A, connecting 3F West to 3F East on foot! We will now walk to (9, 9) on 3F West to verify this connection.