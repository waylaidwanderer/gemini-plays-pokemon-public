# Tile Mechanics
- FLOOR: Traversable.
- WALL: Impassable.
- SHUTTER: Dynamic collision. Impassable (WALL) when CLOSED, Traversable (FLOOR) when OPEN.
- Switch (2,1), (10,1), (16,1): Background objects. Interact from row 2 (facing UP).

# Underground Warehouse Puzzle
- Goal: Open path to Warehouse Entrance (Map 3_55).
- Solution: 3-2-1 sequence (Switch 3 -> Switch 2 -> Switch 1) from (0,0,0) baseline.

# Current Plan: 3-2-1 Sequence and Mapping
1. Baseline: (0,0,0) confirmed (S3=OFF, S2=OFF, S1=OFF). Verified Turn 10561.
2. Turn S3 ON (at 2,1).
3. Run shutter report to map S3 effects.
4. Turn S2 ON (at 10,1).
5. Run shutter report to map S2 effects.
6. Turn S1 ON (at 16,1).
7. Run shutter report to map S1 effects.
8. Verify path to Warehouse (Map 3_55).

## Primary Effects (Mapping in progress)
- S3 (2,1): ?
- S2 (10,1): ?
- S1 (16,1): ?
- Baseline (0,0,0): (2,6) CLOSED, (3,6) CLOSED, (10,6) CLOSED, (16,6) CLOSED, (6,8) CLOSED, (12,8) OPEN, (17,6) CLOSED, (17,7) CLOSED. (Verified Turn 10561)

# Area Notes
- Warehouse Entrance: Southeast quadrant (likely Map 3_55).
- EXIT: (21, 29) leads back to Goldenrod City. Do NOT use.

# Lessons Learned
- Start from (0,0,0) baseline before any sequence.
- (21, 29) is an exit, not the goal.
- 3-2-1 sequence requires starting from all switches OFF.
- Verification requires physically walking to the shutters.
- Do not repeat failed states; analyze data instead.
- Recording start turn: 10544.