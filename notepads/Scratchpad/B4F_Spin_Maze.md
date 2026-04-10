B4F Spin Maze Mapping:
- Start from Stairs at (19, 18).
- Spin Tile at (18, 16) `^^`.
- Spin Tile at (15, 16) `>>`.
- Spin Tile at (15, 18) `vv`.
- Stop Tile at (17, 16).
- Stop Tile at (15, 22).
- Stop Tile at (16, 11).
- Stop Tile at (14, 13).
- Spin Tile at (17, 12) `vv`.
- Spin Tile at (16, 13) `^^`.
- Spin Tile at (14, 11) `>>`.
- Spin Tile at (12, 11) `<<`.
- Spin Tile at (14, 15) `>>`.

Paths tested:
- Start (19, 18) -> Walk Left to (18, 18), Up to (18, 17), Up to (18, 16) `^^` -> Slides Up, hits obstacle at (18, 14), stopping at (18, 15) Normal Floor.
- From (18, 15) Normal Floor -> Walk Left to (16, 15), Up to (16, 13) `^^` -> Slides Up to (16, 11) Stop Tile.
- From (16, 11) Stop Tile -> Right to (17, 11), Down to (17, 12) `vv` -> Slides Down to (17, 16) Stop Tile.
- From (16, 11) Stop Tile -> Left to (15, 11), Down to (15, 13), Left to (14, 13) Stop Tile.