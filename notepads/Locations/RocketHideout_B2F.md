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
- From (2, 9) stop area: (4, 11) R spinner -> (8, 11) stop tile. (4, 14) R spinner -> (9, 16) stop tile.
- Elevator doors located at (2, 8) and (3, 8), accessible from the (2, 9) and (3, 9) tiles. This should be the way to B3F/B4F!