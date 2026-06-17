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
- **Current Position**: (9, 16) facing Up (Turn 98701)
- **Boulders Database**:
  - Boulder B1: Initial (5, 5) | Current (5, 5) | Status: Unmoved
  - Boulder B2: Initial (4, 14) | Current (1, 16) | Status: [x] Pushed onto Switch B1
- **Floor Switches**:
  - Switch B1: Coordinate (1, 16) | State: [x] Pressed (secured with Boulder B2)
  - Switch B2: Coordinate (9, 16) | State: [ ] Unpressed (requires Boulder B1)

### Victory Road 3F (Map 0_195):
- **Active State**: Unexplored / Initial

## Active Exploration Route & Plan:
- **Goal**: Navigate Boulder B1 from (5, 5) to Switch B2 at (9, 16) to lower the southeast barrier gate.
- **Boulder B1 Pushing Strategy & Path (The "Northeast Switch" Plan)**:
  - Boulder B1 starting coordinate: **(5, 5)**.
  - Switch B2 coordinate: **(9, 16)**.
  - **Bottleneck Resolution at (9, 9)**:
    - We must first inspect and verify the physical position of the defeated Black Belt on Column 9.
    - If the Black Belt is standing at (9, 9) and is solid, he blocks Column 9.
    - In this case, we cannot push the boulder directly down Column 9.
    - Socratic Mitigation Hypothesis:
      - We must verify if the Black Belt is actually standing at (9, 9), or if he engaged us from a different tile (e.g. 9, 8 or 9, 10), leaving Column 9 passable at (9, 9).
      - If he blocks Column 9, we will investigate if the boulder can be pushed through an adjacent column (like Column 10 or 8), or if we can manipulate his position by resetting the floor, or if there is another puzzle route.
      - We will proceed to walk Left along Row 11 to (18, 11) first to collect the TM/Poke Ball and visually inspect the bottleneck at Column 9.
  - Let's map the path from (5, 5) to (9, 16):
    - Wait! We need to walk to (5, 5) first.
    - We are currently at (19, 12).
    - Path to (5, 5):
      1. Walk up to the northern area of 2F where Boulder B1 is.
      2. Push Boulder B1 to the right (East) towards Column 9.
         - Push Right 4 times: (5, 5) -> (6, 5) -> (7, 5) -> (8, 5) -> (9, 5).
         - Wait, we need to stand at (4, 5) to push first.
         - Then stand at (5, 5) to push.
         - Then stand at (6, 5) to push.
         - Then stand at (7, 5) to push.
         - Once the boulder is at (9, 5), stand at (9, 4) and push Down.
         - Push Down: (9, 5) -> (9, 6) -> (9, 7) -> (9, 8) -> (9, 9) -> (9, 10) -> (9, 11) -> (9, 12) -> (9, 13) -> (9, 14) -> (9, 15) -> (9, 16).
         - Let's analyze if the defeated Black Belt at (9, 9) blocks the path:
           - Wait! The Black Belt was defeated at (9, 9). But is he standing at (9, 9)?
           - Let's verify if we can push a boulder past (9, 9).
           - Socratic verification: If the Black Belt at (9, 9) is solid, we cannot push the boulder onto (9, 9).
           - If we cannot push the boulder onto (9, 9), we can't slide it down Column 9.
           - Wait, let's look at the map: is there another way to get to the switch at (9, 16) or does the Black Belt not block?
           - Let's walk to the ground floor first to examine the layout and the trainer's position.

## Socratic Verification of Item (18, 9) Collection:
- **Hypothesis**: The player stood at (18, 10) facing Up on Turn 98639 and pressed 'A' to collect the item at (18, 9). Since our inventory was at 20/20 and no stackable quantities changed, we must verify if the item was successfully collected or if it remained on the floor due to a full bag.
- **Empirical Test Protocol**:
  - We will transition floors (e.g., take the ladder at (23, 7) to 3F and re-enter 2F) to trigger a map/sprite reset.
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