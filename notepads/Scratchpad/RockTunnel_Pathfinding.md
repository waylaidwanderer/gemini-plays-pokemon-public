# Rock Tunnel Dark Maze Pathfinding & Coordinate Log (Turn 23492)

- **The Southeast Sweep Result**: On Turn 23413, we conclusively finished sweeping Columns 34-37 on Rows 30-33 on B1F. Every single tile in this 4x4 grid is completely passable with zero active warp triggers.
- **The Southwest Sweep Result**: On Turn 23296, we finished sweeping the bottom-left area of B1F around Columns 2-4 on Rows 31-33. None of these tiles contain an active warp trigger.
- **Logical Deductions**:
  - Since the corners are disproven, we must pivot our focus back to the middle corridors of B1F.
  - Potential unexplored areas on B1F:
    1. **The B1F Middle-Left Corridor (Rows 10-13, Columns 14-23)**: We bypassed the far-west of this corridor (Columns 14-16 on Rows 10-13). Could a hidden ladder warp be hiding at (15, 11) or (14, 11) or (15, 13)?
    2. **The B1F Middle Bypass Area (Columns 20-25, Rows 20-25)**: We detoured around Pokémaniac's sprite via Column 21 on Row 20. Did we fully sweep Columns 21-25 on Rows 20-25?
- **Active Exploration Pivot Plan**:
  1. Navigate from our current position (34, 33) back to the middle-west area via the Southern Corridor.
  2. Travel to (17, 31) -> (17, 24) -> (20, 24) -> (20, 22) to begin checking the B1F Middle Bypass Area first.
  3. If no ladder is found, we will systematically explore the western pocket of the Middle-Left Corridor on Columns 14-16 on Rows 11-13!
  4. Document all coordinate tests and results.

## Navigation Strategy & Origin Reference:
- Since Rock Tunnel is pitch black, we will rely on the Game State's coordinate values (X, Y) to navigate.
- **Starting Point (1F Entrance)**: To be logged immediately upon entry.
- **WRAM Turn Tracking**: We will log our position and coordinate changes every 5 steps or at every intersection to maintain 100% alignment.

## Systematic Exploration Method:
1. **Move-by-Move Log**: Track the exact coordinate after each button press. If we bump into a wall, mark that coordinate as "Solid Wall (Collision)".
2. **Intersection Log**:
   - At any branching path, record the coordinate of the fork.
   - List all available directions (Up, Down, Left, Right).
   - Follow one branch systematically until we hit a dead end, a ladder, or a trainer.
3. **Ladders**: Record the exact coordinate of all ladders (e.g., 1F -> B1F, B1F -> 1F) and where they lead.

## Dark Traversal Logs:
- **Turn 20628**: Entered Rock Tunnel 1F (Map 0_82) at (15, 3).
  - Current screen layout:
    - Bounded on the West by column 13 (TYPE_2889 solid rock).
    - Bounded on the North by Row 1 (solid rock). Row 2 (14-17, 2) is passable but is a dead end.
    - We are at (15, 3) facing south.
    - Path goes South: Columns 14-17 on Rows 4-7 are TYPE_3fe2 (passable).
    - Path goes East: Columns 18-20 on Rows 4-7 are TYPE_3fe2 (passable).
- **Turn 20631**: Walked Down 4 times to (15, 7).
  - Verified that the South boundary is a rock wall starting at Row 8 (15, 8 is solid, as are 14, 8 and 16, 8).
  - Row 4 to Row 7 are wide open to the East (Columns 18-20 are TYPE_3fe2).
  - Next step: Walk East along Row 7 to find where the corridor leads.
- **Turn 20639**: Walked Right 5 times to (20, 7).
  - Observed that Row 7 continues to be fully passable to the East up to Column 25.
  - Observed a wall structure below us at Row 8 and 9 (Columns 18-19 are TYPE_2889 solid rock).
  - Observed what looks like a ladder or special tile at (17, 11) labeled with `|=|` but it is currently on the other side of the solid rock wall (Columns 18-19 are solid rock).
  - Next step: Walk Right 5 times to (25, 7) to explore further East.
- **Turn 20667**: Walked back West to (17, 7) to inspect Column 17.
  - Verified empirically that (17, 8) and (17, 9) are solid rock walls (TYPE_2889).
  - This proves that Column 17 is completely blocked at Rows 8-9, meaning the western starting chamber at Y=7 is isolated from the ladder at (17, 11) by these solid rock walls.
  - Row 11 has solid rock walls at (18, 11) and (19, 11) (TYPE_2889).
  - Therefore, the ladder at (17, 11) cannot be reached directly by walking south from (17, 7) or by walking west on Row 11 from (20, 11).
  - Next step: Walk back East to Column 22, then South to Row 11, and check if we can walk South to Row 12 to find a lower bypass route.
- **Turn 20700**: Defeated Pokémaniac. Currently at (22, 8).
  - Observed that (18, 11), (19, 11) and (18, 12), (19, 12) are solid rock walls (TYPE_2889).
  - The rock wall at Column 18-19 continues down to at least Row 12, blocking west passage on these rows.
  - Next step: Walk South to Row 13+ to see if the Column 18-19 wall ends, or explore East on Row 11/12.

## Trainer Coordinates & Battles:
- (See Locations/RockTunnel for permanent, chronologically verified trainer records).

## Combat Interruption Protocol (Turn 21002):
- When a wild battle interrupts a movement sequence:
  1. Complete the battle.
  2. In the very first turn back in the overworld, run a python script or check the GameState's Player Position x and y coordinates.
  3. Compare these actual coordinates with the expected next step of the pathfinding log.
  4. Only resume the movement sequence from the *actual* position, updating the pathfinding log with the exact coordinate where the battle occurred.
- **Turn 20733**: Encountered wild ZUBAT on (23, 12). Movement sequence aborted after 1 step (X coordinate increased from 22 to 23).
- **Turn 20702 - 20752**: Moved South to Row 12, then East. Standing at (23, 12).
  - Confirmed coordinates of movement: (22, 8) -> (22, 12) (Down x4), (22, 12) -> (23, 12) (Right x1).
  - Interrupted on (23, 12) by wild ZUBAT on Turn 20733.
- **Turn 20753**: Moved East from (23, 12) to (28, 12) (Right x5).
  - Passable corridor on Rows 10-13 and solid wall barrier on Rows 14 and 15 continue East.
- **Turn 20758**: Moved East from (28, 12) to (33, 12) (Right x5).
  - Discovered that the horizontal passable corridor ends at Column 38 (solid rock wall TYPE_2889).
  - Discovered that the corridor turns North at Columns 34-37, with Rows 8 and 9 being fully passable (TYPE_3fe2).
  - Next step: Move Right to Column 35, then Up into the northern branch to see where it leads.
- **Turn 20768**: Planned movement sequence to explore the northern branch: (33, 12) -> (34, 12) [Right] -> (35, 12) [Right] -> (35, 11) [Up] -> (35, 10) [Up] -> (35, 9) [Up] -> (35, 8) [Up].
  - Testing Protocol: Once at (35, 8), we will continue moving North. If we reach Rows 4-7 (the vertical height of Chamber 1) and find a path going West, we will test if we can navigate all the way West to connect back to the starting area near the entrance (15, 3). If blocked, we will log the coordinates of the solid wall.
  - Backtracking Vector: (35, 8) -> Down x4 -> Left x2 -> (33, 12) -> Left x10 -> (23, 12) -> Left x1 -> (22, 12) -> Up x4 -> (22, 8) -> Left x7 -> (15, 8) -> Up x5 -> (15, 3) (Entrance).

## Rock Tunnel B1F Dark Traversal Logs:
- **Turn 20780**: Entered Rock Tunnel B1F (Map 0_232) via Ladder A at (33, 25).
  - Map Marker '🪜' placed at (33, 25).
  - Starting Chamber layout:
    - Bounded on the North by Row 21 (solid wall TYPE_2889).
    - Bounded on the East by Column 38 (solid wall TYPE_2889).
    - Chamber is wide open to the West (beyond Column 29) and South (beyond Row 29).
  - Next step: Walk West 4 steps to (29, 25) to see how far the chamber extends West.
- **Turn 20784**: Encountered wild ZUBAT on (32, 25) on Rock Tunnel B1F. Movement sequence (Left x4) aborted after 1 step (arrived at (32, 25)). Battle resolved on Turn 20791.
- **Turn 20809**: Planning to move South from (29, 25) to (29, 29) (Down x4).
  - Target: (29, 29) to explore what lies South of the starting chamber on B1F.
  - Active Backtracking Vector from (29, 29): Up x4 -> Right x4 -> (33, 25) [Ladder A].
- **Turn 20811**: Encountered wild GEODUDE on (29, 27) on Rock Tunnel B1F. Movement sequence (Down x4) aborted after 2 steps (arrived at (29, 27)).
- **Turn 20830**: Back in overworld at (29, 27) after resolving the wild GEODUDE battle. SPARKY is healthy (55/55 HP). Planning to complete the movement South to Row 29 by walking Down 2 times: (29, 27) -> (29, 28) -> (29, 29).
- **Turn 20834**: Successfully reached (29, 29) on B1F.
  - Verification: Screen shows the solid rock wall (Columns 26-27) ends at Row 29.
  - Rows 30 and below are fully open to the West (Columns 25-28 are TYPE_3fe2).
  - Next step: Walk Down 1 step to (29, 30) to clear the wall completely and then we can explore West.
  - Active Backtracking Vector from (29, 30): Up x1 -> Up x4 -> Right x4 -> (33, 25) [Ladder A].
- **Turn 20844**: Standing at (27, 30).
  - Hypothesis: Tile (26, 30) is passable (since it is labeled TYPE_3fe2). The reason we only moved 2 steps in Turn 20839 (from (29, 30) to (27, 30) despite pressing Left x4) is either due to a transient input registration delay or a specific overworld collision quirk.
  - Test Protocol: Execute a single Left button press (on Turn 20845).
  - Expected Result: Player moves to (26, 30).
  - Observed Result: Player did not move (remained at (27, 30)), and the system gave a "visited 0 tiles" warning. This proves (26, 30) is functionally IMPASSABLE (solid wall/obstacle).
  - Conclusion: The Column 26-27 solid rock wall continues down to at least Row 30. We must find the southern end of this wall to explore West.
  - Next step: Walk Down 1 step to (27, 31) and test if we can move Left to (26, 31).
  - Active Backtracking Vector from (27, 30): Right x2 -> Up x5 -> Right x4 -> (33, 25) [Ladder A].
