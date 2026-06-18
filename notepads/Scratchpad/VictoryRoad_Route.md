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
  - **Current Position**: (23, 7) facing Down (Turn 101380)
- **Strength Status**: Active: [ ] False

### Victory Road 2F Boulders & Switches:
- **Boulders Database**:
  - Boulder B1: Initial (5, 5) | Current (5, 5) | Status: Unmoved
  - Boulder B2: Initial (4, 14) | Current (1, 16) | Status: [x] Pushed onto Switch B1
  - Dropped Boulder: Initial (23, 16) | Current (23, 16) | Status: [ ] Reset back to landing coordinates (Default position)
- **Floor Switches**:
  - Switch B1: Coordinate (1, 16) | State: [x] Pressed (secured with Boulder B2)
  - Switch B2: Coordinate (9, 16) | State: [ ] Unpressed (boulder reset)

### Victory Road 3F Map (Map 0_198):
- **Active State**: In Progress
  - **Current Position**: (23, 2) facing Left (Turn 101405)
- **Boulders Database**:
  - Boulder C1: Initial (22, 3) | Current (22, 3) | Target (3, 5) (Switch C1) | Status: [ ] Reset (Need to push again)
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
  2. Avoid fighting wild encounters by running (flee_battle) to conserve remaining Surf (8 PP), Hydro Pump (5 PP), and Earthquake (4 PP).
  3. Once we reach Indigo Plateau, heal the entire team at the Pokémon Center, restoring all HP and PP (including Blizzard) to full, and retrieve any needed items from the PC before entering the Elite Four lobby.
- **Gemmy's Remaining PP Limits (Turn 100329)**:
  - Surf: 8/15 PP
  - Hydro Pump: 5/5 PP
  - Earthquake: 4/10 PP
  - Blizzard: 0/5 PP (Strategic reserve: will heal at Indigo Plateau PC)

## Active Progress & Current Plan (Turn 101340):
- **Current Task**: Return East to the second boulder C2 at (24, 10) to solve the double-push puzzle.
- **Step-by-Step Plan**:
  1. Push the first boulder from (22, 3) to Switch C1 at (3, 5). [x] Completed (Turn 101301)
  2. Walk back to (23, 7) on 3F East plateau. [ ] In Progress (Currently at 26, 2, session start Turn 101315)
  3. Stand to the right of the second boulder at (24, 10), and push it Left to (22, 10).
  4. Stand at (22, 9) and push the second boulder Down along Column 22 to (22, 15) (which falls off the plateau's southern edge).
  5. Walk to (21, 14) on the plateau, and walk Down to jump South over the cliff edge onto (21, 15) on the ground level.
  6. Stand at (21, 15) and push the boulder Right into the pit hole at (23, 15).
  7. Walk into the pit hole at (23, 15) to land on 2F's ground floor at (23, 16).
  8. Push the dropped boulder West along Row 16 to Switch B2 at (9, 16) to open the northeast barrier on 2F.
  9. Climb the eastern stairs at (21, 15) UP to Row 14, walk to Column 27 on the plateau, and walk Up through the opened northeast barrier to the ladder at (27, 7).
  10. Climb the ladder to 3F East (26, 8) and walk to the exit at the top right of 3F to reach Indigo Plateau!
- **Session Start Turn**: 101370 | Timestamp: Wednesday June 17, 2026 7:35 PM PDT (Time-blindness protection active)
- Turn 101063: Tested walking Down from (21, 11) [z=1] to (21, 12) [z=0]. Result: Bumped (0 tiles visited), remaining at (21, 11). This empirically proves that the transition from Row 11 (red checkered) to Row 12 (purple) is a solid height mismatch barrier on Column 21 as well, and we cannot descend directly to the purple floor on the east side on foot. We must walk West on the red checkered floor (Row 11) to find the correct descent path.

### Active Column 13 Passability Test Session
- **Session Start Turn**: 101100 | Timestamp: Wednesday June 17, 2026 5:17 PM PDT
- **Objective**: Walk Down Column 13 from Row 7 to Row 15 on 3F, systematically testing and documenting the passability of every single row to verify if it connects directly to Row 15 corridor on foot.
- **Passability Database (3F Column 13)**:
  - (13, 7): [x] Passable (Starting Point)
  - (13, 8): [x] Passable (Turn 101107)
  - (13, 9): [x] Passable (Turn 101109)
  - (13, 10): [x] Passable (Turn 101109)
  - (13, 11): [x] Passable (Turn 101110)
  - (13, 12): [ ] Occupied by Boulder C4 (Default position)
  - (13, 13): [x] Passable floor (Visually verified)
  - (13, 14): [ ] IMPASSABLE - Solid rock wall (TYPE_2889, Visually verified on Turn 101114)
  - (13, 15): [ ] IMPASSABLE - Solid rock wall (TYPE_2889, Visually verified on Turn 101114)
- **Conclusion**: Column 13 is a 100% verified dead end below Row 13. Horizontal bypass on Row 12 is blocked by walls on both sides ((12, 12) and (14, 12) are TYPE_2889). We cannot go south on foot from 3F West without solving the 2F puzzle to open the northeast barrier. We must backtrack to 2F immediately.

## Empirical Bypass Test Session (Turn 101402):
- **Objective**: Test the overwatch agent's hypothesis that Column 29 is a passable bypass corridor on Row 6 connecting Row 2 directly to Row 10 on 3F East.
- **Methodology**: Stood at (28, 2) on 3F East (Map 0_198) and pressed Right on Turn 101401 to attempt to step onto (29, 2) (TYPE_2889).
- **Result**: Direct collision bump (0 tiles visited), remaining at (28, 2) on Turn 101402.
- **Conclusion**: The hypothesis is definitively DISPROVEN. Column 29 is a solid border wall of TYPE_2889. There is no off-screen bypass on Column 29. We must solve the puzzles using the canonical 2F/3F pathways.