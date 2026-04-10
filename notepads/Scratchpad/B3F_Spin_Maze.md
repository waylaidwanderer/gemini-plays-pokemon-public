B3F Spin Maze Mapping (North Entrance):
Start at (13, 11) [Walkable].
- Step Left onto (12, 11) `<<`: slides left to (11, 11) -> (10, 11) [Stop Tile].

From (10, 11) Stop Tile:
- Up: (10, 10) is Box.
- Left: (9, 11) is Walkable. Dead end bounded by Wall at X=8 and Boxes at Y=10, Y=12.
- Down: (10, 12) -> (10, 13) `>>` slides right to (14, 13) [Stop Tile].
- Right: (11, 11) is Walkable -> leads to (12, 11) `<<` -> loops to (10, 11).

From (14, 13) Stop Tile:
- Up: Box.
- Left: Walkable to (12, 13). From (12, 13), Down is clear corridor to (12, 16). Left from (12, 16) goes to (9, 16). Down from (12, 16) is (12, 17) `>>` -> (14, 17) `^^` -> (14, 15) `>>` -> (18, 15) Stop Tile.
- Right: (15, 13) -> (16, 13) `^^` slides Up to (16, 11) [Stop Tile] (Exit to Main Area).
- Down: (14, 14) -> (14, 15) `>>` slides Right to (18, 15) [Stop Tile].

From (9, 16) Normal Floor:
- Down to (9, 18), Right to (10, 18).
- From (10, 18), Down is (10, 19) `>>` -> hits (14, 19) `^^` -> hits (14, 17) `^^` -> hits (14, 16) `>>` -> hits (15, 16) `>>` -> stops at (16, 16) Normal Floor.
- From (10, 18), Right is (11, 18) `>>` -> slides Right to hit (15, 18) `vv` -> slides Down to Stop Tile at (15, 22).

From (15, 22) Normal Floor (stopped by Box at 15, 23):
- Up: Walkable to (15, 21), (15, 20), (15, 19). From (15, 19), Left is (14, 19) `^^`.
- Down: Box at (15, 23).
- Right: Wall at (16, 22).
- Left: Walkable corridor going left to (14, 22), (13, 22), (12, 22), (11, 22), (10, 22) [Rocket Grunt].
- From corridor, Up paths:
  - From (14, 22): Up to (14, 21). (14, 20) is Box.
  - From (12, 22): Up to (12, 21), Up to (12, 20) `^^`.

From (16, 16) Normal Floor:
- Right to (17, 16) [Stop Tile].
- Up to (16, 14), then Up to (16, 13) `^^` (Escape path).

From (18, 15) Stop Tile:
- Up: Box.
- Down: (18, 16) `^^` -> loop to (18, 15).
- Left: (17, 15) Walkable.
  - Up from (17, 15): (17, 14) -> (17, 13).
    - Left from (17, 13): (16, 13) `^^` slides to (16, 11) Stop Tile (Exit).
    - Up from (17, 13): (17, 12) `vv` slides to (17, 16) [Stop Tile].
- Right: (19, 15) Walkable.