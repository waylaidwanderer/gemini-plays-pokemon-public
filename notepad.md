# Tile Mechanics
- FLOOR: Traversable.
- WALL: Impassable.
- SHUTTER: Impassable when CLOSED (WALL), traversable when OPEN (FLOOR). Verified at (2, 6), (2, 7), (10, 6), (12, 8), (16, 6).
- LADDER: Traversable (Warp).
- WARP_CARPET_DOWN: Traversable (Warp).

# Puzzle: Goldenrod Underground Switch Puzzle
- Started: Turn 9640
- Goal: Open shutters (10, 6), (12, 8), and (16, 6) to reach the warehouse.
- Current Switch Status (Turn 9860): 3: OFF, 2: OFF, 1: ON.
- Verified Shutter States (Turn 9860):
  - (2, 6/7): OPEN (FLOOR)
  - (6, 8/9): CLOSED (WALL)
  - (10, 6/7): CLOSED (WALL)
  - (12, 8/9): OPEN (FLOOR)
  - (16, 6/7): OPEN (FLOOR)
  - (17, 6/7): OPEN (FLOOR)

# Switch Logic Observations
- Baseline (All OFF): (2,6) OPEN, (6,8) CLOSED, (10,6) CLOSED, (12,8) OPEN, (16,6) OPEN.
- Test 1 (1:ON only): No visible changes from baseline. (12,8) and (16,6) remain OPEN.
- Previous Obs: 3-2-1 from all-OFF (Turn 9834) made (12,8) and (16,6) CLOSED.

# Strategy
1. Current state (1:ON only) has (16,6) and (12,8) OPEN. Explore south through (16,6) for warehouse entrance.
2. If blocked, continue systematic testing: Reset 1 to OFF, turn 2 ON only.
3. Observe shutter effects and document.

# Area Notes
- Warehouse Entrance: Southern unseen area (Map 3_55).
- Trainers: All defeated.
- Rival: Defeated at (20, 4).
- Return Ladders: (23, 3), (21, 25), and (5, 25) lead back to the main Underground (3_52).