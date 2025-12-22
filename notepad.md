# Tile Mechanics
- FLOOR: Traversable.
- WALL: Impassable.
- LADDER: Warp tile.
- WARP_CARPET_DOWN: Warp tile.
- SHUTTER: Dynamic collision. Impassable (WALL) when CLOSED, Traversable (FLOOR) when OPEN. (2,6), (3,6), (10,6), (16,6), (17,6), (16,7), (17,7), (6,8), (12,8).
- Switch: Background object. Interact from adjacent tile (e.g., row 2 facing UP).

# Underground Warehouse Puzzle
- Goal: Open path to Warehouse Entrance (Map 3_55).
- Hint from Rocket Grunt: "the switch on the end is the one to press first."
- Order: Switch 3 -> Switch 2 -> Switch 1.

# Shutter Logic (Hypothesized Toggles)
- Baseline (OFF, OFF, OFF): (12,8) is OPEN, all others CLOSED.
- S1 (16,1) toggles: (16,6), (17,6), (16,7), (17,7), (12,8)
- S2 (10,1) toggles: (10,6), (6,8), (12,8)
- S3 (2,1) toggles: (2,6), (3,6)

# Puzzle Solving Log
- Attempt 4 (Current): 3-2-1 Sequence from clean reset.
  - Reset all switches to OFF (Turn 10831).
  - Step 1: Turn Switch 3 ON (Turn 10832).

# Current Strategy: Execute 3-2-1 Sequence
1. Turn Switch 3 ON (In progress).
2. Turn Switch 2 ON.
3. Turn Switch 1 ON.
4. Enter Warehouse at (12, 13).

# Area Notes
- Warehouse Entrance: Southeast quadrant (likely Map 3_55).

# Lessons Learned
- S1 and S2 both toggle (12, 8). This explains the "unexpected" closing.
- NPC movement or turn-based updates can make shutters appear to move on their own.
- Trust the shutter report tool for state verification.