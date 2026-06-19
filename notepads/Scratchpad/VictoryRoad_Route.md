# Scratchpad: Victory Road Route & Puzzle States
- Current Turn: 105036
- Current Position: (27, 2) on Map 0_198 (Victory Road 3F East)

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
  - From (23, 7) on 2F East, walk Up 2 steps to (23, 5).
  - Walk Right 3 steps to (26, 5) to bypass the Row 4 solid wall on the west.
  - Walk Up 4 steps along Column 26 to Row 1 at (26, 1).
  - Walk Right 2 steps to (28, 1) or (29, 1) to exit to Route 23/Indigo Plateau!

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

## Passability Test: Column 22 Row 4 (Turn 104879-104884)
- **Hypothesis**: The Scratchpad route says "bypass barriers via Column 22 to Row 3". However, (22, 4) is labeled TYPE_2889 (solid rock wall) on screen. We hypothesize that Column 22 on Row 4 is impassable and we cannot walk Up past Row 4 to Row 3 on the west side.
- **Testing Plan**: From (23, 8), walk Left to (22, 8), Up 3 steps to (22, 5), and attempt to walk Up to (22, 4). We will observe if we bump or step forward.
- **Turn 104884**: Visually inspected screen. Row 4 is indeed a continuous line of TYPE_2889 (solid rock wall) from (19, 4) to (24, 4), and Column 24 is a solid rock wall from (24, 4) to (24, 10). Row 6 is a solid rock wall from (24, 6) to (28, 6).
- **Result**: Row 4 on the west side is indeed completely impassable! The old route of "bypass barriers via Column 22 to Row 3" on 2F East is confirmed physically impossible without going to another floor.

## Real Route Analysis: How do we reach the exit (28, 1)?
Let's trace how the map flows.
1. The exit is at (28, 1) on 2F East.
2. The area around (28, 1) (Rows 1-5, Columns 25-28) is bounded on the south by Row 6 (which is a solid rock wall at Columns 24-28).
3. Wait, is there a ladder in that northern section (Rows 1-5)? Let's check!
   Is there any ladder there?
   The map markers do not list any ladder in Rows 1-5 on 2F East.
   Wait, let's verify if there is a ladder on 3F East that goes DOWN to the northern section of 2F East.
   Wait, where are the ladders on 3F East (Map 0_198)?
   - (23, 7) goes to 2F East (23, 7) [inside the west side, below the Row 4 wall].
   - (27, 7) goes to 3F East (26, 8). Wait! (27, 7) on 2F is below the Row 6 wall.
   Wait, what about 2F East?
   Let's check if there is another ladder/warp on 3F East or 2F East.
   Let's use `search_notepads` to find all ladder and warp locations in Victory Road.
## Solving Victory Road Exit (3F East northern bypass)
- Current Turn: 104961
- Current Position: (23, 7) on Victory Road 3F East (Map 0_198)

- **Verification of Route**:
  - We are currently at (23, 7) on 3F East.
  - To bypass the Column 24 vertical wall (which blocks Rows 11-15), we must go around via Row 2/3.
  - Boulder C1 (initially at (22, 3)) has reset because of our map transition (2F -> 3F).
  - It is currently sitting at (22, 3), blocking Row 3.
  - Let's walk to (21, 3) and push it Right to (23, 3) and then bypass it.
  - **Steps to (21, 3)**:
    - From (23, 7), walk Left 2 steps to (21, 7).
    - Walk Up 4 steps to (21, 3).