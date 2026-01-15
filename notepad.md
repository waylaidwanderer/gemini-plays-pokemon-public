# Suicune Quest (Cianwood)
- Quest Start: Turn 48900

## Tile Mechanics: ManiasHouse (22_4)
- FLOOR: Standard ground.
- WALL: Impassable barrier.
- WARP_CARPET_DOWN: Leads to Cianwood City (17, 41).
- TOWN_MAP, BOOKSHELF, TV, RADIO: Background objects in Row 1. Interactable from Row 2 or Row 1.
- WINDOW: Background object at (5, 0).

## Tile Mechanics: Cianwood City (22_3)
- FLOOR: Standard ground.
- WALL: Impassable barrier.
- FLOOR_UP_WALL: One-way ledge. Blocks DOWN (South) movement. Verified at Row 34, 46, 48, 50.
- LEDGE_HOP_DOWN: One-way ledge. Blocks NORTH movement. Allows DOWN jump.
- BUOY: Impassable water barrier.
- WATER: Requires SURF.

## Execution Plan (Terrestrial Maze)
1. Explore Row 0 of Mania's House. <- CURRENT TASK
2. Return to Cianwood City.
3. Navigate to the western corridor (X=2) via Row 51 bypass.
4. Reach the northern plateau at (14, 10).
5. Trigger Suicune sighting.

## Failed Hypotheses
- Island Hop (13, 16) via (11, 15): Dead end alcove at (11, 14).
- Southern Surf Bypass: Eastern channel ends at Row 45.
- Inner Channel (X=12): Blocked at Row 15 by buoy wall.

## Progress Summary
- All 16 Badges obtained.
- Current Focus: Suicune tracking.