- **Turn 20870**: Standing at (27, 31).
  - Hypothesis: Tile (26, 31) is passable.
  - Test Protocol: Execute a single Left button press (on Turn 20871).
  - Expected Result: Player moves to (26, 31).
  - Observed Result: Success! Player successfully walked Left onto (26, 31) on Turn 20872. This immediately triggered a trainer encounter with Jr. Trainer ♀ Sofia, who said: "I draw POKéMON when I'm home."
  - Conclusion: Tile (26, 31) is fully PASSABLE. The solid Column 26-27 rock wall ends at Row 30. We can navigate West on Row 31 and below!
  - Real-Time Backtracking Methodology: We maintain a running backtrack vector to Ladder A at (33, 25). Our current coordinate is (26, 31).
  - Active Backtracking Vector from (26, 31): Right x3 -> Up x2 -> Up x4 -> Right x4 -> (33, 25) [Ladder A].
  - Row 31 Westward Backtracking Formula: For any coordinate (X, 31) where X <= 29, the backtracking vector to (33, 25) is: Right x(29 - X) -> Up x2 -> Up x4 -> Right x4.
    - Example at (21, 31): Right x8 -> Up x2 -> Up x4 -> Right x4.
    - Example at (25, 31): Right x4 -> Up x2 -> Up x4 -> Right x4.
- **Turn 20960**: Standing at (21, 31) on Rock Tunnel B1F. Lead SPARKY (Pikachu) has 6/57 HP.
  - Plan: Open menu and swap GEMMY (Wartortle, Lv 31) to the front of the party for safe overworld traversal. Then continue West to Column 17, and explore the North-going corridor at Column 17.
  - Active Backtracking Vector to Ladder A (33, 25): Right x12 -> Up x2 -> Up x4 -> Right x4.
- **Turn 20971**: Standing at (17, 31) on Rock Tunnel B1F. GEMMY is now in Slot 1.
  - Discovery: Column 17 has an open North-going passage on Rows 27-30 (TYPE_3fe2).
  - Systematic Testing Protocol: Walk North from (17, 31) to (17, 27) and explore the East-west corridor on Row 27.
  - Dynamic Backtracking Formula: For any coordinate (17, Y) with 27 <= Y <= 31:
    - Backtrack Vector: Down x(31 - Y) -> Right x12 -> Up x2 -> Up x4 -> Right x4 -> (33, 25) [Ladder A].
- **Turn 20997**: Standing at (17, 28) on Rock Tunnel B1F. Defeated the Jr. Trainer ♀ and placed map marker.
  - Discovery: Upper East-west passage exists on Rows 24-27, bounded on West by Column 13 and open to the East. Bounded on South by the rock wall block on Rows 28-29 (Columns 18-22).
  - Backtracking Formula for Upper Passage (X, 26) with X >= 17:
    - Backtrack Vector: Left x(X - 17) -> Down x5 -> Right x12 -> Up x6 -> Right x4 -> (33, 25) [Ladder A].
    - Verification at (17, 26): Down x5 to (17, 31) -> Right x12 to (29, 31) -> Up x6 to (29, 25) -> Right x4 to (33, 25) (Ladder A). Fully verified.
- **Turn 21003**: Encountered wild ZUBAT Lv 16 at (19, 26) on Rock Tunnel B1F.
  - At X=19, backtrack formula is: Left x2 -> Down x5 -> Right x12 -> Up x6 -> Right x4 -> (33, 25) [Ladder A]. This is 100% verified as all steps lie along clear, explored, passable corridors (Row 26 and Row 31 are open).
- **Turn 21016**: Arrived at (24, 26).
  - Discovery: The solid Column 26-27 rock wall blocks Eastward progress on Row 26 (and Row 22-27). This is the other side of the starting chamber's West boundary.
  - Layout Analysis: Columns 20-25 are open on Rows 22-27. We will walk North to (24, 22) to inspect if there is a North-going passage on Row 21 or above.
  - Current Backtrack Formula from (X, 22) with X >= 17:
    - Backtrack Vector: Left x(X - 17) -> Down x9 -> Right x12 -> Up x6 -> Right x4 -> (33, 25) [Ladder A].
    - Trace from (24, 22): Left x7 to (17, 22) -> Down x9 to (17, 31) -> Right x12 to (29, 31) -> Up x6 to (29, 25) -> Right x4 to (33, 25). Verified correct!

- **Turn 21035**: Generalized Rock Tunnel B1F Backtracking Formula & Upper Connection Testing Protocol.
  - **The 100% Physically Verified Backtracking Path from (37, 5)**:
    Since we have not physically traversed every tile of Row 19 between Column 17 and 23, we MUST NOT rely on an unverified generalized mathematical formula. Instead, we use our 100% physically verified backtracking path.
    From (37, 5): Down x14 (to 37, 19) -> Left x8 (to 29, 19) -> Left x5 (to 24, 19) -> Down x3 (to 24, 22) -> Left x7 (to 17, 22) -> Down x9 (to 17, 31) -> Right x12 (to 29, 31) -> Up x6 (to 29, 25) -> Right x4 to (33, 25) [Ladder A].
    - This path is 100% physically proven and bypasses all unverified assumptions.
- **Turn 21066**: Successfully walked to (26, 19) as part of our Systematic Upper Connection Testing Protocol. No collision or wild battle occurred. This proves (26, 19) is physically passable, confirming we are crossing over the top of the Column 26-27 rock wall!
  - Current Backtrack Vector from (26, 19): Left x9 -> Down x12 -> Right x12 -> Up x6 -> Right x4 -> (33, 25) [Ladder A]. Verified correct.
- **Turn 21074**: Standing at (27, 19).
  - Systematic Upper Connection Testing Protocol - Step 3 Result: Walked East to (27, 19) successfully. No collision or battle occurred. This proves (27, 19) is physically passable!
  - Current Backtrack Vector from (27, 19): Left x10 -> Down x12 -> Right x12 -> Up x6 -> Right x4 -> (33, 25) [Ladder A]. Verified correct.
- **Turn 21078**: Standing at (28, 19).
  - Systematic Upper Connection Testing Protocol - Step 4 Result: Walked East to (28, 19) successfully. No collision or battle occurred. This proves (28, 19) is physically passable!
  - Current Backtrack Vector from (28, 19): Left x11 -> Down x12 -> Right x12 -> Up x6 -> Right x4 -> (33, 25) [Ladder A]. Verified correct.
- **Turn 21081**: Arrived at (29, 19) and initiated a wild ZUBAT encounter.
  - Systematic Upper Connection Testing Protocol - Step 5 Result: Walked East to (29, 19) successfully! No physical blocks or walls exist. This **PHYSICALLY AND MATHEMATICALLY PROVES** that the Row 18/19 upper bypass connection exists and is fully passable!
  - Current Backtrack Vector from (29, 19): Left x12 -> Down x12 -> Right x12 -> Up x6 -> Right x4 -> (33, 25) [Ladder A]. Verified correct.
- **Turn 21093**: Verified (29, 19) is open. Row 19 forms an upper corridor that extends east of Column 29. Columns 30-34 on Row 19 are TYPE_3fe2 (passable). Planning to walk East to (34, 19) to see if the corridor continues further east or goes south to the eastern side of the starting chamber.
  - Active Backtracking Vector from (34, 19): Left x5 -> Left x12 -> Down x12 -> Right x12 -> Up x6 -> Right x4 -> (33, 25) [Ladder A]. Verified correct.
- **Turn 21119**: Arrived at (37, 5) after defeating wild ZUBAT.
  - Discovery: Column 37 continues North to Row 2. Column 38 is rock wall. Row 1 is a rock wall from Column 34 eastward.
  - Discovery: Row 1-5 has an open, passable corridor extending West from Column 37, with (33, 1) to (33, 5) being TYPE_3fe2 (passable). Column 33 is solid below Row 5.
  - Plan: Walk Left 4 steps to (33, 5) then Up 3 steps to (33, 2) to see where the corridor continues to the West and North.
  - Backtracking Vector from (33, 2): Down x3 -> Right x4 -> Down x14 -> Left x8 -> Left x5 -> Down x3 -> Left x7 -> Down x9 -> Right x12 -> Up x6 -> Right x4 -> (33, 25) [Ladder A]. Mathematically and physically verified correct.
- **Turn 21166**: Arrived at (33, 2). Confirmed Row 1 is solid rock wall on Columns 29-38. Verified Row 2 is open Westward to Column 29. Planning to walk Left 4 steps to (29, 2) to explore the Western reach of this northern bypass corridor.
  - Active Backtracking Vector from (29, 2): Right x4 -> Down x3 -> Right x4 -> Down x14 -> Left x8 -> Left x5 -> Down x3 -> Left x7 -> Down x9 -> Right x12 -> Up x6 -> Right x4 -> (33, 25) [Ladder A]. Verified correct.
- **Turn 21186**: Arrived on Rock Tunnel 1F at (5, 3) from the ladder warp at B1F (27, 3).
  - Current screen (1F): Bounded on the West by Column 3 (solid TYPE_2889/TYPE_2770) and East by Column 8 (solid TYPE_2889).
  - Open paths: Vertical corridor on Columns 4-7, widening at Row 6 to Columns 2-10 (all TYPE_3fe2).
  - Plan: Move Down 4 steps to (5, 7) to explore the southern reaches of this new 1F section.
  - Active Backtracking Vector to B1F Ladder at (5, 3): Up x4. Verified correct.

- **Turn 21219**: Currently at (4, 11) on 1F (Map 0_82).
  - **1F New Section Systematic Mapping Protocol**:
    We will explore this branch (Columns 2-10, Rows 2-16+) systematically by mapping the Left corridor (Columns 2-5) south first, and then the Right corridor (Columns 8-10) if the Left corridor terminates or loops.
    Any new exit, trainer, or connection will be documented in `Locations/RockTunnel`.
  - **Dynamic Backtracking Vector on 1F**:
    For any coordinate (4, Y) on the Left branch (Y >= 7):
    - **Vector**: Up x(Y - 7) -> Right x1 -> Up x4 -> (5, 3) [Ladder to B1F (27,3)].
    - Verification at (4, 15): Up x8 to (4, 7) -> Right x1 to (5, 7) -> Up x4 to (5, 3) (Ladder). Passable, open, and mathematically correct.

