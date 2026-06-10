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

## Answers to Socratic Questions (Turn 79233)

### Socratic Question 1: 3F East Pit Landing Scenarios & Gate 4 Impact
- **Pit Drop Landing Scenarios**:
  - **Scenario A (2F Southeast Room Landing)**: If we drop down and land in the isolated 2F Southeast room, we will find ourselves adjacent to the stairs down at (25, 14) on 2F. We will immediately descend these stairs to land in the 1F East south-central pocket (Columns 21-23, Rows 18-27) near the B1F stairs.
  - **Scenario B (1F South-Central Pocket Direct Landing)**: If we drop down and land directly in the 1F East south-central pocket on ground level (z=0), we are already next to the B1F stairs.
- **State B Gate Status & Escape Strategy**:
  - Under State B, Gate 4 at (21, 17) on 1F East is CLOSED. Since the 1F south-central pocket is completely bounded by Gate 4 (CLOSED), Column 11 solid wall, Column 22 solid rubble, and Row 13 solid walls, we are **100% physically trapped and isolated on foot** once we land in this pocket.
  - However, this does not soft-lock us. Our planned escape strategy is to descend the stairs to B1F, retrieve the Secret Key, and then immediately use one of our **2 Escape Ropes** to safely warp out of the Mansion. This bypasses the need to open Gate 4.

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