# Suicune Quest Log (Crystal Version)
- Prerequisites: Clear Bell (Obtained), All overworld sightings must be triggered in order.
- Quest Start: Turn 24182.

## Sighting Progress
1. Burned Tower: Verified.
2. Cianwood City (North): Verified.
3. Route 42 (Central Island): [MISSING] Mandatory before Route 36.
4. Route 36 (Sudowoodo Junction): [MISSING] Mandatory after Route 42.
5. Tin Tower 1F: Static encounter (Enabled after sighting #4).

## Global Tile Mechanics
- FLOOR: Traversable.
- WALL: Impassable.
- WATER: Traversable ONLY with SURF.
- CUT_TREE: Impassable; remove with CUT. Regrows when map is reloaded.
- LADDER: Vertical transition (Warp).
- FLOOR_UP_WALL: Impassable from the NORTH. Functions like a ledge.
- HEADBUTT_TREE: Impassable. Can be interacted with using HEADBUTT.
- TALL_GRASS: Walkable. Triggers wild encounters.
- CAVE: Entrance/Exit warp.
- WARP_CARPET_DOWN: Triggers map transition when walking OFF the map southwards.
- DOOR: Interactive warp tile.
- WARP_CARPET_LEFT: Triggers map transition when walking OFF the map westwards.

## Strategy
- Current: Check Route 36 or Tin Tower 1F for Suicune.
- Plan:
  1. Fly to Ecruteak City.
  2. Travel south to Route 36 (Sudowoodo junction) and check for Suicune.
  3. If Suicune is not there, enter Tin Tower 1F and check the ground floor.
  4. If still missing, revisit the Burned Tower and Cianwood to ensure no triggers were missed.
  5. Document result: Route 42 island sweep (Turn 26164) yielded no Suicune.

## Time Tracking
- Current Attempt Start: Turn 26101.

## Lessons Learned
- Suicune overworld events are strictly linear.
- NPC dialogue hints (e.g., "tower shook") indicate quest progression but do not always skip steps.
- Check all adjacent tiles when blocked by an NPC.
- Do not mix directional and action buttons in a single press_buttons call.
## Milestones
- Turn 26110: Triggered "Tin Tower Shake" event by entering the gatehouse with the Clear Bell.