# Suicune Quest Log (Crystal Version)
- Prerequisites: Clear Bell (Obtained), All overworld sightings must be triggered in order.
- Status: Searching for Suicune sighting #3 or #4.

## Sighting Progress
1. Burned Tower: Verified.
2. Cianwood City (North): Verified.
3. Route 42 (Central Island): [IN PROGRESS] Route 36 verified empty. Returning for a tile-by-tile search (24, 12 to 31, 17 area).
4. Route 36 (Sudowoodo Junction): [EMPTY] Verified on Turn 25992.
5. Tin Tower 1F: Final encounter (requires all 4 overworld sightings).

## Tile Mechanics
- FLOOR: Traversable.
- WALL: Impassable.
- WATER: Traversable with SURF.
- CUT_TREE: Impassable; remove with CUT.
- LADDER: Vertical transition (Warp).
- FLOOR_UP_WALL: Impassable from the NORTH (cannot move DOWN into it). Acts as a wall or ledge bottom.

## Strategy
- Current: Fly to Ecruteak City and navigate to Route 42 island.
- Method: Perform a tile-by-tile sweep of the island (24, 12 to 31, 17 area) to trigger the Suicune flee event.
- Observation: Route 36 (Sudowoodo spot) was verified empty on Turn 25992, confirming Route 42 must be completed first.

## Timestamps
- Suicune Quest Start: Turn 24182.
- Failed Route 42 Island Sweep: Turn 25893, 25974.
- Pivot to Route 36: Turn 25981.
- Suicune Tracker Advice: Route 42 sighting is mandatory before Route 36. If Route 36 is empty, return to Route 42 and perform a tile-by-tile sweep of the island (24, 13 to 30, 17 area).
- Verification: Route 36 (35, 9) check in progress.
## Sighting Attempts (Route 42 Island)
- Attempt 1: Full island walk-through (Turn 25893). Result: No flee event.
- Attempt 2: Full island walk-through (Turn 25974). Result: No flee event.
- Attempt 3: tile-by-tile search (Turn 26002). [PENDING]

## Lessons Learned
- Suicune overworld events are strictly linear. Check the current location's trigger before moving to the next.
- If a path is blocked by an NPC, check all adjacent tiles for a detour.
- Do not mix directional and action buttons in a single press_buttons call.
- Fly map navigation requires precise city selection.
- If Suicune is not found in a suspected location, re-verify the linear sequence status.
- The Route 42 island flee event is mandatory before Route 36 or Tin Tower.
- Search the island (24, 12 to 31, 17 area) on Route 42 meticulously.