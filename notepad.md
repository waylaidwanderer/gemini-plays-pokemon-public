# I. Game Mechanics & Traversal

## A. Core Principles
- **Game Engine is Truth:** The game engine's behavior is the ultimate source of truth. If a tool or hypothesis is contradicted by the engine (e.g., a blocked movement), the tool/hypothesis is wrong and must be corrected immediately. 

## B. Core Rules
- **Level Cap:** The level cap with 8 badges is 65.
- **"No Will to Fight" Message:** Appears when the party menu cursor is on a fainted Pokémon.
- **HM Usage:** HMs are used from the party menu. Fainted Pokémon can use field moves.
- **PC Interaction:** To use a PC, stand directly below it, face up, and press 'A'.
- **Surfing:** Not all `ground` tiles adjacent to `water` are valid starting points.
- **Boulder Pushing:** Activate Strength from the party menu. Face the boulder and press the directional button. The boulder moves one tile, but the player's position does not change.
- **Puzzle Resets:** Leaving and re-entering a floor resets all boulders to their original positions.

## C. Tile Glossary & Movement Rules
- `ground`: Standard walkable tile.
- `grass`: Wild Pokémon encounters.
- `water`: Requires SURF.
- `impassable`: Wall.
- `elevated_ground`: Walkable, different elevation. Movement between `elevated_ground` and lower elevations is only possible via `steps` tiles. Stepping down directly to `ground` is not possible.
- `steps`: Allows movement between elevations.
- `boulder_switch`: Floor switch for boulders.
- `boulder_barrier`: Impassable barrier linked to a boulder switch.
- `cleared_boulder_barrier`: Acts as a one-way ramp. It is only possible to move DOWN from an elevated area onto this tile, not UP from a lower area.
- `hole`: Drops to a lower floor. Pushing a boulder into one causes it to appear on the floor below.
- `spinner`: Forces movement.
- `ladder_up` / `ladder_down`: Warps between floors.

# II. Battle Intel

## A. Type Effectiveness Chart (Verified)
- **Super Effective (2x):** Psychic > Ghost, Poison; Ghost > Psychic; Electric > Rock, Water; Flying > Grass, Poison, Fighting; Ice > Ground, Grass, Flying, Dragon; Ground > Poison, Fire, Electric, Rock; Rock > Fire, Ice, Flying, Bug; Fighting > Normal, Rock, Ice; Water > Fire, Ground, Rock; Grass > Water, Ground, Rock; Bug > Grass, Poison, Psychic; Poison > Grass, Bug
- **Not Very Effective (0.5x):** Normal !> Rock; Electric !> Grass, Electric, Dragon; Rock !> Psychic; Psychic !> Psychic; Poison !> Poison, Ground, Rock, Ghost; Ice !> Water, Ice, Fire; Fighting > Poison, Flying, Psychic, Bug; Water !> Water, Grass, Dragon; Grass !> Fire, Grass, Poison, Flying, Bug, Dragon
- **Immune (0x):** Flying immune to Ground; Ground immune to Electric; Ghost immune to Normal, Fighting
- **Correction:** Psychic-type moves deal NEUTRAL (1x) damage to Rock-type Pokémon.

## B. Trainer Battle Rules
- **No Respawns:** Defeated trainers do NOT respawn. They become permanent obstacles that are impassable by normal movement, but can be bypassed by using the `gem_pathfinder` tool with the `ignorable_coords` parameter.

# III. Puzzle Mechanics & Key Discoveries

- **Victory Road 1F - Western Dead End:** The western section of this floor, accessed from the main entrance, is a dead end. The ladder at (2, 2) is unreachable from here. The purpose of the two boulders in this area is unknown, but they do not provide immediate access to the rest of the floor. The only exit is back to Route 23.
- **Victory Road 2F - Western Trap:** This puzzle requires a two-step "prime and trigger" mechanic. Pushing the boulder onto the switch at (2, 17) primes the trap. Leaving the floor and re-entering triggers the event, opening the barrier at (8, 9) and (8, 10).
- **Victory Road 3F - Hole Puzzle:** Pushing the boulder at (14, 13) south into the hole at (14, 15) causes it to drop to the floor below, affecting a puzzle there.

# IV. Tool Status & Development

- **Pathfinder Status:** The `gem_pathfinder` is undergoing iterative repair. After a complete overhaul, it still suffers from bugs (e.g., syntax errors) and unreliability on complex maps like Victory Road. Fixing this tool remains a top priority.
- **Puzzle Solver Status:** The `boulder_puzzle_solver` is implemented but its internal pathfinder may also be flawed, preventing it from solving puzzles on this map.

# V. Future Tool/Agent Ideas

- **Paradox Resolution Agent:** An agent that takes conflicting data sources (e.g., tool output vs. overwatch warnings) and proposes hypotheses to resolve the discrepancy. This could help break logical loops faster.
- **Reflection Agent:** An agent to automate the process of answering the periodic reflection questions.
- **Puzzle Path Prioritizer Agent:** An agent that analyzes puzzle elements (boulders, switches) and a navigation goal to suggest which puzzle element should be tackled first. This would help in situations where the overall solution is unknown and multiple starting points are possible.