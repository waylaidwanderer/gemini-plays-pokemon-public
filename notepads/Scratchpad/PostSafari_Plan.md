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
## State B Navigation Plan to 3F East & B1F Access (Turn 76644)
- **Status**: State B (Toggled) is now active.
- **Detailed Step-by-Step Execution Plan**:
  1. **Walk to the 2F West Stairs (7, 10)**:
     - Walk Right to (3, 12).
     - Walk Up to (3, 11).
     - Walk Right 4 steps to (7, 11).
     - Walk Up 1 step to (7, 10) to ascend the stairs to 3F West.
  2. **Navigate to Gate 6 on 3F West (Corrected Detour)**:
     - The stairs land us at (7, 11) on 3F West.
     - Walk Left 5 steps along Row 11 to Column 2: (7, 11) -> (2, 11) (bypassing the solid (7, 7) wall and avoiding the Burglar NPC).
     - Walk North 6 steps along Column 2 to Row 5: (2, 11) -> (2, 5).
     - Walk Right 7 steps along Row 5 to Gate 6: (2, 5) -> (9, 5) (Gate 6 is OPEN under State B).
  3. **Cross Column 11 into 3F East**:
     - Continue Right 3 steps along Row 5 to (12, 5) (Column 11 is open on Row 5, allowing us to cross into the East wing!).
  4. **Drop down the Secret Pit to B1F**:
     - Walk Down 7 steps along Column 12 to (12, 12).
     - Walk Left 1 step to (11, 12) (the Secret Pit).
     - The player will immediately fall down the pit to B1F!
- **Wild Encounter Strategy**:
  - We will use GEMMY (BLASTOISE L60) to sweep or escape any wild encounters using `flee_battle` to keep our team completely healthy.
- **Inventory Check**:
  - We have 11 out of 20 inventory slots filled, leaving 9 empty slots. This is more than enough space for the Secret Key (1 slot) and any other B1F loot. No inventory management is necessary.