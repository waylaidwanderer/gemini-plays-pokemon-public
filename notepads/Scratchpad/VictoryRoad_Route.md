# Scratchpad: Victory Road Route & Puzzle States
- Current Turn: 104817
- Current Position: (27, 1) on Map 0_194 (Victory Road 2F East)

## Flawless Victory Exit Plan (No Ladders/Detours needed on 2F West!)
- **Insight**: We do not need the gate at (24, 8) on 2F East to be open to reach the exit warp at (29, 1)!
- **Why**: 
  - (29, 1) is on the ground level of 2F East, inside the isolated northern pocket (Rows 1-11, Columns 19-27).
  - The ladder at (23, 7) on 3F East leads directly down to (23, 7) on 2F East, which is INSIDE this same northern pocket!
  - Therefore, if we take the ladder at (23, 7) on 3F East DOWN to 2F East, we land in the northern pocket at (23, 7) and can walk directly to (29, 1) on foot without needing any open gates!
- **Path from Current Position (20, 13) to (23, 7) on 3F East**:
  - We have already pushed Boulder C2 at (24, 10) to (22, 10), clearing the Column 23 path!
  - From (20, 13), walk West along the Row 13 ground corridor to Column 15.
  - Walk Up Column 15 to Row 11.
  - Walk East along Row 11 to Column 20.
  - Walk Up Column 20 to Row 7.
  - Walk East along Row 7 to the ladder at (23, 7).
  - Descend the ladder to 2F East at (23, 7).
- **Final Exit Segment (2F East)**:
  - From (23, 7), walk Up to Row 5, bypass barriers via Column 22 to Row 3, walk East along Row 3 to Column 28, walk Up to Row 1, and walk Right to (29, 1) to exit to Route 23/Indigo Plateau!

## Live Execution Logs (Run 53):
- Turn 104711: Warped back UP from 2F East to 3F East, landing at (26, 8).
- Turn 104712: Walked to (25, 10).
- Turn 104714: Activated STRENGTH and pushed Boulder C2 Left twice from (24, 10) to (22, 10), clearing Column 23 at Row 10. Player is at (24, 10).
- Turn 104717: Fled wild Machop.
- Turn 104726: Walked to (20, 13) through the cleared corridor. Fled wild Machop.
- Turn 104835: Successfully transitioned back down to Victory Road 2F East. Current Position is (23, 7). Preparing to walk to (25, 3) via Row 5 and Column 22.

## Passability Test: Column 22 Row 4 (Turn 104879)
- **Hypothesis**: The Scratchpad route says "bypass barriers via Column 22 to Row 3". However, (22, 4) is labeled TYPE_2889 (solid rock wall) on screen. We hypothesize that Column 22 on Row 4 is impassable and we cannot walk Up past Row 4 to Row 3 on the west side.
- **Testing Plan**: From (23, 8), walk Left to (22, 8), Up 3 steps to (22, 5), and attempt to walk Up to (22, 4). We will observe if we bump or step forward.
- **Turn 104879**: Started test. Walking Left to (22, 8).