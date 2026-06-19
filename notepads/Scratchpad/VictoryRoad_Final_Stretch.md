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
## Turn 104608 Current Reality:
- We have successfully solved the 2F West boulder puzzle AGAIN!
- Progress:
  1. Walked Down 3 steps to (5, 14). [x]
  2. Activated STRENGTH using Geodude (ROCKY). [x]
  3. Pushed Boulder Left to (3, 14). Player is at (5, 14) facing Left, and boulder is at (3, 14). [x]
  4. Walk to (3, 13) via (4, 14) and (4, 13). [x]
  5. Push Boulder Down to (3, 15). [x]
  6. Walk Down to (3, 14) and push Boulder Down to (3, 16). [x]
  7. Walk to (4, 16) via (3, 15) and (4, 15). [x]
  8. Stand at (4, 16) facing Left, push Boulder Left to (2, 16). [x]
  9. Walk Left to (3, 16), push Boulder Left to (1, 16) (Switch B1). [x]
  10. Switch B1 is permanently pressed! [x]
  11. Walk across 2F to 2F East without taking any ladders. [Active]
- Let's plot our exact path back to the plateau stairs:
  - We are at (3, 16) facing Left.
  - Up to (3, 15) [1 step]
  - Up to (3, 14) [1 step]
  - Right to (4, 14) [1 step]
  - Up to (4, 13) [1 step]
  - Right to (5, 13) [1 step]
  - Up to (5, 12) [1 step]
  - Up to (5, 11) [1 step]
  - Up to (5, 10) [1 step] (This takes us UP to the plateau stairs)
- Total steps: 8. Button sequence: ["Up", "Up", "Right", "Up", "Right", "Up", "Up", "Up"]
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
- Turn 104528: Arrived on ground level of 2F East at (21, 16). The boulder is indeed at its default position (23, 16) due to the map reset. We must push the boulder West onto Switch B2 at (9, 16) to open the barrier, but wait, do we have to?
Let's analyze if Switch B2 controls the gate on Row 16 or somewhere else.
Wait! In Turn 104407: 'The gate at (24, 8) is closed (shows TYPE_2889) because our transition from 2F -> 3F -> 2F reset all overworld boulders.'
Wait, is the gate at (24, 8) opened by Switch B1 (2F West) or Switch B2 (2F East)?
According to our notes:
- Switch B1 (1, 16): 'opened the gate on 2F East.'
- Switch B2 (9, 16): 'permanently lowered the northeast barrier.'
Wait, if the gate at (24, 8) is closed, does it mean Switch B1 was reset?
Yes, we took a ladder! The map transition reset ALL overworld boulders, including the one on Switch B1 at (1, 16).
Wait, but did we solve the 2F West boulder puzzle on Turn 104486 (which was AFTER we transitioned back to 2F West)?
Yes! On Turn 104486, we pushed the boulder B1 onto Switch B1.
Then on Turn 104500, we climbed the stairs at (5, 10) to access the plateau, and walked across the plateau to (21, 15) and descended to (21, 16).
Since we walked across the plateau, we DID NOT transition maps! We stayed on 2F the entire time.
So Switch B1 at (1, 16) is STILL pressed by the boulder!
Wait, but is Switch B2 at (9, 16) pressed?
No, the 2F East boulder at (23, 16) reset to its default position when we transitioned maps earlier (before solving the 2F West puzzle).
Wait, do we need Switch B2 to be pressed to reach the exit?
Let's look at the exit route:
- Exit of Victory Road is at (29, 1) on 2F East.
- To get to (29, 1) on 2F East, we must walk through the gate at (24, 8).
- Does the gate at (24, 8) require Switch B1 or Switch B2?
Let's check `Scratchpad/VictoryRoad_Final_Stretch`:
'13. On 2F West, activate STRENGTH and push Boulder B1 at (5, 5) onto Switch B1 at (1, 16) to permanently lower the Row 8 gate at (24, 8) on 2F East. [x] (Completed on Turn 103986)'
Wait, but is there any other barrier blocking our path from (21, 16) to (29, 1)?
Let's trace the path from (21, 16) to (29, 1):
- We are at (21, 16).
- If we go Right:
  - (22, 16): TYPE_3fe2 (passable)
  - (23, 16): occupied by the yellow boulder.
