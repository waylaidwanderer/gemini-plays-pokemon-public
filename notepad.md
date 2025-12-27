# Suicune Quest Log (Crystal Version)
- Prerequisites: Clear Bell (Obtained), All overworld sightings must be triggered in order.
- Quest Start: Turn 24182.

## Current Strategy
- Plan:
  1. Fly to Ecruteak City and check Pokémon Center for Eusine. [NEW TRIGGER]
  2. If Eusine is present, talk to him to flag the Route 42 sighting.
  3. Return to Route 42 (Central Island) and approach the sighting spot.
  4. If Suicune appears, follow it to Route 36.
  5. Sighting #4: Route 36 (Sudowoodo Junction).

## Suicune Quest Diagnostic Log
- Burned Tower: Flee event completed.
- Cianwood City (North): Flee event completed. Eusine defeated.
- Current Status: Checking Ecruteak Pokémon Center for Eusine to trigger Route 42 sighting.

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