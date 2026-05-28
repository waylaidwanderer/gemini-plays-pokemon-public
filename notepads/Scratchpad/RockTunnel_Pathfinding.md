# Rock Tunnel Dark Maze Pathfinding & Coordinate Log (Turn 20617)

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

## Trainer Coordinates & Battles:
- **Turn 20677**: Encountered and defeated Pokémaniac at (22, 8) on Map 0_82 (CUBONE Lv 23). Switched to GEMMY to sweep. Resolved on Turn 20698.
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

## Combat Interruption Protocol (Turn 20731):
- When a wild battle interrupts a movement sequence:
  1. Complete the battle.
  2. In the very first turn back in the overworld, run a python script or check the GameState's Player Position x and y coordinates.
  3. Compare these actual coordinates with the expected next step of the pathfinding log.
  4. Only resume the movement sequence from the *actual* position, updating the pathfinding log with the exact coordinate where the battle occurred.
- **Turn 20733**: Encountered wild ZUBAT on (23, 12). Movement sequence aborted after 1 step (X coordinate increased from 22 to 23).
  - Combat status: In progress. Lead SPARKY (Pikachu) Lv 23.
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