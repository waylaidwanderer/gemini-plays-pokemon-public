B2F Spin Maze Logic:
- From (14, 12) Stop Tile, stepping to (12, 11) `^` slides to (12, 9) `<<` -> (10, 9) `<<` -> (8, 9) `<<` -> (4, 9) `<<` -> (2, 9) Stop Tile.
- From (2, 9), can navigate freely down left side. Item at (1, 11).
- Path to (6, 12) Item: From (3, 10), step Right to (4, 10), Down to (4, 11) `>>` -> slide to (6, 11). Grab item at (6, 12).
- Loop back to (2, 9) from (6, 11): Right to (8, 11), Down to (8, 12) `^` -> slide to (8, 9) `<<` -> (4, 9) `<<` -> (2, 9) Stop Tile.
- Path to (16, 8) Item: Need to reach (10, 10) `^` which slides Up to (10, 7) in the top hallway.
Goal: Grab items, then search south of (1, 13) for B3F stairs.