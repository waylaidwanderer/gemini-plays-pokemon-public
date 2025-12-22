# Tile Mechanics (Global)
- FLOOR: Traversable.
- WALL: Impassable.
- SHUTTER: Dynamic collision. Impassable (WALL) when CLOSED, Traversable (FLOOR) when OPEN. (2,6), (3,6), (10,6), (16,6), (17,6), (6,8), (12,8).
- Switch: Background object. Interact from adjacent tile (e.g., row 2 facing UP).
- LADDER: Warp tile. Traversable.
- WARP_CARPET_DOWN: Warp tile. Triggered by walking off the map edge.

# Underground Warehouse Puzzle
- Hint: "the switch on the end is the one to press first." (S3 or S1).
- Target Sequence: 3 (ON) -> 2 (ON) -> 1 (ON).
- Current State (Verified 10926): S3=ON, S2=OFF, S1=OFF.

# Shutter Logic (Verified)
- Baseline (OFF, OFF, OFF): (12,8) OPEN. All others CLOSED.
- S3 (2,1) toggles: (2,6), (3,6), (2,7), (3,7)
- S2 (10,1) toggles: (10,6), (6,8), (12,8)
- S1 (16,1) toggles: (16,6), (17,6), (16,7), (17,7), (12,8)

# Current Strategy: Execute 3-2-1 Sequence
1. S3 is ON.
2. Turn S2 ON (Heading to (10, 2)).
3. Turn S1 ON.
4. Navigate to Warehouse entrance (likely Map 3_55).

# Lessons Learned
- Toggling S1 and S2 both affects shutter (12, 8). If both are ON, it returns to OPEN.
- Shutter status report tool only reflects the Mental Map; must walk to shutters to verify current state.
- (12, 6), (12, 7), (12, 9) are permanent WALL tiles.
- Always check cursor position in menus to avoid turning switches OFF by mistake.