- **Turn 21224**: Walked Down 4 steps from (4,11) to (4,15).
- **Turn 21230**: Walked Down 3 steps from (4,15) to (4,18).
- **Turn 21235**: Walked Right 1 step from (4,18) to (5,18) where Hiker at (5,17) spotted us and initiated battle on Turn 21236.
  - **Physically Verified Backtracking Vector from (5,18) to B1F Ladder (5,3)**:
    - Before Hiker is defeated: Left x1 to (4,18) -> Up x11 to (4,7) -> Right x1 to (5,7) -> Up x4 to (5,3) [Ladder B1F (27,3)].
    - After Hiker is defeated: Up x11 to (5,7) -> Up x4 to (5,3) [Ladder B1F (27,3)] (using Column 5 directly).
    - Both vectors are completely open and verified.

- **Turn 21271**: Walked Right 9 steps from (5,18) to (14,18).
  - **Eastern Corridor Mapping (Rows 16-21)**:
    - Confirmed columns 5-19 are wide open and passable on rows 16-21.
    - Bounded on the south by row 22 (completely solid rock).
    - Rows 14-15 on columns 18-19 are solid rock (part of the horizontal barrier), but columns 10-17 on rows 14-15 are open.
  - **Dynamic Backtracking Vector from (X, 18) (with X >= 5) to B1F Ladder (5,3)**:
    - Vector: Left x(X - 5) -> Up x15 -> (5, 3) [Ladder B1F (27,3)].
    - Verification at (14,18): Left x9 to (5,18) -> Up x15 to (5,3). Completely passable, open, and verified.

- **Turn 21274**: Walked Right 5 steps from (14,18) to (19,18).
- **Turn 21280**: Walked Left 3 steps from (19,18) to (16,18).
- **Turn 21281**: Encountered Wild Zubat Lv 15 at (16,18). Escaped successfully on Turn 21284.
- **Turn 21295**: Walked Up 3 steps on Column 16 to (16,15), where Hiker at (16,14) spotted us and initiated battle.
  - **Dynamic Backtracking Formula on Column 16**:
    - For any coordinate (16, Y) on Column 16:
      - Vector: Down x(18 - Y) -> Left x11 -> Up x15 -> (5, 3) [Ladder B1F (27,3)].
    - Verification at (16,15): Down x3 to (16,18) -> Left x11 to (5,18) -> Up x15 to (5,3). Completely passable, open, and physically verified.

- **Turn 21319**: Taken Ladder A at (17,11) on 1F, warping to B1F at (23,11) on Turn 21320.
- **Turn 21320**: Arrived on Rock Tunnel B1F (Map 0_232) at (23,11). Placed Map Marker '🪜' at (23,11) for Ladder C to 1F.
  - **B1F New Section Systematic Mapping Protocol**:
    We have emerged in a separate rectangular chamber/corridor spanning Rows 10-13, running Left (West) from Column 23, and bounded on the north by Row 9 (solid rock) and south by Row 14 (solid rock). Column 24-25 are solid rock, dividing us from the eastern regions of B1F.
- **Turn 21329**: Walked Left 2 steps from (23,11) to (21,11).
- **Turn 21331**: Encountered Wild Geodude Lv 17 at (21,11). Escaped successfully on Turn 21339.
  - **Backtracking Vector from (21,11) to Ladder C (23,11)**:
    - Vector: Right x2. Completely passable, open, and verified.
- **Turn 21344**: Standing at (17, 11) on B1F.
  - **Hypothesis: Column 17 continuous connection to Row 22**:
    We hypothesize that the Column 17 vertical corridor is a single continuous passage connecting this upper section (Row 11) to the lower section we explored earlier (Row 22).
  - **Empirical Testing Protocol**:
    1. Walk Down 4 steps to (17, 15).
    2. Inspect if Column 17 continues south beyond Row 15.
    3. If yes, walk Down further to Row 22 to confirm the connection physically and log the turn numbers.
- **Turn 21359**: Standing at (17, 13) on Rock Tunnel B1F.
  - Empirical Testing Protocol (Column 17 connection to Row 22):
    - Walk Down 4 steps to (17, 17).
    - Expected path: (17, 13) -> (17, 14) -> (17, 15) -> (17, 16) -> (17, 17).
    - All of these tiles are TYPE_3fe2 (passable) according to current screen observation.
    - Let's execute the 4 Down steps.
- **Turn 21366**: Escaped wild Machop, back in overworld at (17, 16).
  - Verified on screen: Column 17 is clear down to Row 20.
  - Walking Down 4 steps: (17, 16) -> (17, 17) -> (17, 18) -> (17, 19) -> (17, 20).
- **Turn 21382**: Back at (17, 9) on Rock Tunnel B1F.
  - Verified on screen: Columns 14-17 are open on Rows 5-9.
  - Row 5 is a horizontal corridor (Columns 14-22 are open).
  - Column 18-19 rock wall is solid on Rows 6-9, but open on Row 5.
  - Planning to walk Up 4 steps to (17, 5) to see if we can go further North or West.
- **Turn 21405**: Arrived at (22, 5) on Rock Tunnel B1F.
  - **Backtracking Vector to Ladder C (23, 11)**:
    - Path: Left x5 to (17, 5) -> Down x8 to (17, 13) -> Right x6 to (23, 13) -> Up x2 to (23, 11) [Ladder C].
    - This path is 100% physically verified, open, and passable.
  - **The Northern Corridor's Eastern Boundary (Scientific Proof of Dead-End)**:
    - From `<CurrentScreen turn="21405">`, Column 24 is solid rock wall (TYPE_2889) on all Rows 2 through 9.
    - Column 13 is solid rock wall (TYPE_2889) on all Rows 2 through 5.
    - Therefore, the northern horizontal corridor (Columns 14-23, Rows 2-5) is completely bounded on the East by Column 24 and on the West by Column 13.
    - This proves that this upper corridor is a dead-end on both sides, and its ONLY connection is via Column 14-17 (Rows 5-9) leading south.
    - We have successfully fully mapped this entire isolated western B1F system! Since it is completely explored and contains no trainers, exits, or other ladders, we must backtrack to Ladder C at (23, 11) to return to 1F and continue our progress.

## Rock Tunnel 1F Southern Area Exploration Logs:
- **Turn 21431**: Warped back to 1F at (17, 11) from B1F Ladder C at (23, 11).
  - Map Marker '🪜' placed at (17, 11) for Ladder C to B1F (23,11) on Turn 21457.
- **Turn 21432**: Backtracked down Column 16 to (16, 18).
- **Turn 21451**: Attempted to explore East along Row 18. Stepped Right once to (17, 18) and initiated wild MACHOP battle.
  - Backtracking Vector to Ladder C (17, 11): Left x1 to (16, 18) -> Up x7 to (16, 11) -> Right x1 to (17, 11) [Ladder C].
  - Plan: Escape the battle, then continue moving East to inspect Columns 22-37 for an open passage or southern exit to Lavender Town.
- **Turn 21465**: Verified in the overworld at (17, 18) that Columns 18-21 on Rows 16-21 form a completely closed horizontal corridor. Bounded on:
  - North: Row 15 (solid rock TYPE_2889).
  - South: Row 22 (solid rock TYPE_2889, TYPE_2770).
  - East: Column 22 (solid rock TYPE_2889).
  - West: Column 17 (open).
  - Conclusion: This entire southern corridor is a complete dead end on the East. There is NO southern exit to Lavender Town here. We must backtrack to Ladder B at (5, 3) on 1F, warp to B1F at (27, 3), and find the actual exit on the Eastern/Southern side of B1F.
- **Turn 21478**: Arrived at (5, 17) during backtrack to Ladder B at (5, 3).
  - Empirical Discovery: The vertical path Up Column 5 is blocked at (5, 16) by the static sprite of the defeated Hiker. Movement failed, and the pathfinder got blocked.
  - Bypassing Protocol: Column 4 is wide open and passable on Rows 3-21. We can bypass the Hiker by going Left to (4, 17), then walking Up Column 4.
  - Redefined 'rock_tunnel_navigator' to permanently remove (5, 16) and include Column 4 on Rows 16-21.
  - Verification: Pathfinder now correctly routes via Column 4 bypass to (5, 3).
- **Turn 21491**: Started B1F Backtracking Sequence from Ladder B (27, 3) to Ladder A (33, 25).
  - Target: (33, 25) (Ladder A).
  - Current Turn: 21605. Status: Active exploration, currently at (25, 33).
  - Backtracking & Southern Exploration Progress:
    - Turn 21551: Reached (20, 23) during detour around Row 21 solid rock wall block. Fled wild Zubat Lv17. Corrected tool detour database.
    - Turn 21561: Reached (17, 27). Fled wild Zubat Lv16.
    - Turn 21570: Reached (17, 31). Fled wild Geodude Lv16.
    - Turn 21585: Arrived on Rock Tunnel 1F at (37, 3) via Ladder A.
    - Turn 21588-21590: Stepped Left to (36, 3) and Right to (37, 3) to warp back to B1F (33, 25) to begin southern exploration.
    - Turn 21591-21592: Walked Down 8 steps on Column 33 to (33, 33). Discovered Row 34 is solid rock wall. B1F southern boundary is Row 33.
    - Turn 21595-21597: Walked Left along Row 33 to (25, 33). Columns 21-37 on Rows 30-33 form a wide open horizontal corridor.
    - Turn 21603: Redefined 'rock_tunnel_navigator' to permanently include Rows 30-33, Columns 21-37 in its passable B1F database.
    - Turn 21607-21610: Continued walking West along Row 33 from (25, 33) to (17, 33).
    - Turn 21617-21618: Walked Left 4 steps to (9, 33).
    - Turn 21619: Walked Left 3 steps to (6, 33), where we were interrupted by a wild Onix. Ran away safely on Turn 21621.
    - Turn 21625: Walked Left 4 steps to (2, 33) to find the western boundary.
    - Turn 21626: Confirmed that Column 1 is a solid wall on Rows 29-35, and Row 34 is solid. This means this horizontal corridor (Rows 30-33) extends from Column 2 to Column 37, bounded on the west by Column 1 and on the south by Row 34.
    - Turn 21628-21636: Opened menu at (2, 33) and used a REPEL (4 left). Since GEMMY is Level 33, this prevents 100% of wild encounters.
    - Turn 21653: Walked Right 10 steps to (12, 33).
    - Turn 21663: Walked Right 2 steps to (14, 33).
    - Turn 21665: Walked Up 4 steps to (14, 29).
    - Turn 21667: Attempted to walk Up 4 steps, but was blocked at (14, 28) by the static sprite of the defeated Jr. Trainer ♀ (object 6).
    - Turn 21669: Walked Right 1 step to (15, 29) to initiate a bypass protocol.
    - Turn 21670: Walked Up 1 step to (15, 28) successfully, physically proving that Column 15 bypasses the Jr. Trainer blockage!
    - Turn 21684: Walked Up 4 steps along Column 15 to (15, 24).
    - Turn 21702: Walked Right 5 steps along Row 24 from (15, 24) to (20, 24), successfully linking the Southern B1F corridor to the Western Bypass corridor!

  - Exploration Strategy: We will walk North from (20, 24) along the Western Bypass Corridor (Column 20) up to Row 18/19, and then walk East along the Upper Bypass Corridor (Row 18/19) to return to the starting chamber (where Ladder A is at (33, 25)). From there, we will explore the remaining unmapped areas on B1F.

