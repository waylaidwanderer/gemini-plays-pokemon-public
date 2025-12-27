# Suicune Quest Log (Crystal Version)
- Prerequisites: Clear Bell (Obtained), All overworld sightings must be triggered in order.
- Quest Start: Turn 24182.

## Suicune Quest Diagnostic Log
1. Burned Tower: Flee event completed.
2. Cianwood City (North): Flee event completed. Eusine defeated.
3. Flag: Eusine dialogue in Ecruteak PC. [STATUS: Eusine missing from PC at Turn 26204]
4. Flag: Wise Trio dialogue in Tin Tower Gatehouse. [STATUS: Sages mentioned 'tower shook' at Turn 26110]
5. Sighting #3: Route 42 (Central Island). [FAILED - Swept clearing at Turn 26164]
6. Sighting #4: Route 36 (Sudowoodo Junction). [FAILED - Swept spot at Turn 26177]
7. Tin Tower 1F: Static encounter. [LOCKED]

## Current Strategy
- Goal: Unlock Suicune sightings by completing Wise Trio interactions.
- Plan:
  1. Talk to all Sages in Tin Tower 1F (Turn 26237).
  2. If Suicune is still missing, perform a tile-by-tile sweep of Route 36 again.
  3. If still missing, re-sweep Route 42 island clearing.

## Global Tile Mechanics (Verified)
- FLOOR: Traversable. Includes visual "Warp Carpets" and "Exit Mats".
- WALL: Impassable.
- WATER: Traversable ONLY with SURF.
- CUT_TREE: Impassable; remove with CUT. Regrows when map is reloaded.
- LADDER: Vertical transition (Warp).
- FLOOR_UP_WALL: Impassable from the NORTH. Functions like a ledge.
- HEADBUTT_TREE: Impassable.
- TALL_GRASS: Walkable.
- CAVE: Entrance/Exit warp.
- DOOR: Interactive warp tile.

## Lessons Learned
- Suicune events are strictly linear and mandatory.
- Eusine dialogue in Ecruteak PC is a known prerequisite in Crystal.
- Sages granting passage to Tin Tower doesn't mean sightings are done.
- Tile 'type' in XML is the source of truth for collision.

## Milestones
- Turn 26110: Triggered 'Tin Tower Shake' event.
- Turn 26204: Confirmed Ecruteak PC is empty of Eusine.
- Turn 26214: Talked to Sage member of Wise Trio.
- Turn 26227: Talked to Gramps (Wise Trio member?) in Gatehouse.
- Next: Find final member in Wise Trio Room.
- Turn 26233: Wise Trio Room (4_2) confirmed EMPTY. No NPCs present.
- Turn 26233: Returning to Tin Tower 1F to check for Suicune encounter.