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
- **Active State**: In Progress
  - **Current Position**: (20, 6) facing Left (Turn 102971)
- **Boulders Database**:
  - Boulder C1: Initial (22, 3) | Current (3, 5) | Target (3, 5) (Switch C1) | Status: [x] Pressed
  - Boulder C2: Initial (24, 10) | Current (24, 10) | Target (22, 10) (bypasses Column 24 wall) | Status: [ ] Reset to default starting coordinates
  - Boulder C4: Initial (13, 12) | Current (13, 13) | Target (N/A, static/bypass) | Status: [x] Pushed (Turn 102473)
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

## Active Progress & Current Plan (Turn 102961):
- **Current Task**: Re-solved Boulder C1 puzzle (Switch C1 pressed at (3, 5) on Turn 102891). Now walking East along Row 2 to reach Column 27 to descend the ladder at (27, 15) to 2F East.
- **Session Start Turn**: 102872 | State: Active
- **Step-by-Step Plan**:
  1. On 3F East, walk from (17, 5) along the plateau (z=1) via Row 4 West to Column 13, South down Column 13 to Row 13, then East along Row 13 across the plateau to Column 27 to reach the ladder at (27, 15) and descend to 2F East. [In Progress]
  2. On 2F East, walk to (23, 16), push the dropped boulder to (9, 16) to activate Switch B2, opening the exit barrier on 3F East. Then return to (26, 14) and climb back up to 3F East (27, 15). [ ]
  3. Once on 3F East, walk to (26, 8) and descend to 2F East (27, 7). [ ]
  4. From 2F East (27, 7), walk South to the exit cave doorway to emerge onto Route 23/Indigo Plateau. [ ]

## Empirical Bypass Test Session (Turn 101402):
- **Objective**: Test the overwatch agent's hypothesis that Column 29 is a passable bypass corridor on Row 6 connecting Row 2 directly to Row 10 on 3F East.
- **Methodology**: Stood at (28, 2) on 3F East (Map 0_198) and pressed Right on Turn 101401 to attempt to step onto (29, 2) (TYPE_2889).
- **Result**: Direct collision bump (0 tiles visited), remaining at (28, 2) on Turn 101402.
- **Conclusion**: The hypothesis is definitively DISPROVEN. Column 29 is a solid border wall of TYPE_2889. There is no off-screen bypass on Column 29. We must solve the puzzles using the canonical 2F/3F pathways.
- Turn 102482: Verified that pushing Boulder C4 to (13, 13) confirms Column 13 is a dead end below Row 13 due to solid walls at (13, 14) and (13, 15). Backtracking north via Column 13 to Row 1, and heading East to the exit ladder at (26, 8).
- Turn 102695: Standing at (17, 5) on the plateau stairs of Victory Road 3F. We are facing Down. Let's take a step Down to (17, 6) to descend to the ground level of 3F East.
- Verified plan: Descend to (17, 6) and begin our journey to (27, 15) to transition down to 2F East, then walk across the lowered barrier to exit to Route 23/Indigo Plateau.
- Turn 102785: Tested Row 8 passage from (23, 8) to (24, 8) by pressing 'Right'. Hit a solid collision bump and remained at (23, 8). This confirms that the eastern gate on 3F East is closed. The gate is closed because transitioning floors to 2F East on Turn 102767 reset all overworld puzzles, including Switch C1 on 3F West and Switch B2 on 2F East.
- Turn 102790: Updated plan to return to 3F West to solve the 3F West boulder puzzle (Switch C1) again. Then we will proceed with the route.
## Re-solving 3F West Boulder Puzzle (Turn 102872)
- Start Turn: 102872
- Current Position: (5, 2) facing Left
- Boulder C1 Current Position: (4, 2)
- Step-by-Step Execution Plan:
  1. Press Left, Left -> Boulder to (3, 2), Player to (4, 2).
  2. Press Left -> Boulder to (2, 2), Player remains at (4, 2).
  3. Press Left, Up, Left -> Player walks to (2, 1) via (3, 2) and (3, 1).
  4. Press Down, Down, Down, Down, Down -> Boulder to (2, 5), Player to (2, 3).
  5. Press Down, Left, Down -> Player walks to (1, 5) via (2, 4) and (1, 4).
  6. Press Right -> Pushes boulder onto Switch C1 at (3, 5).