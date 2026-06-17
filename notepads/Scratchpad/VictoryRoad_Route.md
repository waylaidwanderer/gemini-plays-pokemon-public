# Scratchpad: Victory Road Route & Puzzle States
- Started: Turn 96968 (pre-entry routing)
- Goal: Navigate Victory Road, solve boulder puzzles, and reach Indigo Plateau.

## Party Overworld HM Dependencies & Readiness:
- **SURF (HM03)**: Known by GEMMY (BLASTOISE) (Slot 1, Level 63). Fully functional.
- **STRENGTH (HM04)**: Known by ROCKY (GEODUDE) (Slot 2, Level 15). Fully functional.
- **FLY (HM02)**: Known by BIRBIE (PIDGEOTTO) (Slot 3, Level 18). Note: Birbie is currently fainted (0/55 HP), but overworld FLY remains fully usable!
- **CUT (HM01)**: Known by PETAL (BELLSPROUT) (Slot 6, Level 13). Fully functional.

## Puzzle Mechanics & Reset Rules (Generation 1):
- **Strength Deactivation**: Moving through stairs/warp transitions completely deactivates the active overworld STRENGTH state. It MUST be manually reactivated from the POKéMON menu upon entering a new floor.
- **Boulder Position Reset**: Transitioning between maps/floors or using DIG/Escape Rope completely resets all boulders on all floors back to their default starting coordinates.
- **Switch Retention**: Standing off a switch usually resets it, but some permanent switches (like plates that open gates) stay pressed once the boulder is pushed onto them. If we leave the floor, they reset.

## Puzzle State Log:

### Victory Road 1F (Map 0_108):
- **Active State**: Completed (Boulder on Switch)
- **Boulders Database**:
  - Boulder A: Initial (5, 15) | Current (17, 13) | Target (17, 13) | Status: [x] Active
- **Floor Switches**:
  - Switch A: Coordinate (17, 13) | State: [x] Pressed (secured with Boulder A)
- **Verified Switch A Pushing Route**:
  - Successfully guided Boulder A via Rows 16, 17, 14, and 12, culminating in a downward push from (17, 11) onto (17, 13).

### Victory Road 2F:
- **Active State**: Unexplored / Initial
- **Boulders Database**:
  - Boulder B: Initial (TBD, TBD) | Current (TBD, TBD) | Target (TBD, TBD) | Status: [ ] Active
- **Floor Switches**:
  - Switch B: Coordinate (TBD, TBD) | State: [ ] Pressed (requires Boulder B)
- **Socratic 2F Strategy Plan**:
  - Upon entering 2F, overworld Strength is automatically deactivated. We must:
    1. Activate STRENGTH from POKéMON menu using ROCKY (Geodude).
    2. Confirm exact text: "ROCKY used STRENGTH!" and "ROCKY can move boulders." before touching any boulders.
    3. Log entry: "Floor: Victory Road 2F | Strength Active: [x] True".
    4. Explore systematically, identify Boulder B starting coordinates, Switch B coordinates, and map out safe push vectors without creating irreversible corners or dead-locks.

### Victory Road 3F:
- **Active State**: Unexplored / Initial
- **Boulders Database**:
  - Boulder C: Initial (TBD, TBD) | Current (TBD, TBD) | Target (TBD, TBD) | Status: [ ] Active
- **Floor Switches**:
  - Switch C: Coordinate (TBD, TBD) | State: [ ] Pressed (requires Boulder C)

## Socratic Challenge: Strength & Puzzle Management Protocol
- **Strength Deactivation Tracker**:
  - Floor transitions (stairs/warps) completely deactivate overworld STRENGTH.
  - Upon entering any floor, we will log: `Floor: [Floor Name] | Turn: [Turn Number] | Strength Active: [ ] False (Needs Reactivation)`.
  - We will activate STRENGTH from the POKéMON menu using ROCKY (Geodude).
  - We will verify the exact text indicators: `ROCKY used STRENGTH!` and `ROCKY can move boulders.`.
  - Only after confirming this text will we log: `Strength Active: [x] True`.
- **Boulder Push Vector Meticulous Logging**:
  - To prevent being trapped or making irreversible incorrect pushes, every single push will be logged before moving further:
    - *Format*: `Turn [N]: Pushed [Boulder ID] [Direction] from (X, Y) to (X_new, Y_new) while standing at (X_player, Y_player) facing [Facing]`.
  - If a puzzle becomes unsolvable or we get stuck, we will immediately use a stairs transition to reset all boulder coordinates and STRENGTH state, updating our logs accordingly.

## Live Progression & Route Logs:
- **Turn 97563 Resource Management Audit**:
  - Blastoise (GEMMY) is currently at 105/207 HP.
  - To prevent entering Victory Road in a vulnerable state, we will open our Bag item menu and use 1 Hyper Potion (currently 7 in inventory) to heal GEMMY to full (207/207 HP).
  - This keeps our primary sweeper healthy and ready for the 1F trainer battles without wasting Max Potions.
- **Floor: Victory Road 1F | Turn: 97593 | Strength Active: [x] True**
- **Turn 97616**: Pushed Boulder A Up from (5, 15) to (5, 14) while standing at (5, 16) facing Up. Corrected chronological logging (Turn 97614 was a premature pre-log before execution, actual movement executed on Turn 97616).

## Victory Road 1F Exploration & Mapping Protocol:
- **Search Goal**: Systematically explore Victory Road 1F to locate Switch A. (Completed: Turn 97771 - Switch A is located at (17, 13) and has Boulder A on it.)
Turn 97771: Floor: Victory Road 1F | Strength Active: [x] True.
We successfully pushed Boulder A onto Switch A! All obsolete multi-line plans for Turn 97756, 97753, and 97750 have been removed to maintain notepad hygiene. Proceeding to find the opened gate and the 2F stairs.
### Victory Road 1F Map Exploration (Continued):
- Turn 97779: Boulder A is successfully on Switch A at (17, 13).
- Turn 97834: Discovered that the object at (2, 10) on the isolated western plateau is a physical Boulder, not an Item Ball.
- Current coordinates: (2, 11) (standing below the boulder at (2, 10)).
- Defensive Pushing Analysis for Boulder at (2, 10):
  - If we push this boulder Up from (2, 11), it moves to (2, 9).
  - Standing at (2, 10), the boulder at (2, 9) cannot be pushed further Up because (2, 8) is a wall (TYPE_2889). It cannot be pushed Left or Right because (1, 9) and (3, 9) are walls.
  - Pushing this boulder is unnecessary because the area behind it (Rows 7, 8, 9) is already fully accessible via the wide-open ground path on Row 8 (Columns 3-7).
  - Defensive Rule: Do NOT push the boulder at (2, 10). It is a decorative blocker that does not need to be moved to access any area. Leave it at (2, 10).
- Path to return to the plateau at (5, 12):
  - Down to (2, 12) -> Left to (1, 12) -> Down to (1, 15) -> Right to (5, 15) -> Up to (5, 13) (stairs) -> Up to (5, 12).
- Plan: Backtrack along this route to return to the plateau and head East to find the 2F ladder.