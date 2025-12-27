# Suicune Quest Log (Crystal Version)
- Prerequisites: Clear Bell (Obtained).
- Quest Start: Turn 24182 (Timestamp: Saturday, Dec 27, 2025, 9:35 AM PST).
- Loop Start: Turn 26164 (Stuck on sightings).
- Current Turn: 26414.

## Current Strategy
- Plan:
  1. Check Ecruteak Dance Theater for Eusine.
  2. If not found, head to Route 42 island (26, 15) to trigger the sighting.
  3. If that fails, go to Route 36 junction (35, 9).
  4. If both sightings fail, talk to the Sages in the Tin Tower Gatehouse again.
  5. If Eusine appears in the PC at any point, talk to him immediately.

## Suicune Quest Diagnostic Log
- 1. Burned Tower: Flee event completed.
- 2. Cianwood City (North): Flee event completed.
- 3. Eusine Battle (Cianwood): COMPLETED (Marker at (11, 20)).
- 4. Route 42 sighting: Attempting (Turn 26374).
- 5. Route 36 sighting: PENDING.
- 6. Ecruteak PC (Eusine): PENDING (Missing at Turn 26333).
- 7. Wise Trio Battle: PENDING (Room 4_2 empty at Turn 26233).
- 8. Tin Tower Battle: LOCKED.

## Tile Mechanics
- FLOOR: Traversable. Verified by walking.
- WALL: Impassable. Verified by bumping.
- WATER: Traversable ONLY with SURF. Verified by using Surf at (13, 9).
- CUT_TREE: Remove with CUT. Verified at (24, 13).
- LADDER/STAIRS: Warp. Verified in Tin Tower Gatehouse.
- FLOOR_UP_WALL: Ledge (North to South). Verified on Route 42.
- HEADBUTT_TREE: Impassable. Verified by bumping.
- TALL_GRASS: Walkable. Verified on Route 42.
- WARP_CARPET: Warp. Verified at Route 42 Gatehouse.

## Lessons Learned
- Suicune events are strictly linear.
- Eusine moves to Ecruteak PC likely AFTER overworld sightings (Hypothesis).
- Sages granting passage to Tin Tower doesn't mean sightings are complete.
- Tile 'type' in XML is the source of truth for collision.
- Verification is key: Marker at (11, 20) confirms Eusine's defeat despite agent confusion.