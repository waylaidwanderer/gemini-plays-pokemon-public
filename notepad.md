# I. Core Gameplay & World Rules

## A. Game Mechanics
- **Level Cap:** 8 badges = Level 65.
- **PC Interaction:** Stand directly below the PC, face up, and press 'A' to access Pokémon Storage. 'Gem's PC' is for items.
- **HM Usage:** HMs are used from the party menu. Fainted Pokémon can use field moves.
- **Surfing:** Not all `ground` tiles adjacent to `water` are valid starting points.
- **Boulder Pushing:** Activate Strength once from the party menu. For each push, simply walk into the boulder. It does not need to be reactivated for every push. When pushing a boulder, the player character moves into the boulder's previous tile after a horizontal push, but does NOT move after a vertical push.
- **Puzzle Resets:** Leaving and re-entering a map (e.g., Victory Road 1F to Route 23) resets its boulder puzzles. Using ladders between floors (e.g., 1F to 2F) does NOT reset them.
- **Off-Screen State Changes:** An object's state (like a `boulder_barrier`) will not update in the map data until it is visible on-screen.

## B. Tile Glossary & Movement Rules
- `ground`: Standard walkable tile (Elevation 0).
- `elevated_ground`: Walkable tile at a higher elevation (Elevation 2). It is IMPOSSIBLE to step directly between `ground` and `elevated_ground`.
- `steps`: Allows two-way movement between `ground` and `elevated_ground`.
- `cleared_boulder_barrier`: A former barrier that acts as a one-way ramp (Elevation 1). Connects to adjacent elevations but cannot be stepped up onto from `ground` or down from to `ground`.
- `ladder_up`: Warp tile leading to a higher floor.
- `ladder_down`: Warp tile leading to a lower floor.
- `ledge`: One-way traversal. Can only be jumped DOWN from the tile directly above. Acts as a wall from all other directions.
- `impassable`: Wall. Defeated trainers on Victory Road 1F & 2F are impassable obstacles.
- `boulder_switch`: Floor switch for boulders.
- `boulder_barrier`: Impassable barrier linked to a switch.
- `hole`: Drops to a lower floor. Pushing a boulder into one moves it to the floor below.

# II. Battle Intelligence

## A. Verified Type Effectiveness Chart
- **Super Effective (2x):** Psychic > Ghost, Poison; Ghost > Psychic; Electric > Rock, Water; Flying > Grass, Poison, Fighting; Ice > Ground, Grass, Flying, Dragon; Ground > Poison, Fire, Electric, Rock, Ground; Rock > Fire, Ice, Flying, Bug; Fighting > Normal, Rock, Ice; Water > Fire, Ground, Rock; Grass > Water, Ground, Rock; Bug > Grass, Poison, Psychic; Poison > Grass, Bug
- **Not Very Effective (0.5x):** Normal !> Rock; Electric !> Grass, Electric, Dragon; Rock !> Psychic; Psychic !> Psychic; Poison !> Poison, Ground, Rock, Ghost; Ice !> Water, Ice, Fire; Fighting > Poison, Flying, Psychic, Bug; Water !> Water, Grass, Dragon; Grass !> Fire, Grass, Poison, Flying, Bug, Dragon
- **Immune (0x):** Flying immune to Ground; Ground immune to Electric; Ghost immune to Normal, Fighting

## B. Strategic Notes & Mechanics
- **"No Will to Fight" Message:** A party menu cursor error on a fainted Pokémon, not a refusal to battle.
- **Struggle Mechanic:** Used automatically only when a Pokémon is out of PP for ALL moves.
- **Full Heal:** Cures status conditions only, does not restore HP.

# III. Core Principles & Methodology
- **Agent-First Approach:** Before attempting any manual solution for a complex problem (puzzles, multi-step navigation, difficult battles), I MUST consult the relevant specialist agent first (`puzzle_strategist_agent`, `battle_strategist_agent`, etc.).
- **Scientific Method:** Use a scientific approach: form a hypothesis, test it, and document the conclusion. Do not modify tools to test hypotheses; test them with in-game actions first.
- **Trust System Feedback:** System feedback (like validation warnings or tool errors) is the source of truth and MUST be trusted over personal assumptions or agent outputs.
- **IMMEDIATE ACTION:** Flaws in tools or data management (notepad, markers) must be addressed immediately, not deferred as goals.

# IV. Puzzle Solutions & Verified Mechanics

## A. Solved Puzzles & Verified Mechanics
- **Victory Road 3F (Boulder Puzzle):** Solved by maneuvering the boulder from (7, 2) to the switch at (4, 6).
- **Victory Road 1F (Elevation):** Confirmed direct movement between `elevated_ground` and `ground` is impossible.
- **Victory Road 2F (Western Boulder):** Solved by pushing the boulder at (5,15) to the switch at (2,17), clearing the barrier at (8,9) and (8,10).
- **Victory Road 2F (Puzzle Resets):** Confirmed that using ladders between floors does NOT reset boulder puzzles.

## B. Discarded Hypotheses
- **Victory Road 3F (Failed Plan):** The initial strategy from the `puzzle_strategist_agent` to push a boulder along the y=2 corridor was a hallucination. The path was blocked by impassable tiles at (5, 2) and (6, 2). This plan is now discarded.
- **Victory Road 2F (Failed Agent Plan):** The puzzle_strategist_agent's plan to move the boulder onto elevated ground was impossible and has been discarded.
- **Victory Road 2F (Trapped Boulder):** All attempts to move the boulder at (6, 8) or (8, 12) to the eastern switch resulted in it becoming trapped. These approaches are invalid.
- **Victory Road 2F (Failed Manual Plan):** The manual plan to push the boulder from (4, 12) south to (4, 17) and then east to (10, 17) failed. The path east from (5, 17) was blocked by an impassable tile at (6, 17).

# V. Lessons Learned & Heuristics
- **Verify 'Trapped' Scenarios:** If a pathfinder tool reports 'No path found' and I believe I am trapped, I must not accept this conclusion without verification. I need to manually inspect the map for alternative routes and trust the game state's list of reachable warps over my own assumptions. (Lesson from Turn 119657 Hallucination)

# VI. Active To-Do & Reminders

## C. Victory Road 1F (Eastern Boulder Puzzle)
- **Status:** Appears unsolvable. `puzzle_strategist_agent` concluded all boulders are trapped or have no viable path to the switch at (18, 14).
- **Hypothesis:** A hidden mechanic or switch exists.
- **Plan:**
  1. Thoroughly re-explore the map for hidden interactable objects.
  2. Investigate the barrier at (10, 13) for an alternative opening mechanism.
  3. If all else fails, reset the puzzle by leaving and re-entering the map.