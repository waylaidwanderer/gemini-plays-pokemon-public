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
- Left: Walkable to (13, 13). Cannot walk to (12, 13) (solid). Dead end.
- Right: (15, 13) -> (16, 13) `^^` slides Up to (16, 11) [Stop Tile] (Exit to Main Area).
- Down: (14, 14) -> (14, 15) `>>` slides Right to (18, 15) [Stop Tile].

From (18, 15) Stop Tile:
- Up: Box.
- Down: (18, 16) `^^` -> loop to (18, 15).
- Left: (17, 15) Walkable.
  - Up from (17, 15): (17, 14) -> (17, 13).
    - Left from (17, 13): (16, 13) `^^` slides to (16, 11) Stop Tile (Exit).
    - Up from (17, 13): (17, 12) `vv` slides to (17, 16) [Stop Tile].
- Right: (19, 15) Walkable.