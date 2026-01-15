# Strategy: Capture Suicune (Started Turn 48227)
- Goal: Reach (14, 10) in Cianwood City to trigger sighting.
- Approach: The Deep Sea Loop (v2)
- Plan:
  1. Walk to (19, 30) and Surf at (20, 30). [IN PROGRESS]
  2. Enter Route 41 at (0, 30).
  3. Navigate North to Route 41 (0, 6) and re-enter Cianwood at (29, 6).
  4. Pass West through the X=22 buoy gap at (22, 6).
  5. Navigate to (19, 11) and explore West (X=18-17) for a landing spot (e.g., (16, 11)).
  6. Walk to (14, 10).
- Reasoning: Land routes (West Beach, Central City, Skyline Path) are all blocked by the Row 15 ledge/wall barrier. The buoy walls at X=26 and X=22 must be bypassed via Route 41 and the Row 6 gap to reach the northern water pocket.

# Failed Hypotheses (Documented)
- West Beach Highway: Blocked by FLOOR_UP_WALL at Row 34 (X=6-8) and Row 46 (X=6-29).
- Central City Land: Blocked by ledge at (10, 15) and walls at (12-17, 15).
- Skyline Path (Row 29): Blocked by Row 15 barrier.
- Southern Artery: Blocked by Row 46/50 cliffs.

# Tile Mechanics (Verified)
- FLOOR: Standard ground. Traversable.
- WALL: Impassable.
- WATER: Surf required. Traversable.
- BUOY: Impassable water obstacle.
- FLOOR_UP_WALL: Impassable cliff face.
- LEDGE_HOP_DOWN: One-way jump (North to South).

# Area Notes: Cianwood City
- Photo Studio: (9, 31) | Poke Seer: (5, 17)
- Pharmacy: (15, 47) | Gym: (8, 43)
- Southern Ledge Gap: (10, 50) provides access to southern beach.