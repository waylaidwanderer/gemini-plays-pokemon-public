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
  - **Current Position**: Historical (Returned to 3F)
- **Strength Status**: Active: [x] True
- **Boulders Database**:
  - Boulder B1: Initial (5, 5) | Current (5, 5) | Status: Unmoved
  - Boulder B2: Initial (4, 14) | Current (1, 16) | Status: [x] Pushed onto Switch B1
- **Floor Switches**:
  - Switch B1: Coordinate (1, 16) | State: [x] Pressed (secured with Boulder B2)
  - Switch B2: Coordinate (9, 16) | State: [ ] Unpressed (requires Boulder B1)

### Victory Road 3F (Map 0_198):
- **Active State**: In Progress (Pivoting to Contingency A: Exploring East Side)
  - **Current Position**: (13, 12) facing Up (Turn 100085)
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

## Active Exploration Route & Plan:
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

## Southern Corridor & Boulder C4 Investigation Strategy (Turn 100051):
We have disproven the previous Column 7 gate and (7, 10) pit hole hypotheses. Our active workspace is now focused on the southern ground-level corridor.
1. Walk South from (8, 12) along Column 8 to (8, 16).
2. Walk East along the safe Row 16 corridor to Column 13: (8, 16) -> (13, 16).
3. Walk North along Column 13 to investigate Boulder C4 at (13, 12) and the real pit hole on 3F.
4. Identify and log the exact coordinates of the real 3F pit hole and formulate a rigorous pushing strategy once verified.

## Gen 1 Boulder Pushing Animation/Timing Note:
- When pushing a boulder, the movement animation takes some frames. Sending consecutive movement presses too quickly (e.g., standard 500ms overworld presses) can cause the engine to ignore subsequent pushes because the boulder is still moving.
- Solution: Chunk presses into single steps or insert generous sleeps (e.g., 'sleep 1000') between consecutive pushes.

- **Plateau Exploration Log (Turns 99994-100024)**:
  - Walked West along Row 4 from (13, 4) to (9, 4).
  - Attempted to walk South along Column 9 to explore the southern boundary of the plateau.
  - Encountered a wild ONIX at (9, 7) on Turn 100002.
  - Walked left along Row 10 from (9, 10) to (5, 10) on Turn 100022.
  - Currently at (5, 10) on the elevated plateau.
  - Plan: Clean up obsolete Southwest Access Test notes, then walk North to (5, 7) to reveal the western portion of 3F.
- **Western Ground Floor Exploration Log (Turns 100035-100041)**:
  - Discovered that the "ladder" at (1, 9) is actually a set of stairs connecting the elevated plateau to the western ground floor of 3F.
  - Walked Down onto the ground floor at (1, 10) on Turn 100035.
  - Walked to (3, 13) on Turn 100041.
  - Visually mapped the southwest ground floor:
    - Moltres (legendary bird sprite) is standing at (6, 14).
    - An undefeated trainer is standing at (7, 13) facing Left.
    - Columns 1-6 on Rows 12-16 are completely open ground floor (TYPE_3fe2).
  - Active Strategy: Walk East along the safe Row 12 corridor to bypass the trainer's line of sight and explore the southern/eastern ground floor of 3F to locate the real pit hole and boulders.