# Tile Mechanics (Global)
- FLOOR: Traversable.
- WALL: Impassable.
- SHUTTER: Dynamic collision. Impassable (WALL) when CLOSED, Traversable (FLOOR) when OPEN. (2,6), (3,6), (10,6), (16,6), (17,6), (6,8), (12,8).
- Switch: Background object. Interact from adjacent tile (e.g., row 2 facing UP).
- LADDER: Warp tile. Traversable.
- WARP_CARPET_DOWN: Warp tile. Triggered by walking off the map edge.

# Underground Warehouse Puzzle
- Hint: "the switch on the end is the one to press first." (S3 or S1).
- Confirmed Sequence: 3 (ON) -> 2 (ON) -> 1 (ON).
- Current State: S3=ON, S2=ON, S1=ON. (Sequence Complete).

# Shutter Logic (Hypothesis)
- Baseline (OFF, OFF, OFF): (12,8) OPEN. All others CLOSED.
- S3 (2,1) toggles: (2,6), (3,6)
- S2 (10,1) toggles: (10,6), (6,8), (12,8)
- S1 (16,1) toggles: (16,6), (17,6), (12,8)

# Current Strategy: Enter Warehouse
1. Walk south through (2, 6) or (12, 8) to update Mental Map and verify all shutters are OPEN.
2. Explore the southern area (Rows 9-29) to locate the Warehouse entrance (likely Map 3_55).

# Lessons Learned
- Toggling S1 and S2 both affects shutter (12, 8). If both are ON, it returns to OPEN.
- Shutter status report tool only reflects the Mental Map; must walk to shutters to verify current state.
- (2, 7), (3, 7), (12, 6), (12, 7) are permanent WALL tiles.