# Safari Zone West Exploration - Run 42 (Turn 68289 - Active)
- **Current Status**: Standing at (22, 29) on ground level in Safari Zone North on Turn 68289.
- **Inventory Status**: 15/20 items.
- **Run 42 Starting Steps**: 500 steps.
- **Current Steps Remaining**: 346 steps.
- **Money remaining**: ¥69,317 (paid ¥500 entry fee).

## Active Campaign Plan (Run 42 Ground Bypass Victory Route)
We will bypass Koga's plateau entirely on Run 42 by using the edge-to-edge transition on the western ground level of Safari Zone North (Row 35, Columns 2-7), which mathematically transitions us directly onto the open ground-level plains of Safari Zone West (Row 0, Columns 20-25) with zero plateaus to climb!

### Step-by-Step Step-Efficient Route (Run 42):
1. **Gatehouse to Center Transition**: Walk Up to transition into Safari Zone Center at (15, 25). (Completed, Turn 67051/68118)
2. **Center to East**: Walk to (29, 11) and transition to Safari Zone East at (0, 23). (Completed, Turn 67069/68133)
3. **East to North**: Climb Eastern Plateau stairs, walk across to Western stairs, descend to ground corridor, climb northern stairs, walk to northern corridor, and transition to Safari Zone North at (39, 31). (In Progress, currently at (10, 3))
4. **North to West via Southern Edge-Bypass**:
   - Walk Left along Row 31 to (28, 31).
   - Climb Eastern Plateau stairs to (28, 26).
   - Descend Eastern Plateau stairs to ground level at (28, 30).
   - Walk Left along Row 29 to (22, 29).
   - Climb Western Plateau stairs to (22, 22).
   - Traverse Western Plateau Left 6 steps to (16, 22).
   - Descend Western Plateau stairs to ground level at (16, 28).
   - Walk Down 2 steps to Row 30, and Left to Column 2/3/4/5/6/7.
   - Walk Down to Row 35 and walk Down to transition directly to Safari Zone West (landing at Columns 20-25 on Row 0 [z=0]).
5. **Safari Zone West Ground-Level Victory**:
   - Land on ground level (z=0) at Column 20-25 Row 0.
   - Walk Left to Column 3 Row 0.
   - Walk Down 3 steps to (3, 3) to enter Secret House and retrieve HM03 Surf.
   - Exit Secret House, walk to (19, 7) on ground level to retrieve Warden's Gold Teeth.
   - Use DIG to warp back to Fuchsia City!

## Socratic Answers & Strategic Revelations (Turn 68225)

### Socratic Question 1: Warden's Gold Teeth Coordinate Contradiction & Verification Protocol
- **Audit of Coordinate Contradictions**:
  1. `(9, 7) [z=0]` is the landing coordinate after jumping down Koga's Column 10 ledge in the northwest ground plains of Safari Zone West (Map 0_219). This was a typo where the landing tile was mistakenly written as the item coordinate.
  2. `(19, 7) [z=0]` is the actual, true overworld coordinate of the Warden's Gold Teeth Pokéball in Safari Zone West (Map 0_219) on ground level z=0.
  3. `(19, 28)` is a copy-paste typo from the Fuchsia City Pokémon Center DIG warp landing location, which was incorrectly written as the Gold Teeth location in the regional notes.
- **True Location**: The Warden's Gold Teeth Pokéball is strictly located at **(19, 7)** in Safari Zone West (Map 0_219).
- **On-Foot Verification Protocol**:
  - Once we enter the northern plains of Safari Zone West at ground level (`z=0`), we will navigate directly to (19, 7) on foot. We will visually confirm the presence of the Pokéball sprite at (19, 7), stand on an adjacent unblocked tile (such as (19, 8) facing Up or (18, 7) facing Right), and press 'A' to pick up the Gold Teeth. We will document the exact Turn number and screen dialogue confirmation in our active logs.

### Socratic Question 2: Southern Edge-Connection Bypass Testing Protocol
- **The Hypothesis**: Walk Down from Safari Zone North (Map 0_218) at Row 35, Columns 2-7 on ground level z=0, transitioning directly to Safari Zone West (Map 0_219) landing on Row 0, Columns 20-25 [z=0] on the open ground plains, completely bypassing Koga's plateau.
- **Why treat as unverified?**: In vanilla Pokémon Red/Blue, Columns 0-9 on Row 35 of Safari Zone North are physically blocked by solid trees and fence assets (`TYPE_2889`). If we assume the shortcut is open and it is actually blocked, we will be forced to backtrack with an expired step budget, failing the run.
- **Empirical On-Foot Testing Protocol**:
  1. Once we descend the Western Plateau in Safari Zone North and land at (16, 28) on ground level, walk Down 2 to (16, 30), Left 4 to (12, 30), and Down 5 to (12, 35).
  2. Visually/physically inspect if Row 35 Columns 2-7 is open or blocked by solid trees.
  3. If open, walk Left to Columns 2-7 and step Down 1 step to trigger the transition.
  4. Verify if we transition into Safari Zone West Row 0 at Columns 20-25 on ground level.
- **Contingency Detour Plan**:
  - If Columns 2-7 on Row 35 of Safari Zone North are physically blocked, we will walk East along Row 33 to Columns 8-9, walk Down through the gap to (9, 35), and transition to Safari Zone West landing at (27, 0) [z=0], then proceed with the standard plateau route climbing stairs at (21, 17).

