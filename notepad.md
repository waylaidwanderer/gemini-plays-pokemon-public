# Tile Mechanics
- FLOOR: Traversable.
- WALL: Impassable.
- SHUTTER: Impassable when CLOSED (WALL), traversable when OPEN (FLOOR). Verified at (2, 6), (2, 7), (10, 6), (12, 8), (16, 6).
- LADDER: Traversable (Warp).
- WARP_CARPET_DOWN: Traversable (Warp).

# Puzzle: Goldenrod Underground Switch Puzzle
- Started: Turn 9640
- Goal: Open shutters (10, 6), (12, 8), and (16, 6) to reach the warehouse.
- Current Switch Status (Turn 9864): 3: OFF, 2: OFF, 1: OFF (Just turned OFF).
- Verified Baseline Shutter States (All OFF):
  - (2, 6/7): OPEN (FLOOR)
  - (6, 8/9): CLOSED (WALL)
  - (10, 6/7): CLOSED (WALL)
  - (12, 8/9): OPEN (FLOOR)
  - (16, 6/7): OPEN (FLOOR)
  - (17, 6/7): OPEN (FLOOR)

# Switch Logic Observations
- Switch 1 ON: Opens (12, 9), (16, 7), (17, 7).
- Switch 1 OFF: Closes (16, 7), (17, 7). (16, 6) and (17, 6) remain OPEN.
- Baseline (All OFF): (2, 6/7) OPEN, (6, 8/9) CLOSED, (10, 6/7) CLOSED, (12, 8) OPEN, (12, 9) CLOSED?, (16, 6) OPEN, (17, 6) OPEN.
- Reset complete (Turn 9864).

# Strategy
1. Reset complete. All switches OFF.
2. Test 2: Turn Switch 2 ON only. Observe effects.
3. Test 3: Reset Switch 2 to OFF. Turn Switch 3 ON only. Record effects.
4. Use results to determine the combination for (10,6), (12,8), (16,6) = OPEN.

# Area Notes
- Warehouse Entrance: Southern unseen area (Map 3_55).
- Trainers: All defeated.
- Rival: Defeated at (20, 4).
- Return Ladders: (23, 3), (21, 25), and (5, 25) lead back to the main Underground (3_52).