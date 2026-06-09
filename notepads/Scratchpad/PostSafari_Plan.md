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
## State B Navigation Plan to 3F East & B1F Access (Turn 76684)
- **Status**: State B (Toggled) is active. We verified on 3F West that Row 7 and Column 2 are blocked by solid bookcase walls, making 3F East unreachable via 3F West. We must use the 2F East detour.
- **Detailed Step-by-Step Execution Plan**:
  1. **Descend back to 2F West**:
     - From (3, 13), walk Right 2 to (5, 13).
     - Walk Up 3 to (5, 10).
     - Walk Right 2 to (7, 10) and take the stairs down to 2F West (arriving at 7, 10).
  2. **Cross to 2F East via Column 10**:
     - From (7, 10) on 2F West, walk Left 2 to (5, 10) (do not step on (5, 10) as it is the stairs to 1F). Actually, walk to (5, 11) or (10, 11) on Row 11.
     - Specifically, from (7, 10), step Down 1 to (7, 11).
     - Walk Right 3 to (10, 11).
     - Walk Up 6 along Column 10 to (10, 5).
     - Walk Right along Rows 1-5 to Column 14.
  3. **Reach southeast stairs at (25, 14) on 2F East**:
     - Cross Column 15 on Row 6: walk Down to (14, 6), Right to (15, 6) (test if passable), and Right to (17, 6).
     - Walk East/North to the Northeast room.
     - Test if Column 25 Row 8 ("Gate E") is open under State B. If open, walk South to the Southeast room.
     - Take the stairs at (25, 14) up to 3F East.
  4. **Drop down the Secret Pit on 3F East to B1F**:
     - On 3F East, walk to Column 12 Row 12: (12, 12).
     - Step Left 1 to (11, 12) (the Secret Pit) to drop down to B1F!
- **Wild Encounter Strategy**:
  - We will use GEMMY (BLASTOISE L60) to sweep or escape any wild encounters using `flee_battle` to keep our team completely healthy.
- **Inventory Check**:
  - We have 11 out of 20 inventory slots filled, leaving 9 empty slots. This is more than enough space for the Secret Key (1 slot) and any other B1F loot. No inventory management is necessary.