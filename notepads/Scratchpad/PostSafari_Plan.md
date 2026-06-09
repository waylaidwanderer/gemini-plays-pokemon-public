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

## Cinnabar Mansion Deep B1F Routing & Switch Matrix (Turn 75675)
- **Active Exploration Mission**: Locate and retrieve the Secret Key.
- **Switch Matrix (State A vs. State B)**:
  - We currently have Statue 2 (2F, (2, 11)) in **State B** (Toggled) on Turn 76255.
  - This has opened Gate 1 (1F, (25, 13)) but closed Gate 4 (1F, (21, 17)) and Gate 5 (1F, (26, 27)).
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
  - *Correction & Toggling (Turn 76111)*: Backtracked to (3, 11) facing Left. We pressed 'A' once to trigger the switch text prompt, selected 'YES' on the prompt, and confirmed. This successfully changed the Mansion's gate network to State A.
  - *Post-Toggle Verification (Turn 76133)*: Once State A was active, we walked East along Row 11 to Column 10, walked North to Row 3, and verified that Row 3 Column 9 at (9, 3) is a solid, impassable wall under State A, meaning Row 11 is the only universal corridor across Column 9.
- **Row 3 Column 9 (9, 3) Socratic Verification (Turn 76133)**:
  - *Socratic Question 2 Test*: Stood at (10, 3) and visually analyzed (9, 3).
  - *Result*: (9, 3) is a solid black partition wall tile of TYPE_2889 under State A. It is CLOSED and impassable.
  - *Conclusion*: Row 3 is NOT an open crossing corridor across Column 9. Under State A, Column 9 is completely blocked on Rows 3-9 (since Gate 6 at (9, 4)-(9, 5) is closed and the rest are solid partition walls).
  - *Bypass Method (Row 11)*: Row 11 is a universal, open corridor across Column 9 (9, 11 is open floor TYPE_3fe2 under both State A and B). We successfully crossed Column 9 along Row 11, and then walked North along Column 10 to reach (10, 3).
- **1F East Stairs Falsification (Turn 76306)**:
  - Hypothesized that there is a staircase at (25, 14) on 1F East South that leads UP to 2F East South.
  - Standing on (25, 14) on Turn 76296-76306 proved that it is a normal floor tile of TYPE_3fe2 with no warp or stairs.
  - Conclusion: There is NO staircase on 1F East. The southeastern staircase only connects 2F East and 3F East. 1F East is only accessed from 2F East via dropping down a balcony/pit, or on foot via Gate 1 under State B. To return to 2F, we must walk back to the southwest stairs at (5, 10) on 1F West.

- **2F East Row 11 Blockage and Row 7 Bypass (Turn 76383)**:
  - Discovered that Row 11 is blocked on the East at Column 13 by solid walls of TYPE_2889 under State A.
  - Visually and physically verified that Row 7 is a completely open, clear horizontal crossing corridor on Columns 10-16 of TYPE_3fe2.
  - Path from (11, 11) to Gate 3: Walk Up 4 steps to (11, 7), walk Right 7 steps to (18, 7), and walk Down 1 step to (18, 8) to cross Gate 3 into 2F East South.

- **Mansion B1F Access & Gate 2 Falsification (Turn 76402)**:
  - *Observation*: Tested (15, 11) on 2F East South on Turn 76394 and found it is a solid decorative table/cabinet of TYPE_2889, NOT a staircase.
  - *Breakthrough*: In vanilla Pokémon Mansion, there is no southeast staircase on 1F or 2F. The only way to reach 3F East is via walking past Gate 2 on 3F Column 11 when it is OPEN under State B.
  - *Falsification of Gate 2 Closed State*: We previously assumed Gate 2 was CLOSED in State B because Column 11 Row 11 is solid. However, Row 11 is a permanent wall on Column 11; the actual open hallway with the gate is on Row 12 or Row 13, which is OPEN under State B!
  - *New Master Plan*:
    1. Backtrack to Statue 2 at (2, 11) on 2F West.
    2. Toggle Statue 2 to State B.
    3. Ascend to 3F West and walk East past Column 11 along Row 12 or Row 13 (which will be OPEN under State B).
    4. Access 3F East, find the Secret Pit at (11, 12), and drop down directly to B1F.
