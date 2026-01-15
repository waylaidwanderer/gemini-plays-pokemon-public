# Suicune Quest (Cianwood)
- Quest Start: Turn 48900

## Strategy: The Western Corridor (X=2)
To reach the northern plateau at (14, 10), Gem must bypass the city's one-way upward ledges. The most efficient route is to reach the western corridor (X=2), which provides a clear path north. Gaps in the city walls at (9, 33) and (5, 35) allow access to this corridor.

## Execution Plan
1. Walk to (9, 33) via (21, 33) corridor. <- CURRENT TASK
2. Walk West through (9, 33) to (8, 33).
3. Walk to (5, 35) and pass West to (2, 35).
4. Walk North along X=2 to (2, 12).
5. Walk East along Row 12 to (14, 12).
6. Walk North to (14, 10) to trigger Suicune sighting.

## Verified Tile Mechanics
- FLOOR_UP_WALL: Blocks DOWN (South) movement. (Verified: Move Down at (12, 49) into (12, 50) failed in Turn 49397).
- LEDGE_HOP_DOWN: Blocks NORTH movement. (Verified: (10, 15) is impassable from the south).
- Wall Gaps: (9, 33) and (5, 35) are traversable FLOOR tiles in the city wall lines.

## Failed Hypotheses
- Island Hop (13, 16): Dead end alcove at (11, 14).
- Southern Surf Bypass: Eastern channel ends at Row 45.
- Row 15 Wall: (12, 15) to (17, 15) are solid WALL tiles.

## Progress Summary
- Badges: 16/16.
- Current Focus: Suicune overworld sighting.