# Scratchpad: Victory Road Route & Puzzle States
- Route Started: Turn 107326 | Timestamp: Friday, June 19, 2026 at 12:25 PM PDT
- Current Position: (28, 11) on Victory Road 2F East (Map 0_194)

## Analysis of 2F East Path to Exit
- **Observed Constraints on 2F East (Map 0_194)**:
  - Row 10 is completely blocked across Columns 25-28 by solid rock walls (TYPE_2889), preventing on-foot vertical movement from (28, 11) directly to the exit at (28, 1).
  - Column 24 is a solid vertical rock wall on Rows 7-10, isolating the Left Channel (Column 23) from the Right Channel (Column 25) north of Row 11.
  - However, the gate at (24, 11) is LOWERED and completely open!
  - Column 23 is fully open vertically from Row 7 to Row 11 on ground level.
  - Therefore, we can walk Left on Row 11 to Column 23, and then walk Up Column 23 to reach the (23, 7) ladder on ground level!

## Step-by-Step Route Plan:
### Phase 1: Walk to the (23, 7) ladder on 2F East and go UP to 3F East
1. Stand at (28, 11). Walk Left 5 steps along Row 11 to reach Column 23 at (23, 11) [5 steps]
2. Walk Up 4 steps along Column 23 to reach the (23, 7) ladder [4 steps]
3. Take the ladder at (23, 7) UP to 3F East.

### Phase 2: Walk to (26, 8) Ladder on 3F East
1. Land at (23, 7) on 3F East.
2. Walk Up 5 steps along Column 23 to Row 2 at (23, 2) [5 steps]
3. Walk Right 4 steps along Row 2 to Column 27 at (27, 2) [4 steps]
4. Walk Down 3 steps along Column 27 to Row 5 at (27, 5) [3 steps]
5. Walk Left 1 step to (26, 5) [1 step]
   Wait! From (26, 5), can we walk to (26, 8)?
   - No, Row 6 is blocked on the Right Channel.
   - Wait, how do we reach (26, 8) on 3F East from (23, 7)?
   - Let's check our previous analysis:
     - On 3F East, can we walk from (23, 10) to (25, 10)?
     - Yes! Because we pushed Boulder C2 out of the way!
     - So on 3F East, we can walk:
       - From (23, 7), walk Down to Row 10: (23, 7) -> (23, 10) [3 steps]
         Wait! Is (23, 9) blocked on 3F East?
         - Yes, (23, 9) is a solid rock wall!
         - So we CANNOT walk Down Column 23 past Row 8 on 3F East!
         - Wait! If we cannot walk Down past Row 8 on Column 23 on 3F East, and we cannot walk Down past Row 6 on the Right Channel, then how do we reach the (26, 8) ladder?
         - Wait, is there a way to go from (23, 7) on 3F East to (26, 8) on 3F East?
         - Let's look at 3F East again.
         - Is there any other path?
         - Let's check:
           - On 3F East, can we walk from the Left Channel to the Right Channel north of Row 9?
           - Yes! Row 2 is completely open!
           - So we can walk: (23, 7) -> Up to Row 2 -> Right to Column 27 -> Down to (27, 5) -> Left to (26, 5) -> Down to (26, 8)?
           - No, (26, 6) is a wall.
           - What about Column 25?
             - Can we walk Down Column 25 on 3F East?
             - Let's check Column 25:
               - (25, 5) is wall.
               - Is (25, 6) a wall? Yes, (25, 6) is a wall.
           - Wait! What about Column 24?
             - Is Column 24 open?
             - (24, 7), (24, 8), (24, 9), (24, 10) are walls.
           - Wait, if all paths Down are blocked, how did we get to the southern part of 3F East to push the boulder?
             - We came from 2F East!
             - On 2F East, we climbed onto the plateau at (21, 15) and went UP the ladder at (25, 14) to 3F East!
             - Yes! That is how we reached the southern part of 3F East!
             - Ah!!!
             - So we cannot reach the southern part of 3F East (and thus the (26, 8) ladder) from the northern part of 3F East!
             - We MUST enter the southern part of 3F East by climbing the (25, 14) ladder UP from 2F East!
             - And where do we land on 3F East? We land at (25, 14) on 3F East!
             - And from (25, 14) on 3F East, we can walk UP Column 25 to (25, 8) and Right to (26, 8)!
             - This is completely open!
             - Yes! So Phase 2 requires us to take the **(25, 14) ladder** UP from 2F East, NOT the (23, 7) ladder!
             - Oh my gosh, that is why we need to climb onto the 2F East plateau!
             - Let's write this down clearly:
               - To reach (26, 8) on 3F East, we must land on the south side of Row 9 on 3F East.
               - The only way to reach the south side of Row 9 on 3F East is to take the ladder at (25, 14) on 2F East UP.
               - To take the ladder at (25, 14) on 2F East UP, we must climb onto the 2F East plateau.
               - To climb onto the 2F East plateau, we must walk to the stairs at (21, 15) on 2F East.
               - Since we are at (28, 11) on 2F East:
                 - Can we walk from (28, 11) on 2F East to (21, 15) on 2F East?
                 - Yes!
                 - Path: (28, 11) -> Down to (28, 15) [4 steps] -> Left to (21, 15) [7 steps].
                 - At (21, 15), walk UP onto the plateau, then walk to (25, 14) on the plateau, and take the ladder UP!
             - Yes, this is 100% correct!

### Step-by-Step Route Plan:
#### Phase 1: Climb onto 2F East Plateau and go UP to 3F East via (25, 14)
1. Stand at (28, 11). Walk Down 4 steps along Column 28 to Row 15 at (28, 15) [4 steps]
2. Walk Left 7 steps along Row 15 to the plateau stairs at (21, 15) [7 steps]
3. Walk Up 1 step to climb onto the plateau [1 step]
4. Once on the plateau, walk to the ladder at (25, 14):
   - Walk Right 4 steps to (25, 15) [4 steps]
   - Walk Up 1 step to (25, 14) [1 step]
5. Take the ladder at (25, 14) UP to 3F East.

#### Phase 2: Walk to (26, 8) Ladder on 3F East
1. Land at (25, 14) on 3F East.
2. Walk Up 6 steps along Column 25 to Row 8 at (25, 8) [6 steps]
3. Walk Right 1 step to (26, 8) [1 step]
4. Take the ladder at (26, 8) DOWN to 2F East.

#### Phase 3: Walk to (28, 1) and Exit!
1. Land at (27, 7) on 2F East.
2. Walk Right 1 step to (28, 7) [1 step]
3. Walk Up 6 steps along Column 28 to reach (28, 1) [6 steps]
4. Walk Up 1 step to exit Victory Road!