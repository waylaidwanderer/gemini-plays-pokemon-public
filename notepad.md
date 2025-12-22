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
- (0,0,0): All CLOSED.
- (0,0,1): S1 ON.
- (0,1,1): S1, S2 ON.
- (1,1,1): All ON. (Previously reached via 3-2-1, failed).

## Toggle Log
- Turn 10471: S1 toggled ON. State is (0,0,1).
- Turn 10463: (0,0,0) baseline reached. All switches OFF.
- Turn 10434: (1,0,0) verified. (2,6), (3,6) OPEN. (12,8) OPEN.
- Turn 10428: (0,0,0) baseline report: All shutters CLOSED.

# Puzzle Logic Analysis
- 3-2-1 sequence (S3->S2->S1) failed to open (6,8) and (16,6).
- New Plan: Test 1-2-3 sequence.

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