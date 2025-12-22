# Tile Mechanics
- FLOOR: Traversable.
- WALL: Impassable.
- SHUTTER: Dynamic collision. Impassable (WALL) when CLOSED, Traversable (FLOOR) when OPEN.
- Switch (2,1), (10,1), (16,1): Background objects. Interact from row 2 (facing UP).

# Underground Warehouse Puzzle
- Goal: Open path to Warehouse Entrance (Map 3_55).
- Verified Solution: 3-2-1 sequence (Switch 3 -> Switch 2 -> Switch 1) from (0,0,0) baseline.

# Current Plan: Reset and Execute
1. Reset all switches to OFF (0,0,0). (In Progress)
2. Verify all shutters are CLOSED.
3. Toggle S3 ON.
4. Toggle S2 ON.
5. Toggle S1 ON.
6. Physically walk through (2,6) -> (6,8) -> (12,8) to southeast.

## Primary Effects (to be verified from 0,0,0)
- S3 (2,1): Toggles (2,6), (3,6), (12,8).
- S2 (10,1): Toggles (10,6), (6,8), (2,6).
- S1 (16,1): Toggles (16,6), (17,6), (10,6).

# Area Notes
- Warehouse Entrance: Southeast quadrant (likely Map 3_55).
- EXIT: (21, 29) leads back to Goldenrod City. Do NOT use.

# Lessons Learned
- Always start from (0,0,0) baseline.
- Toggling a switch multiple times reverses the effect.
- (21, 29) is an exit, not the goal.
- Order of operations is critical.