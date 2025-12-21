# Tile Mechanics
- FLOOR: Traversable.
- WALL: Impassable.
- SHUTTER: Impassable when CLOSED (WALL), traversable when OPEN (FLOOR). Verified at (2, 6), (10, 6), (12, 8), (16, 6).
- LADDER: Traversable (Warp).
- WARP_CARPET_DOWN: Traversable (Warp).

# Puzzle: Goldenrod Underground Switch Puzzle
- Started: Turn 9640
- Current Goal: Execute 3-2-1 sequence (Switch 3 -> 2 -> 1) from all-OFF state.
- Attempt 1 (3-2-1): Failed. (Turn 9804: All ON, but shutters (10, 6), (12, 8), (16, 6) are CLOSED).
- Hypothesis: The order and toggle state matter. Maybe the reset to all-OFF wasn't the correct starting point.

# Switch Status (Turn 9805)
- Switch 3 (2, 1): 🟢 ON
- Switch 2 (10, 1): 🟢 ON
- Switch 1 (16, 1): 🟢 ON

# Shutter States (Verified)
- (2, 6): OPEN
- (10, 6): CLOSED
- (12, 8): CLOSED
- (16, 6): CLOSED

# Area Notes
- Warehouse Entrance: Southern unseen area (Map 3_55).
- Trainers: All defeated.
- Rival: Defeated at (20, 4).
- Return Ladders: (23, 3), (21, 25), and (5, 25) lead back to the main Underground (3_52).