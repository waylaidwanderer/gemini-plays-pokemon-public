# Tile Mechanics
- FLOOR: Traversable.
- WALL: Impassable.
- SHUTTER: Impassable when CLOSED (WALL), traversable when OPEN (FLOOR). Verified at (2, 6), (2, 7), (10, 6), (12, 8), (16, 6).
- LADDER: Traversable (Warp).
- WARP_CARPET_DOWN: Traversable (Warp).

# Puzzle: Goldenrod Underground Switch Puzzle
- Started: Turn 9640
- Goal: Open shutters (10, 6), (12, 8), and (16, 6) to reach the warehouse.
- Current Switch Status (Turn 9856): 3: OFF, 2: OFF, 1: OFF.
- Verified Baseline Shutter States (All OFF):
  - (2, 6/7): OPEN (FLOOR)
  - (6, 8): CLOSED (WALL) - Triggered by Switch 3 OFF.
  - (10, 6): CLOSED (WALL)
  - (12, 8): OPEN (FLOOR) - Triggered by Switch 1 OFF.
  - (16, 6/7): OPEN (FLOOR) - Triggered by Switch 2 OFF.
  - (17, 6/7): OPEN (FLOOR) - Triggered by Switch 2 OFF.

# Switch Logic Observations
- Switch 3 OFF -> (6, 8) closed.
- Switch 2 OFF -> (16, 6/7) and (17, 6/7) opened.
- Switch 1 OFF -> (12, 8) opened.
- 3-2-1 from all-OFF (Turn 9834): Failed (All shutters CLOSED).

# Strategy
1. Baseline established. All switches OFF.
2. Test 1: Turn Switch 1 ON only. Record effects.
3. Test 2: Reset Switch 1 to OFF. Turn Switch 2 ON only. Record effects.
4. Test 3: Reset Switch 2 to OFF. Turn Switch 3 ON only. Record effects.

# Area Notes
- Warehouse Entrance: Southern unseen area (Map 3_55).
- Trainers: All defeated.
- Rival: Defeated at (20, 4).
- Return Ladders: (23, 3), (21, 25), and (5, 25) lead back to the main Underground (3_52).