# Post-Safari Zone Route & Progression Plan

## Cinnabar Mansion Deep B1F Routing & Switch Matrix (Turn 78160)
- **Active Exploration Mission**: Locate and retrieve the Secret Key on B1F.
- **Switch Matrix (State A vs. State B)**:
  - We have toggled Statue 2 (2F, (2, 11)) back to **State A** (Default) on Turn 77818.
  - State A: Gate 1 on 1F (25, 13) is CLOSED, blocking foot access to the Southeast room.
  - State A: Gate 3 on 2F (18, 8)-(19, 8) is OPEN.
  - State A: Gate 4 on 1F East (21, 17) is OPEN.
  - State A: Gate 6 on 2F (9, 4)-(9, 5) is CLOSED.

## Cinnabar Gym Blaine Matchup Preparation Strategy
- **The Balcony Drop Breakthrough (Turn 78541)**:
  - Landing Constraint: Under State A, Gate 1 at (25, 13) on 1F East is CLOSED, occupying the landing tile of the 3F West balcony drop and physically blocking the drop (resulting in bumps during testing).
  - State B Viability: Under State B, Gate 1 on 1F East is OPEN, clearing the landing tile. Our previous bump under State B on Turn 76905 occurred because the wandering Scientist NPC was temporarily occupying the landing tile. Now that we have taken many steps, the NPC has wandered away, leaving the landing tile completely unblocked.
  - Escape Strategy: Once we drop under State B, we take the stairs down from 2F to 1F East. The stairs down to B1F are located directly inside this isolated 1F East south-central pocket, so we can descend to B1F and retrieve the Secret Key without needing Gate 4 to be open. Once we have the Secret Key, we will simply use one of our 2 Escape Ropes to warp out of the Mansion.

## Cinnabar Mansion B1F Progression Status (Turn 78573)
- SW Balcony Drop: Under both State A and State B, all reachable columns (1 to 5) on the southwest balcony of 3F West are 100% solid, impassable railings with no drop-off. Therefore, the southwest balcony of 3F West is NOT a balcony drop.

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
- **3F West (9, 12) State B Re-Verification Plan**: If we ever re-test the passability of (9, 12) under State B, we must visually verify that the Scientist NPC (SPRITE_cdfc) is elsewhere (e.g. at (4, 11)) and not standing on (9, 12) or (9, 13) to prevent a false-positive collision.

## The Definitive Progression Hypothesis (Turn 80836)
- **Problem**: 3F West-East crossover is 100% blocked under both states. 1F East South is blocked from 1F West under State A, and 1F south-central pocket (B1F stairs) is isolated on foot under State B.
- **The Breakthrough Solution**:
  1. Return to 1F West, go up to 2F West, and toggle Statue 2 back to **State A (Default)**.
  2. Under State A, the 2F Row 11 corridor is open and passable to 2F East South.
  3. Walk onto 2F East South under State A.
  4. Walk to Row 22 of 2F East South and investigate if we can cross Column 22 on Row 22 under State A, or check if there is an alternative open crossover on Row 22 to access the 2F Southeast room. Note: The Southeast room is verified to only span Rows 9-15. If Rows 16-27 on Columns 23-28 is black space or solid wall, (23, 22) will be impassable. We will systematically inspect and map the layout of Y=22 to Y=26 on 2F East South under State A.
  5. If an open path exists, go to the 2F Southeast room and climb the stairs up to 3F East at (25, 14).
  6. On 3F East, walk to the balcony pit and jump down to B1F!
- **Verification Plan**: We will backtrack to 2F West, toggle State A, and physically test the pathing in 2F East South under State A. This satisfies the scientific Burden of Proof!