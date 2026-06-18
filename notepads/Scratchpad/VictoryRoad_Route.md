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
  - **Current Position**: (4, 3) facing Up (Turn 101823)
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
  2. Avoid fighting wild encounters by running (flee_battle) to conserve remaining Surf (8 PP), Hydro Pump (5 PP), and Earthquake (4 PP).
  3. Once we reach Indigo Plateau, heal the entire team at the Pokémon Center, restoring all HP and PP (including Blizzard) to full, and retrieve any needed items from the PC before entering the Elite Four lobby.
- **Gemmy's Remaining PP Limits (Turn 100329)**:
  - Surf: 8/15 PP
  - Hydro Pump: 5/5 PP
  - Earthquake: 4/10 PP
  - Blizzard: 0/5 PP (Strategic reserve: will heal at Indigo Plateau PC)

## Active Progress & Current Plan (Turn 101821):
- **Current Task**: Defeat the trainer at (4, 2) on 2F West and push Boulder B1.
- **Session Start Turn**: 101520 | State: Active
- **Step-by-Step Plan**:
  1. Defeat the trainer at (4, 2) on 2F West. [In Progress]
  2. Walk to (5, 4) (1 step Right, 1 step Down), standing directly above Boulder B1 at (5, 5).
  3. Manually activate STRENGTH from the POKéMON party menu using ROCKY (GEODUDE).
  4. Push Boulder B1 at (5, 5) DOWN along Column 5 to (5, 6) to open the path south.
  5. Walk onto (5, 5) and walk south to the ladder to 3F West at (0, 8) or nearby.
  6. Climb the ladder UP to 3F West (lands us on the southern plateau of 3F West).
  7. Walk to the stairs at (1, 9) on 3F West and descend to the southern ground level of 3F West at (1, 10).
  8. Walk to the south side of Boulder C4 at (13, 13).
  9. Push Boulder C4 UP from (13, 12) to (13, 6) to clear Column 13.
  10. Walk to the pit hole at (23, 15) and step in to jump down to 2F East ground floor (23, 16).
  11. Climb the eastern stairs on 2F East from (21, 15) UP to Row 14, walk to Column 27 on the plateau, and walk Up to the ladder at (27, 7).
  12. Climb the ladder at (27, 7) to warp up to 3F East at (26, 8) (the southeastern pocket!).
  13. Walk to (25, 10), standing right of the second boulder at (24, 10).
  14. Push the second boulder Left to (22, 10).
  15. Stand at (22, 9) and push the second boulder Down along Column 22 to (22, 15) (where it falls off the plateau's southern edge).
  16. Walk to (21, 14) on the plateau, and walk Down to jump South over the cliff edge onto (21, 15) on the ground level.
  17. Stand at (21, 15) and push the boulder Right into the pit hole at (23, 15).
  18. Walk into the pit hole at (23, 15) to land on 2F's ground floor at (23, 16).
  19. Push the dropped boulder West along Row 16 to Switch B2 at (9, 16) to open the northeast barrier on 2F.
  20. Climb the eastern stairs at (21, 15) UP to Row 14 on 2F, walk to Column 27 on the plateau, and walk Up through the opened northeast barrier to the ladder at (27, 7).
  21. Climb the ladder to 3F East (26, 8).
  22. Walk to 3F West and push the first boulder C1 from (22, 3) onto Switch C1 at (3, 5).
  23. Walk to the exit at the top right of 3F East to reach Indigo Plateau!

## Empirical Bypass Test Session (Turn 101402):
- **Objective**: Test the overwatch agent's hypothesis that Column 29 is a passable bypass corridor on Row 6 connecting Row 2 directly to Row 10 on 3F East.
- **Methodology**: Stood at (28, 2) on 3F East (Map 0_198) and pressed Right on Turn 101401 to attempt to step onto (29, 2) (TYPE_2889).
- **Result**: Direct collision bump (0 tiles visited), remaining at (28, 2) on Turn 101402.
- **Conclusion**: The hypothesis is definitively DISPROVEN. Column 29 is a solid border wall of TYPE_2889. There is no off-screen bypass on Column 29. We must solve the puzzles using the canonical 2F/3F pathways.