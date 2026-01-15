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
- Step 1: Reach (20, 30) and Surf. (Done)
- Step 2: Navigate North to (20, 21) and West to (14, 21) to bypass buoy wall. <- CURRENT TASK
- Step 3: Land at (13, 16) and navigate zigzag: (11, 16) -> (11, 14) -> (13, 14) -> (13, 10).
- Step 4: Reach (14, 10) to trigger Suicune sighting.

# Area Notes
- Photo Studio: (9, 31) (DOOR)
- Lugia House: (15, 37) (DOOR)
- Poke Seer: (5, 17) (DOOR)
- Obstacle: Ledge at (10, 15) blocks Northward progress. Gap at (11, 15).
- Obstacle: Wall at Row 13 (X=9-12). Gap at (13, 13).
- Obstacle: Wall at Row 15 (X=12-17). Gap at (11, 15).
- Connection: Route 41 (0, 32) <-> Cianwood City (29, 32).
- Route: Gap at (19, 21) in buoy wall allows passage to inner channel.

# Tile Mechanics (Verified)
- FLOOR: Traversable.
- WALL / BUOY: Impassable.
- DOOR: Warp point (Avoid unless entering).
- FLOOR_UP_WALL: Cliff (Impassable).
- LEDGE_HOP_DOWN: One-way jump (North to South).
- WATER: Requires Surf.
- Suicune Trigger: North Beach (14, 10).
- Tool Failure: find_path_v6_fixed failing with sandbox errors (Turn 48981). Manual navigation required.