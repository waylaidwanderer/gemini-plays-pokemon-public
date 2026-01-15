# Tile Mechanics (Verified)
- FLOOR: Standard ground. Traversable.
- WALL: Impassable.
- WATER: Surf required. Traversable.
- BUOY: Impassable water obstacle.
- DOOR: Warp point.
- FLOOR_UP_WALL: Impassable cliff face (e.g., Row 15, Row 30, Row 34).
- LEDGE_HOP_DOWN: One-way jump (North to South).
- BREAKABLE ROCK: Requires Rock Smash. Impassable.
- NPC: Impassable. Interact from adjacent tile.

# Strategy: Capture Suicune (Started Turn 48227)
- Goal: Reach (14, 10) to trigger sighting.
- Approach: The Sequential Gap Path (Verified)
- Plan:
  1. Clear SURF message at (15, 27). [IN PROGRESS]
  2. Navigate to (15, 24), then Right to (17, 24).
  3. Navigate to (17, 26), then Right to (19, 26).
  4. Navigate to (23, 26), then Up to (23, 15) [Gap 6].
  5. Navigate to (23, 14), then Left to (18, 14).
  6. Navigate to (18, 11), then Left to (16, 11) [Land].
  7. Walk to (14, 10).
- Status: At (15, 27) on water, clearing message.
- Reasoning: Row 15 is a continuous wall of cliffs and buoys except for a single gap at (23, 15). Accessing this gap requires navigating a series of vertical buoy walls at X=16 and X=18.

# Area Notes: Cianwood City
- Photo Studio: (9, 31) | Poke Seer: (5, 17)
- Pharmacy: (15, 47) | Gym: (8, 43)
- Breakable Rocks: (5, 29), (10, 27), (8, 16), (9, 17), (4, 19), (4, 25)
- Southern Ledge Gap: at (10, 50) provides access to southern beach.