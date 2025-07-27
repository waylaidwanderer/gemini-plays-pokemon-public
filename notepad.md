# I. Game Mechanics & Traversal

## A. Core Rules
- **Level Cap:** The level cap with 8 badges is 65.
- **"No Will to Fight" Message:** Appears when the party menu cursor is on a fainted Pokémon.
- **HM Usage:** HMs are used from the party menu. Fainted Pokémon can use field moves.
- **PC Interaction:** To use a PC, stand directly below it, face up, and press 'A'.
- **Surfing:** Not all `ground` tiles adjacent to `water` are valid starting points. The game engine can block movement even if a path seems clear.

## B. Boulder Pushing
- **Activation:** Activate Strength from the party menu.
- **Execution:** Face the boulder and press the directional button. The boulder moves one tile, but the player's position does not change.
- **Reset Mechanic:** Leaving and re-entering a floor resets all boulders to their original positions.

## C. Tile Glossary & Movement Rules
- `ground`: Standard walkable tile.
- `grass`: Wild Pokémon encounters.
- `water`: Requires SURF.
- `impassable`: Wall.
- `elevated_ground`: Walkable, different elevation. Movement between `elevated_ground` and lower elevations is only possible via `steps` or `cleared_boulder_barrier` tiles. Stepping down directly to `ground` is not possible.
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

## B. Trainer Rosters
- **Super Nerd (Victory Road 1F):** FLAREON (Lv53), TENTACRUEL (Lv53), NINETALES (Lv53), DEWGONG (Lv53)

## C. Trainer Battle Rules
- **No Respawns:** Defeated trainers do NOT respawn after leaving and re-entering a map. They become permanent, impassable obstacles.

# III. Puzzle Solutions & Progress

## A. Victory Road 1F - Path to Ladder (INCORRECT - DO NOT USE)
- **Status:** This documented solution has been tested and is INCORRECT. Following these steps leads to an unsolvable state where the player is trapped.
- **Failed Steps:**
  - Push boulder (6, 16) to (6, 17).
  - Ascend steps (6, 14).
  - Push boulder (3, 11) to switch (3, 10).
- **Result:** The boulder barrier at (10, 13) remains closed, and the path to the ladder at (2, 2) is blocked.
- **New Goal:** Must reset the puzzle by exiting and re-entering the map to formulate a new solution.

## B. Victory Road 2F - Western Trap
- **Solution:** This puzzle requires a two-step "prime and trigger" mechanic. Pushing the boulder onto the switch at (2, 17) primes the trap. Leaving the floor and re-entering the triggers the event, opening the barrier at (8, 9) and (8, 10).

## C. Victory Road 3F Puzzles
- **Central Boulder (14, 13):** Push south two times into the hole at (14, 15). This affects the floor below.
- **Northern Boulder (23, 4):** Push south three times onto the switch at (23, 7). This opens the boulder barrier at (8, 11).

# IV. Lessons Learned & Tool Status

- **Core Principle:** Trust the game engine over my own assumptions or a tool's flawed logic. If a tool's output contradicts the engine's behavior, the tool's logic is flawed and must be corrected immediately.
- **Lesson Learned:** Do not abandon a path until it has been fully explored. A single obstacle does not mean a dead end. I must check for alternate routes around perceived blockages before reverting to new hypotheses.
- **Pathfinder Status:** The `gem_pathfinder` tool's elevation logic has been repeatedly corrected based on direct game engine tests. The `ignorable_coords` feature is critical for navigating past defeated trainers.
- **Puzzle Solver Status:** The `boulder_puzzle_solver` is implemented but was buggy. A critical fix to its player position tracking logic has been applied.