### Socratic Question 3: Manhattan Distance Tracker Drift & Reconciliation
- **Starting Steps**: 500 steps.
- **Physical Steps Consumed**:
  - Center: 31 steps (leaving 468 steps on entry to East).
  - East Traversal (Turn 68134 to Turn 68221):
    - (0, 23) to (20, 24): 21 steps.
    - (20, 24) to (20, 20): 4 steps.
    - (20, 20) to (12, 20): 8 steps.
    - (12, 20) to (12, 22): 2 steps.
    - (12, 22) to (9, 22): 3 steps.
    - (9, 22) to (9, 10): 12 steps.
    - (9, 10) to (12, 6): 7 steps.
    - (12, 6) to (17, 8): 7 steps.
    - (17, 8) to (21, 7): 5 steps.
    - (21, 7) to (21, 3): 4 steps.
    - (21, 3) to (16, 3): 5 steps.
    - (16, 3) to (10, 3): 6 steps.
    - Total steps consumed in East: 84 steps.
  - Total Steps Remaining: 468 - 84 = 384 actual steps remaining on Turn 68221.
- **Correction**: We have reconciled and confirmed exactly **384 remaining steps** on Turn 68221 (Current Turn 68225). To prevent tracking drift, we will run safari_navigator_agent after every single movement chunk and record actual steps in the log.

## Chronological Movement Log (Run 42)
- Turn 68118: Entered Safari Zone Center (Map 0_220) at (15, 25) with a starting budget of 500 steps. Runs safari_navigator_agent to synchronize to 499 steps.
- Turn 68122: Walked Left 1 step, Up 2 steps, Right 1 step, and Up 6 steps to stand at (15, 17) on clear ground (10 steps used, 489 remaining).
- Turn 68123: Walked Right 3 steps to (18, 17), Up 1 step to (18, 16), and Right 4 steps to (22, 16), bumping twice on Column 18 Row 15 tree wall (8 steps used, 481 remaining).
- Turn 68124: Walked Up 3 steps and Right 6 steps to stand at (28, 13) (9 steps used, 472 remaining).
- Turn 68125: Walked Up 1 step to (28, 12), and bumped Right against (29, 12) tree wall (1 step used, 471 remaining).
- Turn 68129: Walked Up 1 step to (28, 11), and Right 1 step to stand at (29, 11) on the Eastern edge of Safari Zone Center (2 steps used, 469 remaining).
- Turn 68134: Transitioned to Safari Zone East (Map 0_217) at (0, 23). Runs safari_navigator_agent to synchronize to 468 steps (1 step used, 468 remaining).
- Turn 68137: Walked Right 1 step, Down 1 step, and Right 4 steps to stand at (5, 24) on Row 24 (6 steps used, 462 remaining).
- Turn 68138: Walked Right 10 steps along Row 24 to stand at (15, 24) (10 steps used, 452 remaining).
- Turn 68141: Walked Right 4 steps to (19, 24) and encountered a wild Paras in the tall grass (4 steps used, 448 remaining).
- Turn 68142: Successfully selected RUN and escaped the wild Paras, returning to the overworld at (19, 24).
- Turn 68145: Walked Right 1 step along Row 24 to stand at (20, 24) (1 step used, 447 remaining).
- Turn 68146: Walked Up 4 steps from (20, 24) to (20, 20), climbing onto the eastern plateau (4 steps used, 443 remaining).
- Turn 68151: Walked Left 8 steps along Row 20 to stand at (12, 20) on the plateau (8 steps used, 435 remaining).
- Turn 68157: Walked Down 2 steps to descend the western plateau stairs from (12, 20) to ground-level grass at (12, 22) (2 steps used, 433 remaining).
- Turn 68163: Walked Left 3, Up 4 to stand at (9, 18) [z=0] (7 steps used, 426 remaining).
- Turn 68165: Walked Up 8 to stand at (9, 10) [z=0] (8 steps used, 418 remaining).
- Turn 68168: Walked Right 1, Up 2, Right 2, Up 2 to climb northern stairs to stand at (12, 6) [z=1] (7 steps used, 411 remaining).
- Turn 68173: Walked Right 5, Down 2 to descend stairs to stand at (17, 8) [z=0] (7 steps used, 404 remaining).
- Turn 68180: Walked Right 4, Up 1 to stand at (21, 7) [z=0] (5 steps used, 399 remaining).
- Turn 68187: Syncing step budget via safari_navigator_agent (0 steps used, 399 remaining).
- Turn 68214: Walked Left 5 steps from (21, 3) to stand at (16, 3) (5 steps used, 390 remaining).
- Turn 68219: Walked Left 6 steps from (16, 3) to stand at (10, 3) (6 steps used, 384 remaining).
- Turn 68232: Walked Left 1, Down 2, Left 3 to stand at (6, 5) on Row 5 (6 steps used, 378 remaining).
- Turn 68234: Walked Left 6 steps along Row 5 to stand at (0, 5) (6 steps used, 372 remaining).
- Turn 68236: Walked Left 1 step to transition into Safari Zone North, landing at (39, 31) (1 step used, 371 remaining).
- Turn 68245: Walked Left 5 steps along Row 31 from (39, 31) to stand at (34, 31) (5 steps used, 366 remaining).
- Turn 68247: Walked Left 5 steps along Row 31 from (34, 31) to stand at (29, 31) (5 steps used, 361 remaining).
- Turn 68252: Walked Left 1 and Up 4 steps from (29, 31) to stand on the stairs at (28, 27) (5 steps used, 356 remaining).
- Turn 68263: Walked Up 1 step from (28, 27) to stand on the Eastern Plateau at (28, 26) (1 step used, 355 remaining).
- Turn 68267: Walked Down 2 steps to descend the Eastern Plateau stairs to ground level at (28, 28) (2 steps used, 353 remaining).
- Turn 68272: Walked Down 1 step and Left 6 steps to stand at (22, 29) (7 steps used, 346 remaining).
- Turn 68291: Walked Up 6 steps along Column 22 to stand on the Western Plateau stairs at (22, 23) (6 steps used, 340 remaining).