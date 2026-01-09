# Johto Journey - Final Phase (Started Turn 35938)

## Primary Goal: Indigo Plateau (Start Turn 36211)
- Objective: Challenge the Pokémon League.
- Strategy: Navigate Tohjo Falls and Route 27 to reach Victory Road.

## Strategy: Navigate Tohjo Falls (Start Turn 35972)
- Objective: Traverse Tohjo Falls to reach the eastern exit leading to the rest of Route 27.
- Requirements: SURF and WATERFALL (Rising Badge allows use).
- Route: New Bark Town -> Route 27 (East via Surf) -> Tohjo Falls -> Route 27 (East) -> Route 26 (North) -> Victory Road.
- Steps:
  1. Obtain HM07 Waterfall from Ice Path 1F. [Completed]
  2. Teach Waterfall to LAPIS (slot 6). [Completed]
  3. Use Waterfall to climb the falls in Tohjo Falls. [Current]
  4. Locate the eastern exit of Tohjo Falls.

## Strategy: Bug-Catching Contest (Saturday)
- Objective: Obtain a Sun Stone.
- Location: National Park (North of Goldenrod City).
- Method: Win 1st place in the Bug-Catching Contest.
- Preparation: Lead with a Pokemon that can inflict status (e.g., XENON with Hypnosis) or has high HP to endure hits while catching. High-point targets are Scyther and Pinsir.
- Route: Fly to Goldenrod City -> Head North to Route 35 Gatehouse.
- Current Day: Friday (Turn #36391). Contest is tomorrow (Saturday).

## Tile Mechanics (Global)
- FLOOR: Traversable.
- WALL: Impassable.
- WATER: Traversable (requires SURF).
- WATERFALL: Impassable (requires WATERFALL). To climb, face the waterfall tile while surfing and press A. Triggers a scripted movement up the falls.
- LEDGE: Impassable from the "low" side. Jumpable from the "high" side. In Ice Path, sliding into a ledge from the high side triggers a jump.
- FLOOR_UP_WALL: Impassable from the south/below. Functions as a wall in this direction. [Verified Turn 36314]
- COUNTER: Impassable; interactable from front.
- LADDER: Warp to another floor/map. Stepping onto it triggers the warp immediately.
- WARP_CARPET_DOWN: Exit/warp to another map.
- PC: Impassable; interactable from front (up).
- ICE: Causes sliding in the direction of movement until an obstacle or non-ice tile is reached.

## Lessons Learned
- Rising Badge: Allows use of HM07 Waterfall outside battle.
- Tohjo Falls Ledges: Row 16 ledges are reported impassable from North. [TO VERIFY]
- Navigation: If a movement fails twice, the tile is impassable from that direction.
- Item Discovery: Moon Stone found in Tohjo Falls at (2, 6).
- Tool Refinement: ice_pathfinder_v2 updated to handle items as targets and return button sequences.
- Backtracking Loop (Turns 36274-36295): Always verify map connectivity before committing to major backtracking. B3F East and West ARE connected.
- Hallucination Warning (Turn 36248): Position mismatch due to automatic ladder warp. Always verify map ID and coordinates after warps.