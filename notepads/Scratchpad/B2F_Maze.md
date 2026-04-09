B2F Spin Maze Mapping:
Mechanics: A spin tile initiates a slide in its indicated direction. The player continues sliding across normal floor tiles until they hit a Solid Obstacle or a grey 4-square Stop Tile.

Stop Tiles identified:
(2, 9), (8, 11), (14, 12), (14, 15), (11, 20), (9, 24), (14, 25).

Spin Tiles (Direction):
(10, 9) <<, (8, 9) <<, (4, 9) <<
(10, 10) ^
(4, 11) >>
(8, 12) ^
(11, 14) v
(10, 15) ^

Paths tested:
- (4, 11) >> slides right to Stop Tile at (8, 11).
- (10, 10) ^ slides up to (10, 9) <<, slides left to (8, 9) <<, slides left to (4, 9) <<, slides left to Stop Tile at (2, 9).
- (10, 15) ^ slides up to (10, 10) ^ -> loop to (2, 9).

Navigation to East Side:
1. Reach Stop Tile at (14, 15). (Path unknown, need to re-find)
2. Right to (15, 15), Down to (15, 16) `v` -> slides to (15, 18) Stop Tile.
3. Left to (13, 18) `<<` -> hits (11, 18) `v` -> slides to (11, 20) Stop Tile.
4. Right to (14, 20), Down to (14, 22), Left to (13, 22) `<<` -> hits (9, 22) `v` -> slides to (9, 24) Stop Tile.
5. Right to (10, 24), Down to (10, 25) `>>` -> slides to (14, 25) Stop Tile.