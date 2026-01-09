# Johto Journey - Final Phase

## Strategy for Route 26 & Victory Road
- **Route 26 Trek Start:** Turn 36500 (Friday, 4:00 AM)
- **Defeated Trainers:**
  - Fisher Scott at (10, 92).
  - Psychic Richard at (13, 79).
  - Cooltrainer Joyce at (10, 56).
  - Cooltrainer Gaven at (9, 38).
  - Cooltrainer Jake at (14, 24).
  - Cooltrainer Beth at (6, 8) [Defeated Turn 36634].
- **Notes:**
  - Sign at (8, 6): Route 26 / Pokémon League Reception Gate.
  - House at (7, 5): Target for investigation.
  - Item at (9, 15): Blocked by walls from the east; loop around needed.

## Strategy for Bug-Catching Contest (Saturday)
- Objective: Obtain a Sun Stone.
- Location: National Park (North of Goldenrod City).
- Method: Win 1st place in the Bug-Catching Contest.
- Preparation: Lead with a Pokemon that can inflict status (e.g., XENON with Hypnosis). High-point targets are Scyther and Pinsir.
- Timing: Friday (4:49 AM). Contest is tomorrow.

## Battle Mechanics & Type Matchups
- **Psychic:** Super effective against Poison/Ghost (XENON).
- **Water:** 4x effective against Rock/Ground (GNEISS).
- **Fire:** Super effective against Grass/Poison (Victreebel/Parasect).
- **Electric:** Super effective against Water (Kingler/Blastoise/Golduck).
- **Ground (Earthquake):** 4x effective against Fire (Rapidash/Flareon/Arcanine).
- **Strategy:** Switching resets stat drops and accuracy penalties. Use GNEISS vs Fire/Psychic threats.

## Tile Mechanics (Global)
- FLOOR: Traversable.
- WALL: Impassable.
- TALL_GRASS: Traversable; wild encounters.
- WATER: Traversable (requires SURF).
- WATERFALL: Face and press A to climb.
- LEDGE: Impassable from low side, jumpable from high side.
- FLOOR_UP_WALL: Impassable from South.
- LADDER: Warp (except Route 27 bridge).
- PC: Interact from front.
- ICE: Sliding.
- LEDGE_HOP_DOWN: Jump N->S.

## Area-Specific Insights
- Route 27 Bridge: Ladders function as FLOOR.
- Route 27: Item at (53, 12) unreachable from East.
- Ice Path: B3F sides ARE connected.

## Tool Status
- find_path_v2: Reliable.
- ice_pathfinder_v2: Reliable.
- find_closest_unseen_path_v3: Refined version.
- battle_strategist: Active.

## General Lessons & Warnings
- Hallucination Warning: Always verify map ID and coordinates after warps/ladders. Check notepad for accuracy during battles. Avoid Redundant Goal restatements.