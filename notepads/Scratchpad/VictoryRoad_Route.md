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
- **Current Position**: (9, 14) facing Down (Turn 98551)
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
  - Let's map the path from (5, 5) to (9, 16):
    - Wait! We need to walk to (5, 5) first.
    - We are currently at (9, 14).
    - Path to (5, 5):
      1. From (9, 14), go Down to (9, 15).
      2. Move Left on Row 15: (9, 15) -> (8, 15) -> (7, 15) -> (6, 15) -> (5, 15).
      3. Move North on Column 5: (5, 15) -> (5, 14) -> (5, 13) -> (5, 12) -> (5, 11) -> (5, 10).
      4. Wait, let's verify if Column 5 Row 10 is passable. (5, 10) has the stairs. If we go Up, we climb onto the plateau.
      5. Wait! Is there a ground-level path on the west side leading to (5, 5)?
         - Yes! In our western exploration, we walked from (0, 8) to (5, 7) on the ground floor.
         - So (5, 7) is on the ground floor.
         - Is (5, 6) passable? Yes, TYPE_3fe2.
         - And Boulder B1 is at (5, 5).
         - Let's verify how to push Boulder B1 from (5, 5) to Switch B2 at (9, 16).
         - Socratic Push Plan:
           - Since Boulder B1 is at (5, 5), let's inspect the surrounding walls of (5, 5):
             - (5, 4) is a wall? Or is it passable?
             - In standard VR 2F, Boulder B1 starts at (5, 5).
             - We want to push Boulder B1 to the right (East) towards Column 9.
             - Let's check: can we push Boulder B1 Right from (5, 5)?
               - To push Right, we must stand at (4, 5) facing Right, and press Right.
               - This moves Boulder B1 to (6, 5).
               - Then stand at (5, 5) facing Right, and press Right.
               - This moves Boulder B1 to (7, 5).
               - Then stand at (6, 5) facing Right, and press Right.
               - This moves Boulder B1 to (8, 5).
               - Wait, can we push it to (9, 5)?
                 - To push Right to (9, 5), stand at (7, 5) facing Right, and press Right.
                 - This moves Boulder B1 to (9, 5).
               - Let's check if the path on Row 5 is clear:
                 - Yes, Row 5 from Column 5 to Column 9 is completely open ground level!
               - Once Boulder B1 is at (9, 5):
                 - We want to push it Down along Column 9 to Switch B2 at (9, 16)!
                 - To push Down, we stand at (9, 4) facing Down, and press Down.
                 - This moves Boulder B1 to (9, 6).
                 - Then we stand at (9, 5) facing Down, and press Down.
                 - This moves Boulder B1 to (9, 7).
                 - And so on, pushing it Down along Column 9:
                   - (9, 8) -> (9, 9) -> (9, 10) -> (9, 11) -> (9, 12) -> (9, 13) -> (9, 14) -> (9, 15) -> onto Switch B2 at (9, 16)!
                 - Wait! Let's check if there are any obstacles on Column 9 between Row 5 and Row 16:
                   - (9, 9) has the defeated Black Belt. Defeated trainers are solid but can we push a boulder through or past them?
                   - In Gen 1, you CANNOT push a boulder onto a tile occupied by an NPC. Defeated trainers are solid!
                   - So we CANNOT push the boulder through (9, 9) if the Black Belt is standing there!
                   - Oh! Let's check: is the Black Belt at (9, 9)?
                     - Yes! The defeated Black Belt is at (9, 9).
                   - Wait, can we push the boulder around him?
                     - Let's look at the surrounding tiles of (9, 9):
                       - (8, 9) is TYPE_2770 (elevated plateau). The boulder cannot go up onto the plateau.
                       - (10, 9) is TYPE_2770 (elevated plateau).
                       - So Column 9 is a 1-tile wide ground-level bottleneck on Rows 8 and 9!
                       - Oh! This means we CANNOT push Boulder B1 past (9, 9) along Column 9!
                       - Wait, let's verify this carefully. Is the Black Belt really at (9, 9)?
                         - Yes, the map marker says "Black Belt defeated at (9, 9)".
                         - But wait, is he standing at (9, 9) or is he at (11, 5) or somewhere else?
                         - Let's check our notes: we defeated the Black Belt at (9, 9) on Turn 98453.
                         - Wait, in Turn 98453: "I defeated a Black Belt at (9, 9) in Victory Road".
                         - Let's check if he is actually standing at (9, 9). Yes, in Gen 1, trainers remain standing at their spot forever once defeated.
                         - Wait, let's think: is there a different way to get the boulder to Switch B2?
                         - Let's check if there are other ground-level corridors.
                         - What about Column 13?
                           - We can walk Column 13 from Row 8 to Row 13. But is Column 13 passable for a boulder?
                           - Column 13 is on the plateau (Row 8-12 are TYPE_2770). Boulders cannot be pushed onto plateaus!
                         - Wait, let's check: does the boulder need to go onto Switch B2?
                           - Yes, Switch B2 is at (9, 16).
                           - If we cannot push Boulder B1 past (9, 9) because of the trainer, then how do we solve the puzzle?
                           - Wait! Let's check if the trainer at (9, 9) is actually at (9, 9).
                           - Let's walk back and check where the Black Belt is standing.
                           - Let's verify this on the screen when we walk up!

## Archive: Completed Pushing Logs & Discoveries
- **TM05 Collection**: Collected TM05 at (9, 11) on Turn 98542.
- **Boulder B2 Pushing Log (Switch B1 at 1, 16) [Turn 98419]**:
  - Push 1: Pushed Down from (4, 14) to (4, 15) [Turn 98392]
  - Push 2: Pushed Left from (4, 15) to (3, 15) [Turn 98397]
  - Push 3: Pushed Down from (3, 15) to (3, 16) [Turn 98402]
  - Push 4: Pushed Left from (3, 16) to (2, 16) [Turn 98411]
  - Push 5: Pushed Left from (2, 16) onto Switch B1 at (1, 16) [Turn 98419]