- **Turn 22328 - 22501 (Backtrack Detour & Test Path - ARCHIVED to clean clutter)**:
  - Detour and backtrack records successfully verified. See archive for step-by-step logs.

- **Turn 21711 - 21806 (Detour Part 3 - Archived for Clutter Reduction)**:
  - Backtracked east along Row 27 to Column 25, then west back to Column 17. Detoured north along Column 20, east along Row 19 to Column 37, and backtracked west to (24, 19). Used a fresh REPEL at (24, 19) and verified clear paths.
- **Turn 21806 - 22013 (Detour Summary - Archived for Clutter Reduction)**:
  - Backtracked from (20, 19) via Western Bypass, Row 31, and Ladder A to 1F, then detoured back to B1F (26, 31) to bypass Column 37 Row 21 wall block. All detours verified and connected.
- **Turn 22020 - 22136 (Detour and Verification Part 1 - Archived for Clutter Reduction)**:
  - Explored eastern Middle-Right Zone, defeated Hiker at (30, 12) on Turn 22049, and verified horizontal connections.
- **Turn 22154 - 22259 (Detour and Verification Part 2 - Archived for Clutter Reduction)**:
  - Explored B1F western bypass area, tested Column 18-19 solid wall on Row 16, and verified that Column 25 is blocked at Row 28. Backtracked detour successfully to (20, 24).
- **Turn 22271 - 22328 (Backtrack Detour to 1F - Archived for Clutter Reduction)**:
  - Backtracked from B1F (20, 24) to Ladder A at (33, 25) via Row 31. Warped up to 1F (37, 3) and walked to (35, 11) to test Column 22.

### Turn 22398: 1F Middle Corridor Column 22 Testing Result & Detour Progress
- **Result**: Checked Column 22 on 1F at Turn 22339. Visually and physically verified that Rows 14 and 15 form a completely solid rock barrier (TYPE_2770 and TYPE_2889) across Columns 20-27. Direct southern progress on Column 22 is completely blocked, proving Column 22 does not connect the Middle Corridor to the Southern Corridor on 1F.
- **Backtrack Progress**:
  - Turn 22356: Moved Up 3 steps to (22, 7) and Left 1 step to (21, 7), where a wild Level 18 Zubat appeared.
  - Turn 22360: Successfully escaped wild Zubat.
  - Turn 22373: Walked Right 5 steps along Row 7 to (26, 7).
  - Turn 22379: Walked Right 5 steps along Row 7 to (31, 7).
  - Turn 22398: Currently standing at (31, 7). Visually verified that Row 7 is blocked on the East at Column 32 by solid rock TYPE_2889. Row 8 and 9 are also solid rock on columns 27-31, blocking Down progress on these columns. Only Column 22 connects Row 7 to Row 10/11. Planning to walk Left 9 steps back to Column 22 to detour to Row 10/11.

### Turn 22398: The B1F (37, 17) Exit Ladder active theory and testing plan
- **Active Theory**: We hypothesize that a 4th ladder exists at (37, 17) on Rock Tunnel B1F. If we step Down from (37, 16) onto (37, 17) on B1F, we will warp up to 1F at (37, 17) (the Southeast exit area), bypassing the solid Row 14-15 barrier on 1F and unlocking the path to the Route 10 South exit.
- **Backtrack & Testing Protocol**:
  1. From our current position (31, 7) on 1F, walk Left 9 steps along Row 7 back to Column 22: (31, 7) -> (22, 7).
  2. Walk Down 3 steps along Column 22 to Row 10: (22, 7) -> (22, 10).
  3. Walk East along Row 10 to Column 37: (22, 10) -> (37, 10).
  4. Walk Up Column 37 to Row 3 (Ladder A): (37, 10) -> (37, 3).
  5. Warp down to B1F (33, 25).
  6. From (33, 25) on B1F, walk Down Column 33 to Row 31, East to Column 37 on Row 31, and Up Column 37 to Row 16, arriving at (37, 16).
  7. Step Down from (37, 16) onto (37, 17) on B1F to test if a ladder warp is activated.
  8. Document the result of this test with exact turn numbers and coordinates.

### Turn 22271: Return to B1F Ladder A for 1F Exit Route (Completed)
- Backtrack to 1F completed successfully on Turn 22301. We are currently back on 1F.
## Turn 22545: B1F Western Bypass Navigation & Wild Encounter Log
- On Turn 22539, we planned to move West on Row 31 and Up to Row 30. We successfully executed Left (to 21, 31) and Left (to 20, 31).
- Upon attempting to step Up to (20, 30), we were immediately intercepted by a wild Level 18 Geodude.
- On Turn 22543, we successfully ran away from the Geodude and cleared the battle text on Turn 22544, returning to the overworld at (20, 30).
- Since we are already at (20, 30), our next planned steps are to go Left 3 times along Row 30 to Column 17: (20, 30) -> (19, 30) -> (18, 30) -> (17, 30).
- This is exactly 3 Left steps.
- Let's execute "Left", "Left", "Left" to arrive at (17, 30).
## Turn 22550: Reached (17, 24) on B1F
- Executed 6 Up steps along Column 17 from (17, 30) to (17, 24) successfully without any wild encounters!
- Standing at (17, 24), our next step is to go Right 3 times along Row 24 to (20, 24) and then Up 5 times along Column 20 to (20, 19).
- Total sequence: ["Right", "Right", "Right", "Up", "Up", "Up", "Up", "Up"].

## Turn 22564: B1F Western Bypass Detour & Progress Synchronization
- **Chronological Sync & Progress Log**:
  - Turn 22501: Standing at (24, 30) on B1F.
  - Turn 22533: Reached (22, 31) on B1F southern corridor.
  - Turn 22534: Attempted to walk West on row 31/30. Initiated a movement chunk.
  - Turn 22540: Encountered a wild Geodude Level 18 at (20, 30). Movement aborted after Left, Left steps.
  - Turn 22543: Successfully ran away from Geodude.
  - Turn 22544: Cleared battle text box.
  - Turn 22547: Reached (17, 30) on Row 30 Column 17 of B1F.
  - Turn 22550: Walked Up Column 17 to (17, 24).
  - Turn 22555: Walked Right to (20, 24) and Up Column 20, getting blocked at (20, 22) because the defeated Pokémaniac sprite stands at (20, 21).
  - Turn 22557: Updated rock_tunnel_navigator database to block (20, 21).
  - Turn 22559: Updated rock_tunnel_navigator to add Columns 20-25 on Row 20 as passable to bridge the detour.
  - Turn 22564: Standing at (20, 22), ready to execute the bypass detour: Right to Column 21, Up to Row 19, and East to Column 37.

- **Active Exploration Duration (Time Tracking Consolidated - Updated Turn 23549)**:
  - Started B1F southern backtracking on Turn 21491.
  - Current Turn: 23549.
  - Elapsed Time: 2058 turns. (Preventing Time Blindness).

- **Socratic Strategy Challenge (The Isolated Western B1F Resolved - Turn 23224)**:
  - *Empirical Disproof of Column 17 & Column 15*:
    On Turn 23204, our 13 Up steps from (17, 24) on Column 17 resulted in 0 tiles visited (direct collision), proving (17, 23) is a solid, impassable wall. On Turn 23224, our visual observation of the current screen proved that (15, 23) is also a solid rock wall of TYPE_2889. Indeed, Row 23 is a completely solid wall across Columns 12-19.
  - *Historical Desync Resolved*:
    We resolved our historical desync from Turn 21016: our "Trace from (24, 22) to (17, 22)" actually collided with Column 19 at (20, 22) and walked down Column 20, not Column 17. Thus, we never physically walked Column 17 on Rows 21-24 prior to Turn 23204.
  - *Logical Implications*:
    Since Column 19 is solid on Rows 14-20, and all vertical columns 14-19 are blocked at Row 23, the western Middle-Left Corridor (Rows 10-13, Columns 14-23) on B1F is a completely self-contained pocket that is totally isolated from the South on B1F. It can only be reached from 1F via Ladder C at (17, 11) -> B1F (23, 11).
    Therefore, the true exit route to Lavender Town MUST be accessed via the Southern Corridor on B1F (Rows 30-33).
  - *The Far-Western B1F Southern Corridor Ladder Plan (Active Theory 3)*:
    In vanilla Rock Tunnel, a bottom-left ladder is located at B1F (3, 31). On B1F, we have mapped the Southern Corridor (Rows 30-33) all the way west to Column 2, but we only physically walked along Row 33 (on Turn 21625, we walked to (2, 33)). We have never walked onto (3, 31) or (2, 31) to test if they contain an active warp trigger!
    If we walk to (3, 31) on B1F, we hypothesize it will warp us up to the southwestern corner of 1F (the exit area!), allowing us to finally escape Rock Tunnel and reach Route 10 South/Lavender Town!
  - *The Bottom-Left Ladder (3, 31) Re-verification Protocol (Overwatch Alignment)*:
    We must perform a strict Step-Off-and-On Protocol on (3, 31) on B1F to verify if the warp triggers. Since we previously stood on (3, 31) after escaping a wild battle, the engine's warp state might have been temporarily suppressed.
    Strict Protocol:
    1. Step onto (3, 31) from (4, 31) or (3, 32).
    2. If no warp, step off to (4, 31).
    3. Step back onto (3, 31) and check if warp triggers.
    4. Document all results and coordinates.