- Can we walk around the boulder at (23, 16)?
  - Below: (23, 17) is TYPE_3fe2 (passable)
  - So we can walk: (21, 16) -> Right to (22, 16) -> Down to (22, 17) -> Right to (23, 17) -> Right to (24, 17) -> Up to (24, 16) -> Up to (24, 15)?
  Wait, let's look at the screen!
  Row 17:
  (21, 17), (22, 17), (23, 17), (24, 17), (25, 17), (26, 17) are all TYPE_3fe2!
  And below Row 17, is there a wall? Yes, Row 18 has solid rock walls.
  So Row 17 is a wide open, completely passable corridor!
  So we can easily walk around the boulder at (23, 16) via Row 17!
  Let's see:
  From (21, 16) -> Right to (22, 16) -> Down to (22, 17) -> Right 4 steps to (26, 17) -> Up to (26, 16) -> Up to (26, 15) -> Up to (26, 14)?
  Wait! Let's check what is at (25, 14):
  (25, 14) is TYPE_3fe2 (passable ground tile). In our markers, it says: `(25, 14): 🪜 Climb-up Plateau Stairs`? No, wait!
  Let's look at `<CurrentScreen turn="104528">`:
  (25, 14) is TYPE_3fe2 but it has a ladder icon!
  Wait, what is at (25, 14)? Let's check:
  Ah, (25, 14) is TYPE_3fe2 with a ladder on it.
  Wait, is (25, 14) a ladder to 3F East? Yes, our notes say: `Take the (25, 14) ladder UP to 3F East at (27, 15)`.
  But wait! We don't want to take any ladders that would reset our boulder!
  Wait, do we need to take that ladder?
  No, we want to walk to (24, 8) and go through the gate!
  Wait, let's check where the gate at (24, 8) is located.
  Is the gate at (24, 8) on ground level?
  Yes, (24, 8) is on the ground level of 2F East.
  Wait! Can we walk from (21, 16) to (24, 8) on ground level?
  Let's look at the map/notes:
  `Locations/VictoryRoad_2F` says:
  "2F East Isolated Northern Ground Pocket (Verified Turn 102524)
  - Geography: The northern ground floor of 2F East (Columns 19-27, Rows 7-11) is a completely closed, isolated pocket on ground level (z=0).
  - Verification:
    - Column 23 Row 12 is blocked by the elevated plateau cliff of Koga's plateau.
    - Column 15 is occupied by continuous solid rock walls of TYPE_2889 across Rows 8-11, completely blocking western ground-level access.
    - The entire width from Column 19 to Column 27 on Rows 12-14 is elevated plateau (z=1), blocking southern ground-level traversal.
    - The only way to enter or exit this pocket is via the ladder at (23, 7), which connects Bidirectionally to 3F East (23, 7). Taking this ladder DOWN to 2F East leads to a dead end with no other paths."
  Oh!!!
  Read that geography carefully:
  "The northern ground floor of 2F East (Columns 19-27, Rows 7-11) is a completely closed, isolated pocket on ground level (z=0).
  ...
  The only way to enter or exit this pocket is via the ladder at (23, 7), which connects Bidirectionally to 3F East (23, 7). Taking this ladder DOWN to 2F East leads to a dead end with no other paths."
  Wait, if the northern ground floor (Rows 7-11, where (23, 7), (24, 8), and (27, 7) are) is completely isolated from the southern ground floor (Row 16 and below) by the elevated plateau (Rows 12-14), then we CANNOT walk on ground level from Row 16 to Row 8!
  Let's verify this.
  Can we climb onto the plateau?
  Yes, we can climb back onto the plateau via (21, 15) stairs!
  Wait! If we climb onto the plateau, can we walk to the north side of the plateau?
  Where does the plateau go?
  Let's look at the plateau corridor:
  "At Row 12 and 13, the plateau corridor turns East across Columns 15 to 18."
  Wait, does the plateau extend further East?
  Let's look at the tiles on `<CurrentScreen turn="104528">`:
  Row 12:
  (18, 12): TYPE_2770 (plateau)
  (19, 12): TYPE_2770
  (20, 12): TYPE_2770
  (21, 12): TYPE_2770
  (22, 12): TYPE_2889 (solid rock wall)
  Ah! (22, 12) is TYPE_2889 solid rock! So the plateau is blocked on the East.
  Wait, is there any other part of the plateau?
  What about Row 14?
  - (21, 14): TYPE_2770 (plateau)
  - (22, 14): TYPE_2770
  - (23, 14): TYPE_2770
  - (24, 14): TYPE_2770
  - (25, 14): TYPE_3fe2 (ladder)
  - (26, 14): TYPE_2770 (plateau)
  Ah! The plateau extends East on Row 14!
  And at (25, 14), there is a ladder.
  Let's check if the plateau at Row 14 connects to anything else.
  Wait, does the plateau connect to the northern ground pocket?
  No, the plateau is elevated (z=1). The northern ground pocket is at ground level (z=0).
  And the exit at (29, 1) is at ground level.
  Wait! Let's check how we get to the exit.
  Where does the ladder at (25, 14) lead?
  "leads directly UP to 3F East (Map 0_198) at (27, 15)"
  And from 3F East (27, 15), where can we go?
  "On 3F East, walk from (27, 15) to (23, 7) via Row 13 / Column 20 (bypassing the Row 9 wall and Column 24 boulder) and take the ladder DOWN to 2F East."
  Wait! If we take the ladder at (25, 14) to 3F East, does that count as a map transition?
  Yes, 2F to 3F is a map transition.
  But wait! Does taking a ladder reset the boulders?
  Yes, taking a ladder resets the boulders!
  But wait, if we take the ladder UP to 3F, and then walk to the ladder at (23, 7) and go DOWN, does that reset the 2F West boulder?
  Wait! Let's think:
  If taking a ladder resets all boulders, then taking ANY ladder (including (25, 14) or (23, 7)) will reset the 2F West boulder!
  Wait, is that true?
  Let's check our notes!
  `Scratchpad/VictoryRoad_Final_Stretch`:
  "Taking a ladder (map transition) resets all boulders on Victory Road.
  Thus, solving the 2F West boulder puzzle, taking the ladder to 3F, and then taking a ladder back to 2F East will reset the 2F West boulder, closing the gate at (24, 8) on 2F East.
  **The Correct Solution**: We must solve the 2F West boulder puzzle, and then walk *entirely on 2F* (without taking any ladders) across the plateau to 2F East, ensuring the boulder stays on the switch and the gate at (24, 8) remains open."
  Wait, if we must walk entirely on 2F to 2F East, let's look at where the open gate is!
  Wait, the open gate is at (24, 8).
  If we are on 2F West, and we walk across the 2F plateau entirely on 2F, we end up on 2F East.
  Once we are on 2F East, can we reach the gate at (24, 8) without taking any ladders?
  Let's check if (24, 8) is on the ground level, and how we get to it.
  Wait! Let's read `Scratchpad/VictoryRoad_Exit_Verification`:
  "Take the ladder UP at (27, 7) to 3F East (27, 15). Walk to the exit!"
  Wait, where is the exit exactly?
  Is the exit at (29, 1) on 2F East?
  Let's look at `Scratchpad/VictoryRoad_Exit_Verification` again:
  "Thus, the actual exit to Route 23 is on Victory Road 2F East at (29, 1), NOT on Victory Road 3F East.
  We must walk south from (27, 0) to (27, 15) on Victory Road 3F, take the ladder down to 2F East, and walk to (29, 1) on 2F East to exit Victory Road."
  Wait! Let's read `Turn 104394 Discovery`:
  "Verified that the exit of Victory Road to Route 23/Indigo Plateau is located at (29, 1) on Victory Road 2F East (Map 0_194, Warp 5).
  Verified that taking the ladder at (26, 8) on 3F East transitions the player down to 2F East at (27, 7).
  Since we have successfully solved the 2F West boulder puzzle, the gate on 2F East at (24, 8) is permanently open. This allows us to descend the ladder at (26, 8) on 3F East to (27, 7) on 2F East, and then walk directly to the (29, 1) exit warp on 2F East without any barriers!"
  Oh!!!
  Let's re-read that very carefully:
  "This allows us to descend the ladder at (26, 8) on 3F East to (27, 7) on 2F East, and then walk directly to the (29, 1) exit warp on 2F East without any barriers!"
  Wait!
  If we descend the ladder at (26, 8) on 3F East to (27, 7) on 2F East...
  Doesn't descending that ladder count as a map transition?
  Yes! It transitions from 3F East to 2F East!
  But wait! If that transitions from 3F to 2F, doesn't it reset the 2F West boulder?
  Yes, it resets the 2F West boulder!
  But wait, if the 2F West boulder is reset, does the gate at (24, 8) close?
  Yes! The gate at (24, 8) would close!
  Wait! If the gate at (24, 8) closes, can we still walk from (27, 7) to (29, 1)?
  Let's look at the coordinates:
  - (27, 7) is the ladder tile.
  - (29, 1) is the exit warp.
  - Where is the gate?
  The gate is at (24, 8).
  Wait! (24, 8) is to the LEFT of (27, 7)!
  So if the gate at (24, 8) is closed, it blocks passage between (24, 8) and (27, 7).
  But (27, 7) and (29, 1) are BOTH on the EAST side of the gate!
  So if we are at (27, 7), we don't need to cross the gate to get to (29, 1)!
  Oh my god! That is incredibly beautiful and brilliant!
  Let's verify this!
  Let's trace:
  - Is (29, 1) on the East side of the gate at (24, 8)?
  Yes, Column 29 is to the right of Column 24!
  - Is there any other gate blocking (27, 7) to (29, 1)?
  No!
  Wait! If we can just take the ladder from 3F East (26, 8) down to 2F East (27, 7), and then walk to (29, 1) to exit, then why did we need to open the gate at (24, 8) in the first place?
  Ah!
  Let's think:
  To get to the ladder at (26, 8) on 3F East, how do we get there?
  Wait! Where does the ladder at (26, 8) on 3F East connect to?
  "Verified that taking the ladder at (26, 8) on 3F East transitions the player down to 2F East at (27, 7)."
  Wait, let's look at 3F East:
  Where is (26, 8) on 3F East?
  It's on the ground level of 3F East!
  How do we get to (26, 8) on 3F East?
  Let's look at our previous exploration of 3F East:
  - Can we walk to (26, 8) on 3F East from the rest of 3F?
  Wait! On 3F East, there is a barrier or gate!
  "Switch C1: Coordinate (3, 5) ... successfully lowers the central/eastern barrier on 3F East, opening access to the ladder at (23, 7)."
  Wait, what about the gate on 3F East that leads to (26, 8)?
  Is there a gate on 3F East?
  Let's look at `Scratchpad/VictoryRoad_Final_Stretch`:
  "9. Walk East along Row 16 back to Column 21 and climb onto the plateau at (21, 14).
  10. Walk Right 1 step to take the (25, 14) ladder UP to 3F East at (27, 15).
  11. On 3F East, walk from (27, 15) to (23, 7) via Row 13 / Column 20 (bypassing the Row 9 wall and Column 24 boulder) and take the ladder DOWN to 2F East.
  12. Detour to 2F West: Climb back UP to 3F East via (23, 7), walk West along Row 1..."
  Wait! When we are on 3F East, can we walk from (27, 15) directly to (26, 8)?
  Let's check the map markers or our notes for 3F East!
  Is there a wall or gate between (27, 15) and (26, 8) on 3F East?
  Let's search our notepads for "gate" or "barrier" on 3F.
  Wait, let's use `search_notepads` to find out what gates exist on 3F East!
  Wait, is there a gate on 3F East?
  "The pathway on Victory Road 3F East is blocked by closed gates and a solid rock wall."
  Ah! Let's check:
  "[Turns 102736-102785] I discovered that the pathway on Victory Road 3F East is blocked by closed gates and a solid rock wall."
  And:
  "[Turns 99472-103493] I solved the Victory Road 3F West boulder puzzle by pushing the boulder from (22, 3) to the switch at (3, 5) ... which cleared the barrier on Victory Road 3F East."
  Ah! So the barrier on 3F East was cleared by the boulder at (3, 5)!
  But wait, is that boulder still on (3, 5) now?
  Let's look at `Scratchpad/VictoryRoad_Route`:
  "Boulder C1: Initial (22, 3) | Current (3, 5) | Target (3, 5) (Switch C1) | Status: [x] Active (secured with Switch C1)"
  Wait! Did we transition maps since Turn 103493?
  Yes, we went down to 2F and back up to 3F multiple times!
  So Boulder C1 at (3, 5) must have reset to (22, 3)!
  Wait, let's verify if Boulder C1 reset.
  Yes! Any map transition (like taking the ladder from 3F to 2F) resets all boulders on ALL floors!
  Wait, let's look at `Scratchpad/VictoryRoad_Final_Stretch`:
  "Live Execution Logs (2F West Boulder B1 Solved and Walking East):
  - Turn 104312: Stood at (5, 10). Plotted path across plateau to (21, 15).
  - Path: Up 2 to (5, 8) -> Right 8 to (13, 8) -> Down 4 to (13, 12) -> Right 8 to (21, 12) -> Down 3 to (21, 15) -> descend.
  - Turn 104332: Arrived on 3F East at (27, 15). Plotted path to the (23, 7) ladder: Up 13 to (27, 2) -> Left 4 to (23, 2) -> Down 5 to (23, 7) -> descend."
  Wait, why did we do that?
  Ah, in Turn 104332, we were on 3F East!
  Wait, did we transition from 2F to 3F East?
  Ah! On Turn 104330, we took the ladder at (25, 14) on 2F East to 3F East!
  But wait! When we took that ladder, did the 2F West boulder B1 reset?
  Yes, it did!
  But wait, why did we solve the 2F West puzzle if we were just going to reset it?
  Let's look at:
  "[Turn 104407] Analysis:
  - Position: (25, 8) on Victory Road 2F (Map 0_194).
  - Situation: The gate at (24, 8) is closed ... because our transition from 2F -> 3F -> 2F reset all overworld boulders. We are on the East side of the gate, so we cannot walk Left to the rest of the map.
  - Exit Strategy:
    1. Walk to (27, 7) (Up 1, Right 2).
    2. Take the ladder UP to 3F East (lands us at (26, 8) on 3F East).
    3. Walk from 3F East to 3F West.
    4. Descend the ladder at (2, 0) on 3F West to 2F West.
    5. Solve the 2F West boulder puzzle again (pushing Boulder B1 onto Switch B1).
    6. Walk across 2F from 2F West to 2F East WITHOUT taking any ladders.
    7. On 2F East, walk through the open gate at (24, 8) to (27, 7).
    8. Take the ladder UP at (27, 7) to 3F East (26, 8).
    9. Walk from (26, 8) to the exit of Victory Road (Route 23/Indigo Plateau)."
  Ah!!!
  Look at Step 7 and 8 of the Exit Strategy:
  "7. On 2F East, walk through the open gate at (24, 8) to (27, 7).
  8. Take the ladder UP at (27, 7) to 3F East (26, 8).
  9. Walk from (26, 8) to the exit of Victory Road (Route 23/Indigo Plateau)."
  Wait, why does this exit strategy take the ladder UP at (27, 7) to 3F East (26, 8) instead of walking directly to (29, 1) on 2F East?
  Let's check:
  Is there an exit warp at (29, 1) on 2F East, or is the exit on 3F East?
  Wait! Let's read `Turn 104394 Discovery` again carefully:
  "Verified that Victory Road 3F East (Map 0_198) has only 4 warps, all leading to Victory Road 2F (Map 0_194).
  Verified that the exit of Victory Road to Route 23/Indigo Plateau is located at (29, 1) on Victory Road 2F East (Map 0_194, Warp 5).
  Verified that taking the ladder at (26, 8) on 3F East transitions the player down to 2F East at (27, 7)."
  Wait!
  If taking the ladder at (26, 8) on 3F East transitions the player DOWN to 2F East at (27, 7)...
  Then (27, 7) on 2F East is the ladder!
  And (29, 1) on 2F East is the exit warp!
  But wait! If the exit warp is at (29, 1) on 2F East, how do we get to (29, 1) on 2F East?
  Let's check: is (29, 1) connected to (27, 7) on 2F East?
  Yes, they are both on 2F East!
  But wait, why does Step 8 say:
  "8. Take the ladder UP at (27, 7) to 3F East (26, 8).
  9. Walk from (26, 8) to the exit of Victory Road (Route 23/Indigo Plateau)."
  Wait! Is the exit actually on 3F East or 2F East?
  Let's look at `Scratchpad/VictoryRoad_Exit_Verification`:
  "Pokered disassembly analysis confirms Victory Road 2F (Map 194) has a 5th warp at (29, 1) leading to Route 23."
  But wait, let's search our notepads for "exit" or "3F East" to see where the actual exit is.
  Let's use `search_notepads` with query "exit" to find all exit-related notes.
