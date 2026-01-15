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
- Step 1: Reach West Beach (2, 32) via south detour: (7, 44) -> (10, 44) -> (10, 50) gap -> (4, 50) -> (4, 32) -> (2, 32). <- CURRENT TASK
- Step 2: Walk North along West Beach (X=0-2) to Row 12.
- Step 3: Move East to X=14 (under the plateau).
- Step 4: Move North to (14, 10) to trigger Suicune sighting.

# Area Notes
- Photo Studio: (9, 31) (DOOR)
- Lugia House: (15, 37) (DOOR)
- Poke Seer: (5, 17) (DOOR)
- Obstacle: Ledge at (10, 15) blocks Northward progress from city center.
- Connection: Route 41 (0, 32) <-> Cianwood City (29, 32).

# Tile Mechanics (Verified)
- FLOOR: Traversable.
- WALL / BUOY: Impassable.
- DOOR: Warp point (Avoid unless entering).
- FLOOR_UP_WALL: Cliff (Impassable).
- LEDGE_HOP_DOWN: One-way jump (North to South).
- WATER: Requires Surf.
- Suicune Trigger: North Beach (14, 10). Approach via western beach (X=0-2) to bypass ledge at (10, 15).
- Tool Failure: find_path_v6_fixed failing with sandbox errors (Turn 48981). Manual navigation required for Route 41 to Cianwood transition.
- Navigation: Route 41 (0, 32) <-> Cianwood City (29, 32). Moving Left from (0, 32) triggers warp.