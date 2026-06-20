# Scratchpad: Victory Road Route & Puzzle States
- Route Started: Turn 107326 | Timestamp: Friday, June 19, 2026 at 12:25 PM PDT
- Current Position: (28, 7) on Victory Road 2F East (Map 0_194)

## Updated Flawless Exit Route (Verified Turn 108223)
Because Row 10 and Row 6 on 2F East are solid horizontal barriers, the northeastern section of 2F East is a completely closed pocket. The ONLY way to reach the exit is by transitioning between 2F East and 3F East.

### Step-by-Step Execution Plan:

#### Phase 1: Go UP to 3F East via (27, 7)
1. Stand at (28, 7). Walk Left 1 step to (27, 7) [1 step]
2. Take the ladder at (27, 7) UP to 3F East.

#### Phase 2: Traverse 3F East and Go DOWN to 2F East Plateau via (27, 15)
1. Land at (26, 8) on 3F East.
2. Walk Left 1 step to Column 25 at (25, 8) [1 step]
3. Walk Down 7 steps along Column 25 to Row 15 at (25, 15) [7 steps]
4. Walk Right 2 steps along Row 15 to Column 27 at (27, 15) [2 steps]
5. Take the ladder at (27, 15) DOWN to 2F East.

#### Phase 3: Descend 2F East Plateau and Walk to (23, 7) Ladder
1. Land at (26, 14) on 2F East (on the plateau).
2. Walk Down 1 step to Row 15 at (26, 15) [1 step]
3. Walk Left 5 steps along Row 15 to the plateau stairs at (21, 15) [5 steps]
4. Walk Down 1 step to descend to ground level at (21, 16) [1 step]
5. Walk Down 1 step along Column 21 to Row 17 at (21, 17) [1 step]
6. Walk Right 6 steps along Row 17 to Column 27 at (27, 17) [6 steps]
7. Walk Up 6 steps along Column 27 to Row 11 at (27, 11) [6 steps]
8. Walk Left 4 steps along Row 11 to Column 23 at (23, 11) [4 steps]
9. Walk Up 4 steps along Column 23 to (23, 7) [4 steps]
10. Take the ladder at (23, 7) UP to 3F East.

#### Phase 4: Walk to (23, 7) Ladder and Exit via 2F East
1. Stand at (28, 0) on 3F East.
2. Walk Down 2 steps to (28, 2) [2 steps]
3. Walk Left 5 steps to (23, 2) [5 steps]
4. Walk Down 5 steps to (23, 7) [5 steps]
5. Take the ladder at (23, 7) DOWN to 2F East.
6. On 2F East, walk Right 5 steps to (28, 7) and then North to (28, 1) to Exit!

## Warp Trigger Mechanics (Test Protocol Turn 108307)
- **Hypothesis**: In Generation 1, standing directly on an exit warp tile (such as (28, 0) on Victory Road 3F East) and pressing the exit direction (Up) results in a collision bump because (28, -1) is an impassable boundary, and warps are only triggered by the action of stepping *onto* the warp tile.
- **Test Protocol**:
  1. Stand at (28, 0). Press Down to step off the warp onto (28, 1).
  2. From (28, 1), press Up to step onto (28, 0), which should trigger the map transition to Route 23 North / Indigo Plateau.
- **Results**: (Pending execution)
- Turn 108395: Testing Warp Trigger Mechanics at (28, 0). Standing at (28, 0) facing Up, let's step Down to (28, 1) and then step Up to (28, 0) to verify if stepping onto (28, 0) triggers the transition to Route 23 North / Indigo Plateau.
- Turn 108428: Tested stepping Up at (28, 0) on 3F East, which resulted in a collision bump. This confirms (28, 0) on 3F East is NOT a functional exit warp.
- Turn 108537 Breakthrough: Queried map specifications and discovered that the actual exit of Victory Road to Route 23 North / Indigo Plateau is a cave warp located on the 3rd Floor (3F East) at coordinates (23, 1). 
- Active Plan: Backtrack via the ladder at (23, 7) on 2F East UP to 3F East, then walk north along Column 23 directly to (23, 1) to exit Victory Road!
## Breakthrough Path to (23, 7) Ladder (Turn 108551)
We are at (23, 3) on 2F East. (23, 4) is blocked by a wall of TYPE_2889.
To bypass this wall, we must go Left via Column 17:
1. Walk Left 6 steps to (17, 3) via (22, 3), (21, 3), (20, 3), (19, 3), and (18, 3).
2. Walk Down 2 steps to (17, 5) via (17, 4).
3. Walk Right 6 steps to (23, 5) via (18, 5), (19, 5), (20, 5), (21, 5), and (22, 5).
4. Walk Down 2 steps to (23, 7) via (23, 6) to take the ladder UP to 3F East.
5. On 3F East, walk Up to the exit at (23, 1).
- Turn 108576: Arrived on Victory Road 3F East at (23, 7). The exit warp is located at (23, 1) on this floor.
- Path to exit at (23, 1):
  - Walk Up 6 steps along Column 23: (23, 7) -> (23, 6) -> (23, 5) -> (23, 4) -> (23, 3) -> (23, 2) -> (23, 1).
  - Row 1 has the cave exit warp. Stepping onto (23, 1) should trigger the transition to Route 23 North / Indigo Plateau.