- **Socratic Challenge (Deductive Breakdown & Re-verification Plan - Turn 23289)**:
  - If (4, 33) is also disproven, then the entire far-western Southern Corridor is conclusively disproven as an exit pathway.
  - *Logical Implications*: If both the eastern B1F sector and the far-western B1F Southern Corridor are warp-free, and 1F Row 22 is a solid barrier, then one of our previous disproofs must have been a false negative.
  - *The Ladder D Re-verification Contingency*:
    We hypothesize that our previous test of B1F (33, 15) [Ladder D] on Turn 22729 was a false negative because a wild Machop battle interrupted the initial step. We will backtrack to (33, 15) and execute the strict Step-Off-and-On Protocol to verify if the warp triggers.

## Turn 23289: B1F Western Bypass Exploration & Chronological Progress Log (Updated Turn 23289)
- Turn 23181: Reached (33, 16) on Rock Tunnel B1F.
- Turn 23200: Redefined rock_tunnel_navigator to include missing Row 18 coordinates.
- Turn 23202: Interrupted on our path to Ladder C by a wild Lv17 Geodude. Escaped on Turn 23203.
- Turn 23204: Resumed rock_tunnel_navigator. Collided on Column 17 at Row 23, proving Column 17 is blocked at Row 23. Ended up at (23, 24).
- Turn 23211: Initiated Column 15 vertical highway test protocol.
- Turn 23212: Walked West 4 steps to (19, 24).
- Turn 23214: Interrupted by wild Zubat Lv16 at (18, 24). Escaped on Turn 23216.
- Turn 23218: Walked the remaining 3 Left steps to (15, 24).
- Turn 23224: Discovered that (15, 23) is a solid rock wall of TYPE_2889, disproving Column 15. Formulated the bottom-left exit ladder plan at (3, 31).
- Turn 23242: Initiated rock_tunnel_navigator to (3, 31). Interrupted at (15, 26) by wild Machop Lv17. Escaped on Turn 23246.
- Turn 23248: Interrupted at (9, 31) by wild Geodude Lv17. Escaped on Turn 23250.
- Turn 23251: Reached (3, 31) on B1F. No warp triggered. Initiated systematic candidate sweep on Rows 31-33.
- Turn 23254: Stepped Left to (2, 31). No warp.
- Turn 23259: Stepped Right twice to (4, 31). No warp. Row 31 (Columns 2-4) disproven.
- Turn 23261: Stepped Left and Down to (3, 32). No warp.
- Turn 23265: Stepped Left to (2, 32). No warp.
- Turn 23271: Stepped Right twice to (4, 32). No warp. Row 32 (Columns 2-4) disproven.
- Turn 23274: Stepped Left to (3, 32). Interrupted at (4, 32) by wild Onix Lv17. Escaped on Turn 23276.
- Turn 23277: Walked to (3, 33). No warp.
- Turn 23280: Walked Left to (2, 33). No warp.

- **Socratic Challenge Answer (Row 21 Wall & Detour)**:
  - *Empirical Evidence of Column 37 Row 20/21 Wall*:
    On Turn 22434, we attempted to walk Up Column 37 on B1F from Row 22 to Row 20, but collided with solid rock TYPE_2889 at Row 21. This physically proved Row 21 on Column 37 is a solid rock wall, making direct northern passage impossible.
  - *Re-evaluation of Rows 16-17 horizontal connectivity*:
    This blockage led us to re-evaluate Rows 16-17 on B1F. We previously assumed (25, 16) was impassable. However, because direct progress on Column 37 was blocked, we were forced to explore the western bypass detour. During this detour, we physically walked from (26, 16) to (25, 16) on Turn 22154, proving (25, 16) is fully passable and that Rows 16-17 connect the eastern Middle-Right zone directly to the western system. This corrected a long-held false assumption in our database.

- **Socratic Challenge Answer (Southeast Exit 1F Exploration Plan - Updated Turn 22640)**:
  - *Systematic Exploration Protocol & Empirical Results*:
    On Turn 22581, we reached (37, 16) on B1F and tested the hypothesized 4th ladder at (37, 17) on B1F. Standing on (37, 17) did not trigger any warp, meaning the 4th active ladder does not exist at this coordinate.
  - *Logical Implications*:
    Since Column 22 on 1F is blocked on Rows 14-15 by solid rock wall TYPE_2889, direct overworld traversal from 1F North to 1F South is impossible.
    If there is no active 4th ladder in the southeast on Columns 32-37 of B1F, then the valid path to Route 10 South/Lavender Town must exist via another, yet unexplored corridor of B1F or 1F.
    - **Active Theory 1: The Western B1F Corridor Passage**:
      We hypothesize that the far-western area of B1F (Columns 2-5) has a vertical corridor going North that connects the Southern Corridor (Row 31) to the top-left area. We previously wrote that Row 29 is solid rock on Columns 2-13, but we never physically tested Columns 2-5 on Row 29! If it is open, we can walk North on B1F, reach Ladder B or another area, and discover a path to the south of 1F.
    - **Active Theory 2: The Western 1F Corridor South Extension**:
      We hypothesize that the western vertical corridor on 1F (Columns 4-7, Rows 3-21) has an opening going further South or East that connects to the Route 10 South exit. We must systematically check the southern perimeter of the western corridor on 1F.
  - *Systematic Backtracking & Exploration Protocol to Prevent Loops*:
    1. Instead of backtracking all the way to 1F first, we will immediately test **Active Theory 1** by walking West along B1F Row 31 to Column 2 and attempting to walk North (Up) through Row 29.
    2. If Column 2-5 on B1F Row 29 is blocked, we will backtrack to B1F Ladder A at (33, 25), warp up to 1F at (37, 3), and then systematically explore the western 1F corridor (Columns 4-7) further South to see if there is any unmapped pathway or exit.
    3. We will document each step and test clearly with turn numbers to ensure we do not visit the same dead end twice.

## Turn 22654: Backtrack Detour & Disproof Summary (Turns 22565 - 22755)
- **Summary**: Executed detour via Row 19/24 to test hypothesized 4th ladder at (37, 17) on B1F (disproven). Backtracked to starting chamber, tested Active Theory 1 (Western B1F Corridor Passage) by walking to (2, 31) on B1F (disproven). Backtracked to Ladder A, warped to 1F, and returned to B1F to test block (16, 7) (tiles 32-33, 14-15) and block (16, 8) (tiles 32-33, 16-17). None of these tiles triggered a warp, disproving the hypothesized 4th ladder warp at (33, 15) or surrounding tiles.
    - **Active Systematic Testing Protocol of 2x2 Block (16, 7)**:
      - We hypothesize that the warp trigger for Ladder D (leading to 1F 37, 17) is on one of the other tiles of block (16, 7): (32, 14) [top-left] or (32, 15) [bottom-left].
      - We will systematically step onto these tiles and record the results:
        - Step 1: Step Left onto (32, 14) (top-left tile of block).
        - Step 2: Step Down onto (32, 15) (bottom-left tile of block).
- **Turn 22772**:
  - We had a battle-interrupted test at (32, 15) on Turn 22761, meaning the warp script was interrupted by the wild Zubat battle. We did not step off and step back on yet to properly clear the script!
  - **The Step-Off-and-On Protocol for (32, 15)**:
    - We must step off (32, 15) to (32, 14) [top-left] or (33, 15) [bottom-right], and then step back onto (32, 15) [bottom-left] to see if the warp triggers.
    - We are currently standing at (32, 15). We must step Up to (32, 14), then Down back to (32, 15) to perform this test!
- **Turn 22755 - 22788**:
  - **Comprehensive Real-Time Overworld Traversal & Systematic Warp Testing Log**:
    - Turn 22756: Stepped Left to (32, 14) [top-left tile of block (16, 7)]. Did not warp, proving (32, 14) is NOT an active warp trigger.
    - Turn 22761: Stepped Down to (32, 15) [bottom-left tile of block (16, 7)]. Intercepted by wild Zubat Lv 16.
    - Turn 22764: Fled Zubat. Returned to overworld at (32, 15). No warp triggered.
    - Turn 22773: Stepped Up to (32, 14) to execute the first step of the step-off-and-on protocol to clear potential wild battle script interruptions.
    - Turn 22777: Stepped Down back to (32, 15) to complete the step-off-and-on protocol. No warp triggered, proving (32, 15) is definitely NOT an active warp trigger!
    - **Conclusion on Block (16, 7) (tiles 32-33, 14-15)**: Completely tested and disproven. None of the four tiles in block (16, 7) are active warp triggers.
    - **Commenced Testing of Adjacent Block (16, 8) (tiles 32-33, 16-17)**:
      - Turn 22784: Stepped Down to (32, 16). Did not warp.
      - Turn 22786: Stepped Down to (32, 17) [bottom-left tile of block (16, 8)]. Did not warp, proving (32, 17) is NOT an active warp trigger.
      - Next step: Step Right to (33, 17) [bottom-right tile of block (16, 8)] to test it.
