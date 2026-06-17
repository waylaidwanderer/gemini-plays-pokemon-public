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
- **Search Goal**: Systematically explore Victory Road 1F to locate Switch A. (Completed: Turn 97771 - Switch A is located at (17, 13) and has Boulder A on it.)
- **Puzzle Status Verification**: The map layout is modified, requiring a multi-boulder puzzle solution. The standard 2F ladder warp at (17, 2) is verified to be inactive under our current configuration. We must determine if we need to solve the full three-boulder puzzle to activate the warp, or if there is another unexplored route.
- **Unexplored Areas Check**: Systematically explore the western ground floor's northern sections (Columns 1-4, Rows 0-7) to check for alternative paths or switches before resetting the puzzle.
- **Starting turn / timestamp**: Victory Road 1F exploration phase started on Turn 97131 to track time and prevent Time Blindness.
## Victory Road 1F Warp Test Log:
- We are currently standing at (17, 2).
- Tested stand-in-front and face UP on (18, 3) facing (18, 2) on Turn 97915. Result: BUMPED, (18, 2) acts as a solid rock wall and is impassable.
- Tested stepping onto (17, 2) on Turn 97914. Result: Did not warp.
- The northeast corner does not contain an active warp or accessible ladder under the current state.
- Turn 98003: Currently standing at (9, 6) on the central plateau of Victory Road 1F. We picked up TM43 (Sky Attack) from (11, 0) and pushed Boulder A2 to (10, 2). Proceeding Left to Column 7 to battle the Cooltrainer♀ at (7, 5) and descend to the western ground floor via the stairs at (7, 7).

### Western Ground Floor Mapping & Multiple Boulders Verification Protocol (Turn 98021 Plan):
- **Hypothesis**: The standard 2F ladder warp at (17, 2) is disabled because this ROM features a custom three-boulder layout on 1F, requiring a multi-boulder puzzle to be solved first.
- **Protocol Details**:
  1. We must systematically descend the western stairs at (7, 7) to reach the western ground floor.
  2. Map the entire western ground floor (Columns X=1 to X=10) on foot.
  3. Locate any undiscovered floor switch plates (plates similar to Switch A).
  4. Find the Plateau Boulder at (2, 10). Determine its starting environment and check if a switch exists beneath or adjacent to it.
  5. Formulate push vectors for both the Plateau Boulder at (2, 10) and Boulder A2 at (10, 2) to their respective target switches (once located) to fully activate the 2F warp at (17, 2).
  6. Document all results with exact coordinates and turn numbers to maintain a rigorous proof of work.
- **Turn 98036**: Pushed the Plateau Boulder from (2, 10) to (2, 13) via (2, 11) and (2, 12). This cleared the bottleneck at (2, 10) and opened access to the southwest corner.
- **Plateau Boulder Database Entry**: Plateau Boulder | Initial (2, 10) | Current (2, 13) | Target (TBD) | Status: [ ] Active
- **Turn 98044**: Exploring the southwestern and southern ground floor (Columns X=1 to X=6). Standing at (1, 15), heading East toward Column 6 to check passage viability.
- **Victory Road Exploration Start Turn**: 97131 (Time tracking to prevent Time Blindness)

## Reflection at Turn 98063
1. **Immediate Execution**: We successfully navigated from (17, 11) to (5, 13) on the plateau stairs via Row 16, which bypassed the Row 14 solid blockages at Columns 6 and 7. We are currently on the plateau at (5, 9).
2. **Notepad Hygiene**: Our records of Victory Road 1F are updated with the correct routing vectors. We disproved the "three-boulder puzzle on 1F" hypothesis because this ROM is mechanically vanilla. The northeast ladder (17, 2) didn't work on Turn 97914 because we were likely standing on (17, 2) but the actual ladder warp tile is at (17, 1) or we were blocked/unable to step onto it correctly from (17, 2). Wait, in vanilla, is (17, 2) the ladder warp, or is it on the plateau? We will test this as soon as we reach the northeast.
3. **Map Hygiene**: The map markers are mostly clean, tracking the active switch and boulders.
4. **Custom Tools**: Proposed custom tools:
   - `grind_battle_flee`: Automatic running script. Already have `flee_battle` which does exactly this.
   - `menu_navigation_agent`: Custom agent for navigating PC boxes.
   - `overworld_strength_activator`: Automatically opens party menu, selects Geodude, and uses Strength.
   - `route_planner_victory_road`: Coordinates-based movement generator (we can do this ourselves via code execution or manually).
5. **Tool Maintenance**: No broken custom tools currently.
6. **Goal Clarity**: Goals are clean. Method logs are detailed in `Scratchpad/VictoryRoad_Route`.
7. **Error Analysis**: We corrected our pathing model: Column 6/7 Row 14 is solid rock. Row 16 is completely open from Column 5 to 9. We successfully adjusted our pathing.
- **Turn 98142**: Discovered that the sprite at (3, 2) is Cooltrainer♂, who initiated a trainer battle! Also discovered that the true 2F exit ladder is located at (1, 1) in the northwest corner of Victory Road 1F. This explains why (17, 2) is inactive—the layout of the map has been modified, relocating the ladder to (1, 1).
- **Northwest Ground Exploration Details**: We systematically mapped the pathway and confirmed that (1, 1) has the vertical ladder graphic, and (2, 2) allows interaction with (3, 2).
- **Battle Log**: Engaged Cooltrainer♂ at (3, 2). Opponent has 4 Pokémon. GEMMY (Blastoise Lv 63) is lead.

- **Turn 98156 Socratic Challenge Response**: We have successfully mapped the northwest corner of the ground floor and found the visual ladder graphic at (1, 1). This disproves any remaining need to search for additional hidden switch plates on 1F, as the exit warp was simply relocated to (1, 1) rather than disabled. Once we defeat Cooltrainer♂, we will step onto (1, 1) to transition to 2F.

## Victory Road 2F Live Log (Turn 98166):
- Floor: Victory Road 2F (Map 0_194) | Turn: 98166 | Strength Active: [ ] False (Needs Reactivation)
- Initial Position: (0, 8) facing Right.
- Adjacent tiles:
  - North: (0, 7) TYPE_3fe2 (Passable floor)
  - South: (0, 9) TYPE_3fe2 (Passable floor)
  - East: (1, 8) TYPE_2889 (Solid rock)
  - West: Solid wall boundary of the map.
- Mapping strategy: We will walk the immediately accessible areas before activating Strength or pushing any boulders. We must locate all boulders and switch plates systematically.