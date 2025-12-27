# Suicune Quest Log (Crystal Version)
- Prerequisites: Clear Bell (Obtained).
- Quest Start: Turn 24182 (Timestamp: Saturday, Dec 27, 2025, 9:35 AM PST).
- Loop Start: Turn 26164 (Stuck on sightings).

## Current Strategy
- Plan:
  1. Navigate to the north shore of Cianwood City (around (10, 14)).
  2. Verify if Eusine or Suicune are present.
  3. If Eusine is present, battle and defeat him.
  4. If both are absent, re-check the Burned Tower basement (Trigger flag check).
  5. If sightings still won't trigger, talk to the Sages in the Tin Tower Gatehouse again.

## Suicune Quest Diagnostic Log
- 1. Burned Tower: Flee event completed.
- 2. Cianwood City (North): Flee event observed (Suicune fled).
- 3. Eusine Battle (Cianwood): Marker at (11, 20) says defeated, but sightings #4 and #5 FAILED. Need to re-verify.
- 4. Route 42 sighting: FAILED (Reached clearing at (26, 15) on Turn 26434, no trigger).
- 5. Route 36 sighting: FAILED (Reached junction at (35, 9) on Turn 26450, no trigger).
- 6. Ecruteak PC (Eusine): MISSING (Checked Turn 26404).
- 7. Dance Theater (Eusine): MISSING (Checked Turn 26415).
- 8. Wise Trio Battle: PENDING (Room 4_2 empty at Turn 26233).
- 9. Tin Tower Battle: LOCKED.

## Tile Mechanics
- FLOOR: Traversable. Verified by walking.
- WALL: Impassable. Verified by bumping.
- WATER: Traversable ONLY with SURF. Verified by using Surf at (13, 9).
- CUT_TREE: Remove with CUT. Verified at (24, 13).
- LADDER/STAIRS: Warp. Verified in Tin Tower Gatehouse.
- FLOOR_UP_WALL: Ledge (North to South). Verified on Route 42.
- LEDGE_HOP_DOWN: One-way (North to South). Cannot walk up.
- HEADBUTT_TREE: Impassable. Verified by bumping.
- TALL_GRASS: Walkable. Verified on Route 42.
- WARP_CARPET: Warp. Verified at Route 42 Gatehouse.

## Lessons Learned
- Suicune events are strictly linear.
- Eusine's location depends on quest progress.
- Sages granting passage to Tin Tower indicates the "Clear Bell" event is active.
- Verification is key: Marker at (11, 20) in Cianwood confirms Eusine's defeat, but sightings failure suggests a missing flag.