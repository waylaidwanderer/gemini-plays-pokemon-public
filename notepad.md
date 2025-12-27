# Suicune Quest Log (Crystal Version)
- Prerequisites: Clear Bell (Obtained), All overworld sightings must be triggered in order.
- Quest Start: Turn 24182.
- Session Start: Turn 26246.

## Current Strategy
- Plan:
  1. Navigate to (26, 15) on Route 42 island.
  2. If Suicune appears, follow it to Route 36 junction (35, 9).
  3. If Suicune is missing, check Route 36 junction just in case.
  4. If both are missing, re-verify all Wise Trio dialogues.
- Attempt 2 (Route 42): Turn 26311.

## Suicune Quest Diagnostic Log
- Burned Tower: Flee event completed.
- Cianwood City (North): Flee event completed. Eusine defeated.
- Ecruteak PC: Eusine missing (Turn 26293). Agent suggests he appears AFTER Route 42/36.
- Status: Approaching Route 42 island clearing.

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