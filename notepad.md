# Suicune Quest Log (Crystal Version)
- Prerequisites: Clear Bell (Obtained), All overworld sightings must be triggered in order.
- Quest Start: Turn 24182.

## Suicune Quest Diagnostic Log
1. Burned Tower: Flee event completed.
2. Cianwood City (North): Flee event completed. Eusine defeated.
3. Flag: Eusine dialogue in Ecruteak PC. [PENDING]
4. Flag: Wise Trio dialogue in Tin Tower Gatehouse. [PENDING - Sages mentioned 'tower shook' at Turn 26110]
5. Sighting #3: Route 42 (Central Island). [FAILED - Swept (21,10) to (31,17) at Turn 26164]
6. Sighting #4: Route 36 (Sudowoodo Junction). [FAILED - Swept (34,8) to (37,10) at Turn 26177]
7. Tin Tower 1F: Static encounter. [LOCKED]

## Global Tile Mechanics (Verified)
- FLOOR: Traversable. Includes visual "Warp Carpets" and "Exit Mats".
- WALL: Impassable.
- WATER: Traversable ONLY with SURF.
- CUT_TREE: Impassable; remove with CUT. Regrows when map is reloaded.
- LADDER: Vertical transition (Warp).
- FLOOR_UP_WALL: Impassable from the NORTH. Functions like a ledge.
- HEADBUTT_TREE: Impassable. Can be interacted with using HEADBUTT.
- TALL_GRASS: Walkable. Triggers wild encounters.
- CAVE: Entrance/Exit warp.
- DOOR: Interactive warp tile.

## Time Tracking
- Current Attempt Start: Turn 26101.

## Lessons Learned
- Suicune overworld events are strictly linear.
- NPC dialogue hints (e.g., "tower shook") indicate quest progression but do not always skip steps.
- Check all adjacent tiles when blocked by an NPC.
- Do not mix directional and action buttons in a single press_buttons call.
- Tile 'type' in XML is the source of truth for collision (e.g., visual carpets are type FLOOR).
- If overworld sightings fail to trigger, check intermediate NPC flags (Eusine/Sages).

## Milestones
- Turn 26110: Triggered "Tin Tower Shake" event by entering the gatehouse with the Clear Bell.
- Route 36 Sudowoodo Spot (Turn 26177): Suicune NOT found.