# Johto Journey - Final Phase

## Strategy for Route 26 & Victory Road
- **Start Turn:** 36500 (Friday, 4:40 AM)
- **Strategy:** Navigate north to reach Victory Road.
- **Progress:**
  - Defeat trainers on Route 26. [In Progress]
  - Enter house at (7, 5). [Current]
  - Heal at the Heal House at (15, 57). [Completed]
  - Collect Ice Berry at (14, 54). [Completed]

## Defeated Trainers (Route 26)
- Fisher Scott at (10, 92).
- Psychic Richard at (13, 79).
- Cooltrainer Joyce at (10, 56).
- Cooltrainer Gaven at (9, 38).
- Cooltrainer Jake at (14, 24).

## Strategy for Bug-Catching Contest (Saturday)
- Objective: Obtain a Sun Stone.
- Location: National Park (North of Goldenrod City).
- Method: Win 1st place in the Bug-Catching Contest.
- Preparation: Lead with a Pokemon that can inflict status (e.g., XENON with Hypnosis). High-point targets are Scyther and Pinsir.
- Timing: Friday (4:40 AM). Contest is tomorrow.

## Battle Mechanics
- Type Effectiveness:
  - Psychic super effective against Poison/Ghost (XENON).
  - Water 4x effective against Rock/Ground (GNEISS).
  - Fire super effective against Grass/Poison (Victreebel/Parasect).
  - Electric super effective against Water (Kingler/Blastoise/Golduck).
- Strategy:
  - Switching resets stat drops.
  - Bulky physical attackers (GNEISS) vs high-speed Psychic.

## Tile Mechanics (Global)
- FLOOR: Traversable.
- WALL: Impassable.
- TALL_GRASS: Traversable; wild encounters.
- WATER: Traversable (requires SURF).
- WATERFALL: Face and A to climb.
- LEDGE: Impassable from low, jumpable from high.
- FLOOR_UP_WALL: Impassable from South.
- LADDER: Warp (except Route 27 bridge).
- PC: Interact from front.
- ICE: Sliding.
- LEDGE_HOP_DOWN: Jump N->S.

## Area-Specific Insights
- Route 27 Bridge: Ladders are FLOOR.
- Route 27: Item at (53, 12) unreachable from East.
- Ice Path: B3F sides ARE connected.

## Tool Status
- find_path_v2: Reliable.
- ice_pathfinder_v2: Reliable.
- battle_strategist: Active.

## General Lessons & Warnings
- Always verify map ID and coordinates after warps.