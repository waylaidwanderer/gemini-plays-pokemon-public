# Scratchpad: Victory Road Route & Puzzle States
- Started: Turn 96968 (pre-entry routing)

## Party Overworld HM Dependencies & Readiness:
- **SURF (HM03)**: Known by GEMMY (BLASTOISE) (Slot 1, Level 63). Fully functional.
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
- **Strength Status**: Active: [x] True
- **Current Position**: (8, 9) facing Up (Turn 98461)
- **Boulders Database**:
  - Boulder B1: Initial (5, 5) | Current (5, 5) | Status: Unmoved
  - Boulder B2: Initial (4, 14) | Current (1, 16) | Status: [x] Pushed onto Switch B1
- **Floor Switches**:
  - Switch B1: Coordinate (1, 16) | State: [x] Pressed (secured with Boulder B2)
  - Switch B2: Coordinate (TBD, TBD)

### Victory Road 3F (Map 0_195):
- **Active State**: Unexplored / Initial

## Active Exploration Route & Plan:
- **Goal**: Map 2F Eastern Area, defeat trainers, find Switch B2, and locate the exit ladder.
- **Systematic Verification Path (Turn 98461 onwards)**:
  1. From (8, 9) facing Up, move Up to (8, 8).
  2. Walk East along Row 8 on the elevated plateau past Column 8: (8, 8) -> (9, 8) -> (10, 8) -> (11, 8) -> (12, 8) -> (13, 8).
  3. Engage and defeat Cooltrainer♀ at (11, 5) and Juggler/Super Nerd at (12, 9).
  4. Collect floor item (Pokéball) at (9, 11).
  5. Search for Switch B2 (likely at Y=16 on the east side) to confirm its passability and properties.
  6. Plan push vectors for Boulder B1 at (5, 5) if needed.

## Archive: Completed Pushing Logs
- **Boulder B2 Pushing Log (Switch B1 at 1, 16) [Turn 98419]**:
  - Push 1: Pushed Down from (4, 14) to (4, 15) [Turn 98392]
  - Push 2: Pushed Left from (4, 15) to (3, 15) [Turn 98397]
  - Push 3: Pushed Down from (3, 15) to (3, 16) [Turn 98402]
  - Push 4: Pushed Left from (3, 16) to (2, 16) [Turn 98411]
  - Push 5: Pushed Left from (2, 16) onto Switch B1 at (1, 16) [Turn 98419]

## Socratic 2F Second Barrier & Switch B2 Hypothesis:
- **Observation**: A second closed barrier gate of TYPE_de37 is located at (23, 14), directly blocking the ladder/stairs at (23, 15) in the southeast corner.
- **Hypothesis**: The gate at (23, 14) is controlled by a second floor switch (Switch B2) on the eastern side. Boulder B1, located at (5, 5) on the ground level, must be pushed onto Switch B2 to lower this gate and unlock access to the exit ladder at (23, 15), which likely leads to 3F.
- **Verification Plan**:
  1. Complete the battle with Juggler at (21, 13).
  2. Locate the stairs/ladder leading down from the plateau on the east side (potentially at (15, 15) or (21, 15)).
  3. Walk down to the eastern ground floor (lower level, TYPE_3fe2) and systematically explore Columns 13 to 23 on Rows 11 to 16.
  4. Search for Switch B2 (empty plate, likely TYPE_eb90) and record its exact coordinates.
  5. Search for the items at (9, 11) and (18, 9).
  6. Return to Boulder B1 at (5, 5) and plan a safe, non-blocking push vector to navigate it to Switch B2.

## Eastern Ground Floor Exploration & Switch B2 Discovery:
- **Turn 98524**: Definitively located and verified Switch B2 at **(9, 16)** (TYPE_eb90, empty plate on ground level).
- **Plateau Stairs**: Verified stairs connecting the plateau and eastern ground floor at **(21, 15)** (TYPE_4b8d) and **(15, 15)** (TYPE_4b8d).
- **Ground Floor Passages**: Ground floor has continuous tall grass on Rows 16 & 17, and a vertical passage running North-South on Columns 9, 10, 11 (Rows 11-15 are all TYPE_3fe2).
- **Defeated Trainers**:
  - Defeated Juggler at **(21, 13)** (Turn 98497). Defined map marker.
  - Defeated Black Belt at **(9, 9)** (Turn 98453). Defined map marker.