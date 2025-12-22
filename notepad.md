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

# Shutter Logic (Verified Toggles)
- Baseline (OFF, OFF, OFF): (12,8) is OPEN. All others CLOSED.
- S1 (16,1) toggles: (16,6), (17,6), (16,7), (17,7), (12,8)
- S2 (10,1) toggles: (10,6), (6,8), (12,8)
- S3 (2,1) toggles: (2,6), (3,6)

# Puzzle Solving Log
- Attempt 4 (Current): 3-2-1 Sequence from clean reset.
  - Reset all switches to OFF (Turn 10831).
  - Step 1: Turn Switch 3 ON (Turn 10833). (VERIFIED: S3=ON, S2=OFF, S1=OFF)
  - Step 2: Turn Switch 2 ON (In progress).

# Current Strategy: Execute 3-2-1 Sequence
1. Turn Switch 3 ON (COMPLETED).
2. Turn Switch 2 ON (In progress).
3. Turn Switch 1 ON.
4. Enter Warehouse at (12, 13).

# Area Notes
- Warehouse Entrance: Southeast quadrant (likely Map 3_55).

# Lessons Learned
- S1 and S2 BOTH toggle (12, 8). This is why it closes when only one is ON and opens when both are ON.
- Baseline has (12, 8) OPEN, which is the default southern exit.
- 3-2-1 sequence results in ALL shutters being OPEN.
- Trust the report tool over navigation "tile change" messages for state verification, but note that navigation will abort if a shutter closes in its path.