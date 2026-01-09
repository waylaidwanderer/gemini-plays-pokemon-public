# Johto Journey - Final Phase

## Primary Goal: Indigo Plateau
- Objective: Challenge the Pokémon League.
- Strategy: Navigate Tohjo Falls and Route 27 to reach Victory Road.

## Strategy: Navigate Route 27
- Objective: Reach Route 26 and Victory Road.
- Progress:
  - Route 27 West & Tohjo Falls. [Completed]
  - Explore house at (33, 7). [Completed]
  - Route 27 Bridge & Trainers. [Completed]
  - Reach Route 26 Junction. [Current]

## Strategy: Bug-Catching Contest (Saturday)
- Objective: Obtain a Sun Stone.
- Location: National Park (North of Goldenrod City).
- Method: Win 1st place in the Bug-Catching Contest.
- Preparation: Lead with a Pokemon that can inflict status (e.g., XENON with Hypnosis). High-point targets are Scyther and Pinsir.
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
- Route 27 Bridge: Ladder sprites function as FLOOR tiles.
- Route 27 Navigation: Item at (53, 12) is unreachable from the East due to a wall/ledge. Must approach from the West.
- Battle Management: Switching resets stat drops and accuracy penalties.
- Hallucination Warning: Always verify map ID and coordinates after warps/ladders.
- Map Connectivity: Verify connectivity before committing to major backtracking (e.g., Ice Path B3F sides ARE connected).