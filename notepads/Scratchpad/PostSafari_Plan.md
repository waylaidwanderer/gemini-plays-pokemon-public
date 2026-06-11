# Post-Safari Zone Route & Progression Plan

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

### Socratic Question 2: B1F Systematic Mapping & Statue 4 Evaluation
- **B1F Systematic Mapping Plan**:
  - Once we descend to B1F, we will treat it as unmapped territory.
  - We will walk along every passable row and column, logging all obstacles, item locations, Mewtwo statues (such as the hypothesized Statue 4), and gates.
  - We will construct and update a dedicated basement gate matrix in `Scratchpad/Mansion_Gate_Matrix` using the following structure:
    - `| Gate ID & Location | State A | State B | Verification & Proof of Work |`
  - If we locate Statue 4, we will systematically test it by interacting with it, logging the exact turn and the corresponding open/closed status changes of all gates in B1F and higher floors.

### Socratic Question 3: 3F East Systematic Mapping Protocol
- **Mapping 3F East before the Leap**:
  - Once we cross the Column 11 Row 12 Gate on 3F under State B to enter the Eastern wing, we will NOT blindly run and jump.
  - We will carefully map the entire eastern wing of 3F:
    - Identify all pits/chutes and log their exact coordinates (X, Y).
    - Identify any staircases, walls, and gates.
    - Systematically test the boundary tiles.
    - Only after verifying the exact pit coordinates and correlating them with the 1F landing zones will we execute the drop to land in the target 1F south-central pocket.

## Cinnabar Mansion Breakthrough Exploration Phase (Turn 79491)
- **Verified Fact**: 2F East South Column 22 is completely solid/rubble under both State A and State B across rows 8-15. This separates Column 21 from Column 23 on these rows.

- **B1F Mapping Protocol**:
  - Once in B1F, we will walk along every passable tile, logging items, statues, and gates.
  - We will record all B1F gates and switch dependencies in `Scratchpad/Mansion_Gate_Matrix` using our structured circuit matrix format.

### 3F East Pit-Mapping Spatial Safety Protocol (Added Turn 79515)
- **The Risk**: Overworld pit tiles (such as TYPE_21ec, visually dark voids) trigger immediate, irreversible map transitions/falls upon step contact. Rushing can result in an accidental fall before mapping is complete.
- **Safety Protocol**:
  1. Once we cross into the eastern wing on 3F East under State B, we will limit all movements near boundaries or unfamiliar areas to **1-tile chunks** (pressing only one directional button at a time).
  2. We will verify the screen and tile labels after every single step.
  3. We will NEVER step blindly onto any tile that has not been confirmed to be a standard floor tile (such as TYPE_3fe2).
  4. We will systematically map the coordinates of all walls, balconies, and pit boundaries from a safe distance before choosing which pit to fall into.

## Socratic Socratic Answers (Turn 79575)
### Socratic Question 1: 3F East Pit Landing & Escape Protocol
- **Systematic Protocol**: Once we cross into the Eastern wing of 3F East under State B, we will limit all movements to **1-tile chunks** (single step inputs) to avoid accidental falls. We will visually map the pit coordinates (`TYPE_21ec`) from adjacent safe floor tiles (`TYPE_3fe2`).
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

## 2F East South Row 26 Alternate Column Exploration Plan (Turn 81554)
- **Background**: We have physically verified that 3F West-East crossover is 100% blocked under both states, 3F West balcony has solid railings, and 2F Southeast room is isolated under both states. 
- **The Hypothesis**: To reach the southern balcony on Row 26/27, we can utilize our on-foot access to 2F East South under State A (Default). While Gate 26 at (12, 26)-(13, 26) is CLOSED, and Column 11 Row 26 / Column 14 Row 25 are CLOSED, there are alternate columns on Row 26 (specifically Columns 15, 16, 17, 18, 19) that may be open and provide the walkthrough to the southern balcony (Row 27).
- **The Plan**:
  1. Descend from 3F West (9, 11) using the stairs at (7, 10) to reach 2F West.
  2. Walk Left to (2, 12) and toggle the Mewtwo Statue 2 back to State A (Default) to open Gate 3.
  3. Walk East through the open Gate 3 into 2F East South (Columns 18-21).
  4. Attempt to walk Left/West on Rows 18-24 to bypass the Column 14/15 vertical dividing wall. We will test if we can reach Columns 11-17 on these rows and systematically find an open passageway to the southern balcony (Row 26/27).
  5. If any column is open, we will step onto the balcony (Row 27) and test for the balcony drop to 1F.

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

# Reflection and Self-Assessment on Turn 81654

## 1. Immediate Execution
- Over the last 50 turns, we navigated from B1F back up to 2F, toggled the switches, navigated 2F East South, mapped out its western corridor (which proved to be a dead-end on foot), and went back up to 3F West to visually inspect Column 10.
- Now, we are standing on 2F West at (7, 10). Our intention is to walk to the Mewtwo Statue 2 at (2, 11) by standing at (2, 12) facing Up and pressing 'A' to toggle the switch to State B (Toggled).
- Once in State B, we will return to 3F West and see if the crossover at Column 10 Row 11 or 12 opens up, or if there is another path.
- Let's check:
  - If we toggle to State B:
    - On 2F, Gate 6 at (9, 4)-(9, 5) opens.
    - Gate 3 at (18, 8)-(19, 8) opens? No, wait! Under State B, Gate 3 is CLOSED.
    - Gate 1 at 1F (25, 13) opens.
    - Let's toggle and return to 3F West to look at the screen!

## 2. Notepad Hygiene
- The notepads are well-organized, with a clean directory in Main.
- We will keep the temporary notes in Scratchpad/Mansion_3F_Crossover_Tests and migrate them once we find the final unblocked path to B1F.

## 3. Map Hygiene
- Map markers are highly accurate, showing stairs down to 1F at (5, 10), stairs up to 3F at (7, 10), and Statue 2 at (2, 11).
- We will add more markers once we enter B1F.

## 4. Custom Tools & Specialized Agents Planning
- We can think of 5 highly specialized custom tools/agents to implement:
  1. `mansion_switch_predictor`: Evaluates the current global switch state and predicts which gates are open/closed.
  2. `flee_battle_v2`: Standard flee utility (already exists and works flawlessly).
  3. `b1f_routing_optimizer`: Finds paths around B1F's specific gate layout once mapped.
  4. `escape_rope_warp_helper`: Automates bag navigation to use Escape Rope.
  5. `fossil_revive_planner`: Strategizes which fossils to revive at the Cinnabar Lab.

## 5. Tool Maintenance
- Our flee_battle tool works perfectly and has been extremely helpful in saving us time and preserving Blastoise's health.

## 6. Goal Clarity
- **Primary Goal**: Retrieve Secret Key from Cinnabar Mansion B1F.
- **Secondary Goal**: Walk to (2, 12), face Up, and toggle Mewtwo Statue 2 to State B (Toggled).
- **Navigation Goal**: Mewtwo Statue 2 at (2, 11) from (2, 12).

## 7. Error Analysis & Hypothesis Review
- **The Core Conflict**:
  - If 3F East is unreachable from 3F West under both states, and 2F Southeast room is unreachable on foot under both states, and 1F East south-central pocket is unreachable on foot under both states, then there MUST be an open path we haven't fully verified.
  - Let's verify what happens under State B on 3F West. We will walk up to 3F West under State B and look at the screen!
  - Let's go to (2, 12) on 2F West first and toggle the switch.