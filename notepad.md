# Suicune Quest Log (Crystal Version)
- Prerequisites: Clear Bell (Obtained), All overworld sightings must be triggered in order.
- Quest Start: Turn 24182.

## Current Strategy
- Goal: Complete Suicune overworld sightings sequence.
- Plan:
  1. Use Surf at (13, 9) to enter Route 42 water. [START TURN: 26262]
  2. Navigate to (24, 12) on the central island.
  3. Use Cut on the tree at (24, 13).
  4. Approach Suicune at the sighting spot.
  5. If Suicune appears, follow it to Route 36.
  6. If Suicune does not appear, re-verify Ecruteak PC for Eusine.

## Suicune Quest Diagnostic Log
1. Burned Tower: Flee event completed.
2. Cianwood City (North): Flee event completed. Eusine defeated.
3. Flag: Eusine dialogue in Ecruteak PC. [STATUS: Eusine missing from PC at Turn 26204]
4. Flag: Wise Trio dialogue in Tin Tower Gatehouse. [STATUS: Sages mentioned 'tower shook' at Turn 26110]
5. Sighting #3: Route 42 (Central Island). [STATUS: Attempting precision approach]
6. Sighting #4: Route 36 (Sudowoodo Junction). [LOCKED]
7. Tin Tower 1F: Static encounter. [LOCKED]

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
- WARP_CARPET_LEFT: Warp tile at map edge.

## Tile Traversal and Movement Rules
- Standard Movement: Up, Down, Left, Right moves one tile.
- Ledges: Can jump over FLOOR_UP_WALL from South to North? NO, ledges are usually North to South. (Verification needed).
- One-Way Paths: Verified ledges are one-way.
- Surf: Required to enter WATER tiles. Interaction from adjacent tile.
- Cut: Required to remove CUT_TREE. Interaction from adjacent tile.

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
- Turn 26233: Wise Trio Room (4_2) confirmed EMPTY. No NPCs present.
- Turn 26245: Completed dialogue with all Sages in Tin Tower 1F. Clear Bell reactive.