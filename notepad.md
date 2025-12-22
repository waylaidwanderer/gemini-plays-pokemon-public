# Tile Mechanics
- FLOOR: Traversable.
- WALL: Impassable.
- SHUTTER: Dynamic collision. Impassable (WALL) when CLOSED, Traversable (FLOOR) when OPEN.
- Switch (2,1), (10,1), (16,1): Background objects. Interact from row 2 (facing UP).

# Underground Warehouse Puzzle
- Goal: Open path to Warehouse Entrance (unseen southeast area, likely Map 3_55).
- Sequence Strategy: 3-2-1 (Switch 3 -> Switch 2 -> Switch 1).
- Note: (21, 29) is the EXIT to Goldenrod City, NOT the Warehouse entrance.

## Shutter Toggle Mapping (S3, S2, S1)
- State (0,0,0): All CLOSED.
- State (1,1,1) [reached via 3-2-1]: (2,6) OPEN, (12,8) OPEN. This clears a path toward the southeast quadrant.

## Toggle Log
- Turn 10505: S2 toggled ON. State is (1,1,0).
- Turn 10499: S3 toggled ON. State is (1,0,0). (2,6), (3,6) verified OPEN.
- Turn 10490: (0,0,0) baseline reached. All switches OFF.

# Area Notes
- Warehouse Entrance: Southeast quadrant.
- Key NPCs: Rocket Girl (19,12), Emergency Switch (20,11).
- Ladders: (23,3) To Switch Room Entrance, (21,25) To North, (5,25) To South.

# Lessons Learned
- Standardize switch states as (S3, S2, S1).
- Visual confirmation is required after every toggle.
- (21, 29) is an exit, not the objective.
- 3-2-1 sequence clears the path to the southeast via (2,6) and (12,8).
- Reset to (0,0,0) before starting the sequence.