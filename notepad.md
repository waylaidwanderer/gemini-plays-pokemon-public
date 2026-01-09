# Johto Journey - Final Phase (Started Turn 35938)

## Primary Goal: Indigo Plateau (Start Turn 36211)
- Objective: Challenge the Pokémon League.
- Strategy: Navigate Tohjo Falls and Route 27 to reach Victory Road.

## Strategy: Navigate Tohjo Falls
- Start Turn: 35972
- Objective: Traverse Tohjo Falls to reach the eastern exit leading to the rest of Route 27.
- Requirements: SURF and WATERFALL (Rising Badge allows use).
- Steps:
  1. Obtain HM07 Waterfall from Ice Path 1F. [Completed Turn 36179]
  2. Teach Waterfall to LAPIS (slot 6). [Completed Turn 36232]
  3. Use Waterfall to climb the falls in Tohjo Falls.
  4. Locate the eastern exit of Tohjo Falls.

## Strategy: Exit Ice Path
- Plan:
  1. Navigate B1F to ladder at (17, 3) leading to B2F. [Completed Turn 36250]
  2. Navigate B2F to ladder at (9, 11) leading to B3F. [Completed Turn 36267]
  3. Navigate B3F to collect item at (5, 7), then to ladder at (15, 5) leading back to B2F South. [Current]
  4. Reach ladder at (5, 25) on B1F leading to 1F South.
  5. Exit Ice Path at (36, 27).
  6. Fly to New Bark Town and head east to Tohjo Falls.

## Tile Mechanics (Global)
- FLOOR: Traversable.
- WALL: Impassable.
- WATER: Traversable (requires SURF).
- WATERFALL: Impassable (requires WATERFALL).
- LEDGE (FLOOR_UP_WALL): Impassable from North (+y).
- COUNTER: Impassable; interactable from front.
- LADDER: Warp to another floor/map.
- WARP_CARPET_DOWN: Exit/warp to another map.
- PC: Impassable; interactable from front (up).
- ICE: Causes sliding in the direction of movement until an obstacle or non-ice tile is reached.

## Lessons Learned
- Rising Badge: Allows use of HM07 Waterfall outside battle.
- Tohjo Falls Ledges: Row 16 ledges are impassable from North.
- Navigation: If a movement fails twice, the tile is impassable from that direction.
- Item Discovery: Moon Stone found in Tohjo Falls at (2, 6).
- Wild Encounters: Trigger battles and block movement on the turn they occur.
- Ice Ledges: Jumping down ledges from ICE tiles might be blocked or require specific landing logic.
- Tool Refinement: ice_pathfinder_v2 updated to return coordinates and handle ledge jumping correctly. (Turn 36237)
- Menu Navigation: Use menu_navigator agent for complex multi-step menus to avoid loops.
- Hallucination Warning (Turn 36248): Position mismatch due to automatic ladder warp. Always verify map ID and coordinates after warps.