# Tile Mechanics (Global)
- FLOOR: Standard ground. Traversable.
- WATER: Surf required. Traversable.
- BUOY: Impassable water obstacle.
- WALL: Impassable ground/object.
- DOOR: Warp point. Traversable.
- FLOOR_UP_WALL: Ledge face. Blocks North movement.
- LEDGE_HOP_DOWN: One-way jump (North to South).
- BREAKABLE ROCK: Requires Rock Smash. Impassable.
- NPC: Impassable. Interact from adjacent tile.

# Strategy: Capture Suicune
- Goal: Reach (14, 10) to trigger sighting.
- Approach: The West Beach Corridor (Verified Logic)
- Plan:
  1. Navigate to Row 51 via the ledge gap at (11, 50).
  2. Walk West to the beach corridor at X=2.
  3. Walk North along X=2 to Row 10 (Clear path verified).
  4. Walk East to (14, 10) to trigger sighting.
- Status: At (12, 30), starting the southern loop.
- Failed Hypotheses:
  - Buoy Maze: Too complex and potentially blocked.
  - Northern Flank: Blocked by buoys and ledges.
  - Direct West: Blocked by walls at X=5 and X=9.

# Tile Mechanics (Verified)
- FLOOR_UP_WALL (12, 50): Blocks South movement (North-facing ledge).
- FLOOR_UP_WALL (6, 34): Blocks South movement.
- LEDGE_HOP_DOWN (10, 15): One-way jump South.
- X=2 Corridor: Verified FLOOR from Y=49 to Y=11.

# Area Notes: Cianwood City
- Photo Studio: (9, 31) | Poke Seer: (5, 17)
- Pharmacy: (15, 47) | Gym: (8, 43)
- Breakable Rocks: (5, 29), (8, 16), (9, 17), (10, 27), (4, 19), (4, 25)