# Post-Safari Zone Route & Progression Plan (Cinnabar Mansion)

## Cinnabar Mansion Deep B1F Routing & Switch Matrix (Turn 78160)
- **Active Exploration Mission**: Locate and retrieve the Secret Key on B1F.
- **State A (Statue 2 Default)**:
  - Gate 1 on 1F (25, 13) is CLOSED, blocking foot access to the Southeast room.
  - Gate 3 on 2F (18, 8)-(19, 8) is OPEN.
  - Gate 4 on 1F East (21, 17) is OPEN.
  - Gate 6 on 2F (9, 4)-(9, 5) is CLOSED.
  - Gate 18 on 2F (2, 18) is CLOSED.
  - Gate 26 on 2F (12, 26)-(13, 26) is CLOSED.
  - Gate 13 on 2F (12, 13)-(13, 13) is CLOSED.

- **State B (Statue 2 Toggled)**:
  - Gate 1 on 1F (25, 13) is OPEN, allowing foot access to the Southeast room.
  - Gate 3 on 2F (18, 8)-(19, 8) is CLOSED.
  - Gate 4 on 1F East (21, 17) is CLOSED.
  - Gate 6 on 2F (9, 4)-(9, 5) is OPEN.
  - Gate 18 on 2F (2, 18) is CLOSED?
  - Gate 26 on 2F (12, 26)-(13, 26) is CLOSED.
  - Gate 13 on 2F (12, 13)-(13, 13) is CLOSED.

## Cinnabar Gym Blaine Matchup Preparation Strategy
- **The Balcony Drop Breakthrough (Turn 78541) - Disproven**:
  - We have verified that all five columns on the 3F West southwest balcony are 100% solid, impassable railings under both State A and State B (Verified Turn 77948-77972 and Turn 81256).
  - We have also verified that the 3F West-East crossover is 100% blocked under both states.
  - Therefore, the 3F West balcony drop and 3F East pit drop under State B are not reachable or passable, and this hypothesis is fully disproven.

## Cinnabar Mansion B1F Progression Status (Turn 78573)
- SW Balcony Drop: Under both State A and State B, all reachable columns (1 to 5) on the southwest balcony of 3F West are 100% solid, impassable railings with no drop-off. Therefore, the southwest balcony of 3F West is NOT a balcony drop. This was explicitly verified on Turn 81256 under State B, where standing at (5, 16) facing Down and pressing Down resulted in a direct collision/bump against (5, 17) (TYPE_2889).

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
- **Systematic Protocol**: Once we cross into the Eastern wing of 3F East, we will limit all movements to **1-tile chunks** (single step inputs) to avoid accidental falls. We will visually map the pit coordinates (`TYPE_21ec`) from adjacent safe floor tiles (`TYPE_3fe2`).
- **Landing and Routing**:
  - **Landing in 2F Southeast Room**: If we land in the 2F Southeast room (Columns 23-28, Rows 9-15), we will walk directly to the Southeast staircase at (25, 14) and descend to 1F East. This lands us directly inside the 1F East south-central pocket adjacent to the B1F stairs.
  - **Landing in 1F South-Central Pocket**: If we land directly on 1F East in the south-central pocket (Columns 21-23, Rows 18-27), we are already next to the B1F stairs.
  - **Closed Gate 4 Impact**: Gate 4 at (21, 17) is CLOSED under State B, isolating this pocket on foot. Our strategy is simple and robust: we will descend to B1F, navigate to the Secret Key, collect it, and immediately use one of our **2 Escape Ropes** to warp out of the Mansion. This avoids the need to open Gate 4.

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

## 2F East South Column 22 Balcony Passability Plan (Turn 81307) - Completed & Disproven
- **The Hypothesis**: In unmodded Pokémon Red/Blue, the southern balcony on the second floor (2F East South) is a completely continuous and open walkway spanning horizontally across Column 22 on Rows 16 and 17, or Row 26 provides a walkthrough bypass to Row 27 (the southern balcony).
- **The Strategy Results**: This strategy has been **fully executed and 100% disproven**. We have systematically and physically tested Column 22 on Rows 9-15 under both State A and State B, and Row 26 on Column 11 and Column 14 under State A. All resulted in physical collisions (bumps), proving that 2F East South is completely isolated and has no walkable connection or bypass to Row 27 under State A.

