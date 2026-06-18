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
  - **Current Position**: (23, 8) facing Right (Turn 103387)
- **Boulders Database**:
  - Boulder C1: Initial (22, 3) | Current (3, 5) | Target (3, 5) (Switch C1) | Status: [x] Active (secured with Switch C1)
  - Boulder C2: Initial (24, 10) | Current (24, 10) | Target (22, 10) (bypasses Column 24 wall) | Status: [ ] Reset to default starting coordinates
  - Boulder C4: Initial (13, 12) | Current (13, 12) | Target (N/A, static/bypass) | Status: [ ] Reset to default starting coordinates
- **Floor Switches & Holes**:
  - Pit Hole: Coordinate (23, 15) | State: Open [x] (verified on Turn 100130, boulder dropped through)
  - Switch C1: Coordinate (3, 5) | State: Pressed [x]

### Victory Road 2F Map (Map 0_194):
- **Active State**: In Progress
  - **Current Position**: (23, 11) facing Down (Turn 102524)
- **Strength Status**: Active: [ ] False (Deactivated due to floor transition)
- **Boulders Database**:
  - Switch B2: Coordinate (9, 16) | State: Unpressed [ ] (Reset due to floor transition)

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

## Active Progress & Current Plan (Turn 103172):
- **Current Task**: Traversing 3F East to execute the C2 Boulder Puzzle and fall through the pit hole at (23, 15).
- **Session Start Turn**: 102872 | State: Active
- **Step-by-Step Plan**:
  1. Walk East via Row 2 to 3F East (ground level) and walk Down to standing at (25, 10). [ ]
  2. Stand at (25, 10) and push Boulder C2 Left to (22, 10) to clear Column 23 on Row 10. [ ]
  3. Walk Down Column 23 and step into the open pit hole at (23, 15) to fall down to 2F East. [ ]
  4. On 2F East (ground floor), walk to (23, 16) and push the dropped boulder all the way West along Row 16 to Switch B2 at (9, 16) to permanently lower all barriers. [ ]
  5. Walk East to the plateau stairs at (21, 15), climb up, and take the ladder at (26, 14) back up to 3F East (27, 15). [ ]
  6. On 3F East, walk to (26, 8) and descend the ladder to 2F East (27, 7). [ ]
  7. From 2F East (27, 7), walk South to the exit cave doorway to emerge onto Route 23/Indigo Plateau. [ ]

## Empirical Bypass Test Session (Turn 101402):
- **Objective**: Test the overwatch agent's hypothesis that Column 29 is a passable bypass corridor on Row 6 connecting Row 2 directly to Row 10 on 3F East.
- **Methodology**: Stood at (28, 2) on 3F East (Map 0_198) and pressed Right on Turn 101401 to attempt to step onto (29, 2) (TYPE_2889).
- **Result**: Direct collision bump (0 tiles visited), remaining at (28, 2) on Turn 101402.
- **Conclusion**: The hypothesis is definitively DISPROVEN. Column 29 is a solid border wall of TYPE_2889. There is no off-screen bypass on Column 29. We must solve the puzzles using the canonical 2F/3F pathways.

## Empirical Gate Test Log:
- **Turn 103381**: Tested the passability of the Row 8 gate at (24, 8) by standing at (22, 8) and pressing Right, Right.
- **Result**: Player moved to (23, 8) on the first press, and bumped against (24, 8) on the second press (Game State on Turn 103386 shows player at (23, 8) facing Right).
- **Conclusion**: The Row 8 gate at (24, 8) is definitively CLOSED and impassable. Bypassing it via the Row 2/3 northern corridor and Column 28 is strictly mandatory to reach the C2 boulder on the East side.
## Boulder Reset & Realignment (Turn 103405):
- Visually verified that taking the ladder at (27, 7) on 2F East transitions back to (23, 7) on 3F East (Map 0_198).
- This map transition has completely reset all boulders on 3F East:
  - Boulder C1 has returned to (22, 3).
  - Boulder C2 has returned to (24, 10).
- Since we are standing at (23, 7) on 3F East, we can walk directly west and go back to 3F West.
- We must re-solve the 3F West Boulder C1 Puzzle by pushing the boulder at (22, 3) onto Switch C1 at (3, 5).
- After re-solving the C1 puzzle, we can walk back east to 3F East, proceed to the east side via the northern Row 2 corridor, and execute the Boulder C2 puzzle.
- Current location: (23, 7). Path to (22, 4) is ['Left', 'Up', 'Up', 'Up']. Let's execute these steps to align south of Boulder C1.