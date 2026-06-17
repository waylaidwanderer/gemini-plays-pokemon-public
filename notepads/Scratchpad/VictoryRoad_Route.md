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
- **Boulders Database**:
  - Boulder B1: Initial (5, 5) | Current (5, 5) | Status: Unmoved
  - Boulder B2: Initial (4, 14) | Current (1, 16) | Status: [x] Pushed onto Switch B1
- **Floor Switches**:
  - Switch B1: Coordinate (1, 16) | State: [x] Pressed (secured with Boulder B2)
  - Switch B2: Coordinate (9, 16) | State: [ ] Unpressed (requires Boulder B1)

### Victory Road 3F (Map 0_198):
- **Active State**: In Progress (Pivoting to Contingency A: Exploring East Side)
  - **Current Position**: (22, 6) facing Up (Turn 99883)
  - **East-Wing & Plateau Pivot Start**: Turn 99693
- **Campaign Start (Victory Road 3F)**: Turn 98794 (Time: Wednesday, June 17, 2026 at 7:57 AM PDT)
- **Strength Status**: Active [x]
- **Landing Position**: (23, 7)
- **Warp Translation**: Ladder at (27, 7) on 2F (Map 0_194) connects to landing spot at (23, 7) on 3F (Map 0_198).
- **Boulders Database**:
  - Boulder C1 (Northeast North): Initial (22, 3) | Current (3, 5) | Status: Pushed onto Switch C1
  - Boulder C2 (Northeast South): Initial (24, 10) | Current (24, 10) | Status: Unmoved
  - Boulder C3 (West Upper): Initial (7, 7) | Current (7, 7) | Status: Blocked (tested on Turn 99678, gates at 7,8/7,9 remain solid)
  - Boulder C4 (East Lower): Initial (13, 12) | Current (13, 12) | Status: Unmoved (on ground floor Column 13)
- **Floor Switches & Holes**:
  - Pit Hole: Coordinate (7, 10) | State: Open [x] (verified on Turn 98869)
  - Switch C1: Coordinate (3, 5) | State: Pressed [x]

### Empirical Push Test Failure & Pivot Log (Turn 99693):
- **Verification of Failure**: On Turn 99678, with Boulder C1 resting on Switch C1 at (3, 5), the player attempted to push Boulder C3 at (7, 7) southwards from (7, 6). The push failed due to a solid collision bump, and tiles (7, 8) and (7, 9) remain TYPE_2889 rock walls.
- **Conclusion**: Switch C1 at (3, 5) does NOT open the Column 7 gates. Its function is elsewhere, likely lowering a barrier on the East or Northeast side of 3F.
- **Active Strategy**: Pivot immediately to Contingency A. Walk East along the Row 1 corridor to investigate if any eastern or northeast barrier was lowered, or if there is another switch/trigger on the East side.

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

## Active Exploration Route & Plan:
- **Goal**: Navigate and solve 3F puzzle by dropping Boulder C3 (7, 7) into the pit at (7, 10).
- **Core Realization (Turn 99377) & Empirical Disproof (Turn 99678)**:
  - *Initial Hypothesis*: We hypothesized that the switch at (3, 5) opens the Column 7 gates.
  - *Empirical Disproof (Turn 99678)*: Even with Boulder C1 resting on Switch C1 at (3, 5), the gate at (7, 8) and (7, 9) remained CLOSED and Boulder C3 at (7, 7) could not be pushed. Thus, Switch C1 at (3, 5) does NOT open the Column 7 gates. Its actual function is either to open a barrier on the east side, or there is another switch/puzzle element we need to trigger.
- **Active Exploration Strategy**:
  - We are currently exploring the East wing of 3F to inspect the southeastern and northeastern areas, locate Boulder C2 at (24, 10) and Boulder C4 at (13, 12), and search for any other active switches or paths that lead to solving the floor.

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
### Southwest Plateau Access Test (Turn 99771):
- **Hypothesis**: The player stood at (1, 6) facing Down and attempted to walk south onto (1, 7) (TYPE_2770) to see if it acts as a stairs tile to climb the southwest plateau.
- **Result**: The player bumped against (1, 7), remaining at (1, 6). Visually, (1, 7) has a solid cliff face block rather than stairs.
- **Conclusion**: The southwest plateau is impassable from the north at (1, 6).