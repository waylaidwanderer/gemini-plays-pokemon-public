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
*To be populated as we encounter trainers in the dark.*