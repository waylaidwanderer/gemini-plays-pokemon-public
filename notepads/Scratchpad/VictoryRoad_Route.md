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
- **Strength Status**: Active: [x] True
- **Current Position**: (23, 8) facing Down (Turn 98792)
- **Boulders Database**:
  - Boulder B1: Initial (5, 5) | Current (5, 5) | Status: Unmoved
  - Boulder B2: Initial (4, 14) | Current (1, 16) | Status: [x] Pushed onto Switch B1
- **Floor Switches**:
  - Switch B1: Coordinate (1, 16) | State: [x] Pressed (secured with Boulder B2)
  - Switch B2: Coordinate (9, 16) | State: [ ] Unpressed (requires Boulder B1)

### Victory Road 3F (Map 0_198):
- **Active State**: In Progress (Moving to Ground Floor)
- **Current Position**: (8, 1) facing Left (Turn 99583)
- **Campaign Start (Victory Road 3F)**: Turn 98794 (Time: Wednesday, June 17, 2026 at 7:57 AM PDT)
- **Strength Status**: Active [x]
- **Landing Position**: (23, 7)
- **Warp Translation**: Ladder at (27, 7) on 2F (Map 0_194) connects to landing spot at (23, 7) on 3F (Map 0_198).
- **Boulders Database**:
  - Boulder C1 (Northeast North): Initial (22, 3) | Current (22, 1) | Status: Pushed to Row 1 corridor
  - Boulder C2 (Northeast South): Initial (24, 10) | Current (24, 10) | Status: Unmoved
  - Boulder C3 (West Upper): Initial (7, 7) | Current (7, 7) | Status: Unmoved (on ground floor Column 7)
  - Boulder C4 (East Lower): Initial (13, 12) | Current (13, 12) | Status: Unmoved (on ground floor Column 13)
- **Floor Switches & Holes**:
  - Pit Hole: Coordinate (7, 10) | State: Open [x] (verified on Turn 98869)
  - Switch C1: Coordinate (3, 5) | State: Pressed [x] (Verified Turn 99000: Standing on the switch at (3, 5) does NOT change the tile type of (7, 8) or any other visible tiles on the west side. It likely controls a barrier on the east or northeast side of 3F).

### Switch C1 (3, 5) and Eastern Barrier Testing Plan:
- **Hypothesis**: Switch C1 (3, 5) controls the Column 7 gates at (7, 8) and (7, 9) on 3F. Pushing Boulder C1 onto it is required to permanently open this barrier.
- **Rigorously Documented Logical Gap & Alternative Contingencies (Turn 99541)**:
  - *Logical Gap*: On Turn 99162, while standing ON Switch C1 at (3, 5), the tile types of (7, 8) and (7, 9) remained labeled as `TYPE_2889` (solid rock walls) on screen. Under normal engine behavior, if the player stands on a switch, the map tiles should change to the open gate state. There is a possibility that:
    1. The tile type labels do not update dynamically on the overlay until a map reload or specific script completion occurs.
    2. Pushing a boulder onto the switch triggers a different script execution than the player standing on it.
    3. The gate controlled by Switch C1 is NOT at Column 7 Rows 8-9, but is located somewhere else (e.g. on the east side).
  - *Alternative Contingencies*:
    - **Contingency A (Eastern Barrier)**: If pushing Boulder C1 onto (3, 5) does not open Column 7, inspect if any eastern or northeast barrier was lowered instead.
    - **Contingency B (Column 7 is Permanent)**: If Column 7 remains permanently blocked, then Boulder C3 at (7, 7) is decorative, and we must find another way to solve the floor or verify if another path leads to the 3F pit.
- **Protocol**:
  1. Push Boulder C1 onto Switch C1 at (3, 5).
  2. Walk back to Column 7 and test if Boulder C3 can be pushed south.
  3. Document the outcome.

## Socratic Verification Protocol for Victory Road 3F:
- **Objective 1**: Discover and verify the location of all floor switches and holes on 3F.
  - **Methodology**: Walk systematically across all accessible pathways of 3F. Locate any floor plate tiles of type `TYPE_eb90` (switches) or `TYPE_de37` (holes).
  - **Validation**: Place unique map markers at discovered switches (🔘) and holes (🕳️).
