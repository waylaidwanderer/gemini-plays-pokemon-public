# Scratchpad: Victory Road Route & Puzzle States
- Started: Turn 96968 (pre-entry routing)

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
  - Boulder A2: Initial (14, 2) | Current (10, 2) | Target (10, 2) | Status: [ ] Active
- **Floor Switches**:
  - Switch A: Coordinate (17, 13) | State: [x] Pressed (secured with Boulder A)
- **Verified Switch A Pushing Route**:
  - Successfully guided Boulder A via Rows 16, 17, 14, and 12, culminating in a downward push from (17, 11) onto (17, 13).

### Victory Road 2F Map Entry & Mapping Protocol:
- **Strength Deactivation Tracker**:
  - Floor transitions (stairs/warps) completely deactivate overworld STRENGTH.
  - Upon entering 2F, we will immediately log the coordinate state:
    `Floor: Victory Road 2F | Turn: [Turn Number] | Strength Active: [ ] False (Needs Reactivation)`.
- **Systematic Boundary & Object Mapping (No-Touch Rule)**:
  - Do NOT touch or walk adjacent to any boulders until overworld Strength is activated.
  - Walk the perimeter of the immediately accessible ground to map boundaries, passages, and solid rock divisions.
  - Identify and log all physical boulders: assign IDs (e.g. Boulder B1, Boulder B2) and note their starting coordinates.
  - Identify and log all floor switch plates (empty or occupied): assign IDs (e.g. Switch B1, Switch B2) and note their coordinates.
  - Socratic Verification: We will test the passability of all critical bottleneck tiles on foot to see if there are any active barriers or custom blockages that may require a multi-boulder solution.
- **Strength Activation Protocol**:
  - Only after mapping the initial layout and defining the puzzle elements will we open the POKéMON menu, select ROCKY (Geodude), and select STRENGTH.
  - We will verify the exact text indicators: "ROCKY used STRENGTH!" and "ROCKY can move boulders."
  - Log: `Strength Active: [x] True`.
- **Pre-Push Vector formulation**:
  - Never push any boulder without first formulating and validating a clear step-by-step vector path to a switch.
  - Ensure we do not push any boulder into a corner, wall, or 1-tile bottleneck where it becomes irreversibly stuck.
- **Backtrack & Reset Rule**:
  - If any boulder becomes irreversibly stuck, immediately take the stairs back to 1F and return to 2F to fully reset all boulder coordinates and room states.

### Victory Road 2F:
- **Active State**: Unexplored / Initial
- **Strength Status**: Floor: Victory Road 2F | Turn: 98171 | Strength Active: [ ] False (Needs Reactivation)
- **Boulders Database**:
  - Boulder B1: Initial (5, 4) | Current (5, 4) | Target (TBD, TBD) | Status: [ ] Active
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

## Victory Road 1F Exploration & Mapping Protocol:
- Status: Completed (Boulder A on Switch A at 17, 13 on Turn 97771, which lowered the barrier on the eastern plateau).

## Victory Road 1F Warp Test Log:
- Status: Resolved. The northwest ladder warp is located at (1, 1). This warp is fully active and was taken on Turn 98164 to transition to 2F.

## Victory Road 2F Exploration Phase (Started Turn 98165)
- Floor: Victory Road 2F (Map 0_194) | Strength Active: [x] True (Activated on Turn 98245)
- Initial Position: (0, 8) facing Right.
- Current Position: (7, 7) facing Down (Turn 98317)
- Explored Pathway:
  - Traversed from (0, 8) to (5, 7) (Row 7, Columns 0-5).
  - Traversed Row 7 Left from (5, 7) to (1, 7).
  - Bypassed solid rock at (1, 8) by moving Right to (2, 7) -> Down to (2, 8) -> Down to (2, 9).
  - Explored southwest Western Chamber down to (1, 16).
  - Mapped (1, 16) as a passable Switch plate (Switch B1) rather than a pitfall hole.
  - Returned to (3, 9) on Turn 98240 and successfully activated overworld Strength.
  - Moved from (3, 11) up to (3, 7) then east along Row 7 to (7, 7). Triggered a wild Graveler battle on (7, 7) which was successfully fled from on Turn 98305.
- Boulders Logged:
  - Boulder B1: Verified at (5, 5) | Status: Unmoved | Strength Active: [x] True
  - Boulder B2: Verified at (4, 14) | Status: Unmoved | Strength Active: [x] True
- Floor Switches Logged:
  - Switch B1: Coordinate (1, 16) | State: [ ] Pressed (requires Boulder B2)
  - Switch B2: Coordinate (9, 16) (Visual duplicate of Switch B1, to be verified)
- Socratic 2F Western Chamber Mapping Plan:
  - Objective: Systematically map the boundaries and accessible tiles of the western chamber (Columns 0-3, Rows 9-11) on foot to identify hidden switch plates or passages, and verify if 2F features a custom multi-boulder puzzle.
  - Coordinate-by-Coordinate Verification Path:
    1. From (2, 9), step Left to (1, 9), then Left to (0, 9) to test passability of the western-most column. (Completed: Turn 98212. Verified passable.)
    2. Backtrack to (1, 9), step Down to (1, 10), then Down to (1, 11). (Completed: Turn 98215. Verified passable.)
    3. From (1, 11), step Left to (0, 11) to check if the corner is passable or if there is a switch. (Updated: (0, 11) is solid rock TYPE_2889. Skipped.)
    4. From (1, 11), step Right to (2, 11), then Right to (3, 11) to inspect the bottom right of the western chamber. (Completed: Turn 98221.)
    5. From (3, 11), step Up to (3, 10) and then Up to (3, 9). (Completed: Turn 98240.)
    6. Log the status of every tile to confirm whether a switch plate exists in this western pocket. (Completed: Confirmed Switch B1 exists at (1, 16) and is passable, not a hole.)
    7. Once mapped, if no switch exists here, we will return to (5, 7) to activate Strength and proceed with pushing Boulder B1 at (5, 5). (Completed: Returned and activated Strength.)
  - New Observation (Turn 98215): Detected a circular orange-brown object at (4, 14). We will route to (4, 13) to inspect this object from adjacent tiles. (Completed: Confirmed as Boulder B2.)
- **Socratic 2F Central/Eastern Verification Plan (Turn 98271)**:
  - Objective: Systematically explore and verify the central and eastern sections of Victory Road 2F (Columns 4-20) to find Switch B2 and check for additional puzzle elements.
  - Coordinate-by-Coordinate Verification Path:
    1. From current position (3, 9), move Up to (3, 8), then Up to (3, 7).
    2. Move Right to (7, 7) via (4, 7) -> (5, 7) -> (6, 7) -> (7, 7).
    3. Step South onto the plateau stairs at (7, 8) (TYPE_de37).
    4. Step Right onto the plateau at (8, 8) (TYPE_2770).
    5. Head East on the plateau past Column 8 to map the eastern elevated section and find the exit or further switches.
    6. Locate and verify the coordinates of Switch B2 (visually a duplicate of Switch B1, likely at Y=16 on the east side).
    7. Once verified, map precise push vectors for both Boulder B1 at (5, 5) and Boulder B2 at (4, 14) to solve the multi-boulder puzzle.