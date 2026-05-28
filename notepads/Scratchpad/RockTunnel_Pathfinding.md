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
- **Turn 20677**: Encountered Pokémaniac at (22, 8) on Map 0_82.
  - Opponent: CUBONE Lv 23 (Ground-type).
  - Matchup: Lead SPARKY (Pikachu) Lv 23. Ground is immune to Electric, and super-effective against Pikachu.
  - Battle Strategy: Switch immediately to GEMMY (Wartortle) Lv 31 to use Water Gun (super-effective) and sweep.
  - Battle Status: In Progress.
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