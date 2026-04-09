B3F Spin Maze Mapping:
- Started from (20, 11). Walkable area leading to the maze.
- Stop Tile at (16, 11).
- Spin Tile at (17, 12) [Red v].
- Spin Tile at (16, 13) [Red ^].
- Stop Tile at (18, 15).
Exploring this maze to reach item at (20, 14) and stairs.
Path to Item (20, 14):
From (20, 11) -> Left to (17, 11) -> Down to (17, 12) [v] -> slides to normal floor. Walk Down to (17, 16). Right to (18, 16) [^] -> slides to (18, 15) Stop Tile. Right to (20, 15), Up to (20, 14) Item.
Return path from (18, 15): Left to (17, 15), Up to (17, 13), Left to (16, 13) [^] -> slides to (16, 11) Stop Tile.
Path Forward Analysis:
- Eastern side (X>=16) is blocked from going South by tables.
- X=14 and X=15 South paths are trapped by spin tiles pushing me back into the start area or item area.
- To progress, I must return to (16, 11) Stop Tile, walk West to X<=13, and then walk South to bypass the spin tile blockades, before cutting back East to (15, 18) [v] spin tile or finding the real stairs.