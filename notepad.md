# Gem's Strategic Journal

## I. Core Principles & Lessons Learned
- **Progression over Perfection:** The main goal is to move forward. If a path is blocked, note it and find another way.
- **Hypothesize, Test, Pivot:** When stuck, form a hypothesis, test it, and if it fails, immediately pivot. Do not repeat failed actions.
- **Trust the Game State:** The game data (map connections, reachability) is the source of truth. My spatial reasoning can be flawed.
- **Mark Everything & Use Your Markers:** Diligently mark key locations, and more importantly, *trust* the warnings you set for yourself.

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
    - DIG can be used to escape caves but **cannot be used in cities**.

## III. Agent Log
### `pathfinder_agent` (Status: Reliable)
- **LESSON LEARNED:** The agent's `path_found: false` responses in Cerulean City were correct. They accurately indicated that my target was in an isolated map segment unreachable from my position. This is not an agent failure, but critical map information.
- **MANDATE:** Trust agent pathfinding results. If a path is not found, re-evaluate the map for alternative routes (warps, other map connections) instead of assuming the agent is wrong.

### Other Agents
- **`unseen_tile_navigator_agent`:** Reliable for overworld navigation when stuck.
- **Created, Untested:** `battle_menu_navigator`, `move_tutor_advisor`, `multi_map_route_planner_agent`.

## IV. Route & City Debriefs
- **Cerulean City:** The path east requires Cut. The correct path for story progression is south, through the burgled house at (28, 12), which is accessible after navigating the main part of the city. The southeastern yard is a trap that loops back through a small, dead-end section of the gym.

## V. Pending Tasks & Hypotheses
- **Hypothesis:** The officer blocking the east exit of Cerulean City might move now that the Trashed House/Team Rocket event is resolved. I need to go back and check on him after escaping this loop.

## VI. Traps & One-Way Paths
- **Cerulean City Ledge Trap:** Jumping down the ledges at (23, 18) and (24, 18) traps you in the western segment of the city. To escape, you must exit the city (e.g., north to Route 24) and re-enter.