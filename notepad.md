# Strategy: Trigger Suicune Sightings
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
- Step 1: Reach (12, 28) and Surf north to (12, 16). <- CURRENT TASK
- Step 2: Land at (12, 16).
- Step 3: Navigate land route to Suicune:
  - (12, 16) -> (11, 16) -> (11, 14) (via gap (11, 15)).
  - (11, 14) -> (13, 14) -> (13, 12) (via gap (13, 13)).
  - (13, 12) -> (14, 12) -> (14, 10).
- Step 4: Trigger Suicune sighting.

# Area Notes
- Ledge (10, 15) blocks north at X=10.
- Gap at (11, 15) is FLOOR and allows northward passage.
- Water at Row 16-24 blocks land passage from city center. Surf required.
- Landing point: (12, 16) is FLOOR.
- Highway: X=12 is a clear vertical corridor (land/water mix) from Row 44 to Row 16.
- Highway: X=9 is land from Row 29 to Row 21.

# Tile Mechanics
- FLOOR: Traversable.
- WALL: Impassable.
- FLOOR_UP_WALL: Cliff face (Impassable).
- LEDGE_HOP_DOWN: One-way jump (North to South).
- WATER: Requires Surf.
- ROCK: Obstacle (Smashable).

# Failed Hypotheses
- Attempting to go around via Row 51 (Multiple failures due to unseen cliffs at Y=46-50).
- Attempting to walk north via X=11/12 (Blocked by water at Row 24).
- Attempting to enter plateau from East (Blocked by Buoy wall at Row 15 and Wall at X=18).
- Positional Hallucination (Turn 49021): Believed I was at (21, 36) while actually at (19, 46). Corrected by verifying Game State.