- Turn 104536: Arrived on 3F East at (27, 15) by taking the ladder. Tested and confirmed that the barrier on Row 10 on the right side of 3F East is currently closed (shows TYPE_2889 solid wall at (25, 10), (26, 10), etc.) because the map transition reset Boulder C1 on 3F West off of Switch C1 (3, 5). 
- Thus, we cannot reach the exit ladder at (26, 8) from here on foot without opening that barrier first.
- To open the barrier, we must go to 3F West and push Boulder C1 onto Switch C1 (3, 5).
- To get to 3F West, we must take the ladder back down to 2F East, walk across the 2F plateau to 2F West, and climb the top-left ladder at (2, 0) up to 3F West.
- Once on 3F West, we push Boulder C1 onto Switch C1 (3, 5). Then, we walk on foot from 3F West to 3F East entirely on 3F (no ladders!), keeping the switch pressed so the barrier stays open!
- Then we walk through the open barrier to the (26, 8) ladder, descend to the 2F East exit pocket at (27, 7), and walk to the (29, 1) exit warp!
- First step: Walk Left to (26, 15) to step off the ladder, then walk Right to (27, 15) to transition back down to 2F East.
- Turn 104552: Standing at (2, 5) on 2F West. Realized we are on the south side of the Row 4 blockage, and the boulder at (5, 5) blocks the only passage at (5, 4). We cannot reach the (1, 1) ladder.
- Turn 104564: Attempted to walk Down Column 5 to reach the stairs, but bumped against the solid cliff edge at (5, 8).
- Turn 104567: Standing at (5, 7) facing Down. Plotting path to walk around the cliff using Column 3 ground corridor: Left x2 to Column 3, Down x4 to Row 11, Right x2 to Column 5 (5, 11), and Up x1 to take the stairs back to 2F East.
- Turn 104622: Currently at (5, 8) on Victory Road 2F West. We fled from a wild Onix at (5, 8). We are facing Right. We need to walk across the plateau corridor to 2F East.
- Step 1: Walk to the right edge of the screen at (10, 8).
  - From (5, 8), (10, 8) is 5 steps to the Right.
  - Button sequence: ['Right', 'Right', 'Right', 'Right', 'Right']
  - Let's execute this to reach (10, 8).
- Turn 104624: Arrived at (10, 8). Now walking to (13, 12).
  - Button sequence: ['Right', 'Right', 'Right', 'Down', 'Down', 'Down', 'Down']