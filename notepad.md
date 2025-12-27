# Suicune Quest Log (Crystal Version)
- Prerequisites: Clear Bell (Obtained).
- Quest Start: Turn 24182.
- Loop Start: Turn 26164 (Stuck on sightings).

## Current Strategy
- Plan:
  1. Fly to Ecruteak City.
  2. Go to Ecruteak Pokémon Center and talk to Eusine (Mandatory trigger for overworld sightings).
  3. Return to Route 42 island and walk onto (26, 15) to trigger the sighting.
  4. If that fails, go to the Route 36 junction and walk onto (35, 9).
  5. If both fail, re-consult with Sages in Tin Tower Gatehouse.

## Suicune Quest Diagnostic Log
- 1. Burned Tower: Flee event completed.
- 2. Cianwood City (North): Flee event completed.
- 3. Eusine Battle (Cianwood): COMPLETED (Marker at (11, 20)).
- 4. Route 42 sighting: Attempting (Turn 26374).
- 5. Route 36 sighting: PENDING.
- 6. Ecruteak PC (Eusine): PENDING (Missing at Turn 26333).
- 7. Wise Trio Battle: PENDING (Room 4_2 empty at Turn 26233).
- 8. Tin Tower Battle: LOCKED.

## Global Tile Mechanics (Verified)
- FLOOR: Traversable.
- WALL: Impassable.
- WATER: Traversable ONLY with SURF.
- CUT_TREE: Remove with CUT.
- LADDER/STAIRS: Warp.
- FLOOR_UP_WALL: Ledge (North to South).
- HEADBUTT_TREE: Impassable.
- TALL_GRASS: Walkable.
- WARP_CARPET: Warp.

## Lessons Learned
- Suicune events are strictly linear.
- Eusine moves to Ecruteak PC likely AFTER overworld sightings (Hypothesis).
- Sages granting passage to Tin Tower doesn't mean sightings are complete.
- Tile 'type' in XML is the source of truth for collision.
- Verification is key: Marker at (11, 20) confirms Eusine's defeat despite agent confusion.