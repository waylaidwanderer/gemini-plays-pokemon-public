# Suicune Quest Log (Crystal Version)
- Prerequisites: Clear Bell (Obtained), All overworld sightings must be triggered in order.
- Status: Searching for Suicune sighting #3 or #4.

## Sighting Progress
1. Burned Tower: Verified.
2. Cianwood City (North): Verified.
3. Route 42 (Central Island): Relocated to Tin Tower 1F (Clear Bell + Tower Shook event).
4. Route 36 (Sudowoodo Junction): Relocated to Tin Tower 1F (Clear Bell + Tower Shook event).
5. Tin Tower 1F: Static encounter (Current Goal).

## Tile Mechanics
- FLOOR: Traversable.
- WALL: Impassable. (Includes ledges and patterned blocks).
- WATER: Traversable with SURF.
- CUT_TREE: Impassable; remove with CUT.
- LADDER: Vertical transition (Warp).
- FLOOR_UP_WALL: Impassable from the NORTH (cannot move DOWN into it). Acts as a wall or ledge bottom.
- HEADBUTT_TREE: Impassable. Can be interacted with using Headbutt.
- TALL_GRASS: Walkable. Triggers wild encounters.
- CAVE: Entrance/Exit warp.

## Strategy
- Current: Navigate to Route 42 island via Surf.
- Method: Perform a tile-by-tile sweep of the island (24, 12 to 31, 17 area) to trigger the Suicune flee event.
- Tool: Use sweep_area_v2 for exhaustive coverage.

## Timestamps
- Suicune Quest Start: Turn 24182.
- Route 42 Island Search Start: Turn 26011.

## Lessons Learned
- Suicune overworld events are strictly linear. Check the current location's trigger before moving to the next.
- If a path is blocked by an NPC, check all adjacent tiles for a detour.
- Do not mix directional and action buttons in a single press_buttons call.
- Fly map navigation requires precise city selection.
- The Route 42 island flee event is mandatory before Route 36 or Tin Tower.