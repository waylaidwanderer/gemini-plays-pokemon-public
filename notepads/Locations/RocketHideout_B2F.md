# Rocket Hideout B2F
[Start: Turn 10168]

## Spinner Maze
- Entrance at right side.
- Top path: (17, 11) L -> (14, 11) U -> (14, 9) L -> (4, 9) L. Player ends up at (2, 9).
- Items visible: (1, 11), (6, 12).
- Middle path: (4, 15) R -> (8, 15) U -> (8, 12) U -> stops at (8, 11).
- From (8, 11), going L leads to item at (6, 12).
### Tile Dictionary
- UP: TYPE_cf9b
- DOWN: TYPE_55cd
- LEFT: TYPE_55d0
- RIGHT: TYPE_64a2
- STOP: TYPE_55d4
- WALK: TYPE_3fe2
- Bottom path: From (8, 11) stop tile, go R to (10, 11), U to (10, 10) Up spinner. Leads to (2, 9) stop tile, which is near an elevator.
- Found Item at (16, 8). Reached via navigating the right-side paths after the initial top/middle exploration.
- From (8, 11) stop tile, going R, R, D, D, D, R hits (11, 14) Down spinner. Leads to (15, 18) stop tile.
- From (15, 18) stop tile, L L hits (13, 18) L spinner -> (11, 18) D spinner -> (11, 20) stop tile.
- From (11, 20) stop tile, L U hits (10, 19) U spinner -> (10, 17) R spinner -> (12, 17) R spinner -> (14, 17) U spinner -> (14, 15) stop tile.
- From (14, 15) stop tile, R R D hits (16, 16) U spinner -> (16, 14) U spinner -> (16, 13) stop tile.
- From (16, 13) stop tile, going U U L hits (16, 11) U spinner -> (16, 9) L spinner -> (14, 9) L spinner -> (2, 9) stop tile.
- Wait, I ended up at (14, 12) somehow.
- From (9, 16) stop tile: R R hits (11, 16) R spinner. R D hits (10, 17) R spinner. U R hits (10, 15) U spinner. U L U hits (8, 14) which is walkable.
- The stairs at (27, 8) go back UP to B1F (at 23, 2). Not down to B3F!
- From (2, 9) stop area: (4, 11) R spinner -> (8, 11) stop tile. (5, 14) R spinner -> (9, 16) stop tile.
- The grey panels at (2, 9) and (3, 9) are just the graphics for the stop tiles! No elevator here.
- The entire left corridor from (2, 9) to (4, 15) is a dead end. All three right-facing spinners return to the maze at (8, 11) or (9, 16).
- From (16, 13) stop tile, going R R U U L hits (17, 11) L spinner -> (2, 9) stop tile.
- From (11, 20) stop tile, going R R R D D L hits (13, 22) L spinner -> (9, 24) stop tile.
- From (9, 24) stop tile: 
  - Option A: L U hits (8, 23) U spinner.
  - Option B: R D hits (10, 25) R spinner.
- From (14, 25) stop tile, I can walk freely in the corridor to the right (X=14..19, Y=21..25).
- From (8, 23) U spinner, path leads to (2, 19) stop tile. Item found at (3, 21).
- From (2, 19) area, can walk down to (4, 22) U spinner.
- From (6,20) stop tile, going D L L L leads to item at (3,21).
- From (6,20) stop tile, going U L hits (4,19) L spinner -> (2,19) stop tile.
- Found stairs at (21, 8) leading to B3F (Map 0_201)!
## TRUE ELEVATOR PATH (Step-by-Step)
1. From B2F (27, 8) stairs, walk to (17, 11) Top Spinner -> Ends at (2, 9) Stop.
2. From (2, 9) Stop: Walk D D R R to (4, 11) spinner -> Ends at (8, 11) Stop.
3. From (8, 11) Stop: Walk R R D D D R to (11, 14) spinner -> Ends at (15, 18) Stop.
4. From (15, 18) Stop: Walk L L to (13, 18) spinner -> Ends at (11, 20) Stop.
5. From (11, 20) Stop: Walk R R R D D L to (13, 22) spinner -> Ends at (9, 24) Stop.
6. From (9, 24) Stop: Walk R D to (10, 25) spinner -> Ends at (14, 25) Stop.
7. From (14, 25) Stop: Walk right and up to (21, 22) stairs -> Takes you to B1F South.