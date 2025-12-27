# Suicune Quest Log (Crystal Version)
- Prerequisites: Clear Bell (Obtained), All overworld sightings must be triggered in order.
- Quest Start: Turn 24182.
- Session Start: Turn 26246.

## Current Strategy
- Plan:
  1. Fly to Ecruteak City and check Pokémon Center for Eusine. [RE-VERIFYING FLAG]
  2. Perform a full-tile sweep of the Pokémon Center (1F and 2F).
  3. Talk to Eusine to set the Route 42 sighting flag.
  4. Return to Route 42 (Central Island) and approach (26, 15).
  5. Sighting #4: Route 36 (Sudowoodo Junction).
- Attempt 3 (Route 42): Turn 26322 (Failed - Suicune missing).

## Suicune Quest Diagnostic Log
- Burned Tower: Flee event completed.
- Cianwood City (North): Flee event completed. Eusine defeated.
- Route 42: Attempt 1 (Turn 26164) and Attempt 2 (Turn 26322) failed.
- Status: Re-checking Ecruteak PC for Eusine flag. [START TURN: 26326]

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