# I. Active Investigations

## A. Victory Road 1F (Eastern Boulder Puzzle)
- **Directive:** System feedback implies this puzzle must be solved to exit the northwest corner of the map.
- **Objective:** Move a boulder to the switch at (18, 14) to clear the barrier at (10, 13).
- **Hypothesis:** The boulder at (15, 3) is the likely candidate, but I must find a path to the eastern side of the map first, possibly via other floors.

# II. Core Gameplay & World Rules

## A. Game Mechanics
- **Level Cap:** 8 badges = Level 65.
- **PC Interaction:** Stand directly below the PC, face up, and press 'A' to access Pokémon Storage. 'Gem's PC' is for items.
- **HM Usage:** HMs are used from the party menu. Fainted Pokémon can use field moves.
- **Surfing:** Not all `ground` tiles adjacent to `water` are valid starting points.
- **Boulder Pushing (Under Investigation):** Activate Strength once from the party menu. The exact player/boulder movement mechanic for horizontal pushes is unconfirmed and has shown conflicting results. Needs systematic testing.
- **Puzzle Resets:** Leaving and re-entering a map (e.g., Victory Road 1F to Route 23) resets its boulder puzzles. Using ladders between floors (e.g., 1F to 2F) does NOT reset them.
- **Off-Screen State Changes:** An object's state (like a `boulder_barrier`) will not update in the map data until it is visible on-screen.

## B. Tile Glossary & Movement Rules
- `ground`: Standard walkable tile (Elevation 0).
- `elevated_ground`: Walkable tile at a higher elevation (Elevation 2). It is IMPOSSIBLE to step directly between `ground` and `elevated_ground`.
- `steps`: Allows two-way movement between `ground` and `elevated_ground`. Boulders cannot be pushed onto `steps` tiles.
- `cleared_boulder_barrier`: A former barrier that acts as a one-way ramp (Elevation 1). Connects to adjacent elevations but cannot be stepped up onto from `ground` or down from to `ground`.
- `ladder_up`: Warp tile leading to a higher floor.
- `ladder_down`: Warp tile leading to a lower floor.
- `ledge`: One-way traversal. Can only be jumped DOWN from the tile directly above. Acts as a wall from all other directions.
- `impassable`: Wall. **Verified (Turn 120183): Defeated trainers on Victory Road 1F are impassable obstacles.**
- `boulder_switch`: Floor switch for boulders.
- `boulder_barrier`: Impassable barrier linked to a switch.
- `hole`: Drops to a lower floor. Pushing a boulder into one moves it to the floor below.

# III. Battle Intelligence

## A. Verified Type Effectiveness Chart
- **Super Effective (2x):** Psychic > Ghost, Poison; Ghost > Psychic; Electric > Rock, Water; Flying > Grass, Poison, Fighting; Ice > Ground, Grass, Flying, Dragon; Ground > Poison, Fire, Electric, Rock, Ground; Rock > Fire, Ice, Flying, Bug; Fighting > Normal, Rock, Ice; Water > Fire, Ground, Rock; Grass > Water, Ground, Rock; Bug > Grass, Poison, Psychic; Poison > Grass, Bug
- **Not Very Effective (0.5x):** Normal !> Rock; Electric !> Grass, Electric, Dragon; Rock !> Psychic; Psychic !> Psychic; Poison !> Poison, Ground, Rock, Ghost; Ice !> Water, Ice, Fire; Fighting > Poison, Flying, Psychic, Bug; Water !> Water, Grass, Dragon; Grass !> Fire, Grass, Poison, Flying, Bug, Dragon
- **Immune (0x):** Flying immune to Ground; Ground immune to Electric; Ghost immune to Normal, Fighting

## B. Strategic Notes & Mechanics
- **"No Will to Fight" Message:** A party menu cursor error on a fainted Pokémon, not a refusal to battle.
- **Struggle Mechanic:** Used automatically only when a Pokémon is out of PP for ALL moves.
- **Full Heal:** Cures status conditions only, does not restore HP.

# IV. Core Principles & Methodology
- **Agent-First Approach:** Before attempting any manual solution for a complex problem (puzzles, multi-step navigation, difficult battles), I MUST consult the relevant specialist agent first.
- **Scientific Method:** Use a scientific approach: form a hypothesis, test it, and document the conclusion. Do not modify tools to test hypotheses; test them with in-game actions first.
- **Trust System Feedback:** System feedback (like validation warnings or tool errors) is the source of truth and MUST be trusted over personal assumptions or agent outputs.
- **IMMEDIATE ACTION:** Flaws in tools or data management (notepad, markers) must be addressed immediately, not deferred as goals.

# V. Solved Puzzles & Discarded Hypotheses

## A. Solved Puzzles & Verified Mechanics
- **Victory Road 3F (Boulder Puzzle):** Solved by maneuvering the boulder from (7, 2) to the switch at (4, 6).
- **Victory Road 2F (Western Boulder):** Solved. The system has confirmed the barrier corresponding to the switch at (2, 17) is already cleared.
- **Victory Road 2F (Puzzle Resets):** Confirmed that using ladders between floors does NOT reset a puzzle.

## B. Discarded Hypotheses
- **Victory Road 3F (Failed Plan):** The initial strategy from the `puzzle_strategist_agent` to push a boulder along the y=2 corridor was a hallucination. The path was blocked by impassable tiles at (5, 2) and (6, 2).
- **Victory Road 2F (Agent Failure - Turn 120163):** The `puzzle_strategist_agent`'s plan to use the southern boulder at (8, 15) failed. The agent's proposed path to push the boulder to (9, 16) was blocked by an impassable tile at (9, 16). This confirms the agent can hallucinate invalid paths. The boulder is now trapped at (8, 16).

# VI. Unsolved Puzzles (Inactive)
- **Victory Road 2F (Eastern Boulder Puzzle):** Appears unsolvable with the southern boulder. The northern boulder at (6,6) is the only remaining option, but is currently inaccessible due to impassable objects.

# VII. Agent & Tool Development Notes
## A. Agent Notes
- **pathfinder_debugger_agent:** Used to diagnose failures in `gem_pathfinder_v2`. Requires the tool's source code and a verbose log as input.

## B. Tool Notes
- **gem_pathfinder_v2:** **Under Repair.** Critical bug where destination tiles are incorrectly flagged as impassable. `pathfinder_debugger_agent` diagnosed the issue (logical conflict between `find_path` and `is_traversable`) and suggested a fix. Currently attempting to implement this fix.

# VIII. Lessons Learned & Heuristics
- **Verify 'Trapped' Scenarios:** If a pathfinder tool reports 'No path found' and I believe I am trapped, I must not accept this conclusion without verification. I need to manually inspect the map for alternative routes and trust the game state's list of reachable warps over my own assumptions.
- **Boulders cannot be pushed up `steps` tiles:** This was tested and confirmed on Victory Road 2F.

# IX. Strategic Reassessment (Post-Reflection)
- **Conclusion:** My repeated attempts to solve the eastern boulder puzzle on Victory Road 2F have failed due to a high random encounter rate and critically low party health. My assumption that I could safely traverse the map was incorrect.
- **New Directive:** The immediate priority is no longer the puzzle, but the survival and recovery of my party. I must retreat from Victory Road and heal at the Indigo Plateau Pokémon Center. Only then can I return to address the system's puzzle directive with a viable team.