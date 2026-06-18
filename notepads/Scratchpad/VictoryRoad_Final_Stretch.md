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