# Tile Mechanics
- FLOOR: Traversable.
- WALL: Impassable.
- LADDER: Warp tile.
- WARP_CARPET_DOWN: Warp tile.
- SHUTTER: Dynamic collision. Impassable (WALL) when CLOSED, Traversable (FLOOR) when OPEN. (2,6), (3,6), (10,6), (16,6), (17,6), (16,7), (17,7), (6,8), (12,8).
- Switch: Background object. Interact from adjacent tile (e.g., row 2 facing UP).

# Underground Warehouse Puzzle
- Goal: Open path to Warehouse Entrance (Map 3_55).
- Hint: "the switch on the end is the one to press first."
- Confirmed Sequence: Switch 3 -> Switch 2 -> Switch 1 (3-2-1).

# Shutter Logic (Verified Toggles)
- Baseline (OFF, OFF, OFF): (12,8) is OPEN. All others CLOSED.
- S1 (16,1) toggles: (16,6), (17,6), (16,7), (17,7), (12,8)
- S2 (10,1) toggles: (10,6), (6,8), (12,8)
- S3 (2,1) toggles: (2,6), (3,6)

# Puzzle Strategy (Attempt 4)
- Start Turn: 10831.
- Logic: S3, S2, and S1 all ON results in all shutters OPEN.
- Current Status: S3=ON, S2=ON.
- Next: Turn S1 ON.

# Area Notes
- Warehouse Entrance: Southeast quadrant (likely Map 3_55).

# Lessons Learned
- Shutter (12, 8) is toggled by BOTH S1 and S2. This explains its behavior when only one is active.
- Turn-based map updates can make it seem like shutters move "on their own" during navigation.
- Trust the `shutter_status_report_v2` and `shutter_puzzle_analyst_v2` for reliable state tracking.
- Always verify position before interaction to avoid menu-navigation errors.