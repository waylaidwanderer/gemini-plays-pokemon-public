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
### `pathfinder_agent` (Probationary Status)
- **CRITICAL FAILURE:** The agent is demonstrably UNRELIABLE for complex, multi-turn paths in southern Cerulean City. It has now led me into a marked one-way trap TWICE.
- **MANDATE:** DO NOT use the agent for multi-turn navigation in this area. Proceed with careful, manual navigation, breaking the journey into small, verifiable steps.

### Other Agents
- **`unseen_tile_navigator_agent`:** Reliable for overworld navigation when stuck.
- **Created, Untested:** `battle_menu_navigator`, `move_tutor_advisor`, `multi_map_route_planner_agent`.

## IV. Route & City Debriefs
- **Cerulean City:** The path east requires Cut. The correct path for story progression is south, through the burgled house at (28, 12), which is accessible after navigating the main part of the city. The southeastern yard is a trap that loops back through a small, dead-end section of the gym.

## V. Pending Tasks & Hypotheses
- **Hypothesis:** The officer blocking the east exit of Cerulean City might move now that the Trashed House/Team Rocket event is resolved. I need to go back and check on him after escaping this loop.