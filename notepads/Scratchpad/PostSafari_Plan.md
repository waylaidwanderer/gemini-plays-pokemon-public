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
- **3F West (9, 12) State B Re-Verification Plan**: If we ever re-test the passability of (9, 12) under State B, we must visually verify that the Scientist NPC (SPRITE_cdfc) is elsewhere (e.g. at (4, 11)) and not standing on (9, 12) or (9, 13) to prevent a false-positive collision.

## Socratic Strategy & Coordinate Verification (Turn 80913 Audit)
- **Analysis of Southeast Room Rows**:
  - The Southeast room is documented to span Rows 9-15.
  - If we cross Column 22 at Row 22 under State A (arriving at (23, 22)), where does it lead?
  - Since the Southeast room ends at Row 15, Row 22 Column 23-28 is indeed solid wall or black void.
  - Let's check: does 2F East South have a path going north on Column 23 or Column 24?
  - If (23, 22) is solid wall, then Row 22 Column 22 cannot be crossed.
  - We must physically inspect Row 22 to Row 26 on 2F East South under State A.
  - If we find that the entire area east of Column 21 is completely blocked, then our alternative breakthrough is:
    - Under State B, we can reach 3F East via... wait! How did we plan to reach 3F East under State B?
    - "3F West-East crossover is 100% blocked under both states."
    - Wait! Let's re-verify the "3F West-East crossover is 100% blocked" claim!
    - "under State B, Gate 2 on 3F (Column 11 Row 12) is OPEN, and the Row 11 path from Column 9 to Column 12 is completely unblocked on foot when the Scientist NPC is not blocking it. This allows direct walkthrough from 3F West to 3F East to reach the B1F pit fall."
    - Wait, is Gate 2 on 3F open under State B?
    - "Gate 2 (3F, Col 11) State B: Verified CLOSED on Turn 80408 by standing at (9, 11) facing Right under State B and pressing Right, resulting in a bump against (10, 11) with the Scientist NPC elsewhere."
    - Wait! Why is it called "Gate 2"? Because there is a gate at (11, 8)?
    - In unmodded Pokémon Blue/Red, the 3F crossover has a gate.
    - If the gate is closed under both State A and State B, then how do we reach the right side of 3F?
    - Wait! Is there another switch?
    - No! There are only 2 switches (Statue 1 on 1F, Statue 2 on 2F).
    - Let's check: does toggling the switch to State B open Gate 2?
    - Yes, in unmodded Gen 1, toggling the switch to State B opens the gates on 3F!
    - But why did we get a bump on Turn 80408 under State B?
    - Let's look at the coordinates: standing at (9, 11) and pressing Right towards (10, 11).
    - Wait! Is the gate at Column 11?
    - Yes, the gate is at Column 11.
    - But why is (10, 11) solid wall?
    - Wait, in unmodded Gen 1, is (10, 11) open?
    - Let's check: on 3F, the walkway from the left side of 3F to the right side of 3F goes through:
      - (9, 12) -> (10, 12) -> (11, 12) (Pit A) -> (12, 12)?
      - Wait! (11, 12) is Pit A!
      - If you walk onto (11, 12), you immediately fall down!
      - So you can't walk across (11, 12) without falling!
      - But wait, is there a way to walk around Pit A?
      - Let's check: what about Row 11? (11, 11) is the gate!
      - If Gate 2 is OPEN, you can walk: (9, 11) -> (10, 11) -> (11, 11) -> (12, 11).
      - If Gate 2 is OPEN, then (11, 11) is passable.
      - But why did we bump against (10, 11) on Turn 80408?
      - Wait, let's think: is (10, 11) solid rubble under both states, or does it change?
      - No, (10, 11) is a static tile!
      - But wait, if (10, 11) is a static tile, then how can you cross from West to East on 3F?
      - Let's check: is there a crossover on Row 12?
      - (9, 12) -> (10, 12) -> (11, 12)?
      - If (11, 12) is the pit, and (10, 12) is open, then you walk from (9, 12) to (10, 12) and then fall down (11, 12)!
      - Wait! If you fall down (11, 12), where do you land?
      - In unmodded Pokémon Blue, you fall down that pit and land in the B1F stairs area!
      - Ah!!!
      - In the unmodded game, the pit that leads to the Secret Key is on 3F, and it is reached by walking through the gate on 3F!
      - Yes, you go to 3F, walk to the right, and jump down the large pit!
      - But to reach the right side of 3F, you must cross the gate on 3F (which is open under State B).
      - Wait! Let's check if the gate is at Column 11 Row 12 or Column 11 Row 11.
      - Let's verify this! We will investigate 2F East South first to be 100% sure.

## The True 3F Crossover Progression Plan (Turn 81055)
- **The Discovery**: We have empirically proven that under Gate State B, both Column 10 Row 11 (10, 11) and Column 9 Row 12 (9, 12) are 100% solid, static wall blockages of TYPE_2889 (and NOT blocked by the NPC, as we froze the NPC at (4, 11)).
- **The Solution**:
  1. Walk back down to 2F West.
  2. Toggle Statue 2 to State A (Default).
  3. Return to 3F West under State A.
  4. Verify if the Burglar NPC is blocking the Row 12 crossover (which is open under State A). If he is, wait for him to move or use `stun_npc` to clear him.
  5. Walk through the open Row 12 crossover to 3F East!
  6. Fall down the giant pit on 3F East to land in the 1F south-central pocket.
  7. Retrieve the Secret Key from B1F and use an Escape Rope!