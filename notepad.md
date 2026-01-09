# Johto Journey - Final Phase

## Strategy for Victory Road
- **Victory Road Entry:** Turn 36644 (Friday, 4:53 AM)
- **Status:** Exploring 1F at (3, 50). Turn 36659 (Friday, 5:02 AM).
- **Warp:** Exit to Reception Gate at (9, 67).
- **Strategy:** Navigate north, reveal reachable unseen tiles, and manage wild encounters. Ensure team is healthy for the final stretch.

## Strategy for Route 26 (Completed)
- **Defeated Trainers:** Fisher Scott, Psychic Richard, Cooltrainer Joyce, Cooltrainer Gaven, Cooltrainer Jake, Cooltrainer Beth.
- **Reception Gate:** Officer at (8, 11) verified eight Johto badges.

## Strategy for Bug-Catching Contest (Saturday)
- Objective: Obtain a Sun Stone.
- Location: National Park (North of Goldenrod City).
- Method: Win 1st place in the Bug-Catching Contest. 
- Preparation: Lead with a Pokemon that can inflict status (e.g., XENON with Hypnosis). High-point targets are Scyther and Pinsir.
- Timing: Friday (5:02 AM). Contest is tomorrow.

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
- find_closest_unseen_path_v3: Refined version.
- battle_strategist: Active.

## General Lessons & Warnings
- Hallucination Warning: Always verify map ID and coordinates after warps/ladders. Check notepad for accuracy during battles. Avoid Redundant Goal restatements. Check root hypotheses regularly.
- **Ladder Connection:** (1, 35) <-> (1, 49). Connects the lower and middle sections of 1F.
- **Victory Road Mechanic:** No trainers are present in this cave, only wild Pokémon and the Rival at the exit.
- **Exploration Strategy:** Use Max Repel to avoid wild encounters. Use `find_closest_unseen_path_v3` to reveal the map. Current focus: Southern section (y > 45).
- **Repel Status:** Max Repel used at Turn 36666. Lasts for 250 steps.
- **Team Training:** Ouroboros (Lv15) and XENON (Lv38) need leveling before the Elite Four.
- **Items Found:**
  - (15, 48): Full Heal (Collected)
  - (12, 48): Max Revive (Collected)
  - (7, 38): Poke Ball (Spotted)