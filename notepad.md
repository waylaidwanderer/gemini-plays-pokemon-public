# Gem's Strategic Journal

## I. Core Principles & Lessons Learned
- **Progression over Perfection:** The main goal is to move forward. Don't get bogged down by optional side content or dead ends. If a path requires an item I don't have (like Cut), note it and move on.
- **Hypothesize, Test, Pivot:** When stuck, form a hypothesis, test it with one or two actions, and if it fails, immediately pivot to a new hypothesis. Do not repeat failed actions.
- **Systematic Exploration (When Stuck):** If the main path is unclear, use agents like `unseen_tile_navigator_agent` to explore methodically rather than wandering randomly.
- **Mark Everything:** Diligently mark defeated trainers, used warps, key items, and especially one-way paths or traps (like the Cerulean ledge).

## II. Game Mechanics & Battle Intel
- **Type Matchups (Verified):**
    - Grass is 4x effective vs. Rock/Ground.
    - Electric is not very effective vs. Electric or Bug/Grass (Paras).
    - Ice is super-effective vs. Grass.
- **Status Effects:**
    - Confusion wears off after battle.
    - Poison-types are immune to poison.
- **EXP Distribution:**
    - Pokémon at the level cap do not gain EXP.
    - All non-fainted party members share EXP.
- **Field Moves:**
    - DIG can be used to escape caves and some areas to the entrance of the last-used Pokémon Center, but **cannot be used in cities**.

## III. Agent Log
- **`pathfinder_agent`:** Highly unreliable for complex maps with ledges. Has been refined multiple times. Must be tested on simple paths before being trusted for critical navigation.
- **`battle_menu_navigator`:** Created. For efficient battle menu navigation.
- **`unseen_tile_navigator_agent`:** Reliable for overworld navigation when stuck.
- **`move_tutor_advisor`:** Created. Ready for use when a new TM is acquired.
- **`multi_map_route_planner_agent`**: Created. For planning routes across multiple maps.

## IV. Route & City Debriefs
- **Cerulean City:** The path east out of Cerulean City is a dead end that requires Cut. The correct path for story progression is south, through the burgled house at (28, 12).

`pathfinder_agent` (Lesson Learned): The agent's failures in Cerulean City were due to my own misinterpretation of the map's complex layout, not a flaw in the agent itself. The water tiles and segregated areas created paths that seemed illogical to me but were technically correct. **Mandate: Trust agent pathing but verify by checking the map for non-obvious obstacles or routes before execution. Use manual navigation to supplement, not replace, the agent when paths seem complex.**