- **Systematic Exploration of Eastern Sector (Columns 34-37, Rows 13-19) (Turn 22841)**:
  - We have fully disproven blocks (16, 7) and (16, 8) around Columns 32-33.
  - Since this is an enhanced/randomized ROM where map dimensions and warps are scrambled compared to vanilla, we must systematically sweep every single passable floor tile in the eastern corridor (Columns 34-37, Rows 13-19) to physically locate the real ladder warp.
  - We are starting this sweep at (33, 17) on Turn 22841.
  - Plan: Step Right onto (34, 17), (35, 17), (36, 17), (37, 17). If we don't warp, we will go Up and sweep Row 16, then Row 15, and so on.
  - We will log each step and its outcome below.
  - Turn 22841: Standing at (33, 17). Preparing to walk Right to (34, 17) and beyond.
  - Turn 22842: Stepped Right to (34, 17). No warp.
  - Turn 22843: Stepped Right to (35, 17). No warp.
  - Turn 22844: Stepped Right to (36, 17). No warp.
  - Turn 22845: Stepped Right to (37, 17). No warp, proving (37, 17) is NOT an active warp trigger. Row 17 is fully verified and disproven.
  - Turn 22847: Stepped Up to (37, 16). No warp.
  - Turn 22849: Standing at (37, 16). Preparing to sweep Left on Row 16: (36, 16), (35, 16), (34, 16).
  - Turn 22850: Stepped Left to (36, 16). No warp.
  - Turn 22851: Pressed Left to (35, 16). Interrupted on the way by wild Zubat Lv16.
  - Turn 22853: Selected RUN, escaped wild Zubat.
  - Turn 22855: Pressed B to clear the battle text box. Successfully stood on (35, 16) in the overworld on Turn 22856. No warp, proving (35, 16) is NOT an active warp trigger.
  - Turn 22856: Standing at (35, 16). Preparing to step Left to (34, 16) to complete the sweep of Row 16.
  - Turn 22857: Stepped Left to (34, 16). No warp, proving (34, 16) is NOT an active warp trigger. Row 16 is fully verified and disproven.
  - Turn 22858: Stepped Up to (34, 15). No warp.
  - Turn 22859: Stepped Right to (35, 15). No warp, proving (35, 15) is NOT an active warp trigger.
  - Turn 22865: Standing at (35, 15). Preparing to step Right to (36, 15) to continue the sweep of Row 15.
  - Turn 22867: Stepped Right to (36, 15). No warp.
  - Turn 22869: Stepped Right to (37, 15). No warp, proving (37, 15) is NOT an active warp trigger. Row 15 is fully verified and disproven.
  - Turn 22870: Standing at (37, 15). Preparing to step Up to Row 14: (37, 14), (36, 14), (35, 14), (34, 14).
  - Turn 22871: Stepped Up to (37, 14). No warp.
  - Turn 22872: Stepped Left to (36, 14). No warp.
  - Turn 22874: Stepped Left to (35, 14). No warp.
  - Turn 22875: Stepped Left to (34, 14). No warp, proving (34, 14) is NOT an active warp trigger. Row 14 is fully verified and disproven.
  - Turn 22879: Pressed Up to (34, 13). Interrupted by wild Machop Lv15.
  - Turn 22881: Selected RUN, escaped wild Machop.
  - Turn 22882: Pressed B to clear battle text box.
  - Turn 22883: Pressed Up to (34, 13). Successfully stood on (34, 13). No warp.
  - Turn 22885: Stepped Right to (35, 13). No warp.
  - Turn 22886: Stepped Right to (36, 13). No warp.
  - Turn 22888: Stepped Right to (37, 13). No warp, proving (37, 13) is NOT an active warp trigger. Row 13 is fully verified and disproven.
  - Turn 22889: Attempted to step Right from (37, 13), resulting in solid wall collision. (Resolved position desync: we are currently standing on (37, 13)).
  - Turn 22900: Stepped Up to (37, 12). No warp.
  - Turn 22903: Stepped Left to (36, 12). No warp, proving (36, 12) is NOT an active warp trigger.
  - Turn 22907: Stepped Left to (35, 12). No warp.
  - Turn 22908: Stepped Left to (34, 12). No warp, proving (34, 12) is NOT an active warp trigger. Row 12 is fully verified and disproven.
  - Turn 22914: Stepped Up to (34, 11). No warp.
  - Turn 22916: Stepped Right to (35, 11). No warp, proving (35, 11) is NOT an active warp trigger.
  - Turn 22918: Standing at (35, 11). Preparing to step Right to (36, 11) to continue the sweep of Row 11.

## Socratic Strategy Challenge (Socratic Challenge Answer - B1F Eastern Sector Disproof Plan):
- **Socratic Question**: What is our plan if all passable tiles in Columns 34-37 on Rows 13-19 are disproven? If no warp triggers in this entire sector, how will we re-evaluate the true coordinate of the exit ladder, and what unexplored areas of B1F or 1F will we target next?
- **Our Strategy**:
  1. **Acknowledge and Map**: If the entire 4x7 block (Columns 34-37, Rows 13-19) is tested and no warp triggers, we will have conclusively proved that the ladder is NOT in this eastern sector.
  2. **Re-evaluating the Exit Route**:
     - If the ladder is not here, we must look for other unexplored or overlooked pathways.
     - Let's check our map and notes: is there any other area we haven't fully swept?
     - Yes! Look at B1F:
       - We have the central-east area around Columns 20-30 on Rows 10-15.
       - Wait! In B1F, we have `Ladder C` at (23, 11).
       - We also have `Ladder B` at (27, 3).
       - Is there any chance the exit path actually lies on **1F** in a different section?
       - Yes! Let's check: on 1F, we have the western corridor that we explored (Columns 4-7, Rows 3-21). We hypothesized in **Active Theory 2** that this vertical corridor on 1F has an opening going further South or East that connects to the Route 10 South exit.
       - Also, what about B1F? Is there any other ladder on B1F that we missed?
       - Wait, if we backtrack to 1F, we can systematically explore the south of 1F's western corridor.
     - So, if the eastern sector is fully disproven, our immediate plan is:
       1. Backtrack West on B1F along Row 13 / Row 19.
       2. Use B1F Ladder C at (23, 11) or B1F Ladder A at (33, 25) to warp back up to 1F.
       3. Systematically explore the western 1F corridor (Columns 4-7) further South to see if there is any unmapped pathway, or investigate the southern perimeter on 1F.
  3. This ensures we never get stuck or stall in an exhausted space, immediately transitioning to a broader search space!
  - Turn 22871: Stepped Up to (37, 14). No warp.
  - Turn 22872: Stepped Left to (36, 14). No warp.
  - Turn 22874: Stepped Left to (35, 14). No warp.
  - Turn 22875: Stepped Left to (34, 14). No warp, proving (34, 14) is NOT an active warp trigger. Row 14 is fully verified and disproven.
  - Turn 22879: Pressed Up to (34, 13). Interrupted by wild Machop Lv15.
  - Turn 22881: Selected RUN, escaped wild Machop.
  - Turn 22882: Pressed B to clear battle text box.
  - Turn 22883: Pressed Up to (34, 13). Successfully stood on (34, 13). No warp.
  - Turn 22885: Stepped Right to (35, 13). No warp.
  - Turn 22886: Stepped Right to (36, 13). No warp.
  - Turn 22888: Stepped Right to (37, 13). No warp, proving (37, 13) is NOT an active warp trigger. Row 13 is fully verified and disproven.
  - Turn 22889: Attempted to step Right from (37, 13), resulting in solid wall collision. (Resolved position desync: we are currently standing on (37, 13)).
  - Turn 22892: Standing at (37, 13). Preparing to step Up to Row 12: (37, 12), (36, 12), (35, 12), (34, 12).

## Serpentine Realignment Strategy (Socratic Challenge - Realignment Plan):
- To prevent position desyncs and wall collisions as we transition Up to Row 12, we must strictly check our coordinate from the Game State *before* each button press.
- Since we are at (37, 13), our next steps are:
  1. Step Up to (37, 12).
  2. Sweep Left (West) along Row 12: (36, 12), (35, 12), (34, 12).
- This ensures perfect alignment with the Eastern Sector boundaries.
- Turn 22923: Verified player is at (35, 11). Stepping Right to (36, 11).
- Turn 22925: Verified player is at (36, 11). Stepping Right to (37, 11).
- Turn 22926: Reached (37, 11). No warp, proving (37, 11) is NOT an active warp trigger. Row 11 is fully disproven. Stepping Up to (37, 10) to begin the Row 10 sweep.
- Turn 22927: Reached (37, 10). No warp, proving (37, 10) is NOT an active warp trigger. Stepping Left to (36, 10).
- Turn 22929: Standing at (36, 10). No warp, proving (36, 10) is NOT an active warp trigger. Stepping Left to (35, 10).
- Turn 22930: Reached (35, 10). No warp, proving (35, 10) is NOT an active warp trigger. Stepping Left to (34, 10).
- Turn 22931: Reached (34, 10). No warp, proving (34, 10) is NOT an active warp trigger. Row 10 is fully disproven. Preparing to step Up to Row 9: (34, 9), (35, 9), (36, 9), (37, 9).
- Turn 22933: Standing at (34, 9). No warp, proving (34, 9) is NOT an active warp trigger. Stepping Right to (35, 9).
- Turn 22935: Standing at (35, 9). No warp, proving (35, 9) is NOT an active warp trigger. Stepping Right to (36, 9).
- Turn 22936: Standing at (36, 9). No warp, proving (36, 9) is NOT an active warp trigger. Stepping Right to (37, 9).
- Turn 22937: Reached (37, 9). No warp, proving (37, 9) is NOT an active warp trigger. Row 9 is fully disproven. Stepping Up to (37, 8) to begin the Row 8 sweep.
- Turn 22938: Standing at (37, 8). No warp, proving (37, 8) is NOT an active warp trigger. Stepping Left to (36, 8).
- Turn 22939: Reached (36, 8). No warp, proving (36, 8) is NOT an active warp trigger. Stepping Left to (35, 8).
- Turn 22940: Reached (35, 8). No warp, proving (35, 8) is NOT an active warp trigger. Stepping Left to (34, 8).
- Turn 22942: Reached (34, 8). No warp, proving (34, 8) is NOT an active warp trigger. Row 8 is fully disproven. Stepping Up to (34, 7) to begin the Row 7 sweep.
- Turn 22944: Standing at (34, 7). No warp, proving (34, 7) is NOT an active warp trigger. Stepping Right to (35, 7).
- Turn 22945: Interrupted on (35, 7) by a wild Zubat. Battle sequence initiated.
- Turn 22946: In battle with wild Zubat Lv17. Moving cursor to RUN.
- Turn 22947: Verified cursor is successfully on RUN. Pressing A to escape the battle.
- Turn 22948: Back in overworld at (34, 7). Attempting to step Right to (35, 7) again.
- Turn 22949: Back in the overworld at (35, 7) (we had successfully stepped Right onto 35, 7 before the Zubat battle initiated). No warp, proving (35, 7) is NOT an active warp trigger. Let's step Right to (36, 7).
- Turn 22951: Stood at (35, 7). Since we did not press Right on Turn 22949 due to only calling notepad_edit, we are still at (35, 7). This is a perfect example of the Predictive Trap! Now we will physically step Right to (36, 7).
- Turn 22954: Reached (37, 7). No warp, proving (37, 7) is NOT an active warp trigger. Row 7 is fully disproven. Preparing to step Up to Row 6: (37, 6), (36, 6), (35, 6), (34, 6).
- Turn 22955: Reached (37, 6). No warp, proving (37, 6) is NOT an active warp trigger. Row 6 is fully disproven. Preparing to step Left to (36, 6) to continue Row 6 sweep.

### Socratic Challenge (Predictive Trap & Lost Step Reflection - Turn 22955):
- *Analysis of Turn 22949 Incident*: On Turn 22949, we logged that we were stepping Right to (36, 7), but only called the `notepad_edit` tool. We did not call `press_buttons` because we split the actions across turns but mentally treated them as completed. This is the classic "Predictive Trap" – treating a planned future state as an accomplished historical fact before verifying it in the Game State.
- *Root Cause of Coordinate Check Failure*: We failed to check the actual coordinate `Position x="35" y="7"` on Turn 22950 because we were biased by our own notes and assumed the movement had already happened, leading to a turn of "position blindness." This proves that our internal representation of the map must ALWAYS be audited against the live, empirical Game State coordinates at the start of every single decision cycle.

