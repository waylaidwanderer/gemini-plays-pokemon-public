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
- Goal: Complete Suicune overworld sightings (Crystal Version).
- Current Step: Identify why sighting #3 (Route 42) or #4 (Route 36) hasn't triggered.
- Hypotheses:
  1. Missed dialogue with Eusine in Ecruteak Pokemon Center.
  2. Missed dialogue with Wise Trio in Tin Tower Gatehouse.
  3. Specific trigger tile on Route 42 island clearing was missed.
- Action Plan:
  1. Check Ecruteak Pokemon Center for Eusine.
  2. Check Wise Trio room in Tin Tower Gatehouse.
  3. Re-sweep Route 42 island (tile-by-tile).
- Result Log:
  - Route 42 Island (Turn 26164): Southern/Northern clearings empty.
  - Route 36 (Turn 26177): Sudowoodo spot empty.

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