# Strategy: Capture Suicune (Started Turn 48227)
- Goal: Reach (14, 10) in Cianwood City to trigger sighting.
- Approach: The Row 51 Land Bridge
- Plan:
  1. Close Surf menu at (27, 44). [IN PROGRESS]
  2. Walk to (18, 51) via gap at (19, 46).
  3. Walk West along Row 51 to West Beach (X=2).
  4. Walk North along West Beach (X=2) to Row 12.
  5. Walk East along Row 12 to (14, 12), then North to (14, 10).
- Reasoning: Pathfinding script confirmed no direct land path from the east side center to the north plateau due to Row 15 barriers. Row 51 is the only continuous horizontal line in the mental map that might bridge the east and west sides below the city walls. X=2 is a clear vertical highway to the northern plateau. Row 12 provides the final horizontal entry.

# Blocked Routes (Verified)
- Row 15: Solid line of WALL and LEDGE_HOP_DOWN from X=3 to X=17.
- City Walls: Vertical walls at X=5, X=9, X=11, X=17 block most horizontal movement.
- Buoy Maze: Outer channel (X > 22) is separated from inner channel by solid buoy walls with few gaps (e.g., Row 6).

# Tile Mechanics (Verified)
- FLOOR: Standard ground. Traversable.
- WALL: Impassable.
- WATER: Surf required.
- BUOY: Impassable water obstacle.
- FLOOR_UP_WALL: Impassable cliff face.
- LEDGE_HOP_DOWN: One-way jump (North to South).

# Area Notes: Cianwood City
- Photo Studio: (9, 31) | Poke Seer: (5, 17)
- Pharmacy: (15, 47) | Gym: (8, 43) | PokeCenter: (23, 43)
- Southern Corridor: Row 51 (X=4-24 confirmed).