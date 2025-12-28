# Ice Path B2F Ladder Solution
- Goal: Reach the ladder to B3F at (9, 11).
- Strategy: Use boulders as stoppers to land on the central FLOOR strip.

## Boulder Stoppers (Confirmed)
- Boulder 1: (11, 3). Status: Confirmed (Turn 29023).
- Boulder 2: (4, 7). Status: Confirmed (Turn 29019).
- Boulder 3: (3, 12). Status: Confirmed (Turn 29026).
- Boulder 4: (12, 13). Status: Confirmed (Turn 29025).

## Sliding Sequence
1. From (3, 17), move Right -> Slide to (16, 17).
2. From (16, 17), move Up -> Walk to (16, 16).
3. From (16, 16), move Up -> Slide to (16, 3).
4. From (16, 3), move Left -> Hit B1 at (11, 3), stop at (12, 3).
5. From (12, 3), move Down -> Hit B4 at (12, 13), stop at (12, 12).
6. From (12, 12), move Left -> Hit B3 at (3, 12), stop at (4, 12).
7. From (4, 12), move Up -> Hit B2 at (4, 7), stop at (4, 8).
8. From (4, 8), move Right -> Stop on FLOOR at (8, 8).
9. Walk to (8, 9) to pick up item, then to ladder at (9, 11).

## Tile Mechanics
- FLOOR: Walkable.
- WALL: Impassable.
- ICE: Sliding mechanic.
- BOULDER: Stopper for sliding.

## Progress
- Turn 29021: Confirmed all 4 boulders are in position on B2F. Verified sliding path to ladder.
- Turn 29031: Item collected. Proceeding to ladder at (9, 11).

# Ice Path B3F
- Goal: Explore and find exit to B4F or beyond.
- Status: Just arrived from B2F.

## Map Objects
- Item: (5, 7) - Uncollected.
- Rock: (6, 6) - ID 2.
- Wall: (9, 2) and (10, 2) are FLOOR_UP_WALL tiles that block movement from above.
- Wall: (12, 4) is a FLOOR_UP_WALL tile.

## Exploration
- Path to (5, 7) is blocked by walls (9, 2) and the rock at (6, 6). Exploring the eastern corridor via (13, 1) to find a way around.