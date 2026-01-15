# Suicune Quest (Cianwood)
- Quest Start: Turn 48900

## Strategy: The Southern Bypass (Row 51)
To reach the northern plateau at (14, 10), Gem must bypass the city's one-way upward ledges. The confirmed path is to reach the southern corridor at Row 51, walk west to the western corridor (X=2), and then head north.

## Execution Plan
1. Use Super Repel (Done Turn 49487).
2. Reach Row 51 via (18, 46) and (10, 50) gaps. <- CURRENT TASK
   - Current Path: (20, 40) -> (20, 45) -> (18, 45) -> (18, 49) -> (12, 49) -> (10, 49) -> (10, 51).
3. Walk west to (2, 51), then north along X=2 to (2, 12).
4. Walk east along Row 12 to (14, 12).
5. Walk north to (14, 10) to trigger Suicune sighting.

## Verified Tile Mechanics
- FLOOR_UP_WALL: Blocks DOWN (South) movement. (Verified: Move Down at (12, 49) into (12, 50) failed in Turn 49397).
- LEDGE_HOP_DOWN: Blocks NORTH movement. (Verified: (10, 15) is impassable from the south).
- Row 15: (12, 15) to (17, 15) are WALL tiles.
- Row 14: (11, 14) is a dead-end pocket surrounded by WALLs.

## Hypothesized Gaps (To be tested)
- Row 46 Gap: (18, 46) and (19, 46) (FLOOR tiles).
- Row 48 Gap: (12, 48) (FLOOR tile).
- Row 50 Gap: (10, 50) and (11, 50) (FLOOR tiles).

## Failed Hypotheses
- Island Hop (13, 16): Dead end alcove at (11, 14).
- Southern Surf Bypass: Eastern channel ends at Row 45.
- Terrestrial Center (Row 34): Blocked by upward ledges.

## Progress Summary
- Badges: 16/16.
- Current Focus: Suicune overworld sighting.