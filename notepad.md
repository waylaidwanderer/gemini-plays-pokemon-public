# Strategy: Trigger Suicune Sightings (Started Turn 48828, 11:50 PM)
- Goal: Complete sightings to trigger Tin Tower battle.
- Status: 16 Badges, Clear Bell.

## Suicune Chase Sequence (Crystal)
1. Burned Tower (Done)
2. Cianwood City (North Beach (14, 10)) <- CURRENT
3. Route 42
4. Kanto Route 14
5. Route 25
6. Tin Tower 1F

## Plan: Reach North Plateau (Started Turn 48972)
- Goal: Reach Suicune at (14, 10).
- Step 1: Reach (11, 21) via Town Center: (18, 42) -> (12, 42) -> (12, 29) -> (9, 29) -> (9, 21) -> (11, 21). <- CURRENT TASK
- Step 2: Walk North through Row 15 gap: (11, 21) -> (11, 15) -> (11, 14).
- Step 3: Reach (14, 10) to trigger Suicune sighting: (11, 14) -> (14, 14) -> (14, 10).

# Area Notes
- Photo Studio: (9, 31) (DOOR)
- Lugia House: (15, 37) (DOOR)
- Poke Seer: (5, 17) (DOOR)
- Obstacle: Ledge at (10, 15) blocks Northward progress. Gap at (11, 15) is FLOOR.
- Obstacle: Wall at X=9 blocks horizontal movement between Row 30 and 34. Gap at Row 29 and Row 33.
- Obstacle: Wall at X=5 blocks horizontal movement. Gap at (5, 35).
- Obstacle: Water at Row 22-25. Path at X=9 is land.
- Highway: X=12 is a clear vertical path from Row 42 to Row 29.
- Highway: X=9 is a clear vertical path from Row 29 to Row 21.
- Highway: X=11 is a clear vertical path from Row 21 to Row 14 (passes Row 15 gap).
- Connection: Route 41 (0, 32) <-> Cianwood City (29, 32).

# Tile Mechanics (Verified)
- FLOOR: Traversable.
- WATER: Requires Surf.
- BUOY: Impassable.
- LEDGE_HOP_DOWN: One-way jump (North to South).
- FLOOR_UP_WALL: Cliff face (Impassable).
- Suicune Trigger: North Beach (14, 10).
- Tool Failure: find_path_v6_fixed failing with sandbox errors. Manual navigation required.