## 2F East Southeast Stairs Hypothesis & Verification (Turn 76508)
- **Hypothesis (Socratic Question 1)**: The southeast staircase at (25, 14) exists on 2F East and connects 2F East South directly to 3F East. Since State A (Default) is active, Gate 3 at (18, 8)-(19, 8) is OPEN, which allows us to walk directly onto 2F East South on foot, locate the stairs at (25, 14), and ascend directly to 3F East (bypassing the closed Gate 2 on 3F West).
- **Testing Protocol**:
  1. From (4, 11) on 2F West, walk East along Row 11 to Column 10.
  2. Walk North along Column 10 to Row 7.
  3. Walk East along Row 7 to Column 18/19.
  4. Walk South through the open Gate 3 at (18, 8) to Row 11.
  5. Walk East from Column 18 to Column 25 on Row 11/12/13/14.
  6. Search the far-southeast corner of 2F East (specifically (25, 14)) for the staircase.
  7. Step onto the staircase to verify if it connects to 3F East.
- **Turn 76550 Progress**:
  - Found that Row 3 Column 19 is blocked by a wall, but Row 4 Columns 20-21 are open, and Row 3 Columns 20-24 are open floor of TYPE_3fe2.
  - Planned route to cross into the eastern wing on 2F under State A: From (19, 4) face Right and walk to (21, 4), then Up to (21, 3), and then East along Row 3 to (24, 3) and further east. This will allow us to see if we can reach the Southeast room and the stairs at (25, 14) on 2F.
- **Turn 76592 Verification & Progress**:
  - We have systematically tested 2F East under State A. We proved that Row 8 is a solid partition wall from Column 22 to 28 (all TYPE_2889), and Row 6-7 Column 28 is blocked/solid as well.
  - *Conclusion*: 2F East South (containing the stairs at (25, 14)) is completely isolated on foot under State A. The stairs at (25, 14) are unreachable on foot.
  - Thus, we are backtracking to 3F West to test Gate 2 at Column 11 under State A.
  - Currently standing at (18, 7) facing UP. We will execute the 11-step movement sequence to reach (11, 11) now.
## Gate 2 (3F Column 11) State A Testing Protocol (Turn 76598)
- **Objective**: Determine if Gate 2 on 3F Column 11 is OPEN or CLOSED under State A (Default).
- **Previous Discovery**: Column 11 Row 11 is a permanent wall, meaning any potential passage must exist on Row 12 or Row 13.
- **Testing Route**:
  1. Ascend from 2F West stairs (7, 10) to 3F West (7, 11).
  2. Walk Down 1 step to (7, 12).
  3. Walk East along Row 12 to (11, 12).
     - **If we bump at Column 11 (standing at (10, 12) facing Right and pressing Right results in a bump)**: This proves the Gate 2 barrier on Row 12 is CLOSED under State A.
     - **If we walk into (11, 12) and fall down the pit to B1F**: This proves Gate 2 on Row 12 is OPEN under State A.
  4. If we bumped on Row 12, walk Down 1 step to (7, 13).
  5. Walk East along Row 13 to (11, 13).
     - **If we bump**: This proves Gate 2 on Row 13 is CLOSED under State A.
     - **If we successfully walk past Column 11 along Row 13 into 3F East**: This proves Gate 2 on Row 13 is OPEN under State A.
- **Documentation**:
  - Once tested, we will update `Scratchpad/Mansion_Gate_Matrix` by filling in the Gate 2 State A cell with the empirical results and turn numbers.