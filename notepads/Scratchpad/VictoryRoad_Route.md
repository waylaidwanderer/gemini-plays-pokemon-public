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
- **Active State**: Unexplored / Initial
- **Strength Status**: Deactivated
- **Landing Position**: (23, 7)
- **Warp Translation**: Ladder at (27, 7) on 2F (Map 0_194) connects to landing spot at (23, 7) on 3F (Map 0_198).
- **Boulders Database**:
  - Boulder C1 (Northeast North): Initial (22, 3) | Current (22, 3) | Status: Unmoved
  - Boulder C2 (Northeast South): Initial (24, 10) | Current (24, 10) | Status: Unmoved
- **Floor Switches & Holes**:
  - To be discovered and verified systematically.

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
- **Goal**: Navigate to 3F (Map 0_198) via the northeast ladder at (27, 7).
- **Empirical Breakthrough (Turn 98709)**:
  - We have visually inspected Column 9 from (9, 12) on the ground floor.
  - **Findings**:
    1. Row 10 is a solid rock wall of TYPE_2889 spanning Columns 6 to 12.
    2. The Black Belt is at (9, 9) on the plateau level (TYPE_2770).
    3. The ground floor at Column 9 ends at Row 11 and does not connect to the plateau.
    4. Therefore, it is physically impossible to push Boulder B1 (at (5, 5) on the plateau) down Column 9 to Switch B2 (at (9, 16) on the ground floor).
    5. **New Puzzle Solution Hypothesis**: The boulder that goes on Switch B2 (9, 16) must fall from the ceiling of 2F (which is a hole on 3F). Once it lands on the ground floor of 2F, it can be pushed west along Row 16 to (9, 16).
- **Next Action Steps**:
  1. Walk Down, Right, and Up to bypass the Column 24 wall on 2F and climb the real ladder at (27, 7).
  2. Enter 3F at (23, 7).
  3. Explore 3F to locate the boulder and hole to drop it to 2F.

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
- **Item at (18, 9) Collected**: Successfully retrieved the Poké Ball item at (18, 9) on Turn 98639.
- **Boulder B2 Pushing Log (Switch B1 at 1, 16) [Turn 98419]**:
  - Push 1: Pushed Down from (4, 14) to (4, 15) [Turn 98392]
  - Push 2: Pushed Left from (4, 15) to (3, 15) [Turn 98397]
  - Push 3: Pushed Down from (3, 15) to (3, 16) [Turn 98402]
  - Push 4: Pushed Left from (3, 16) to (2, 16) [Turn 98411]
  - Push 5: Pushed Left from (2, 16) onto Switch B1 at (1, 16) [Turn 98419]
- Turn 98826: Replaced northwest plateau, met Cooltrainer♀ at (13, 3). Positioned at (13, 4) facing Up. We are about to engage her in battle.