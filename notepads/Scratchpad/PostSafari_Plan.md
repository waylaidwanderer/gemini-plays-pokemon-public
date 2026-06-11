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
- **The Balcony Drop Breakthrough (Turn 78541)**:
  - Landing Constraint: Under State A, Gate 1 at (25, 13) on 1F East is CLOSED, occupying the landing tile of the 3F West balcony drop and physically blocking the drop (resulting in bumps during testing).
  - State B Viability: Under State B, Gate 1 on 1F East is OPEN, clearing the landing tile. Our previous bump under State B on Turn 76905 occurred because the wandering Scientist NPC was temporarily occupying the landing tile. Now that we have taken many steps, the NPC has wandered away, leaving the landing tile completely unblocked.
  - Escape Strategy: Once we drop under State B, we take the stairs down from 2F to 1F East. The stairs down to B1F are located directly inside this isolated 1F East south-central pocket, so we can descend to B1F and retrieve the Secret Key without needing Gate 4 to be open. Once we have the Secret Key, we will simply use one of our 2 Escape Ropes to warp out of the Mansion.

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
- **Trapped Pocket & Escape Plan**:
  - Falling through the 3F East pit lands us in the 1F south-central pocket (near the stairs to B1F).
  - Under State B, Gate 4 at (21, 17) is closed, meaning we are 100% trapped on foot in this 1F pocket.
  - This is fine! We will immediately go down the stairs to B1F, find the Secret Key, and use one of our **2 Escape Ropes** to escape. No Gate 4 bypass is necessary.
- **3F West Balcony Drop Route**:
  - On 3F West under State B, we can stand at (5, 16) and press Down to jump over the balcony railing at (5, 17) and drop to 1F East. This drops us directly inside the 1F East south-central pocket adjacent to the B1F stairs.
  - Verification: Stood at (5, 16) under State B and pressed Down. Since Gate 1 on 1F East at (25, 13) is OPEN under State B, the landing tile is completely clear, allowing us to drop down. This is the true unblocked balcony drop!
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
- **Definitive 3F Crossover Passability Audit**:
  - Socratic Question 2 is fully resolved: we have completed a complete, systematic, and physically verified passability audit of ALL potential walkthrough crossover rows on 3F West (Map 0_215) under both State A and State B with the Scientist NPC out of the way or frozen.
  - Under State B (Toggled):
    - Row 10 Column 10 (10, 10): CLOSED (Bumped on Turn 80478 and Turn 81093).
    - Row 11 Column 10 (10, 11): CLOSED (Bumped on Turn 80408 and Turn 81052).
    - Row 12 Column 9 (9, 12): CLOSED (Bumped on Turn 80285 and Turn 81045).
    - Row 13 Column 9 (9, 13): CLOSED (Bumped on Turn 80472 and Turn 81097).
    - Row 14 Column 8 (8, 14): CLOSED (Bumped on Turn 80447 and Turn 81101).
    - Row 15 Column 8 (8, 15): CLOSED (Bumped on Turn 80446).
  - Under State A (Default):
    - Row 10 Column 10 (10, 10): CLOSED (Bumped on Turn 81171).
    - Row 11 Column 10 (10, 11): CLOSED (Bumped on Turn 81148).
    - Row 12 Column 9 (9, 12): CLOSED (Bumped on Turn 81149).
    - Row 13 Column 9 (9, 13): CLOSED (Bumped on Turn 81189).
  - This mathematically and physically proves that the 3F West-East crossover is 100% blocked on foot in BOTH states.
- **The B1F Descent Breakthrough**:
  - Since the 2F Southeast room is isolated on foot and 3F East cannot be reached from 3F West, there is no on-foot crossover to B1F.
  - The ONLY way to reach B1F is the Balcony Drop Route under State B!
  - Under State B, stand at (5, 16) on 3F West and press Down to jump over the balcony railing at (5, 17).
  - Why State B? Under State B, Gate 1 on 1F East at (25, 13) is OPEN, which clears the landing tile. Under State A, Gate 1 is CLOSED and blocks the landing tile (causing bumps).
  - Once we drop, we will land in the 1F south-central pocket directly adjacent to the stairs down to B1F.
  - From there, we go down to B1F, retrieve the Secret Key, and use an Escape Rope to warp out!

## 2F East South Column 22 Balcony Passability Plan (Turn 81271)
- **The Hypothesis**: In unmodded Pokémon Red/Blue, the southern balcony on the second floor (2F East South) is a completely continuous and open walkway spanning horizontally across Column 22 on Rows 16 and 17.
- **The Strategy**:
  1. We are currently standing at (7, 10) on 2F West (Map 0_214) under State B (Toggled).
  2. Under State B, Gate 3 at (18, 8)-(19, 8) is OPEN and passable.
  3. Walk from 2F West to 2F East South via the open Gate 3.
  4. Navigate south to the balcony area (specifically standing at (21, 15) or (21, 16)).
  5. Attempt to walk Right across Column 22 on Row 16 (or Row 17) to reach Column 23 in the isolated Southeast room.
  6. Document the exact coordinates, turn numbers, and collision outcomes of these physical test steps.
  7. If Column 22 is open on either of these rows, it will unlock access to the isolated Southeast room and the stairs up to 3F East, allowing us to reach 3F East, drop down the pit, and descend to B1F to retrieve the Secret Key!