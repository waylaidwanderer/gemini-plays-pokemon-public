# Tile Mechanics
- FLOOR: Traversable.
- WALL: Impassable.
- SHUTTER: Impassable when CLOSED (WALL), traversable when OPEN (FLOOR). Verified at (2, 6), (2, 7), (10, 6), (12, 8), (16, 6).
- LADDER: Traversable (Warp).
- WARP_CARPET_DOWN: Traversable (Warp).

# Puzzle: Goldenrod Underground Switch Puzzle
- Started: Turn 9640
- Goal: Open shutters (10, 6), (12, 8), and (16, 6) to reach the warehouse.
- Current Switch Status (Turn 9868): 3: OFF, 2: OFF, 1: OFF.

## Verified Baseline Shutter States (All OFF)
- (2, 6/7): OPEN (FLOOR)
- (6, 8/9): CLOSED (WALL)
- (10, 6/7): CLOSED (WALL)
- (12, 8/9): CLOSED (WALL)
- (16, 6/7): CLOSED (WALL)

## Lessons Learned
- Memory of "3-2-1" solution is unreliable; must rely on observation.
- Initial state matters significantly for toggle logic.
- Systematic isolation tests (one switch at a time) are necessary.

## Switch Logic Observations (Isolated)
- Switch 1 ON (Hypothesis): Opens (12, 8) and (16, 7).
- Switch 2 ON (Hypothesis): Closes (16, 6) and (17, 6). (Based on it being OPEN when 2 was OFF).
- Switch 3 ON (Hypothesis): Opens (6, 8) and Closes (12, 8).

## Strategy
1. Test 2: Turn Switch 2 ON only. Observe and document shutter effects (Current task).
2. Test 3: Reset Switch 2 to OFF. Turn Switch 3 ON only. Observe and document.
3. Combine results to find the state where (10,6), (12,8), (16,6) = OPEN.

# Area Notes
- Warehouse Entrance: Southern unseen area (Map 3_55).
- Trainers: All defeated.
- Rival: Defeated at (20, 4).
- Return Ladders: (23, 3), (21, 25), and (5, 25) lead back to the main Underground (3_52).