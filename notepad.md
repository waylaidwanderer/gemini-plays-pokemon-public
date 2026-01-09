# Johto Journey - Final Phase

## Primary Goal: Indigo Plateau
- Objective: Challenge the Pokémon League.
- Strategy: Navigate Tohjo Falls and Route 27 to reach Victory Road.

## Strategy: Navigate Tohjo Falls
- Objective: Traverse Tohjo Falls to reach the eastern exit leading to Route 27.
- Requirements: SURF and WATERFALL.
- Route: New Bark Town -> Route 27 (Surf East) -> Tohjo Falls -> Route 27 (East) -> Route 26 (North) -> Victory Road.
- Steps:
  1. Obtain HM07 Waterfall from Ice Path 1F. [Completed]
  2. Teach Waterfall to LAPIS (slot 6). [Completed]
  3. Use Waterfall to climb the falls in Tohjo Falls. [Completed]
  4. Locate the eastern exit of Tohjo Falls. [Completed]
  5. Exit Tohjo Falls at (25, 15). [Completed]
  6. Navigate Route 27 East to Route 26. [In Progress]
    - 6a. Explore house at (33, 7). [Completed]
    - 6b. Continue East on Route 27. [In Progress]
      - Battle Psychic Gilbert on bridge. [Completed]
      - Battle Cooltrainer Brian on bridge. [Completed]
      - Battle Cooltrainer F at (72, 8). [Current]
      - Move East past the bridge. [Next]
  7. Navigate Route 26 North to Victory Road. [Next]

## Time Tracking
- Route 27 Navigation: Started Turn 36404.

## Strategy: Bug-Catching Contest (Saturday)
- Objective: Obtain a Sun Stone.
- Location: National Park (North of Goldenrod City).
- Method: Win 1st place in the Bug-Catching Contest.
- Preparation: Lead with a Pokemon that can inflict status (e.g., XENON with Hypnosis). High-point targets are Scyther and Pinsir.
- Route: Fly to Goldenrod City -> Head North to Route 35 Gatehouse.
- Timing: Current Day: Friday. Contest is tomorrow (Saturday).

## Tool Status
- find_path_v2: Reliable for standard overworld navigation.
- ice_pathfinder_v2: Refined to handle items and FLOOR_UP_WALL. Reliable.
- solve_boulders_v2: Unverified in current context.
- battle_strategist: Active. Use for wild encounters and trainer battles.

## Tile Mechanics (Global)
- FLOOR: Traversable.
- WALL: Impassable.
- TALL_GRASS: Traversable; may trigger wild encounters.
- WATER: Traversable (requires SURF).
- WATERFALL: Face tile while surfing and press A to climb. Triggers scripted movement.
- LEDGE: Impassable from the \"low\" side. Jumpable from the \"high\" side.
- FLOOR_UP_WALL: Impassable from the south/below. Functions as a wall in this direction.
- COUNTER: Impassable; interactable from front.
- LADDER: Warp to another floor/map. Triggers immediately on entry. Exception: On the Route 27 bridge, these tiles function as FLOOR.
- WARP_CARPET_DOWN: Exit/warp to another map.
- PC: Impassable; interactable from front (up).
- ICE: Causes sliding until obstacle or non-ice tile is reached.
- LEDGE_HOP_DOWN: Jumpable from North to South. Impassable from South to North.
- LEDGE_HOP_LEFT: Jumpable from Right to Left. Impassable from Left to Right.
- VOID: Impassable area outside the map boundaries.

## Lessons Learned
- Rising Badge: Enables Waterfall use outside battle.
- Tohjo Falls Ledges: Row 16 ledges are reported impassable from North. [TO VERIFY]
- Navigation: Repeated movement failure indicates the tile is impassable from that direction.
- Item Discovery: Moon Stone found in Tohjo Falls at (2, 6).
- Hallucination Warning: Always verify map ID and coordinates after warps/ladders.
- Map Connectivity: Verify connectivity before committing to major backtracking (e.g., Ice Path B3F sides ARE connected).