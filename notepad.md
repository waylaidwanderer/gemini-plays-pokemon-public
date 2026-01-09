# Johto Journey - Final Phase (Started Turn 35938)

## Primary Goal: Indigo Plateau (Start Turn 36211)
- Objective: Challenge the Pokémon League.
- Strategy: Navigate Tohjo Falls and Route 27 to reach Victory Road.

## Strategy: Navigate Tohjo Falls (Start Turn 35972)
- Objective: Traverse Tohjo Falls to reach the eastern exit leading to the rest of Route 27.
- Requirements: SURF and WATERFALL (Rising Badge allows use).
- Steps:
  1. Obtain HM07 Waterfall from Ice Path 1F. [Completed]
  2. Teach Waterfall to LAPIS (slot 6). [Completed]
  3. Use Waterfall to climb the falls in Tohjo Falls.
  4. Locate the eastern exit of Tohjo Falls.

## Strategy: Exit Ice Path (Start Turn 36156)
- Plan:
  1. Navigate B2F Blackthorn Side to ladder at (3, 15) leading to B1F. [Current]
     - Path: (6, 1) -> (9, 1) -> (9, 3) -> (9, 4) (ICE) -> Slide Down to (9, 15) -> Slide Left to (3, 15).
  2. Reach ladder at (5, 25) on B1F leading to 1F South.
  3. Exit Ice Path at (36, 27) on 1F.
  4. Fly to New Bark Town and head east to Tohjo Falls.

## Items Collected
- Ice Path 1F: HM07 Waterfall (31, 7)
- Ice Path B1F: Iron (5, 35)
- Ice Path B2F: TM44 Rest (8, 16)
- Ice Path B3F: NeverMeltIce (5, 7)
- Tohjo Falls: Moon Stone (2, 6)

## Tile Mechanics (Global)
- FLOOR: Traversable.
- WALL: Impassable.
- WATER: Traversable (requires SURF).
- WATERFALL: Impassable (requires WATERFALL).
- LEDGE: Impassable from the "low" side. Jumpable from the "high" side. In Ice Path, sliding into a ledge from the high side triggers a jump.
- COUNTER: Impassable; interactable from front.
- LADDER: Warp to another floor/map. Stepping onto it triggers the warp immediately.
- WARP_CARPET_DOWN: Exit/warp to another map.
- PC: Impassable; interactable from front (up).
- ICE: Causes sliding in the direction of movement until an obstacle or non-ice tile is reached.

## Lessons Learned
- Rising Badge: Allows use of HM07 Waterfall outside battle.
- Tohjo Falls Ledges: Row 16 ledges are impassable from North.
- Navigation: If a movement fails twice, the tile is impassable from that direction.
- Item Discovery: Moon Stone found in Tohjo Falls at (2, 6).
- Tool Refinement: ice_pathfinder_v2 updated to handle items as targets and return button sequences.
- Backtracking Loop (Turns 36274-36295): Always verify map connectivity before committing to major backtracking. B3F East and West ARE connected.
- Hallucination Warning (Turn 36248): Position mismatch due to automatic ladder warp. Always verify map ID and coordinates after warps.