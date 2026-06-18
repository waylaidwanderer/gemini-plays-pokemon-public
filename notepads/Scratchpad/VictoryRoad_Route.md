# Scratchpad: Victory Road Route & Puzzle States
- Started: Turn 96968 (pre-entry routing)

## Party Overworld HM Dependencies & Readiness:
- **SURF (HM03)**: Known by GEMMY (BLASTOISE) (Slot 1, Level 64). Fully functional.
- **STRENGTH (HM04)**: Known by ROCKY (GEODUDE) (Slot 2, Level 15). Fully functional.
- **FLY (HM02)**: Known by BIRBIE (PIDGEOTTO) (Slot 3, Level 18). Fainted but overworld FLY is usable!
- **CUT (HM01)**: Known by PETAL (BELLSPROUT) (Slot 6, Level 13). Fully functional.

## Puzzle Mechanics & Reset Rules (Generation 1):
- **Strength Deactivation**: Moving through stairs/warp transitions completely deactivates the active overworld STRENGTH state. It MUST be manually reactivated from the POKéMON menu upon entering a new floor.
- **Boulder Position Reset**: Transitioning between maps/floors or using DIG/Escape Rope completely resets all boulders on all floors back to their default starting coordinates.
- **Switch Retention**: Standing off a switch usually resets it, but some permanent switches (like plates that open gates) stay pressed once the boulder is pushed onto them. If we leave the floor, they reset.

## Puzzle State Log:

### Victory Road 1F (Map 0_108):
- **Active State**: Completed (Boulder on Switch)
- **Boulders Database**:
  - Boulder A: Initial (5, 15) | Current (17, 13) | Target (17, 13) | Status: [x] Active (secured with Switch A)
  - Boulder A2: Initial (14, 2) | Current (10, 2) | Target (10, 2) | Status: [ ] Active

### Victory Road 3F Map (Map 0_198):
- **Active State**: Completed (Boulder C1 on Switch)
  - **Current Position**: (20, 5) facing Down (Turn 103561)
- **Boulders Database**:
  - Boulder C1: Initial (22, 3) | Current (3, 5) | Target (3, 5) (Switch C1) | Status: [x] Active (secured with Switch C1)
  - Boulder C2: Initial (24, 10) | Current (24, 10) | Target (22, 10) (bypasses Column 24 wall) | Status: [ ] Reset
  - Boulder C4: Initial (13, 12) | Current (13, 12) | Target (N/A, static/bypass) | Status: [ ] Reset
- **Floor Switches & Holes**:
  - Pit Hole: Coordinate (23, 15) | State: Open [x] (verified on Turn 100130, boulder dropped through)
  - Switch C1: Coordinate (3, 5) | State: Pressed [x]

### Victory Road 2F Map (Map 0_194):
- **Active State**: Completed (Boulder on Switch B2)
  - **Current Position**: (10, 16) facing Left (Turn 103681)
- **Strength Status**: Active: [x] True
- **Boulders Database**:
  - Switch B2: Coordinate (9, 16) | State: Pressed [x] (Solved on Turn 103671)

### Empirical Push Test Failure & Pivot Log (Turn 99693):
- **Verification of Failure**: On Turn 99678, with Boulder C1 resting on Switch C1 at (3, 5), the player attempted to push Boulder C3 at (7, 7) southwards from (7, 6). The push failed due to a solid collision bump, and tiles (7, 8) and (7, 9) remain TYPE_2889 rock walls.
- **Conclusion**: Switch C1 at (3, 5) does NOT open the Column 7 gates. Its function is elsewhere, likely lowering a barrier on the East or Northeast side of 3F.
- **Active Strategy**: Pivot immediately to Contingency A. Walk East along the Row 1 corridor to investigate if any eastern or northeast barrier was lowered, or if there is another switch/trigger on the East side.
## Elite Four & Champion Preparation Plan (Blizzard PP Strategic Response - Turn 100193):
- **Observation**: GEMMY (BLASTOISE) has 0 PP remaining on Blizzard, which is our prime move for sweeping dragons.
- **Strategic Constraint**: DIG/FLY/Escape Rope to heal at a Pokémon Center or retrieve MAX ETHER from the PC will completely reset all solved boulder puzzles on 1F, 2F, and 3F, forcing us to redo them.
- **Strategic Plan**:
  1. Complete the 2F boulder puzzle and Victory Road to reach Indigo Plateau without leaving.
  2. Avoid fighting wild encounters by running (flee_battle) to conserve remaining Surf (5 PP), Hydro Pump (5 PP), and Earthquake (3 PP).
  3. Once we reach Indigo Plateau, heal the entire team at the Pokémon Center, restoring all HP and PP (including Blizzard) to full, and retrieve any needed items from the PC before entering the Elite Four lobby.
