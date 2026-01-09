# Johto Journey - Final Phase

## Strategy for Route 26 & Victory Road
- **Start Turn:** 36500 (Friday, 4:00 AM)
- **Progress:**
  - Defeat trainers on Route 26. [In Progress]
  - Heal at the Heal House at (15, 57). [Completed]
  - Collect Ice Berry at (14, 54). [Completed]

## Defeated Trainers (Route 26)
- Fisher Scott at (10, 92).
- Psychic Richard at (13, 79).
- Cooltrainer Joyce at (10, 56).
- Cooltrainer Gaven at (9, 38).
- Cooltrainer Jake at (14, 24). [Current]

## Strategy for Bug-Catching Contest (Saturday)
- Objective: Obtain a Sun Stone.
- Location: National Park (North of Goldenrod City).
- Method: Win 1st place in the Bug-Catching Contest.
- Preparation: Lead with a Pokemon that can inflict status (e.g., XENON with Hypnosis). High-point targets are Scyther and Pinsir.
- Timing: Current Day: Friday. Contest is tomorrow (Saturday).

## Battle Mechanics
- Type Effectiveness:
  - Psychic moves are super effective against Poison/Ghost types (like XENON).
  - Water moves are 4x effective against Rock/Ground types (like GNEISS).
  - Fire moves are super effective against Grass/Poison types (like Victreebel).
  - Electric moves are super effective against Water types (like Kingler/Blastoise).
- Strategy:
  - Switching resets stat drops and accuracy penalties.
  - Bulky physical attackers (like GNEISS) are effective against high-speed Psychic threats.

## Tile Mechanics (Global)
- FLOOR: Traversable.
- WALL: Impassable.
- TALL_GRASS: Traversable; may trigger wild encounters.
- WATER: Traversable (requires SURF).
- WATERFALL: Face tile while surfing and press A to climb.
- LEDGE: Impassable from "low", jumpable from "high".
- FLOOR_UP_WALL: Impassable from South.
- LADDER: Warp (except Route 27 bridge where it's FLOOR).
- PC: Interact from front.
- ICE: Sliding.
- LEDGE_HOP_DOWN: Jump N->S.

## Area-Specific Insights
- Route 27 Bridge: Ladder sprites function as FLOOR tiles.
- Route 27 Navigation: Item at (53, 12) unreachable from East.
- Ice Path: B3F sides ARE connected.

## Tool Status
- find_path_v2: Reliable.
- ice_pathfinder_v2: Reliable.
- battle_strategist: Active.

## General Lessons & Warnings
- Hallucination Warning: Always verify map ID and coordinates after warps/ladders.