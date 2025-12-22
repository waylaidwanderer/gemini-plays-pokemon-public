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

# Shutter Logic (Verified from system messages)
- Baseline (OFF, OFF, OFF): (12,8) OPEN. All others CLOSED.
- S3 (2,1) toggles: (2,6), (3,6), (2,7), (3,7)
- S2 (10,1) toggles: (10,6), (6,8), (12,8)
- S1 (16,1) toggles: (16,6), (17,6), (16,7), (17,7), (12,8)

# Attempt 5 Log (Completed)
- Turn 10907: Turned Switch 3 ON. Verified (2,6), (3,6) OPEN.
- Turn 10914: Turned Switch 2 ON. Verified (10,6), (6,8) OPEN.
- Turn 10925: Turned Switch 1 ON.
- Result: Sequence 3-2-1 complete. All shutters should be OPEN.

# Current Strategy: Enter Warehouse
1. Walk south to row 6 to update Mental Map.
2. Navigate to Warehouse entrance at (12, 13).

# Lessons Learned
- Toggling S1 and S2 both affects shutter (12, 8). If both are ON, it returns to OPEN.
- Shutter status report tool only updates for tiles currently in the Mental Map (seen). Must walk to shutters to verify state.
- (2, 7) and (3, 7) are shutters toggled by S3 (verified Turn 10908).