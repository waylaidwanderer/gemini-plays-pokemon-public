# I. Game Mechanics & Traversal
## A. Core Rules
- **Level Cap:** 8 badges = Level 65.
- **PC Interaction:** Stand directly below the PC, face up, and press 'A'.
- **HM Usage:** HMs are used from the party menu. Fainted Pokémon can use field moves.
- **Surfing:** Not all `ground` tiles adjacent to `water` are valid starting points.
- **Puzzle Resets:** Leaving and re-entering a map (e.g., by using a ladder to another floor) resets all boulders on that map to their original positions.
- **Off-Screen State Changes:** An object's state will not update in the map data until it is visible on-screen.
- **Boulder Pushing:** A boulder can be pushed from an adjacent tile by facing it and walking into it. Pressing 'A' does not work.

## B. Tile Glossary & Movement Rules
- `ground`: Standard walkable tile.
- `grass`: Wild Pokémon encounters.
- `water`: Requires SURF.
- `impassable`: Wall. Defeated trainers on Victory Road 1F & 2F are impassable obstacles.
- `ledge`: One-way traversal. Can only be jumped DOWN from the tile directly above. Acts as a wall from all other directions.
- `elevated_ground`: Walkable, different elevation. It is NOT possible to step down from an `elevated_ground` tile to an adjacent `ground` tile.
- `steps`: Allows movement between `ground` and `elevated_ground` in both directions.
- `boulder_switch`: Floor switch for boulders.
- `boulder_barrier`: Impassable barrier linked to a boulder switch.
- `cleared_boulder_barrier`: A former barrier that acts as a ramp. It connects `ground` (elevation 0) and `elevated_ground` (elevation 2). It is NOT possible to move from `ground` onto this tile. It is possible to move from this tile directly down to an adjacent `ground` tile.
- `hole`: Drops to a lower floor. Pushing a boulder into one causes it to appear on the floor below.
- `spinner`: Forces movement.
- `cuttable`: A tree that can be removed with the HM Cut.
- `ladder_up`: Warps to a higher floor.
- `ladder_down`: Warps to a lower floor.

# II. Battle Intel
## A. Type Effectiveness Chart (Verified)
- **Super Effective (2x):** Psychic > Ghost, Poison; Ghost > Psychic; Electric > Rock, Water; Flying > Grass, Poison, Fighting; Ice > Ground, Grass, Flying, Dragon; Ground > Poison, Fire, Electric, Rock, Ground; Rock > Fire, Ice, Flying, Bug; Fighting > Normal, Rock, Ice; Water > Fire, Ground, Rock; Grass > Water, Ground, Rock; Bug > Grass, Poison, Psychic; Poison > Grass, Bug
- **Not Very Effective (0.5x):** Normal !> Rock; Electric !> Grass, Electric, Dragon; Rock !> Psychic; Psychic !> Psychic; Poison !> Poison, Ground, Rock, Ghost; Ice !> Water, Ice, Fire; Fighting > Poison, Flying, Psychic, Bug; Water !> Water, Grass, Dragon; Grass !> Fire, Grass, Poison, Flying, Bug, Dragon
- **Immune (0x):** Flying immune to Ground; Ground immune to Electric; Ghost immune to Normal, Fighting
- **Correction:** Psychic-type moves deal NEUTRAL (1x) damage to Rock-type Pokémon.

## B. Strategic Notes
- **"No Will to Fight" Message:** A party menu cursor error on a fainted Pokémon, not a refusal to battle.
- **Struggle Mechanic:** Struggle is only used automatically when a Pokémon is out of PP for ALL of its moves.
- **Full Heal Mechanic:** This item ONLY cures status conditions. It does NOT restore HP.

# III. Core Principles & Methodology
- **Agent-First Approach:** Before attempting any manual solution for a complex problem (puzzles, multi-step navigation, difficult battles), I MUST consult the relevant specialist agent first (`puzzle_strategist_agent`, `battle_strategist_agent`, etc.).
- **Scientific Method:** Use a scientific approach: form a hypothesis, test it, and document the conclusion. Do not modify tools to test hypotheses; test them with in-game actions first.
- **Trust System Feedback:** System feedback (like validation warnings or tool errors) is the source of truth and MUST be trusted over personal assumptions or agent outputs.
- **IMMEDIATE ACTION:** Flaws in tools or data management (notepad, markers) must be addressed immediately, not deferred as goals.

# IV. Current Puzzle: Victory Road 2F
- **Objective:** Solve the two-boulder puzzle to progress.

## Puzzle 1: Western Boulder
- **Hypothesis #1 (Original):** Push boulder at (5, 15) south to (5, 17), then left to switch at (2, 17).
- **Test:** Pushed boulder to (5, 17).
- **Conclusion:** FAILED. Could not access (6, 17) to push left. Boulder was trapped.

- **Hypothesis #2:** Push boulder at (6, 15) left to (5, 15), then down to (5, 17), then left to switch at (2, 17).
- **Test:** Pushed boulder to (2, 17).
- **Conclusion:** SUCCESS. Barrier at (8, 9) and (8, 10) was cleared after visual confirmation.

## Puzzle 2: Eastern Boulder
- **Hypothesis #1 (Push Up):** Push boulder at (6, 6) UP to (6, 5).
- **Test:** Pushed boulder to (6, 5).
- **Conclusion:** FAILED. Path upwards is a dead end. The only way forward is down.

- **Hypothesis #2 (Push Down):** Push boulder at (6, 6) down to (6, 8), then right through the cleared barrier at (8, 9), then down to the switch at (10, 17).
- **Status:** Untested. This is the new current plan.

# V. Archived Lessons & Puzzle Solutions
- **Victory Road 3F Puzzle:** The `gem_pathfinder_v2` tool repeatedly failed to find a path to the warp at (27, 9). This was initially mistaken for a bug in the A* algorithm. The tool was working correctly; the path was blocked by a boulder I had inadvertently moved into the main corridor. This highlights the importance of careful movement during puzzle-solving to avoid creating new obstacles.
- **Vertical Pushing:** When pushing a boulder up or down, the player character does not move into the boulder's previous tile.

## Puzzle 2: Eastern Boulder (Agent Strategy)
- **Strategic Summary:** The puzzle should be solved by undertaking the complex task of navigating the boulder from (6, 6) through a long and narrow maze to reach the switch at (10, 17). The primary challenge is avoiding the numerous trap locations along the path.
- **Sub-Goal:** Move the boulder at (6, 6) to the switch at (10, 17).