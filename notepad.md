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
- Warehouse Entrance: Likely behind the shutters in the southeast (Map 3_55).
- Key NPCs: Rocket Girl (19,12), Emergency Switch (20,11).
- EXIT: (21, 29) leads back to Goldenrod City. Do NOT use until Director is rescued.

# Puzzle Strategy
- Committed to 3-2-1 sequence.
- Step 1: Switch 3 ON (Done).
- Step 2: Switch 2 ON (Done).
- Step 3: Switch 1 ON (Next).
- Step 4: Walk south to (2,6) -> (12,8) -> Southeast to find Map 3_55 entrance.
- Verification: Do NOT reset until path is physically tested.