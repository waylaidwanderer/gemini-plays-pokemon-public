# Tile Mechanics
- FLOOR: Traversable.
- WALL: Impassable.
- SHUTTER: Impassable when CLOSED (WALL), traversable when OPEN (FLOOR). Verified at (2, 6), (10, 6), (12, 8), (16, 6).
- LADDER: Traversable (Warp).
- WARP_CARPET_DOWN: Traversable (Warp).

# Puzzle: Goldenrod Underground Switch Puzzle
- Started: Turn 9640
- Current Goal: Systematic testing of switches to determine individual effects.
- Attempt 1 (3-2-1 from all-OFF): Failed. Results in all shutters CLOSED.
- Planned Test 1: Reset all to OFF. Turn ON Switch 1 only.

# Switch Status (Turn 9808)
- Switch 3 (2, 1): 🟢 ON (Resetting...)
- Switch 2 (10, 1): 🟢 ON (Resetting...)
- Switch 1 (16, 1): 🔴 OFF (Just turned OFF)

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