## State A Column 22 Balcony Passability Test Logs (Turn 81341)
- **Turn 81341 (Row 15)**: Stood at (21, 15) under State A and pressed Right to attempt to step onto (22, 15) (TYPE_2889). Result: **Bump**, remaining at (21, 15). This physically and empirically proves that Column 22 is CLOSED and solid/impassable on Row 15 under State A.
- **Turn 81347 (Row 14)**: Stood at (21, 14) under State A and pressed Right to attempt to step onto (22, 14) (TYPE_2889). Result: **Bump**, remaining at (21, 14). This physically and empirically proves that Column 22 is CLOSED and solid/impassable on Row 14 under State A.
- **Turn 81358 (Row 13)**: Stood at (21, 13) under State A and pressed Right to attempt to step onto (22, 13) (TYPE_2889). Result: **Bump**, remaining at (21, 13). This physically and empirically proves that Column 22 is CLOSED and solid/impassable on Row 13 under State A.
- **Turns 81365-81371 State A Column 22 passability tests**:
  - Stand at (21, 12) under State A, pressed Right. Result: **Bump** against (22, 12) (Turn 81365).
  - Stand at (21, 11) under State A, pressed Right. Result: **Bump** against (22, 11) (Turn 81367).
  - Stand at (21, 10) under State A, pressed Right. Result: **Bump** against (22, 10) (Turn 81369).
  - Stand at (21, 9) under State A, pressed Right. Result: **Bump** against (22, 9) (Turn 81371).
  - **Conclusion**: Column 22 is completely blocked by solid/impassable rubble across all Rows from 9 to 15 under BOTH State A and State B. This confirms that 2F East South and the isolated 2F Southeast room are 100% separated on foot on this floor.
- **Turn 81471-81472 State A Row 25 Column 14 passability test**:
  - Stand at (13, 25) under State A, pressed Right to attempt to step onto (14, 25) (TYPE_2889).
  - Result: **Bump**, remaining at (13, 25) (Turn 81472).
  - **Conclusion**: Column 14 Row 25 is completely solid/impassable under State A. This disproves the hypothesis that we can bypass Gate 26 on foot by walking east onto Column 14.
- **Turn 81479 State A Row 26 Column 11 passability test**:
  - Stand at (10, 26) under State A, pressed Right to attempt to step onto (11, 26) (TYPE_2889).
  - Result: **Bump**, remaining at (10, 26) (Turn 81479).
  - **Conclusion**: Column 11 Row 26 is completely solid/impassable under State A. This disproves the hypothesis that we can bypass Gate 26 on foot by walking west onto Column 11.

## State A Column 12 Row 13 Physical Passability Test (Turn 81812 Verification)
- **Physical Test Result**: Standing at (12, 12) under State A on Turn 81812, we attempted to walk Down onto (12, 13). Result: **Bump** (stayed at (12, 12)), physically and empirically proving that Column 12 Row 13 is CLOSED and solid/impassable under State A. This confirms our original layout model that Column 12 is blocked at Row 13 on 1F under State A.

## State A Column 16 Row 7 Physical Passability Test (Turn 81823 Verification)
- **Physical Test Result**: Standing at (16, 6) under State A on Turn 81823, we attempted to walk Down onto (16, 7). Result: **Bump** (stayed at (16, 6)), physically and empirically proving that Column 16 Row 7 is CLOSED and solid/impassable under State A. This confirms that the southern half of 1F East is completely cut off from the northern half of 1F East under State A.

## State B 1F East Northeast Room Staircase Search Protocol (Turn 81848 Plan)
- **Active Exploration Mission**: Access the 1F Northeast Room under State B (Mewtwo Statue 1 Toggled), which is open and passable via the northern crossings on Rows 2 and 3.
- **The Hypothesis**:
  - In vanilla Pokémon Red/Blue, there is an active staircase warp in the 1F East Northeast room (such as (27, 11) or surrounding tiles) that warps the player up to 2F Southeast (or 3F East).
  - Under State B, we can reach 1F East on foot.
  - We will walk to Cinnabar Mansion 1F West Statue 1 at (2, 5), stand at (2, 6) facing Up, and toggle it to State B.
  - Then we will walk to the Northeast room on 1F East:
    - (2, 6) -> (3, 6) -> (3, 2) -> (10, 2) -> (25, 2) (Crossing Column 22 on Row 2/3).
    - From (25, 2), we will enter the Northeast room (Columns 23-28, Rows 2-13) and systematically foot-test all staircase-like coordinates on foot.
  - This systematic test will locate the active staircase warp that grants us access to 2F Southeast and 3F East, allowing us to drop down the pit to B1F!
### Live Exploration Log (Turns 81886-81899)
- **Turn 81886**: Standing at (27, 9) in the Northeast room of 1F under State B. Visually verified that (27, 10) and (27, 11) are solid rubble.
- **Turn 81893**: Walked from (27, 9) to (23, 11) via (26, 9) -> (26, 10) -> (26, 11) -> (25, 11) -> (24, 11) -> (23, 11). No warp triggered on any of these tiles.
- **Turn 81899**: standing at (23, 11). We will now walk Right to (28, 12) via (26, 11) and (26, 12) to test (27, 12) and (28, 12).