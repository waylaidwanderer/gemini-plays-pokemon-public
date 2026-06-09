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
  - We currently have Statue 2 (2F, (2, 11)) in **State B** (Toggled).
  - This has opened Gate 1 (1F, (25, 13)) but closed Gate 4 (1F, (21, 17)) and Gate 5 (1F, (26, 27)).
  - To reach the basement (B1F), we must find the correct path. Historically, B1F is accessed via a pit on 3F.
  - The Secret Pit is at (11, 12) on 3F. This pit is currently blocked by Gate 2 (Col 11) being CLOSED.
  - Wait! To open Gate 2 on 3F, we need to find Statue 3 on 3F Left!
  - We are currently on 3F. We must systematically search 3F Left (southwest and northwest chambers) to find Statue 3 and toggle it.

## Empirical Badge Boost Audit PC Navigation Protocol (Turn 75700)
- **Objective**: Safely deposit BUGGY (Butterfree) and withdraw SLUDGY (Muk, Level 39) or KILN (Magmar, Level 34) to conduct the Badge-Boost Multiplier Empirical Audit.
- **PC Navigation Sequence (Cinnabar PC, standing at (4, 3) facing Up)**:
  1. Press 'A' to boot up GEM's PC.
  2. Select `BILL'S PC` (cursor starts on it, press 'A').
  3. Select `DEPOSIT PKMN` (press Down once, then 'A').
  4. In the party list, navigate to BUGGY (index 4):
     - Press Down 3 times (moves from SPARKY -> ROCKY -> BIRBIE -> BUGGY).
     - **CRITICAL**: Confirm the cursor is pointing at BUGGY and NOT GEMMY (index 5).
     - Press 'A' to deposit BUGGY.
  5. Select `WITHDRAW PKMN` (press Up once from Deposit PKMN, or press 'A' on Withdraw PKMN).
  6. In Box 1, locate SLUDGY (Muk, Level 39) at index 2 or KILN (Magmar, Level 34) at index 1:
     - To withdraw KILN: The cursor starts on index 1 (KILN). Press 'A'.
     - To withdraw SLUDGY: The cursor starts on index 1 (KILN). Press Down once to reach index 2 (SLUDGY). Press 'A'.
  7. Select `SEE YA!` to log off and exit the PC.

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