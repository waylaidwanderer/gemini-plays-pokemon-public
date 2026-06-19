# Scratchpad: Victory Road Route & Puzzle States
- Current Turn: 105235
- Current Position: (23, 7) on Map 0_194 (Victory Road 2F East)

## Real Victory Road Exit Route Analysis
- The northern ground floor section of 2F East (Rows 1-5, Columns 19-27) is completely isolated on foot from the southern section by:
  - Row 6 solid wall (Columns 24-28) on the east.
  - Row 4 solid wall (Columns 19-24) on the west, and (24, 5) solid wall.
- There is no direct walk path on 2F East from the southern half to the northern half.
- The ONLY way to reach the northern half of 2F East is to:
  1. Take the ladder at (27, 7) on 2F East UP to 3F East (lands at (26, 8) on 3F East).
  2. Walk north on 3F East to the top-right corner where a ladder leads DOWN to the northern half of 2F East.
  3. This drops us inside the isolated northern pocket of 2F East where we can walk to the exit doorway at (28, 1).

## Live Execution Logs (Run 53):
- Turn 104711: Warped back UP from 2F East to 3F East, landing at (26, 8).
- Turn 104712: Walked to (25, 10).
- Turn 104714: Activated STRENGTH and pushed Boulder C2 Left twice from (24, 10) to (22, 10), clearing Column 23 at Row 10. Player is at (24, 10).
- Turn 104717: Fled wild Machop.
- Turn 104726: Walked to (20, 13) through the cleared corridor. Fled wild Machop.
- Turn 104835: Successfully transitioned back down to Victory Road 2F East. Current Position is (23, 7). Preparing to walk to (25, 3) via Row 5 and Column 22.
- Turn 105110: Confirmed position at (23, 7) on 2F East. Preparing to walk to the ladder at (27, 7) to transition back up to 3F East and navigate to the northern section.
- Turn 105185: Walked from (23, 7) to (21, 3) on 3F East.
- Turn 105194: Activated STRENGTH and pushed the boulder at (22, 3) Right 1 step to (23, 3).
- Turn 105202: Walked to (25, 2) after fleeing a wild Zubat.
- Turn 105207: Preparing to walk back to the ladder at (23, 7) on 3F East to go down to 2F East.
- Turn 105235: Standing at (23, 7) on 2F East. Ready to head to (27, 7) via the open gate at (24, 8).
- Turn 105237: Took the ladder at (23, 7) UP to 3F East (lands at (23, 7) on 3F East).
- Turn 105244: Standing at (23, 8) on 3F East. Discovered that (24, 8) is a rock wall (TYPE_2889), so Row 8 on 3F East does not connect Column 23 to Column 25.
- Turn 105257: Walked back Up to the ladder at (23, 7) and went DOWN to 2F East.
- Turn 105264: Standing at (23, 8) on 2F East. Preparing to walk to the other ladder at (27, 7) on 2F East via Row 9.

## Path to Ladder (27, 7) on 2F East:
- From (23, 8), walk Down 1 to (23, 9).
- Walk Right 4 to (27, 9).
- Walk Up 2 to (27, 7) (ladder).
- Turn 105277: Stepped Down to (23, 8) and triggered a wild Machop encounter. Preparing to flee.
- Turn 105362: Arrived at (22, 4) on 3F East adjacent to the reset boulder at (22, 3). Preparing to activate STRENGTH on ROCKY and push the boulder Up 1 tile to (22, 2) to open the Row 3/Row 2 pathway.
- Turn 105394: Position (23, 2) on 3F East. Boulder successfully pushed to (22, 2). Next, we will cross to the east side of 3F East by walking Right to (27, 2). From there, we will walk Down to the ladder at (26, 8) to descend into the northern isolated ground pocket of 2F East.
- Step-by-step route to (26, 8):
  1. Walk Right 4 steps to (27, 2).
  2. Walk Down 6 steps to (27, 8).
  3. Walk Left 1 step to (26, 8).
  4. Interact with the ladder at (26, 8) to go down to 2F East.

## Verified True Route to Victory Road Exit (Turn 105427):
1. Walk from current position (27, 2) on 3F East to the ladder at (23, 7) and go DOWN to 2F East.
2. Walk on 2F East to the plateau stairs, climb up, and walk east through the open gate to the ladder at (26, 14).
3. Take the ladder at (26, 14) UP to 3F East (lands at (27, 15)).
4. On 3F East, walk to (26, 8) via the cleared Row 10 passage (Boulder C2 is already pushed).
5. Take the ladder at (26, 8) DOWN to 2F East (lands at (27, 7) inside the isolated pocket).
6. Walk north to the exit at (28, 1)!

## COMPLETE MACRO ROUTE TO VICTORY ROAD EXIT (Turn 105441):
1. Walk from (21, 11) to (23, 7) on 2F East and go UP to 3F East.
2. From (23, 7) on 3F East, walk West to 3F West.
3. On 3F West, take the stairs down to 2F West.
4. On 2F West, walk East to the main area of 2F East.
5. On 2F East, walk to (21, 16) and walk Up onto the plateau stairs at (21, 15).
6. Walk East along the plateau through the open gate to the ladder at (25, 14) and go UP to 3F East (lands at (27, 15)).
7. On 3F East, walk to the ladder at (26, 8) via:
   - Walk West along Row 13 to Column 23.
   - Walk North along Column 23 to Row 10 (passable since Boulder C2 was pushed to (22, 10)).
   - Walk East to Column 26.
   - Walk North to (26, 8).
8. Take the ladder at (26, 8) DOWN to 2F East (lands at (27, 7) inside the isolated northern pocket).
9. Walk north to the exit at (28, 1)!