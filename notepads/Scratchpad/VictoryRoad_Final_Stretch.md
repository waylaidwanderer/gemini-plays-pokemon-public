# Scratchpad: Victory Road Final Stretch Route
- Created: Turn 104205

## The Reset Rule Discovered:
- Taking a ladder (map transition) resets all boulders on Victory Road.
- Thus, solving the 2F West boulder puzzle, taking the ladder to 3F, and then taking a ladder back to 2F East will reset the 2F West boulder, closing the gate at (24, 8) on 2F East.
- **The Correct Solution**: We must solve the 2F West boulder puzzle, and then walk *entirely on 2F* (without taking any ladders) across the plateau to 2F East, ensuring the boulder stays on the switch and the gate at (24, 8) remains open.

## Step-by-Step Execution Plan:
1. Backtrack to 2F West:
   - From current (23, 7) on 3F East, walk Up 6 steps to (23, 1).
   - Walk Left 17 steps to (6, 1).
   - Walk Down 1 step to (6, 2).
   - Walk Left 4 steps to (2, 2).
   - Walk Up 2 steps to (2, 0).
   - Take the ladder DOWN to 2F West.
2. Solve 2F West Boulder:
   - Stand at (5, 4) facing Down and activate STRENGTH.
   - Push Boulder B1 (at (5, 5)) Down to (5, 7).
   - Walk around the boulder to (6, 7) facing Left.
   - Push Boulder B1 Left to (3, 7).
   - Push Boulder B1 Down to (3, 15).
   - Walk to (3, 16) and push Boulder B1 Left onto the switch at (1, 16).
3. Walk Across 2F to 2F East (No Ladders!):
   - Walk East across the 2F plateau corridor to 2F East.
   - Walk Down the stairs at (21, 15) to ground level.
   - Walk to (23, 7) on 2F East.
4. Exit Victory Road:
   - Walk through the open gate at (24, 8) to (27, 7).
   - Take the ladder UP at (27, 7) to 3F East (27, 15).
   - Walk to the exit!
## Live Execution Logs (2F West Boulder B1 Push):
- Turn 104258: Arrived at (3, 8) facing Down. STRENGTH was inactive due to map transition.
- Turn 104262: Activated STRENGTH from the Pokémon party menu using ROCKY (Geodude).
- Turn 104267: Pressed Down, Down. Pushed Boulder B1 from (3, 9) to (3, 10). Player stepped to (3, 9).
- Turn 104274: Pressed Down, Down, Down, Down. Pushed Boulder B1 from (3, 10) to (3, 12). Player stepped to (3, 11).
## Live Execution Logs (2F West Boulder B1 Solved and Walking East):
- Turn 104312: Stood at (5, 10). Plotted path across plateau to (21, 15).
- Path: Up 2 to (5, 8) -> Right 8 to (13, 8) -> Down 4 to (13, 12) -> Right 8 to (21, 12) -> Down 3 to (21, 15) -> descend.
- Turn 104332: Arrived on 3F East at (27, 15). Plotted path to the (23, 7) ladder: Up 13 to (27, 2) -> Left 4 to (23, 2) -> Down 5 to (23, 7) -> descend.
## Turn 104394 Discovery:
- Verified that Victory Road 3F East (Map 0_198) has only 4 warps, all leading to Victory Road 2F (Map 0_194).
- Verified that the exit of Victory Road to Route 23/Indigo Plateau is located at (29, 1) on Victory Road 2F East (Map 0_194, Warp 5).
- Verified that taking the ladder at (26, 8) on 3F East transitions the player down to 2F East at (27, 7).
- Since we have successfully solved the 2F West boulder puzzle, the gate on 2F East at (24, 8) is permanently open. This allows us to descend the ladder at (26, 8) on 3F East to (27, 7) on 2F East, and then walk directly to the (29, 1) exit warp on 2F East without any barriers!
- Our path from current position (24, 10) to the ladder at (26, 8) on 3F East is:
  1. Right to (25, 10)
  2. Up to (25, 9)
  3. Right to (26, 9)
  4. Up to (26, 8) (this activates the ladder)
- Let's execute this sequence now.
## Turn 104407 Analysis:
- Position: (25, 8) on Victory Road 2F (Map 0_194).
- Situation: The gate at (24, 8) is closed (shows TYPE_2889) because our transition from 2F -> 3F -> 2F reset all overworld boulders. We are on the East side of the gate, so we cannot walk Left to the rest of the map.
- Exit Strategy:
  1. Walk to (27, 7) (Up 1, Right 2).
  2. Take the ladder UP to 3F East (lands us at (26, 8) on 3F East).
  3. Walk from 3F East to 3F West.
  4. Descend the ladder at (2, 0) on 3F West to 2F West.
  5. Solve the 2F West boulder puzzle again (pushing Boulder B1 onto Switch B1).
  6. Walk across 2F from 2F West to 2F East WITHOUT taking any ladders.
  7. On 2F East, walk through the open gate at (24, 8) to (27, 7).
  8. Take the ladder UP at (27, 7) to 3F East (26, 8).
  9. Walk from (26, 8) to the exit of Victory Road (Route 23/Indigo Plateau).
- Let's begin by walking to the ladder at (27, 7) on 2F East.
  - From (25, 8), the ladder at (27, 7) is at (27, 7).
  - Path: Up to (25, 7) [1 step], Right to (26, 7) [1 step], Right to (27, 7) [1 step] -> this steps onto the ladder.
  - Total steps: 3. Button sequence: ["Up", "Right", "Right"]