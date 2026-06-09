# Post-Safari Zone Route & Progression Plan

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
## State B Navigation Plan to 3F East & B1F Access (Turn 76644)
- **Status**: We are standing at (2, 12) facing UP in front of Mewtwo Statue 2. We are about to toggle the switch to State B.
- **Detailed Step-by-Step Execution Plan once State B is active**:
  1. **Interact with Statue 2**: Press 'A', then select 'YES' to change the gate network to State B.
  2. **Walk to the 2F West Stairs (7, 10)**:
     - Walk Right to (3, 12).
     - Walk Up to (3, 11).
     - Walk Right 4 steps to (7, 11).
     - Walk Up 1 step to (7, 10) to ascend the stairs to 3F West.
  3. **Navigate to Gate 6 on 3F West**:
     - The stairs land us at (7, 11) on 3F West.
     - Walk Up 6 steps to (7, 5) (Column 7 is verified 100% open on Rows 5-11).
     - Walk Right 2 steps to (9, 5) (cross Column 9 through Gate 6, which is OPEN under State B).
  4. **Cross Column 11 into 3F East**:
     - Continue Right 3 steps to (12, 5) (Column 11 is open on Row 5, allowing us to cross into the East wing!).
  5. **Drop down the Secret Pit to B1F**:
     - Walk Down 7 steps along Column 12 to (12, 12).
     - Walk Left 1 step to (11, 12) (the Secret Pit).
     - The player will immediately fall down the pit to B1F!
- **Wild Encounter Strategy**:
  - We will use GEMMY (BLASTOISE L60) to sweep or escape any wild encounters using `flee_battle` to keep our team completely healthy.
- **Inventory Check**:
  - We have 11 out of 20 inventory slots filled, leaving 9 empty slots. This is more than enough space for the Secret Key (1 slot) and any other B1F loot. No inventory management is necessary.