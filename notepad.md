# Tile Mechanics
- FLOOR: Traversable.
- WALL: Impassable.
- SHUTTER: Dynamic collision. Impassable (WALL) when CLOSED, Traversable (FLOOR) when OPEN.
- Switch (2,1), (10,1), (16,1): Background objects. Interact from row 2 (facing UP).

# Underground Warehouse Puzzle
- Goal: Open path to Warehouse Entrance at (21, 29) [leading to Map 3_55].
- Current Sequence Strategy: 1-2-3 (Switch 1 -> Switch 2 -> Switch 3).
- 3-2-1 sequence failed to open southeast path at Turn 10448.

## Shutter Toggle Mapping (S3, S2, S1)
| State | (2,6/7) | (3,6/7) | (10,6/7) | (12,8/9) | (16,6/7) | (17,6/7) | (6,8/9) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| (0,0,0) | CLOSED | CLOSED | CLOSED | CLOSED | CLOSED | CLOSED | CLOSED |
| (0,0,1) | CLOSED | CLOSED | CLOSED | OPEN? | OPEN | OPEN | CLOSED |
| (1,0,0) | OPEN | OPEN | CLOSED | OPEN | CLOSED | CLOSED | CLOSED |
| (1,1,0) | ? | ? | ? | ? | ? | ? | ? |
| (1,1,1) | ? | ? | ? | ? | ? | ? | ? |

## Verified Toggle Logic (Primary Effects from 0,0,0)
- Switch 1 (16,1): Toggles (16,6/7), (17,6/7).
- Switch 2 (10,1): Toggles (10,6/7), (6,8/9).
- Switch 3 (2,1): Toggles (2,6/7), (3,6/7), (12,8/9).

## Toggle Log
- Turn 10434: (1,0,0) verified. (2,6), (3,6), (2,7), (3,7) are OPEN. (12,8) is OPEN. (10,6), (6,8) are CLOSED.
- Turn 10428: (0,0,0) baseline report: All shutters CLOSED.
- Turn 10415: (0,0,1) verified. (16,6), (17,6) are OPEN.

# Area Notes
- Warehouse Entrance: Southeast quadrant.
- Key NPCs: Rocket Girl (19,12), Emergency Switch (20,11).
- Ladders: (23,3) To Switch Room Entrance, (21,25) To North, (5,25) To South.

# Lessons Learned
- Standardize switch states as (S3, S2, S1).
- Visual confirmation is required after every toggle.
- Deductions are not verifications.
- Reset to (0,0,0) before sequence attempts.
- Shutter (12,8) has inconsistent behavior; verify visually.