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

### Victory Road 2F Map (Map 0_194):
- **Active State**: In Progress
  - **Current Position**: (16, 16) facing Left (Turn 102069)
- **Strength Status**: Active: [x] True (Activated Turn 102004)

### Victory Road 2F Boulders & Switches:
- **Boulders Database**:
  - Boulder B1: Initial (5, 5) | Current (5, 5) | Status: Unmoved
  - Boulder B2: Initial (4, 14) | Current (4, 14) | Status: Unmoved
  - Dropped Boulder: Initial (23, 16) | Current (14, 16) | Status: [ ] Reset back to landing coordinates (Default position)
- **Floor Switches**:
  - Switch B1: Coordinate (1, 16) | State: Unpressed [ ]
  - Switch B2: Coordinate (9, 16) | State: [ ] Unpressed (boulder reset)

### Victory Road 3F Map (Map 0_198):
- **Active State**: In Progress
  - **Current Position**: (2, 2) facing Down (Turn 101800)
- **Boulders Database**:
  - Boulder C1: Initial (22, 3) | Current (22, 3) | Target (3, 5) (Switch C1) | Status: [ ] Reset (Turn 101726 warp transition)
  - Boulder C2: Initial (24, 10) | Current (24, 10) | Target (23, 15) (Pit Hole)
  - Boulder C4: Initial (13, 12) | Current (13, 12) | Target (N/A, static/bypass)
- **Floor Switches & Holes**:
  - Pit Hole: Coordinate (23, 15) | State: Open [x] (verified on Turn 100130, boulder dropped through)
  - Switch C1: Coordinate (3, 5) | State: Unpressed [ ]

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

## Active Progress & Current Plan (Turn 102003):
- **Current Task**: Activate Strength and push the boulder West along Row 16.
- **Session Start Turn**: 101520 | State: Active
- **Step-by-Step Plan**:
  1. Defeat the trainer at (4, 2) on 2F West. [x] Completed (Turn 101816)
  2. Walk to (5, 4) (1 step Right, 1 step Down), standing directly above Boulder B1 at (5, 5). [x] Completed (Turn 101844)
  3. Manually activate STRENGTH from the POKéMON party menu using ROCKY (GEODUDE). [x] Completed (Turn 101850)
  4. Push Boulder B1 at (5, 5) DOWN along Column 5 to (5, 6) to open the path south. [x] Completed (Turn 101860)
  5. Climb stairs at (5, 10) to access the 2F West plateau. [x] Completed (Turn 101908)
  6. Walk along the plateau Eastward to the eastern stairs at (21, 15). [x] Completed (Turn 101977)
  7. Descend stairs at (21, 15) to 2F East ground area. [x] Completed (Turn 101978)
  8. Walk around the boulder to stand at (24, 16). [x] Completed (Turn 101989)
  9. Activate STRENGTH and push the boulder at (23, 16) West along Row 16 to Switch B2 at (9, 16). [In Progress]

## Empirical Bypass Test Session (Turn 101402):
- **Objective**: Test the overwatch agent's hypothesis that Column 29 is a passable bypass corridor on Row 6 connecting Row 2 directly to Row 10 on 3F East.
- **Methodology**: Stood at (28, 2) on 3F East (Map 0_198) and pressed Right on Turn 101401 to attempt to step onto (29, 2) (TYPE_2889).
- **Result**: Direct collision bump (0 tiles visited), remaining at (28, 2) on Turn 101402.
- **Conclusion**: The hypothesis is definitively DISPROVEN. Column 29 is a solid border wall of TYPE_2889. There is no off-screen bypass on Column 29. We must solve the puzzles using the canonical 2F/3F pathways.