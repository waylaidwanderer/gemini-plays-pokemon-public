# Tile Mechanics
- FLOOR: Traversable.
- WALL: Impassable.
- SHUTTER: Dynamic collision. Impassable (WALL) when CLOSED, Traversable (FLOOR) when OPEN.
- Switch: Background object. Interact from adjacent tile (e.g., row 2 facing UP).

# Underground Warehouse Puzzle
- Hint: "the switch on the end is the one to press first." (S3 or S1).
- Target Sequence: 3 (ON) -> 2 (ON) -> 1 (ON).

# Shutter Logic (Hypothesis)
- Baseline (OFF, OFF, OFF): (12,8) OPEN. All others CLOSED.
- S3 (2,1) toggles: (2,6), (3,6), (2,7), (3,7)
- S2 (10,1) toggles: (10,6), (6,8), (12,8)
- S1 (16,1) toggles: (16,6), (17,6), (16,7), (17,7), (12,8)

# Attempt 5 Log (Current)
- Turn 10831-10896: All switches reset to OFF.
- Turn 10907: Turned Switch 3 ON.
- Turn 10910: Visually verified (2, 6) and (3, 6) are OPEN. Row 7 shutters (2, 7) and (3, 7) are also OPEN.

# Current Strategy: 3-2-1 Sequence
1. Turn S3 ON (In progress).
2. Walk to (2, 6) to verify it is OPEN.
3. Turn S2 ON.
4. Walk to (10, 6) and (12, 8) to verify states.
5. Turn S1 ON.
6. Enter Warehouse at (12, 13).

# Lessons Learned
- Don't trust the report tool for off-screen tiles; walk to them to update the Mental Map.
- Toggling S1 and S2 both affects shutter (12, 8).
- Always verify switch state via text before concluding a step.