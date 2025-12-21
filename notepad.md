# Tile Mechanics
- FLOOR: Traversable.
- WALL: Impassable.
- SHUTTER: Impassable when CLOSED (WALL), traversable when OPEN (FLOOR). Verified at (2, 6), (10, 6), (12, 8), (16, 6).
- LADDER: Traversable (Warp).
- WARP_CARPET_DOWN: Traversable (Warp).

# Puzzle: Goldenrod Underground Switch Puzzle
- Started: Turn 9640
- Current Goal: Execute 3-2-1 sequence (Switch 3 -> 2 -> 1) from all-OFF state.
- Hypothesis: Turning switches ON in order 3, 2, 1 will open the path to the warehouse.

# Switch Status (Turn 9797)
- Switch 3 (2, 1): 🟢 ON
- Switch 2 (10, 1): 🟢 ON (Just turned ON)
- Switch 1 (16, 1): 🔴 OFF

# Shutter States (Estimated)
- (2, 6): OPEN
- (10, 6): CLOSED
- (12, 8): OPEN
- (16, 6): CLOSED

# Area Notes
- Warehouse Entrance: Southern unseen area (Map 3_55).
- Trainers: All defeated.
- Rival: Defeated at (20, 4).
- Return Ladders: (23, 3), (21, 25), and (5, 25) lead back to the main Underground (3_52).