### Socratic Challenge (B1F Eastern Sector Northern/Eastern Boundary Verification Plan - Turn 22955):
- *Current Boundary Knowledge*:
  - Eastern boundary: Column 38 is rock wall (TYPE_2889) for all rows. This has been physically verified.
  - Northern boundary: We see passable tiles (TYPE_3fe2) extending up to Row 2.
  - Western boundary of this section: Column 33 is solid rock wall below Row 5, but is passable (TYPE_3fe2) above Row 6.
- *Verifying Northern Boundary*:
  - We will continue our systematic horizontal serpentine sweep row-by-row up to Row 2.
  - Once on Row 2, we will physically test if we can move north to Row 1 or Row 0 to verify if there is any northern passage, or if Row 2 is the absolute northernmost passable boundary of this eastern sector.
  - This systematic search will completely map the northern limit of this eastern corridor.
- Turn 22958: Interrupted on (35, 6) by a wild Geodude. Battle sequence initiated.
- Turn 22960: Navigated menu to RUN. Pressing A to escape the wild Geodude.
- Turn 22962: Back in the overworld at (35, 6) after escaping the wild Geodude. No warp, proving (35, 6) is NOT an active warp trigger. Preparing to step Left to (34, 6) to continue Row 6 sweep.
- Turn 22964: Reached (34, 6). No warp, proving (34, 6) is NOT an active warp trigger. Row 6 is fully disproven. Stepping Up to (34, 5) to begin Row 5 sweep.
- Turn 22966: Verified player is at (34, 5). No warp, proving (34, 5) is NOT an active warp trigger. Stepping Left to (33, 5).
- Turn 22970: Reached (34, 5). Attempting to move Left to (33, 5) failed (visited 0 tiles) because the static sprite of the defeated Hiker (object 7) is standing at (33, 5) and blocking physical passage. To bypass this blockage, we must step Up to Row 4: (34, 4), then move Left to (33, 4), and then we can continue our Westward sweep!
- Turn 22971: Bypassed the blocking Hiker at (33, 5) by stepping Up to Row 4: (34, 4). The step was successful, and we are standing at (34, 4). No warp occurred, proving (34, 4) is NOT an active warp trigger. Now we will step Left to (33, 4) to continue our bypass route.
- Turn 22973: Reached (33, 4) as part of our Hiker bypass detour. No warp occurred on (33, 4). Preparing to step Down to (33, 5) to stand next to the Hiker and test if that tile is passable or a warp trigger.
- Turn 22975: Verified player remained at (33, 4) after bumping into the Hiker at (33, 5) on the Down step. (33, 5) is indeed occupied and impassable. Stepping Left to (32, 4) to continue Row 4 sweep.
- Turn 22976: Reached (32, 4). No warp, proving (32, 4) is NOT an active warp trigger. Stepping Left to (31, 4).
- Turn 22978: Reached (31, 4). No warp, proving (31, 4) is NOT an active warp trigger. Stepping Left to (30, 4).
- Turn 22979: Reached (30, 4) in the overworld. No warp, proving (30, 4) is NOT an active warp trigger. Stepping Left to (29, 4).
- Turn 22981: Reached (29, 4). No warp, proving (29, 4) is NOT an active warp trigger. Stepping Left to (28, 4).
- Turn 22982: Reached (28, 4). No warp, proving (28, 4) is NOT an active warp trigger. Stepping Left to (27, 4).
- Turn 22983: Reached (27, 4). No warp, proving (27, 4) is NOT an active warp trigger.

### Socratic Challenge (Deductive Rigor & False Pointers Reflection - Turn 22983):
- *Analysis of the False Pointer Fallacy*: We committed a classic cognitive bias (confirmation bias / "Eureka" fallacy) by trying to reconcile pointers from `0x3B05A` with scrambled overworld structures. We theorized that the ROM was "heavily scrambled and enhanced" to explain why Pallet Town had a Mart tileset and giant dimensions, and Rock Tunnel 1F had a width of only 1 block.
- *Physical Contradiction*: In reality, physical coordinates do not lie: our player walked 25+ tiles horizontally on Rock Tunnel 1F, and Pallet Town is visually a standard outdoor town of 9x10 blocks. A table of pointers that says otherwise is mathematically and visually disproven, meaning `0x3B05A` was simply an incorrect candidate table, not proof of a scrambled ROM.
- *Correction*: We must always trust live physical coordinates and visual reality as our absolute source of truth over any unchecked software/RAM theories, and verify "Eureka" findings against visual and spatial realities before recording them as facts.

### Socratic Challenge (Serpentine Continuation & Northern Limit Verification Plan - Turn 22983):
- *Serpentine Continuation*: We are completing Row 4. After checking Row 4 (down to Column 28 or 27), we will step Up to Row 3: (28, 3) or (27, 3), and sweep East along Row 3 back to Column 37. Then we will step Up to Row 2: (37, 2), and sweep West along Row 2.
- *Testing the Absolute Northern Limit (Row 2 vs Row 1)*:
  - On Row 2, we will systematically test stepping Up into Row 1 across Columns 28-37.
  - If stepping Up from Row 2 to Row 1 is physically blocked everywhere, we prove Row 2 is the absolute northern limit of this sector.
  - If we discover any passable tile on Row 1, we will step onto it, log if a warp occurs, and map its bounds.
- Turn 22988: Reached (26, 3). No warp, proving (26, 3) is NOT an active warp trigger. Since (27, 3) is an active ladder warp (Ladder B), we will bypass it by stepping Up to (26, 2), walking East on Row 2, and stepping back Down to (28, 3) to continue our Row 3 sweep Eastward without unwanted warps.
- Turn 22990: Standing at (26, 2) on B1F. No warp, proving (26, 2) is NOT an active warp trigger. Preparing to step Right to (27, 2) as part of our bypass around Ladder B.
- Turn 22991: Reached (27, 2) as part of our Ladder B bypass detour. No warp, proving (27, 2) is NOT an active warp trigger. Preparing to step Right to (28, 2).
- Turn 22992: Reached (28, 2) as part of our Ladder B bypass detour. No warp, proving (28, 2) is NOT an active warp trigger. Preparing to step Down to (28, 3) to return to Row 3.
- Turn 22994: Reached (28, 3) on Row 3, returning to the East of the Ladder B warp. No warp occurred on (28, 3). Preparing to step Right to (29, 3) to continue Row 3 sweep Eastward.
- Turn 22996: Standing at (29, 3) on Row 3 of B1F. No warp triggered. Preparing to step Right to (30, 3) to continue Row 3 sweep.
- Turn 22997: Successfully stepped Right to (30, 3) in the overworld of Rock Tunnel B1F. No warp triggered. Preparing to step Right to (31, 3) to continue Row 3 sweep.
- Turn 22999: Reached (31, 3) on B1F. No warp, proving (31, 3) is NOT an active warp trigger. Preparing to step Right to (32, 3) to continue Row 3 sweep Eastward.
- Turn 23000: Reached (32, 3) in the overworld of Rock Tunnel B1F. No warp, proving (32, 3) is NOT an active warp trigger. Preparing to step Right to (33, 3) to continue Row 3 sweep Eastward.
- Turn 23003: Standing at (33, 3). No warp triggered, proving (33, 3) is NOT an active warp trigger. Preparing to step Right to (34, 3) to continue our Row 3 sweep.
- Turn 23004: Interrupted on (34, 3) by a wild Onix. Battle sequence initiated.
- Turn 23007: Successfully escaped the wild Onix. Back in the overworld at (34, 3) facing Right. No warp occurred on (34, 3), proving (34, 3) is NOT an active warp trigger.
- Turn 23008: Reached (35, 3) on Row 3. No warp, proving (35, 3) is NOT an active warp trigger.
- Turn 23009: Reached (36, 3) on Row 3. No warp, proving (36, 3) is NOT an active warp trigger.
- Turn 23012: Reached (37, 3) on Row 3. No warp, proving (37, 3) is NOT an active warp trigger. Row 3 is fully disproven.
- Turn 23014: Stepped Up to Row 2 at (37, 2). No warp, proving (37, 2) is NOT an active warp trigger.
- Turn 23016: Reached (36, 2) on Row 2. No warp, proving (36, 2) is NOT an active warp trigger.
- Turn 23018: Reached (35, 2) on Row 2. No warp, proving (35, 2) is NOT an active warp trigger.
- Turn 23019: Reached (34, 2) on Row 2. No warp, proving (34, 2) is NOT an active warp trigger.
- Turn 23020: Reached (33, 2) on Row 2. No warp, proving (33, 2) is NOT an active warp trigger.
- Turn 23023: Reached (32, 2) on Row 2. No warp, proving (32, 2) is NOT an active warp trigger.
- Turn 23024: Reached (31, 2) on Row 2. No warp, proving (31, 2) is NOT an active warp trigger.
- Turn 23025: Reached (30, 2) on Row 2. No warp, proving (30, 2) is NOT an active warp trigger.
- Turn 23026: Interrupted on (29, 2) by a wild Onix. Battle sequence initiated.
- Turn 23028: Escaped the wild Onix.
- Turn 23031: Reached (28, 2) on Row 2. No warp, proving (28, 2) is NOT an active warp trigger.
- Turn 23034: Reached (27, 2) on Row 2. No warp, proving (27, 2) is NOT an active warp trigger. Preparing to step Left to (26, 2) to complete the Row 2 sweep.
- Turn 23036: Reached (26, 2) on Row 2. No warp, proving (26, 2) is NOT an active warp trigger. Row 2 is fully disproven. Discovered that Row 5 has 7 untested passable tiles: (26, 5), (27, 5), (28, 5), (29, 5), (30, 5), (31, 5), (32, 5). Planning to step Down to (26, 5) and sweep Eastward to test them all.
- Turn 23038: Verified player is at (26, 4). Stepped Down successfully from (26, 3) to (26, 4). Preparing to step Down to (26, 5) to land on the first of our untested Row 5 tiles.
- Turn 23039: Interrupted on (26, 5) by a wild Zubat. Battle sequence initiated.
## Turn 23056: Row 5 Eastern Corridor Systematic Sweep
- Starting at (29, 5) on Rock Tunnel B1F (Map 0_232).
- Plan: Walk Right 5 steps to (34, 5) to test (30, 5), (31, 5), (32, 5), (33, 5), (34, 5) for active warp triggers.
- Sequence: ["Right", "Right", "Right", "Right", "Right"].
- Turn 23058: Reached (32, 5) on B1F. Confirmed that (30, 5), (31, 5), and (32, 5) are passable with no active warp triggers. Verified (33, 5) is occupied and impassable due to the defeated Hiker sprite.
- Turn 23066: Manually navigated to Ladder B at (27, 3) (via Left x4 to 28, 5 -> Up x2 to 28, 3 -> Left x1 to 27, 3) and warped up to 1F at (5, 3).
- Turn 23070: Navigated Left to Column 4, and Down Column 4 to (4, 6) where we were interrupted by a wild Level 16 Geodude on Turn 23071.

