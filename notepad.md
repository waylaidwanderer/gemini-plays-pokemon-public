# Tile Mechanics
- FLOOR: Traversable.
- WALL: Impassable.
- SHUTTER: Dynamic collision. Impassable (WALL) when CLOSED, Traversable (FLOOR) when OPEN. (2,6), (3,6), (10,6), (16,6), (17,6), (6,8), (12,8).
- Switch: Background object at (2,1), (10,1), (16,1). Interact from row 2 (facing UP).

# Underground Warehouse Puzzle
- Goal: Open path to Warehouse Entrance (Map 3_55).
- Rumored Solution: 3-2-1 Sequence (S3 -> S2 -> S1).

# Verified Shutter Logic
- S3 (2,1) toggles: (2,6), (3,6)
- S2 (10,1) toggles: (10,6), (6,8), (12,8)
- S1 (16,1) toggles: (16,6), (17,6), (16,7), (17,7), (12,8)
- Baseline (OFF, OFF, OFF): (12,8) is OPEN, all others CLOSED.

# Current Strategy: Execute 3-2-1 Sequence
1. Step 1: Switch 3 (ON) - COMPLETED.
2. Step 2: Switch 2 (ON) - In progress (Current position: (10,3)).
3. Step 3: Switch 1 (ON) - Heading to (16,1).
4. Enter Warehouse (Map 3_55).

# Puzzle Logic Theory
- The 3-2-1 sequence is based on the Rocket Grunt's hint: "the switch on the end is the one to press first."
- S3 opens the leftmost path. S2 opens the middle path but closes the baseline path at (12,8). S1 opens the rightmost path and re-opens (12,8).
- Result: All southern paths are FLOOR, allowing full access to the Warehouse.

# Area Notes
- Warehouse Entrance: Southeast quadrant (likely Map 3_55).
- EXIT: (21, 29) leads back to Goldenrod City. Do NOT use.

# Lessons Learned
- Verify shutter states visually or via tool.
- NPCs and Items block paths like WALLs.