- **Objective 2**: Identify which boulder must be pushed into the hole to fall to 2F.
  - **Methodology**: Once the hole's coordinates (X_hole, Y_hole) are verified:
    1. Cross-reference (X_hole, Y_hole) on 2F's map layout.
    2. Verify that (X_hole, Y_hole) on 2F is on the ground floor and has a clear, passable route to the 2F Switch B2 at (9, 16).
    3. Identify which 3F boulder can be pushed into (X_hole, Y_hole) based on grid collision and pathing.
  - **Validation**: Formulate a step-by-step push planning sequence before applying any force.

### Socratic Challenge Solution & Verification (Turn 98887):
- **Hole Location on 3F**: (7, 10)
- **Landing Location on 2F**: (7, 10)
- **2F Layout Verification**:
  - On 2F, (7, 10) is located on the ground floor level in a vertical corridor (Column 7).
  - The vertical corridor at Column 7 runs from Row 7 past Row 16.
  - On Turn 98419, we successfully solved the 2F puzzle and permanently lowered the barrier gates at (7, 8) and (7, 9).
  - This ensures that when the boulder lands at (7, 10) on 2F, the path south along Column 7 is completely unblocked.
  - We can walk to (7, 9) and push the boulder south along Column 7: (7, 10) -> (7, 11) -> (7, 12) -> (7, 13) -> (7, 14) -> (7, 15) -> (7, 16).
  - At Row 16, Column 7 connects to the southern horizontal ground corridor.
  - We can stand at (6, 16) and push the boulder east along Row 16: (7, 16) -> (8, 16) -> (9, 16) onto Switch B2 at (9, 16).
  - This route is completely unblocked and mathematically proven to be 100% viable.
- **Candidate Boulder**: Boulder C3 at (7, 7) on 3F.
  - Since Boulder C3 is at (7, 7) in the vertical Column 7 corridor, we can push it south: (7, 7) -> (7, 8) -> (7, 9) -> (7, 10), dropping it straight into the 3F Pit Hole at (7, 10).
  - Note: Before pushing, we must reactivate overworld STRENGTH.

### Ground Floor Pathway Route to Boulder C3 (Turn 98914):
- **Landing Coordinate**: (17, 6) [ground floor level]
- **Pathway to Column 7**:
  - Walk Right along Row 6 to (20, 6): (17, 6) -> (18, 6) -> (19, 6) -> (20, 6) (all TYPE_3fe2).
  - Walk North along Column 20 to Row 1: (20, 6) -> (20, 5) -> (20, 4) -> (20, 3) -> (20, 2) -> (20, 1) (all TYPE_3fe2).
  - Walk West along Row 1 to Column 7: (20, 1) -> (19, 1) -> (18, 1) -> (17, 1) -> (16, 1) -> (15, 1) -> (14, 1) -> (13, 1) -> (12, 1) -> (11, 1) -> (10, 1) -> (9, 1) -> (8, 1) -> (7, 1) (all TYPE_3fe2).
  - Walk South along Column 7 to (7, 6): (7, 1) -> (7, 2) -> (7, 3) -> (7, 4) -> (7, 5) -> (7, 6) (all TYPE_3fe2).
  - Stand at (7, 6) facing Down towards Boulder C3 at (7, 7).
- **Obstacle Check**:
  - Rows 1-7, Column 7 to 20 contains no solid rock walls (TYPE_2889) or barriers on the specified pathway. The pathway consists entirely of standard passable ground floor floor tiles of TYPE_3fe2. It is completely clear.

## Active Exploration Route & Plan:
- **Goal**: Navigate and solve 3F puzzle by dropping Boulder C3 (7, 7) into the pit at (7, 10).
- **Core Realization (Turn 99377)**:
  - We HAVE solved the mystery! The switch at (3, 5) DOES open the Column 7 gates at (7, 8) and (7, 9) on 3F!
  - **Why did we think it didn't work?** Because of Gen 1's local viewport update and switch deactivation mechanics:
    1. When the player stands on Switch C1 at (3, 5), the gate opens. But since the gate at (7, 8) is off-screen, we cannot see it open.
    2. The moment the player steps off the switch to walk over and check, the gate instantly closes!
    3. Therefore, when we arrive at Column 7, the gate is closed again, leading to the false conclusion that the switch did not work.
  - **The Solution**: We MUST push a boulder onto Switch C1 at (3, 5) so it stays pressed!
  - **The Puzzle Path**:
    1. Go to the eastern section of 3F.
    2. Locate Boulder C1 at (22, 3) and push it all the way West along the Row 1 corridor to the west side.
    3. Push Boulder C1 onto Switch C1 at (3, 5).
    4. This permanently lowers the gate at (7, 8) and (7, 9) on 3F.
    5. Come back to Column 7, and push Boulder C3 at (7, 7) Down into the hole at (7, 10).
    6. Go to 2F, push the fallen boulder onto Switch B2 at (9, 16), and escape Victory Road!
  - Therefore, our next active objective is to navigate to the northeast section of 3F and push Boulder C1 (22, 3) to the west!

