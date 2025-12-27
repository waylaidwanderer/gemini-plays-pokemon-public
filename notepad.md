# Suicune Quest Log (Crystal Version)
- Prerequisites: Clear Bell (Obtained), All overworld sightings must be triggered in order.
- Quest Start: Turn 24182.
- Session Start: Turn 26246.

## Current Strategy
- Plan:
  1. Exit Pokémon Center and go to Tin Tower Gatehouse (18, 11).
  2. Re-talk to all Sages in the Gatehouse to ensure the 'Wise Trio' event is primed.
  3. Check the Wise Trio Room (4_2) for the battle event.
  4. If the battle occurs, complete it and then re-attempt the Route 42 sighting.
  5. If no battle, proceed to Route 36 junction (35, 9) to check for Suicune there.
- Attempt 4 (Trigger Search): Turn 26333.

## Suicune Quest Diagnostic Log
- Burned Tower: Flee event completed.
- Cianwood City (North): Flee event completed. Eusine defeated.
- Route 42: Attempt 1 (Turn 26164) and Attempt 2 (Turn 26322) failed.
- Ecruteak PC: Eusine MISSING (Confirmed at Turn 26293 and 26333).
- Wise Trio: Room (4_2) was empty at Turn 26233.
- Status: Searching for the 'Wise Trio' battle or next trigger in Ecruteak.

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
- Ledges: Verified ledges are one-way (North to South).
- Surf: Required to enter WATER tiles. Interaction from adjacent tile.
- Cut: Required to remove CUT_TREE. Interaction from adjacent tile.

## Lessons Learned
- Suicune events are strictly linear and mandatory.
- Eusine dialogue in Ecruteak PC is a known prerequisite in Crystal.
- Sages granting passage to Tin Tower doesn't mean sightings are done.
- Tile 'type' in XML is the source of truth for collision.