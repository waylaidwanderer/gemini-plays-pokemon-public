# Gem's Strategic Journal

## I. Core Principles & Lessons Learned
- **Progression over Perfection:** The main goal is to move forward. Don't get bogged down by optional side content or dead ends. If a path requires an item I don't have (like Cut), note it and move on.
- **Hypothesize, Test, Pivot:** When stuck, form a hypothesis, test it with one or two actions, and if it fails, immediately pivot to a new hypothesis. Do not repeat failed actions.
- **Systematic Exploration (When Stuck):** If the main path is unclear, use agents like `unseen_tile_navigator_agent` to explore methodically rather than wandering randomly.
- **Mark Everything:** Diligently mark defeated trainers, used warps, key items, and especially one-way paths or traps.

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
- **`pathfinder_agent` (CRITICAL LESSON):** The agent is not inherently flawed, but its effectiveness is highly dependent on the complexity of the map. In areas with many ledges and segregated paths like southern Cerulean City, it has repeatedly failed by providing paths into one-way traps. **MANDATE: For complex, multi-turn paths in maze-like areas, do not trust the agent's output blindly. Either break the navigation into smaller, verifiable segments or switch to careful manual navigation.**
- **`battle_menu_navigator`:** Created. For efficient battle menu navigation.
- **`unseen_tile_navigator_agent`:** Reliable for overworld navigation when stuck.
- **`move_tutor_advisor`:** Created. Ready for use when a new TM is acquired.
- **`multi_map_route_planner_agent`**: Created. For planning routes across multiple maps.

## IV. Route & City Debriefs
- **Cerulean City:** The path east out of Cerulean City is a dead end that requires Cut. The correct path for story progression is south, through the burgled house at (28, 12).

## V. Pending Tasks & Hypotheses
- **Hypothesis:** The officer blocking the east exit of Cerulean City might move now that the Trashed House/Team Rocket event is resolved. I need to go back and check on him after leaving the gym.