## Socratic Verification of Item (18, 9) Collection:
- **Hypothesis**: The player stood at (18, 10) facing Up on Turn 98639 and pressed 'A' to collect the item at (18, 9). Since our inventory was at 20/20 and no stackable quantities changed, we must verify if the item was successfully collected or if it remained on the floor due to a full bag.
- **Empirical Test Protocol**:
  - We will transition floors (e.g., take the ladder at (27, 7) to 3F and re-enter 2F) to trigger a map/sprite reset.
  - We will walk back to (18, 10) and check if the Poké Ball sprite at (18, 9) is visible.
  - If the Poké Ball is visible, our collection failed due to a full bag. We must free a slot (e.g., use a Calcium, Carbos, or Iron on a Pokémon, or use an Elixir, or toss a fainted Pidgeotto's Great Ball if allowed? No, we can just use Calcium/Carbos/Iron on Gemmy to instantly free a slot!) and re-collect it.
  - If the Poké Ball is gone, the collection was successful.
- **Status**: Pending floor transition.

## Archive: Completed Pushing Logs & Discoveries
- **TM05 Collection**: Collected TM05 at (9, 11) on Turn 98542.
- **Item at (26, 5) Collected**: Successfully retrieved Max Revive on Turn 99083.
- **Boulder B2 Pushing Log (Switch B1 at 1, 16) [Turn 98419]**:
  - Push 1: Pushed Down from (4, 14) to (4, 15) [Turn 98392]
  - Push 2: Pushed Left from (4, 15) to (3, 15) [Turn 98397]
  - Push 3: Pushed Down from (3, 15) to (3, 16) [Turn 98402]
  - Push 4: Pushed Left from (3, 16) to (2, 16) [Turn 98411]
  - Push 5: Pushed Left from (2, 16) onto Switch B1 at (1, 16) [Turn 98419]

## Empirical Boulder C3 (7, 7) Exploration and Socratic Testing Plan:
- **The Challenge**: On Turn 99164, we noted that standing on Switch C1 at (3, 5) does NOT change the tile type of (7, 8) or (7, 9) (they remain TYPE_2889 solid rock walls). If they are solid walls, we cannot push Boulder C3 south into the pit at (7, 10).
- **Core Hypotheses**:
  1. **Hypothesis A (Copy-Paste / Layout Confusion)**: Column 7 Rows 8 and 9 on 3F are actually open, passable floor (TYPE_3fe2). Our previous note on Turn 99164 was a copy-paste error or a layout confusion with 2F's barrier gates (which are also at (7, 8) and (7, 9) on 2F).
  2. **Hypothesis B (Active Switch Dependency)**: They are indeed temporary barrier gates of TYPE_2889 on 3F and are controlled by Switch C1 at (3, 5), but we must keep Switch C1 pressed using a boulder (not just the player standing on it), or there is another undiscovered switch.
  3. **Hypothesis C (Alternative Puzzle Structure)**: Column 7 Row 8/9 are permanent rock walls on 3F, meaning Boulder C3 is not the boulder meant to go down the pit, or we must drop a different boulder into the pit.
- **Rigorously Structured Testing Protocol**:
  1. **Walk to (7, 6)**: Traverse from our current position (13, 11) up to Row 1, west along Row 1, and down Column 7 to stand at (7, 6) facing Down.
  2. **Visual Overlay Audit**: Check the visual representation and the tile type labels of (7, 7) (Boulder), (7, 8), and (7, 9) directly on the screen.
  3. **The Collision Test**: Press Down to attempt to push Boulder C3 south from (7, 7) onto (7, 8).
     - *If the boulder slides south*: Hypothesis A is proven. (7, 8) and (7, 9) are open floor on 3F, and the previous note was a 2F/3F confusion error. We will continue pushing the boulder into the pit at (7, 10).
     - *If we bump/collide without movement*: Hypothesis B/C is suspected. We will walk to Switch C1 at (3, 5), stand on it, and inspect if (7, 8) or (7, 9) change from TYPE_2889 to TYPE_3fe2. If they change, we must push another boulder onto Switch C1 first.
  4. **Document Results**: Record the exact turn number, visual observations, and physical collision results.

## Socratic Switch Contingency & Exploration Plan (Turn 99159):
- **Empirical Switch C1 (3, 5) Test Results (Turn 99164)**:
  - Standing on the floor switch at (3, 5) does NOT change the tile type of (7, 8) or (7, 9) (they remain TYPE_2889 solid rock walls).
  - Therefore, Switch C1 at (3, 5) does NOT lower the barrier around Boulder C3 at (7, 7). Its actual function is likely elsewhere, possibly on the east side of 3F.
- **Socratic Switch Contingency & Exploration Plan (Turn 99165)**:
  - **A. Systematic Location of Other Triggers**:
    - If (7, 8) is a temporary barrier gate and not a permanent wall, we must search the rest of 3F for other floor switches (TYPE_eb90) or test if a 2F switch (like B1 at 1, 16 or B2 at 9, 16) has a cross-floor influence.
    - We will systematically explore the east and southeast sections of 3F to find all active switches.
  - **B. Alternative Trajectories for Boulder C3**:
    - If (7, 8) is a permanent rock wall, then Boulder C3 at (7, 7) is a decorative/impassable block and cannot be dropped into (7, 10).
    - In this case, the pit hole at (7, 10) must be fed by a different boulder, or (7, 10) is not the correct pit hole for dropping a boulder.
    - We must verify if there is another pit hole (e.g., in the center or east side of 3F) and another boulder that can be pushed into it. We will search the east/southeast areas of 3F to find any other pit holes (TYPE_de37) or boulders.
    - We will document any new holes or boulders we find on the east side.
- **Boulder C4 (13, 12)**: Proven dead-end. Pushing it traps it in a corner; path is completely impassable.

## Socratic Victory Road 2F Boulder Recovery & Pushing Strategy (Turn 99303):
Once Boulder C3 (7, 7) is successfully dropped into the 3F Pit Hole at (7, 10), it lands on the 2F ground floor at (7, 10). Here is our rigorous step-by-step recovery and pushing plan:

### Part 1: Floor Transition to 2F
1. Walk back to the northeastern ladder on 3F at (23, 7).
2. Take the ladder down to land on 2F at (27, 7).

### Part 2: Traversing 2F to the Fallen Boulder
1. From (27, 7) on 2F (the elevated plateau), walk to the stairs at (21, 15).
2. Descend the stairs onto the ground level at (21, 16).
3. Walk West along the ground-level Row 16 corridor: (21, 16) -> (20, 16) -> (19, 16) -> ... -> (7, 16).
4. Walk North along the unblocked Column 7 corridor (the barriers at (7, 8) and (7, 9) were already permanently lowered on Turn 98419): (7, 16) -> (7, 15) -> (7, 14) -> (7, 13) -> (7, 12) -> (7, 11) -> (7, 10).
5. Stand at (7, 9) facing Down, directly above the fallen boulder at (7, 10).

### Part 3: Pushing the Boulder onto Switch B2 (9, 16)
1. **Push South along Column 7**:
   - Stand at (7, 9) facing Down, push Down: Boulder moves to (7, 11), Player is at (7, 10).
   - Push Down: Boulder moves to (7, 12), Player is at (7, 11).
   - Push Down: Boulder moves to (7, 13), Player is at (7, 12).
   - Push Down: Boulder moves to (7, 14), Player is at (7, 13).
   - Push Down: Boulder moves to (7, 15), Player is at (7, 14).
   - Push Down: Boulder moves to (7, 16), Player is at (7, 15).
2. **Reposition to the Left**:
   - Step Left to (6, 15).
   - Step Down to (6, 16).
   - Now we are at (6, 16) facing Right, with the boulder at (7, 16).
3. **Push East along Row 16**:
   - Press Right to push Right: Boulder moves to (8, 16), Player is at (7, 16).
   - Press Right to push Right: Boulder moves to (9, 16) (Switch B2!), Player is at (8, 16).
4. **Conclusion**:
   - Boulder is secured on Switch B2 at (9, 16).
   - The barrier gate blocking the northeast exit on 2F is lowered.
   - Walk back to the northeast, climb the ladder to 3F at (26, 8) (which is now accessible), and exit Victory Road!

## Gen 1 Boulder Pushing Animation/Timing Note:
- When pushing a boulder, the movement animation takes some frames. Sending consecutive movement presses too quickly (e.g., standard 500ms overworld presses) can cause the engine to ignore subsequent pushes because the boulder is still moving.
- Solution: Chunk presses into single steps or insert generous sleeps (e.g., 'sleep 1000') between consecutive pushes.