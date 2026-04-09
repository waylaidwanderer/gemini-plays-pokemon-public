B2F Spin Maze Logic:
- Spin momentum continues through normal floor tiles until hitting a wall or Stop Tile!
- (3,11) `>>` slides to (4,11) `>>` and continues sliding to (8,11) Stop Tile.
- (10,10) `^` slides to (10,9) `<<` -> (8,9) `<<` -> (4,9) `<<` -> (2,9) Stop Tile (Trap).
- To reach South maze: From (8,11) Stop Tile, walk Right to (10,11), then Down to (10,14). Turn Left to (9,14) `v` -> slides to (9,16) Stop Tile.
- From (9,16): Step Right to (10,16).
  - Path A: Down to (10,17) `>>` -> (12,17) `>>` -> (14,17) `^` -> (14,15) Stop Tile.
  - Path B: Right to (11,16) `>>` -> (13,16) `>>` -> unknown (East).
Goal: Execute Path A to (14,15) and search for B3F stairs.