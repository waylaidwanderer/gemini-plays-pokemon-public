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
- **Active State**: Mapping/Exploration
- **Boulders Database**:
  - Boulder A: Initial (5, 15) | Current (5, 14) | Target (17, 13) | Status: [ ] Active
- **Floor Switches**:
  - Switch A: Coordinate (17, 13) | State: [ ] Pressed (requires Boulder A)
- **Verified Switch A Pushing Route**:
  1. Boulder A must be guided to (16, 12).
  2. Stand at (15, 12) and push Boulder A Right to (17, 12).
  3. Stand at (17, 11) and push Boulder A Down to (17, 13) (the switch).
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
- **Turn 97563 Resource Management Audit**:
  - Blastoise (GEMMY) is currently at 105/207 HP.
  - To prevent entering Victory Road in a vulnerable state, we will open our Bag item menu and use 1 Hyper Potion (currently 7 in inventory) to heal GEMMY to full (207/207 HP).
  - This keeps our primary sweeper healthy and ready for the 1F trainer battles without wasting Max Potions.
- **Floor: Victory Road 1F | Turn: 97593 | Strength Active: [x] True**
- **Turn 97616**: Pushed Boulder A Up from (5, 15) to (5, 14) while standing at (5, 16) facing Up. Corrected chronological logging (Turn 97614 was a premature pre-log before execution, actual movement executed on Turn 97616).

## Victory Road 1F Exploration & Mapping Protocol:
- **Search Goal**: Systematically explore Victory Road 1F to locate Switch A.
- **Safety Rule**: Do NOT perform any further pushes on Boulder A (currently at (5, 14)) until Switch A has been found and its coordinates are verified and logged. Keeping Boulder A in its current position allows us to move around it without blocking any paths or pushing it into an unrecoverable state.
- **Verification Rule**: Any candidates for Switch A must be stood on, interacted with, and verified to check if they are the correct active plate switch.
Turn 97682: Prepared to push Boulder A.
- Push Vector: Push DOWN from (5, 14) to (5, 16) while standing at (5, 14) facing Down.
- Transition Plan to Position Left of Boulder A: Once Boulder A is at (5, 16), the player is at (5, 14). We will stand at (4, 16) to push it Right. Path: Left to (4, 14), Down to (4, 15), Down to (4, 16) facing Right.
- Guided Coordinates: Boulder A will pass through (6, 16), (7, 16), (8, 16), (9, 16), (10, 16), (11, 16)? Wait, (11, 16) is a wall (TYPE_2889). So we will push it to (10, 16), and from there we must navigate carefully near the rock wall at (10, 15) to see how we transition columns. We will analyze the layout around (10, 15) and column 10 as we push.
- Corner Prevention: We will ensure we do not push the boulder flush against a corner where we cannot get behind it to push it in the next required direction. No blind pushes. We will check collision on every single step.
Turn 97703: Mapped the next phase of Boulder A's route to bypass the Column 10 wall at (10, 16).
- Step 1: Push Boulder A Right from (8, 16) to (9, 16) by standing at (7, 16) and pressing Right.
- Step 2: Reposition Player to (9, 17) to push Up. Path: Down to (8, 17), Right to (9, 17) facing Up.
- Step 3: Push Boulder A Up from (9, 16) to (9, 15) by standing at (9, 17) facing Up and pressing Up.
- Step 4: Step Up to (9, 16), then push Boulder A Up from (9, 15) to (9, 14) (the main open corridor).
- Step 5: Reposition Player to (8, 14) to push Right. Path from (9, 16) is: Left to (8, 16), Up to (8, 15), Up to (8, 14) facing Right.
- Step 6: Push Boulder A Right along Row 14 corridor to (13, 14) / (14, 14) etc. toward the switch.
This prevents the boulder from getting stuck against the solid Column 10 wall at (10, 16). No blind pushes. Checking coordinates on every turn.