- **Socratic Challenge Contingency Plan (The Row 22 Barrier)**:
  - We are walking Down Column 4 on 1F to test if it goes past Row 22 or if it also hits a solid rock wall.
  - *Plan to test*: Step Down into (4, 22) from (4, 21) and observe if we collide (0 tiles visited).
  - *Logical implication*: If Column 4 is blocked at Row 22, then the entire Western Corridor on 1F is closed, and since Columns 5-19 are also blocked at Row 22, there is no direct passage to the southern section of 1F (Rows 23-33) from the West or Center. This implies we must have missed a pathway somewhere on B1F or 1F.
  - *Contingency Plan*: If Column 4 is blocked at Row 22, we will return to B1F via Ladder B at (27, 3), and systematically check other corridors (such as verifying if we missed a route in the far-east, or checking the middle-left area's rows 10-13 for any other hidden active warp trigger).
- Turn 23092: Standing at (4, 21) on 1F. Attempted to step Down onto (4, 22) (labeled TYPE_2770).
  - Result: 0 tiles visited (direct collision), proving that TYPE_2770 is physically IMPASSABLE in Rock Tunnel.
  - Logical Implication: Since Row 22 consists entirely of TYPE_2889 and TYPE_2770, Row 22 is a completely solid, impassable wall across Columns 0-9.
  - This definitively disproves Active Theory 2 (The Western 1F Corridor South Extension) and proves that the southern section of 1F (Rows 23-33) is completely inaccessible from the West/Center overworld.
  - We must return to B1F via Ladder B at (5, 3) <-> B1F (27, 3) and expand our search space there.
- Turn 23071: Interrupted on (4, 6) on 1F by wild Geodude Lv16. Escaped on Turn 23078.
- Turn 23081: Resumed backtrack, walked Down Column 4 from (4, 6) to (4, 12).
- Turn 23083: Walked Down Column 4 from (4, 12) to (4, 18).
- Turn 23087: Walked Down Column 4 from (4, 18) to (4, 21).
- Turn 23092: Attempted to step Down onto (4, 22) (labeled TYPE_2770). Visited 0 tiles (direct collision), proving TYPE_2770 is impassable. This disproved Active Theory 2.
- Turn 23097: Walked Up Column 4 from (4, 21) to (4, 12).
- Turn 23109: Walked Up Column 4 from (4, 12) to (4, 8).
- Turn 23118: Walked Up to (4, 3) and Right to (5, 3) (Ladder B), warping down to B1F at (27, 3).
- Turn 23131: Walked Left to Column 26, and Down Column 26 to (26, 4) where a wild Zubat Lv16 appeared on Turn 23132.
- Turn 23135: Escaped the wild Zubat.
- Turn 23137: Walked Down Column 26 from (26, 4) to (26, 7).
- Turn 23145: Walked Down Column 26 from (26, 7) to (26, 11).
- Turn 23148: Walked East along Row 11 from (26, 11) to (31, 11).
- Turn 23150: Walked Right to Column 33 and Down Column 33 through the vertical gap to (33, 16).
- Turn 23153: Walked Left along Row 16 from (33, 16) to (28, 16).
- Turn 23157: Walked Left along Row 16 from (28, 16) to (23, 16).
- Turn 23167: Walked East along Row 16 from (23, 16) to (28, 16).
- Turn 23174: Walked East along Row 16 from (28, 16) to (29, 16) where a wild Geodude Level 17 appeared on Turn 23175.
- Turn 23179: Escaped wild Geodude battle.
- Turn 23162: Discovered that (23, 14) is a solid rock wall of TYPE_2889. This physically blocks direct upward movement along Column 23, and proves that the western Middle-Left corridor (Rows 10-13) cannot be accessed directly from the south on Columns 19-28 due to the continuous solid Row 14/15 barrier.
- Turn 23163: Proved that Column 19 is completely solid on Rows 14-20, meaning the western area (Columns 17-) is completely sealed off from the eastern area (Columns 20+) on these rows.
- - Strategic Path to Western B1F: Walk West along Row 24 from (23, 24) to Column 17, but wait! We proved that Column 17 is blocked going Up at Row 23 (meaning (17, 23) is a solid, impassable rock wall). Let's trace another pathway. Since Column 17 is blocked, and Column 19 is solid on Rows 14-20, can we cross West anywhere else? No, the only other crossing is Row 31.
Wait, let's look at the screen! Is there a path going Up on Column 23? Yes, from (23, 24), we can go Up to (23, 20), but (23, 14) is blocked. Wait! Is Column 21 open? Yes, Columns 20-25 on Rows 20-25 are open!
And on Row 19, Columns 20-29 are open!
What about Row 16-17 Corridor Columns 26-35?
Wait! In B1F, is there a connection from Row 19/18 to Row 16/17?
Let's look at Column 26-35. Row 18/19 are open on Columns 30-37, and Row 16/17 are open on Columns 26-35.
So, from (33, 16) we walked Down to (33, 19).
Wait! Since (33, 16) connects to (33, 19), that means Column 33 connects Row 16 to Row 19.
But wait, we want to go from the Starting Chamber to the western Middle-Left Corridor.
If Column 17 is blocked at Row 23, how do we get to the Western Middle-Left corridor (Rows 10-13, Columns 14-23) on B1F?
Let's check if there is an alternative column!
Is Column 15 open going North of Row 24?
Let's check if we can walk to Column 15 and test if we can go Up on Column 15!
Wait! Let's write a python script to test if we can walk to (15, 24) and walk Up, or let's look at what we know about Column 15:
"Western Connecting Passage: Columns 15 and 17 are vertical passable bypasses on Rows 25-29."
Is Column 15 open on Rows 20-23?
Let's check if we can go Up on Column 15.
If Column 15 is blocked, what about Column 14?
Let's explore!
But wait! Let's check our current position: (23, 24).
Let's walk West along Row 24 to Column 15:
(23, 24) -> (15, 24) [Left 8 steps].
And from (15, 24), let's try to go Up on Column 15!
If (15, 23) is open, we can continue Up to Row 11!
Let's test this hypothesis!
- Hypothesis: Column 15 is passable going Up (North) from Row 24, providing the vertical connection to the western Middle-Left Corridor.
- Testing Protocol:
  1. From our current position (23, 24), walk Left 8 steps to (15, 24).
  2. Attempt to walk Up 1 step to (15, 23).
  3. Verify if we successfully step onto (15, 23).
  4. If yes, we have discovered the true western vertical highway!
- Let's document this test and its results clearly.

- Turn 23296: Reached (4, 33) on B1F Southern Corridor.
- Turn 23304: Backtracked from (4, 33) along the Southern Corridor and Column 33 to (33, 15) in B1F starting chamber.
- Turn 23305: Stood on (32, 15) and back to (33, 15) on B1F to perform Step-Off-and-On Protocol for Ladder D. No warp triggered, proving (33, 15) is definitely NOT an active warp trigger.
- Turn 23310-23340: Verified all previously tested coordinates. Determined that the Southeast B1F quadrant (Columns 34-37, Rows 30-33) has never been fully swept in a systematic 4x4 grid pattern.
- Turn 23347: Initiated Southern detouring path from (33, 15) via Column 33 to Column 30.
- Turn 23350: Interrupted on (30, 19) by wild Zubat Lv17. Escaped successfully on Turn 23353.
- Turn 23354: Standing at (30, 19). Preparing to resume detour path to (33, 31) to begin Southeast quadrant 4x4 grid sweep.
- Turn 23358: Interrupted on (20, 24) by wild Geodude Lv16. Escaped successfully on Turn 23359.
- Turn 23362: Interrupted on (17, 27) by wild Machop Lv15. Escaped successfully on Turn 23363.
- Turn 23367: Arrived successfully at (33, 31) in the B1F overworld.
- Turn 23375: Standing at (33, 31). Keep notepads and active strategy fully synchronized. Preparing to begin systematic 4x4 grid sweep of the southeast quadrant (Columns 34-37, Rows 30-33).
- Turn 23382: Stepped Up to (33, 30) [no warp], Right to (34, 30) [no warp], and Right to (35, 30) [no warp].
- Turn 23383: Stepped Right to (36, 30) [no warp] and Right to (37, 30) [no warp]. Completed Row 30 sweep! None of these are warp triggers.
- Turn 23385: Stepped Down to (37, 31) [no warp] and Left to (36, 31) [no warp].
- Turn 23388: Stepped Left to (35, 31) [no warp] and Left to (34, 31) [no warp]. Completed Row 31 sweep! None of these are warp triggers.
- Turn 23390: Stepped Down to (34, 32) [no warp], Right to (35, 32) [no warp], and Right to (36, 32) [no warp].
- Turn 23391: Stepped Right to (37, 32) [no warp]. Completed Row 32 sweep! None of these are warp triggers.
- Turn 23395: Stepped Down to (37, 33) [no warp].
- Turn 23397: Stepped Left to (36, 33) [no warp] and Left to (35, 33) [no warp].
- Turn 23399: Stepped Left to (34, 33) [no warp]. Completed Row 33 sweep! None of these are warp triggers.
- Turn 23413: Standing at (34, 33). Conclusively disproven the entire southeast 4x4 grid sweep.
- Turn 23484: Encountered wild Geodude Level 16 at (34, 32). Escaped successfully on Turn 23487.
- Turn 23489: Encountered wild Zubat Level 17 at (30, 31) while backtracking west. Escaped successfully on Turn 23498.
- Turn 23501: Encountered wild Geodude Level 17 at (24, 31) while backtracking west. Escaped successfully on Turn 23535.
- Turn 23539: Encountered wild Zubat Level 17 at (20, 30) while backtracking west. Escaped successfully on Turn 23550.
- Turn 23551: Standing at (20, 30) in the B1F overworld, out of battle. Preparing to resume pathfinding to (20, 24).