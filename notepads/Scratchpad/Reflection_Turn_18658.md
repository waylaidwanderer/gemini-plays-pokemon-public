B2F Spin Maze Logic:
- Spin momentum continues through normal floor tiles until hitting a wall or Stop Tile!
- (3,11) `>>` slides to (4,11) `>>` and continues sliding to (8,11) Stop Tile.
- (10,10) `^` slides to (10,9) `<<` -> (8,9) `<<` -> (4,9) `<<` -> (2,9) Stop Tile (Trap).
- (12,11) `^` slides to (12,9) `<<` -> ... -> (2,9) Stop Tile (Trap).
- To reach South maze: From (8,11) Stop Tile, walk Right to (10,11), then Down. At (10,14), turn Left to (9,14) `v` or Right to (11,14) `v` to slide South. (10,15) `^` is a trap.
Goal: Grab item at (6,12), then navigate South via (10,14).