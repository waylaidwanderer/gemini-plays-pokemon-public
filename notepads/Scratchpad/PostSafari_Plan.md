# Post-Safari Zone Route & Progression Plan (Cinnabar Mansion)

## Cinnabar Mansion Deep B1F Routing & Switch Matrix (Turn 78160)
- **Active Exploration Mission**: Locate and retrieve the Secret Key on B1F.
- **State A (Statue 2 Default)**:
  - Gate 1 on 1F (25, 13) is CLOSED, blocking foot access to the Southeast room.
  - Gate 3 on 2F (18, 8)-(19, 8) is CLOSED (Verified CLOSED on Turn 80229).
  - Gate 4 on 1F East (21, 17) is OPEN.
  - Gate 6 on 2F (9, 4)-(9, 5) is CLOSED.
  - Gate 18 on 2F (2, 18) is CLOSED.
  - Gate 26 on 2F (12, 26)-(13, 26) is CLOSED.
  - Gate 13 on 2F (12, 13)-(13, 13) is CLOSED.

- **State B (Statue 2 Toggled)**:
  - Gate 1 on 1F (25, 13) is OPEN, allowing foot access to the Southeast room.
  - Gate 3 on 2F (18, 8)-(19, 8) is OPEN (Verified OPEN on Turn 79932).
  - Gate 4 on 1F East (21, 17) is CLOSED.
  - Gate 6 on 2F (9, 4)-(9, 5) is OPEN.
  - Gate 18 on 2F (2, 18) is CLOSED?
  - Gate 26 on 2F (12, 26)-(13, 26) is CLOSED.
  - Gate 13 on 2F (12, 13)-(13, 13) is CLOSED.

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
- **Active State A Strategy**: Under State A, Gate 4 at (21, 17) is OPEN and Gate 1 at (25, 13) is CLOSED. Since Row 13 is fully impassable on foot on all columns (proven on Turns 84175-84186), we must utilize the newly discovered State A 2F East South Balcony Drop Route to access the southern pocket of 1F East. This route is fully described in 'Scratchpad/Mansion_B1F_Access_Model'. We previously hypothesized walking directly south from the Northeast room of 1F East under State A, but this was disproven on Turns 84175-84186.

### Socratic Question 2: Systematic 3F East Mapping
- We will document all tile coordinates of 3F East in a new temporary notepad `Scratchpad/Mansion_3F_East_Layout`. We will test all boundaries and check for pits.
- We will specifically look for the break in the southern balcony railing on 3F East, and map the large central pit boundaries before making the deliberate leap.

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

## State B Column 24 Passability Testing Protocol (Turn 83089 Plan) - RESOLVED (Turn 83182)
- **Objective**: Physically test the horizontal passability of Column 24 (specifically Row 14) on 1F East under State B, verifying if the eastern Southeast room is connected on foot to the south-central pocket.
- **Methodology & Results**:
  1. Walked to (26, 12), then Left to (25, 12), and Down through Gate 1 at (25, 13) to reach (25, 14). (Completed)
  2. Stood at (25, 14) facing Left (West). (Completed)
  3. Attempted to walk Left onto (24, 14). (Completed)
  4. Result: Traversal was 100% successful! Stood on (24, 14) with zero collisions on Turn 83182, proving that Column 24 Row 14 is open and passable under State B.
- **Conclusive Separation Analysis (Turn 83201)**:
  - While Column 24 is open on Row 14 under State B, Column 24's passability on Rows 19 to 24 under State B has NOT been physically tested on foot. We previously made an unverified assumption that it was blocked by solid wall of TYPE_2889 on these rows based on visual interpretation, but standard vanilla layout has this room open on the south. If Column 24 is actually open under State B, then walking to the B1F stairs on foot from Gate 1 is 100% functional, rendering all complex balcony drops completely unnecessary. We must physically test this immediately.
  - Row 16 is open horizontally, but Gate 4 at (21, 17) is CLOSED under State B.
  - This means since Column 24 is indeed physically blocked on Y=19-24 under State B (verified Turn 84296), the B1F stairs at (21, 23) cannot be reached on foot from the entrance of 1F under State B. We must utilize the newly discovered State A 2F East South Balcony Drop Route to access the southern pocket of 1F East, as detailed in 'Scratchpad/Mansion_B1F_Access_Model'.