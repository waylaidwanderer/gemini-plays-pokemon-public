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
- **Active State**: Unexplored / Initial
- **Boulders Database**:
  - Boulder A: Initial (TBD, TBD) | Current (TBD, TBD) | Target (TBD, TBD) | Status: [ ] Active
- **Floor Switches**:
  - Switch A: Coordinate (TBD, TBD) | State: [ ] Pressed (requires Boulder A)
- **Sliding Log / Push Vectors**:
  - *Format*: Push [Direction] from (X, Y) to (X_new, Y_new) on Turn [N].

### Victory Road 2F:
- **Active State**: Unexplored / Initial
- **Boulders Database**:
  - Boulder B: Initial (TBD, TBD) | Current (TBD, TBD) | Target (TBD, TBD) | Status: [ ] Active
- **Floor Switches**:
  - Switch B: Coordinate (TBD, TBD) | State: [ ] Pressed (requires Boulder B)

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
- **Turn 97389**: Re-entered Pokemon League Gatehouse (Map 0_193) at (4, 7). Heading North to exit onto Route 23 to make our way back to Victory Road.
- **Party Status check**: GEMMY is healed (105/207 HP - wait, healed? Ah, GEMMY is at 105 HP, not fully healed? Wait, did we heal at Viridian Center? Turn 97143 healed party, but did we take some damage or was GEMMY already at 105 HP because of something else? Ah, GEMMY fought Rival Blue or wild Spearow or we did some training? Let's check: on Turn 97310-97312 we encountered a wild Spearow and fled, maybe took some damage, or maybe GEMMY took damage in some other fight. It's fine, GEMMY has 105/207 HP, which is plenty for now, and we have many Hyper Potions and Max Potions in our inventory if needed.)
- **Bicycle status**: Riding the Bicycle (outdoors).

## Cross-Floor Vertical Boulder Transitions Database
To solve the Victory Road puzzle progression, some boulders must be pushed down holes/pits on higher floors to activate switches below.
- To track this without backtracking (which resets the state), we will record:
  - **Transition Event**: Pushed Boulder [ID] down Pit [Coordinate] on [Source Floor] on Turn [N].
  - **Landed State**: Lands on [Target Floor] at coordinate [X_target, Y_target].
  - **Target Interaction**: Standing at [X_player, Y_player] facing [Direction], pushing the landed boulder to switch at [X_switch, Y_switch].
  - **State Lock Rule**: Do not exit the floor or leave Victory Road entirely until the target switch is finalized, as backtracking resets the boulder positions!
- **Turn 97449**: Bypassed the Row 131 wall structure. Currently at (7, 124) facing Left on the bicycle. Heading East to Column 8 to begin our northward journey toward the Thunder Badge checkpoint at Y=119.