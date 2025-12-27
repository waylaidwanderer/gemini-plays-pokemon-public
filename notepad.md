# Suicune Quest Log (Crystal Version)
- Prerequisites: Clear Bell (Obtained), All overworld sightings must be triggered in order.

## Sighting Progress
1. Burned Tower: Verified.
2. Cianwood City (North): Verified.
3. Route 42 (Central Island): [MISSING] Mandatory before Route 36.
4. Route 36 (Sudowoodo Junction): [MISSING] Mandatory after Route 42.
5. Tin Tower 1F: Static encounter (Enabled after sighting #4).

## Tile Mechanics
- FLOOR: Traversable.
- WALL: Impassable.
- WATER: Traversable with SURF.
- CUT_TREE: Impassable; remove with CUT.
- LADDER: Vertical transition (Warp).
- FLOOR_UP_WALL (Hypothesis): Impassable from the NORTH. Needs verification from other directions.
- HEADBUTT_TREE: Impassable. Can be interacted with using Headbutt.
- TALL_GRASS: Walkable. Triggers wild encounters.
- CAVE: Entrance/Exit warp.

## Strategy
- Current: Fly to Mahogany Town and approach Route 42 island from the East.
- Goal: Trigger Suicune sighting #3 (Route 42) and #4 (Route 36).
- Verification: Tracker (Turn 26064) confirms overworld sightings are required despite having the Clear Bell.

## Time Tracking
- Suicune Quest Start: Turn 24182.
- Tin Tower Investigation: Turn 26041 - 26067.
- Route 42 East Approach Start: Turn 26074.

## Lessons Learned
- Suicune overworld events are strictly linear.
- NPC dialogue hints (e.g., "tower shook") indicate quest progression but do not always skip steps.
- Check all adjacent tiles when blocked by an NPC.
- Do not mix directional and action buttons in a single press_buttons call.
## Verification Plans
- FLOOR_UP_WALL: Test collision from SOUTH, EAST, and WEST (current hypothesis: only impassable from NORTH).