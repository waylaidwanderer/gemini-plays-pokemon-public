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
- Step 1: Reach Row 51 via detour: (21, 36) -> (22, 36) -> (22, 38) -> (21, 38) -> (21, 45) -> (19, 45) -> (19, 49) -> (20, 49) -> (20, 51). <- CURRENT TASK
- Step 2: Walk West across Row 51 to (10, 51).
- Step 3: Walk North through gap at (10, 50) to (10, 49).
- Step 4: Walk West on Row 49 to (2, 49) (West Beach).
- Step 5: Walk North along West Beach (X=2) to (2, 10).
- Step 6: Walk East to (14, 10) to trigger Suicune sighting.

# Area Notes
- Photo Studio: (9, 31) (DOOR)
- Lugia House: (15, 37) (DOOR)
- Poke Seer: (5, 17) (DOOR)
- Obstacle: Ledge at (10, 15) blocks Northward progress from city center.
- Obstacle: Wall/Cliff line at X=3-9 blocks Westward progress from city center.
- Gap: Row 51 is a clear horizontal path (X=4-24) bypassing all cliff lines.
- Gap: Row 50 has gaps at X=10 and X=20-24.
- Gap: Row 46 has a gap at X=19.
- Highway: X=2 (West Beach) is a clear vertical path from Row 49 to Row 10.
- Connection: Route 41 (0, 32) <-> Cianwood City (29, 32).

# Tile Mechanics (Verified)
- FLOOR: Traversable.
- WATER: Requires Surf.
- BUOY: Impassable.
- LEDGE_HOP_DOWN: One-way jump (North to South).
- FLOOR_UP_WALL: Cliff face (Impassable).
- Suicune Trigger: North Beach (14, 10).
- Tool Failure: find_path_v6_fixed failing with sandbox errors. Manual navigation required.