- **Gemmy's Remaining PP Limits (Turn 102031)**:
  - Surf: 5/15 PP
  - Hydro Pump: 5/5 PP
  - Earthquake: 3/10 PP
  - Blizzard: 0/5 PP (Strategic reserve: will heal at Indigo Plateau PC)

## Active Progress & Current Plan (Turn 103655):
- **Current Task**: Falling through 3F East Pit Hole to Solve 2F Switch B2 Puzzle.
- **Session Start Turn**: 103416 | State: Active
- **Step-by-Step Plan**:
  1. Activate STRENGTH and push Boulder C1 at (22, 3) onto Switch C1 at (3, 5). [x] (Completed on Turn 103493)
  2. Navigate 3F East to the (23, 7) ladder and descend to 2F East. [x] (Completed on Turn 103572)
  3. Walk around the (23, 16) boulder via Row 17 to reach the East stairs at (21, 15). [x] (Completed on Turn 103625)
  4. Climb UP onto the plateau and take the (25, 14) ladder to 3F East (27, 15). [x] (Completed on Turn 103630)
  5. Stand at (25, 10), activate STRENGTH, and push Boulder C2 Left to (22, 10). [x] (Completed on Turn 103645)
  6. Walk to (23, 15) and fall through the pit hole to 2F East (the boulder was already dropped in a previous attempt). [ ]

## Empirical Bypass Test Session (Turn 101402):
- **Objective**: Test the overwatch agent's hypothesis that Column 29 is a passable bypass corridor on Row 6 connecting Row 2 directly to Row 10 on 3F East.
- **Methodology**: Stood at (28, 2) on 3F East (Map 0_198) and pressed Right on Turn 101401 to attempt to step onto (29, 2) (TYPE_2889).
- **Result**: Direct collision bump (0 tiles visited), remaining at (28, 2) on Turn 101402.
- **Conclusion**: The hypothesis is definitively DISPROVEN. Column 29 is a solid border wall of TYPE_2889. There is no off-screen bypass on Column 29. We must solve the puzzles using the canonical 2F/3F pathways.
## Empirical Passability Hypothesis & Test Protocol (Turn 103531):
- **Hypothesis**: The northern detour to reach the East side of 3F East (Column 25 and above) on foot relies on Column 28 being a passable vertical corridor.
- **Testing Method**: Walked along Row 1/2 to Column 28, then down to (28, 3).
- **Result**: On Turn 103531, visually confirmed on screen that Row 6 is completely blocked by solid rock walls of TYPE_2889 across Columns 24-29. Specifically:
  - (24, 6): TYPE_2889
  - (25, 6): TYPE_2889
  - (26, 6): TYPE_2889
  - (27, 6): TYPE_2889
  - (28, 6): TYPE_2889
  - (29, 6): TYPE_2889
- **Conclusion**: The hypothesis is definitively DISPROVEN. There is no foot passage from the northern Row 1/2 corridor to the southern half on the eastern side.
- **Active Strategy**: Pivot to falling through the (23, 15) pit hole. We must check if Column 22 or any other path can lead us south past Row 9 on the west-center side of 3F East.