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

# Shutter Logic (Hypothesis)
- Baseline (OFF, OFF, OFF): (12,8) OPEN. All others CLOSED.
- S3 (2,1) toggles: (2,6), (3,6)
- S2 (10,1) toggles: (10,6), (6,8), (12,8)
- S1 (16,1) toggles: (16,6), (17,6), (16,7), (17,7), (12,8)

# Attempt 5 Log (Current Strategy)
- S3 (2,1): ON (Turn 10907).
- S2 (10,1): ON (Turn 10914).
- S1 (16,1): ON (In progress).
- Goal: All shutters OPEN.
- Next: Navigate to Warehouse entrance at (12, 13).

# Lessons Learned
- Toggling S1 and S2 both affects shutter (12, 8). If both are ON, it returns to OPEN.
- Always verify switch state via text before concluding a step.
- Trust the report tool for state verification but walk to tiles to update Mental Map.
- (2, 7) and (3, 7) are permanent WALL tiles, not shutters.