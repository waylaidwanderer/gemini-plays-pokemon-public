# Tile Mechanics
- FLOOR: Traversable.
- WALL: Impassable.
- SHUTTER: Dynamic collision. Impassable (WALL) when CLOSED, Traversable (FLOOR) when OPEN.
- Switch: Background object. Interact from adjacent tile (e.g., row 2 facing UP).
- LADDER: Warp tile. Traversable.
- WARP_CARPET_DOWN: Warp tile. Triggered by walking off the map edge.

# Underground Warehouse Puzzle
- Hint: "the switch on the end is the one to press first." (S3 or S1).
- Target Sequence: 3 (ON) -> 2 (ON) -> 1 (ON).

# Shutter Logic (Verified from 10832 report & navigation)
- Baseline (OFF, OFF, OFF): (12,8) OPEN. All others CLOSED.
- S3 (2,1) toggles: (2,6), (3,6), (2,7), (3,7)
- S2 (10,1) toggles: (10,6), (6,8), (12,8)
- S1 (16,1) toggles: (16,6), (17,6), (16,7), (17,7), (12,8)

# Attempt 5 Log (Completed)
- S3 (2,1): ON (Turn 10907). Verified (2,6), (3,6), (2,7), (3,7) OPEN.
- S2 (10,1): ON (Turn 10914). Verified (10,6), (6,8) OPEN, (12,8) CLOSED.
- S1 (16,1): ON (Turn 10925).
- Result: Sequence 3-2-1 complete. All shutters should be OPEN.

# Current Strategy: Enter Warehouse
1. Verify all shutters are OPEN (In progress).
2. Navigate to Warehouse entrance at (12, 13).