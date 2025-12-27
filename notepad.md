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
- Current: Return to Route 42 to trigger Suicune sighting #3.
- How:
  1. Fly to Ecruteak City.
  2. Travel east to Route 42.
  3. Surf to the central island.
  4. Perform an exhaustive, tile-by-tile sweep of the island's clearing (especially near the Apricorn trees) to trigger Suicune.
  5. If Suicune flees, immediately proceed to Route 36 (Sudowoodo junction).
  6. If Suicune is still missing, talk to Eusine in Ecruteak Pokemon Center and the Sages.
- Result Log:
  - Route 42 Island (Turn 26164): Initial sweep yielded no Suicune. Retrying after confirming sequence with tracker.
  - Route 36 (Turn 26177): Suicune not found (confirmed unavailable until Route 42 is triggered).

## Time Tracking
- Current Attempt Start: Turn 26101.

## Lessons Learned
- Suicune overworld events are strictly linear.
- NPC dialogue hints (e.g., "tower shook") indicate quest progression but do not always skip steps.
- Check all adjacent tiles when blocked by an NPC.
- Do not mix directional and action buttons in a single press_buttons call.
## Milestones
- Turn 26110: Triggered "Tin Tower Shake" event by entering the gatehouse with the Clear Bell.
- Route 36 Sudowoodo Spot (Turn 26177): Suicune NOT found.