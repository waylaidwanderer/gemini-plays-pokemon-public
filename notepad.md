# Johto Journey - Final Phase

## Strategy for Route 26 & Victory Road
- **Route 26 Trek Start:** Turn 36500 (Friday, 4:00 AM)
- **Defeated Trainers (Route 26):**
  - Fisher Scott (10, 92), Psychic Richard (13, 79), Cooltrainer Joyce (10, 56), Cooltrainer Gaven (9, 38), Cooltrainer Jake (14, 24), Cooltrainer Beth (6, 8).
- **Victory Road Gate (ID: 23_13):**
  - Officer at (8, 11) verified eight Johto badges.
  - Exit to Victory Road located at (9, 0) and (10, 0).
- **Recent Lessons:**
  - `select_battle_option` should only be used once per turn; check intermediate states for menu progress.
  - The "house" at (7, 5) on Route 26 is actually the Pokémon League Reception Gate.
  - Route 27 Bridge: Ladder sprites function as FLOOR tiles.

## Strategy for Bug-Catching Contest (Saturday)
- Objective: Obtain a Sun Stone.
- Location: National Park (North of Goldenrod City).
- Method: Win 1st place in the Bug-Catching Contest.
- Preparation: Lead with a Pokemon that can inflict status (e.g., XENON with Hypnosis). High-point targets are Scyther and Pinsir.
- Timing: Friday (4:53 AM). Contest is tomorrow.

## Battle Mechanics & Type Matchups
- **Psychic:** Super effective against Poison/Ghost (XENON).
- **Water:** 4x effective against Rock/Ground (GNEISS).
- **Fire:** Super effective against Grass/Poison (Victreebel/Parasect).
- **Electric:** Super effective against Water (Kingler/Blastoise/Golduck).
- **Ground (Earthquake):** 4x effective against Fire (Rapidash/Flareon/Arcanine).
- **Strategy:** Switching resets stat drops. Use GNEISS vs Fire/Psychic threats.

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

## Tool Status
- find_path_v2: Reliable.
- ice_pathfinder_v2: Reliable.
- find_closest_unseen_path_v3: Refined version.
- battle_strategist: Active.

## General Lessons & Warnings
- Hallucination Warning: Always verify map ID and coordinates after warps/ladders. Check notepad for accuracy during battles. Avoid Redundant Goal restatements. Check root hypotheses regularly.