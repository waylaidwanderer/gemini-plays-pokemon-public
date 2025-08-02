# I. Game Mechanics & Traversal
## A. Core Rules
- **Level Cap:** 8 badges = Level 65.
- **PC Interaction:** Stand directly below the PC, face up, and press 'A'.
- **HM Usage:** HMs are used from the party menu. Fainted Pokémon can use field moves.
- **Surfing:** Not all `ground` tiles adjacent to `water` are valid starting points.
- **Puzzle Resets:** Leaving and re-entering a map (e.g., by using a ladder to another floor) resets all boulders on that map to their original positions. This was confirmed when the solved southern boulder puzzle on Victory Road 2F was reset after traveling to 3F and back.
- **Off-Screen State Changes:** An object's state will not update in the map data until it is visible on-screen.
- **Boulder Pushing:** A boulder can be pushed from an adjacent tile by facing it and pressing the corresponding direction. The game's behavior regarding player movement is highly inconsistent. Pushing a boulder usually moves the player into the boulder's vacated space, but this is not guaranteed (e.g., pushing the boulder at (5,16) left from (6,16) did not move the player). The game may also move the player to an unexpected adjacent tile (e.g., pushing a boulder at (5,15) down from (5,14) resulted in the player moving to (6,15)). This mechanic requires careful, turn-by-turn observation.

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
- `cleared_boulder_barrier`: A former barrier that acts as a ramp. It connects `ground` (elevation 0) and `elevated_ground` (elevation 2). It is NOT possible to move from `ground` onto this tile (verified at (8,8)->(8,9)). It is also NOT possible to move from this tile directly down to an adjacent `ground` tile.
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
- **Full Heal Mechanic:** This item ONLY cures status conditions. It does NOT restore HP. This was verified by attempting to use it on multiple injured Pokémon with no status effects, which resulted in the message 'It won't have any effect.'

# III. Core Principles & Methodology
- **Agent-First Approach:** Before attempting any manual solution for a complex problem (puzzles, multi-step navigation, difficult battles), I MUST consult the relevant specialist agent first (`puzzle_strategist_agent`, `battle_strategist_agent`, etc.). This prevents wasted effort on flawed manual plans and is a non-negotiable first step.
- **Break Unproductive Loops:** If a tool proves too difficult to fix in a reasonable time, or if a particular strategy repeatedly fails despite refinement, I must abandon the approach and switch to an alternative strategy (like exploration of unseen areas or unvisited warps) to maintain forward progress. Getting stuck is a sign of a flawed strategy, not a flawed game.
- **Scientific Method:** Use a scientific approach: form a hypothesis, test it, and document the conclusion. Do not modify tools to test hypotheses; test them with in-game actions first.
- **Trust System Feedback:** System feedback (like validation warnings or tool errors) is the source of truth and MUST be trusted over personal assumptions or agent outputs.
- **IMMEDIATE ACTION:** Flaws in tools or data management (notepad, markers) must be addressed immediately, not deferred as goals.

# IV. Untested Assumptions & Hypotheses
- **Victory Road 3F Puzzle:** The `puzzle_strategist_agent` hypothesizes that solving the main boulder puzzle requires the player to find a way to access the tile at (13, 13), which is currently marked as impassable. This suggests a hidden mechanic or an alternative path to that specific tile is the core of the puzzle. This needs to be tested once the boulder is in position at (13, 12).