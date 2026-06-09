# Post-Safari Zone Route & Progression Plan

## Cinnabar Mansion 2F Systematic Search Strategy (Turn 75700)
- **Objective**: Fully explore 2F East and identify any balconies/falls or hidden switches.
- **State Matrix Analysis**:
  - We currently have Statue 2 (2F, (2, 11)) in State B (Toggled).
  - Let's check 2F East under State B. If we find any gates on 2F, we must document them.
  - After mapping 2F East under State B, we will return to (2, 11) on 2F and toggle Statue 2 back to State A (Default).
  - Then we will re-explore 2F East and 1F South under State A to find the switch that actually controls Gate 2 on 3F!
- **Systematic Search Areas**:
  - We will walk every single walkable tile of 2F East on Columns 12-28, Rows 2-27.
  - We will locate the exact coordinate of "Fall Spot 1" on 2F.
  - We will verify where "Fall Spot 1" drops us on 1F (hypothesized to be the blocked southern section of 1F's eastern room).

## Balcony Fall Spot 1 Empirical Verification Plan (Turn 75700)
- **Hypothesis**: Jumping off the balcony/fall spot on 2F East drops the player to the blocked southern section of 1F East (behind Gate 1/4/5), bypassing closed gate barriers.
- **Verification Protocol**:
  1. Stand on 2F adjacent to the balcony ledge (Fall Spot 1).
  2. Press the directional button to jump off/fall down the pit.
  3. Immediately upon landing, log the 1F overworld coordinates.
  4. Explore the landing zone on 1F and verify if any switches/statues are present.

## Cinnabar Mansion State A Systematic Verification & Safety Protocol (Turn 75752)
- **Objective**: Verify Gate 1, 4, 5, and 2 states under State A (Default) without getting trapped on 1F.
- **Safety Analysis**:
  - In State A (Default), Gate 1 (1F, (25, 13)) is CLOSED. This blocks access to the southern section of 1F's eastern room from the northern entrance.
  - However, Gate 4 (1F, (21, 17)) and Gate 5 (1F, (26, 27)) are hypothesized to be OPEN under State A.
  - If we toggle Statue 2 back to State A on 2F, then walk to 1F:
    - We cannot reach the southern section of 1F's eastern room from the North because Gate 1 is CLOSED.
    - Thus, to verify Gate 4/5 under State A, we must use the **Balcony Fall Spot 1** on 2F East!
    - Under State A, the 2F Gate at (18, 8)-(19, 8) is OPEN. This allows us to walk to 2F East, go through that gate, reach Fall Spot 1, and jump down to 1F.
    - This drops us directly in the southern section of 1F's eastern room, completely bypassing the closed Gate 1!
    - Once we land on 1F, since State A is active, Gate 4 at (21, 17) and Gate 5 at (26, 27) will be OPEN and passable, allowing us to safely explore and verify them on foot!
    - We can then walk through Gate 4 to the West corridor to exit the southern section, meaning we will **never get trapped**!
- **State Matrix Update**: We will record these findings in `Scratchpad/Mansion_Gate_Matrix` by updating the State A column once verified.

## KILN (Magmar L34) Team Integration & Grinding Plan (Turn 75752)
- **Combat Profile**: KILN has high Special and knows Ember. While fire is extremely useful against Grass/Ice/Bug types, GEMMY (BLASTOISE) is already Level 60 and completely outclasses all encounters.
- **Integration Decision**: We will keep KILN in Box 1 as a valuable Fire-type reserve. We do not need to actively switch-train or grind him because BLASTOISE sweeps the Cinnabar Gym with 100% consistency using SURF.
- **Grinding Analysis**: If we ever decide to train KILN, the most optimal overworld area is Cinnabar Island's western water channel or grass fields on Route 21. However, since GEMMY's Surf easily handles Blaine, no grinding is required.

## Cinnabar Mansion Deep B1F Routing & Switch Matrix (Turn 75675)
- **Active Exploration Mission**: Locate and retrieve the Secret Key.
- **Switch Matrix (State A vs. State B)**:
  - We currently have Statue 2 (2F, (2, 11)) in **State A** (Default).
  - This has closed Gate 1 (1F, (25, 13)) but opened Gate 4 (1F, (21, 17)) and Gate 5 (1F, (26, 27)).
  - To reach the basement (B1F), we must find the correct path. Historically, B1F is accessed via a pit on 3F.
  - The Secret Pit is at (11, 12) on 3F. This pit is currently blocked by Gate 2 (Col 11) being CLOSED.

## Cinnabar Gym Blaine Matchup Preparation Strategy
- **Opponent Profile**: Gym Leader Blaine utilizes a Fire-type lineup (typically Growlithe, Ponyta, Rapidash, Arcanine, all around Level 42-47).
- **Type Effectiveness**: Fire is weak to Water, Ground, and Rock (taking 2x damage).
- **GEMMY (Level 59 BLASTOISE) Offensive Plan**:
  - **Priority Move 1: SURF** (Water, Special, Power 95, 100% Accuracy).
    - *Calculation*: Benefitting from same-type attack bonus (STAB), base power becomes 142.5. Against Blaine's Fire-types, it deals 2x super-effective damage, yielding an effective base power of **285** with 100% accuracy.
    - *Utility*: This is our ultimate sweeping move. At Level 59, GEMMY's Special stat will guarantee a one-shot KO on every single member of Blaine's team, entirely eliminating combat RNG.
  - **Priority Move 2: HYDRO PUMP** (Water, Special, Power 120, 80% Accuracy).
    - *Utility*: While even more powerful (effective base power 360), its 80% accuracy introduces unnecessary miss risk. We will only use this if SURF PP is fully depleted.
  - **Priority Move 3: DIG** (Ground, Physical, Power 100, 100% Accuracy).
    - *Utility*: Ground is also 2x super-effective against Fire, but in Gen 1 DIG is a 2-turn move, giving opponents a turn to act or use status moves. SURF is infinitely more efficient.
## 2F East & Row 3 Crossing Corridor Verification (Turn 75910)
- **Socratic Answer**: Crossing horizontally from West to East on Row 7 or 8 is blocked by solid rubble (Columns 23-25, Row 7) and wall (Row 8).
- **The Corridor**: Row 3 (specifically Columns 21-28, Row 3) is the single, continuous horizontal corridor that connects the western and eastern halves of 2F.
- **Routing Effect**:
  - Under State A: We can cross to the Northeast room (Columns 25-28, Rows 3-7) via Row 3, but the Southeast room (containing the stairs at 25, 14) is blocked by the closed gate/wall on Row 8.
  - Under State B: Gate 6 at (9, 4)-(9, 5) is OPEN, allowing us to cross Column 9. We then walk East along Row 3, cross Column 22/23, and since the eastern gate on Row 8 is OPEN under State B, we can walk South to reach the stairs at (25, 14).
- **Live Strategy**: 
  1. Walk back to the 2F stairs at (5, 10) and go down to 1F.
  2. Verify if Gate 4 at (21, 17) and Gate 5 at (26, 27) are OPEN under State A.
  3. Explore 1F South and East under State A.
  4. Return to 2F, go to (2, 11), and toggle Statue 2 to State B.
  5. Go through Gate 6, cross Row 3, walk South to (25, 14), and explore B1F to retrieve the Secret Key.
- **North-East Room Balcony Verification (Turns 76017-76045)**:
  - Hypothesized that we could jump off the balcony in the North-East room (Rows 3-7, Columns 25-28).
  - Standing at (28, 5) facing Right and pressing Right bumped (Turn 76029).
  - Standing at (28, 6) facing Right and pressing Right bumped (Turn 76040).
  - Standing at (28, 7) facing Right and pressing Right bumped (Turn 76043).
  - *Conclusion*: There are no jumpable tiles in the North-East room's balcony (Rows 5-7, Column 28). The balcony ledge is completely solid there.
  - *New Plan*: Since Row 8 is a solid divider (TYPE_2889) between the North-East and South-East rooms on Column 24-28, we cannot walk directly South to the South-East room from here. We must backtrack West through Row 3 (the crossing corridor), then walk South on 2F West, and cross East through Gate 3 at (18, 8)-(19, 8) (which is OPEN under State A) to reach the South-East room where the actual jumpable balcony (Fall Spot 1) and/or stairs to 1F at (25, 14) are located.
- **Column 9 Row 4 & 5 Empirical Collision Boundaries Test (Turns 76079-76086)**:
  - Hypothesized that we could walk through Gate 6 on Row 4 under State B.
  - Successfully moved to (9, 4) on Turn 76081/76086 (TYPE_3fe2 open floor).
  - This verifies that Gate 6's physical collision barrier is OPEN under State B, permitting horizontal crossing of Column 9 along Row 4.
  - Socratic Verification of Gate 6: Since (9, 4) is passable, and Gate 3 is closed (as verified by the bump at (18, 7)), this confirms the active overworld state is **State B**.
- **State A Toggled Verification (Turns 76094-76111)**:
  - *Failed Toggle Attempt (Turn 76094)*: Stood at (3, 11) facing Left and pressed 'A' once. We incorrectly assumed this toggled the switch. However, in Gen 1, Mewtwo statues display a dialogue prompt: "A secret switch! Who wouldn't press it? ▶YES / NO". Pressing 'A' once only opened the textbox; because we walked away without pressing 'A' again to select 'YES', the prompt closed without toggling the switch. The Mansion remained in State B.
  - *Proof of Failure (Turn 76102)*: Walked to Gate 3 at (18, 8) and bumped into it, proving it remained CLOSED and confirming we were still in State B.
  - *Correction Plan (Turn 76111)*: Backtracked to (3, 11) facing Left. We will press 'A' once to trigger the switch text prompt, wait for the YES/NO menu to appear, and press 'A' again to confirm 'YES'. This will successfully change the Mansion to State A.
  - *Post-Toggle Verification Plan*: Once State A is active, we will walk East along Row 11 to Column 10, walk North to Row 3, and walk West to (8, 3) across Column 9 to verify that Row 3 is indeed open and passable under State A (Socratic Question 2). Then we will cross East along Row 3 to 2F East and walk through the newly-opened Gate 3 at (18, 8) to reach the South-East room.
- **Row 3 Column 9 (9, 3) Socratic Verification (Turn 76133)**:
  - *Socratic Question 2 Test*: Stood at (10, 3) and visually analyzed (9, 3).
  - *Result*: (9, 3) is a solid black partition wall tile of TYPE_2889 under State A. It is CLOSED and impassable.
  - *Conclusion*: Row 3 is NOT an open crossing corridor across Column 9. Under State A, Column 9 is completely blocked on Rows 3-9 (since Gate 6 at (9, 4)-(9, 5) is closed and the rest are solid partition walls).
  - *Bypass Method (Row 11)*: Row 11 is a universal, open corridor across Column 9 (9, 11 is open floor TYPE_3fe2 under both State A and B). We successfully crossed Column 9 along Row 11, and then walked North along Column 10 to reach (10, 3).