# Tile Mechanics
- FLOOR: Traversable.
- WALL: Impassable.
- SHUTTER: Impassable when CLOSED (WALL), traversable when OPEN (FLOOR). Verified at (2, 6), (2, 7), (10, 6), (12, 8), (16, 6).
- LADDER: Traversable (Warp).
- WARP_CARPET_DOWN: Traversable (Warp).

# Puzzle: Goldenrod Underground Switch Puzzle
- Started: Turn 9640
- Goal: Open shutters (10, 6), (12, 8), and (16, 6) to reach the warehouse.
- Current Switch Status: 3: ON, 2: ON, 1: ON.
- Verified Shutter States (Turn 9841):
  - (2, 6): OPEN (FLOOR)
  - (2, 7): OPEN (FLOOR)
  - (10, 6): CLOSED (WALL)
  - (12, 8): CLOSED (WALL)
  - (16, 6): CLOSED (WALL)

# Switch Logic Observations
- 3-2-1 from all-OFF (Turn 9834): Results in all shutters CLOSED except (2, 6/7).
- Resetting switches to OFF to perform systematic one-by-one tests.

# Strategy
1. Turn Switch 3 OFF (Current task).
2. Turn Switch 2 OFF.
3. Turn Switch 1 OFF.
4. Test 1: Turn Switch 1 ON only. Record effects.
5. Test 2: Turn Switch 2 ON only. Record effects.
6. Test 3: Turn Switch 3 ON only. Record effects.

# Area Notes
- Warehouse Entrance: Southern unseen area (Map 3_55).
- Trainers: All defeated.
- Rival: Defeated at (20, 4).
- Return Ladders: (23, 3), (21, 25), and (5, 25) lead back to the main Underground (3_52).