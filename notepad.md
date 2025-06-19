# Gem's Strategic Journal

## I. Core Principles & Lessons Learned
- **Progression over Perfection:** The main goal is to move forward. If a path is blocked, note it and find another way.
- **Hypothesize, Test, Pivot:** When stuck, form a hypothesis, test it, and if it fails, immediately pivot. Do not repeat failed actions.
- **Trust the Game State & Agents:** The game data (map connections, reachability) and agent outputs are the source of truth. A `path_found: false` result from an agent means the target is in an unreachable map segment, not that the agent failed.
- **Mark Everything & Use Your Markers:** Diligently mark key locations, and more importantly, *trust* the warnings you set for yourself.

## II. Game Mechanics & Battle Intel
- **Type Matchups (Verified):**
    - **Bug:**
        - Not very effective (0.5x) vs. Fire (Charmander).
    - **Electric:**
        - Not very effective (0.5x) vs. Electric.
        - Not very effective (0.5x) vs. Bug/Grass (Paras).
    - **Fire:**
        - Super-effective (2x) vs. Bug/Poison (Venonat).
    - **Grass:**
        - Super-effective (4x) vs. Rock/Ground.
    - **Ice:**
        - Super-effective (2x) vs. Grass.
    - **Psychic:**
        - Super-effective (2x) vs. Poison (Zubat).
- **Status Effects:**
    - Confusion wears off after battle.
    - Poison-types are immune to poison.
- **EXP Distribution:**
    - Pokémon at the level cap do not gain EXP.
    - All non-fainted party members share EXP.
- **Field Moves & Navigation:**
    - DIG can be used to escape caves but **cannot be used in cities**.
    - **Unseen Tile Navigation:** To explore an unseen tile, you must navigate to a *traversable adjacent tile*, not the unseen tile itself. The `unseen_tile_navigator_agent` handles this automatically.
- **Tool Limitations:**
    - `stun_npc` cannot be used on Pikachu (ID 15) or the player (ID 0).

## III. Agent Log
### Reliable Agents
- **`pathfinder_agent`:** Returns the shortest path to a single coordinate. A `path_found: false` response is a critical and accurate indicator that the target is in an unreachable map segment.
- **`unseen_tile_navigator_agent`:** Calculates the shortest path to the nearest 'Reachable Unseen Tile'. Essential for systematically exploring new areas.
- **`battle_menu_navigator`:** Calculates the precise button sequence to navigate battle menus. (Used 5 times, seems reliable).
### Untested Agents
- **`multi_map_route_planner_agent`**

## IV. Route & City Debriefs
### Cerulean City
- The path east (Route 9) is blocked by an officer post-Rocket event.
- The path south is through the burgled house at (28, 12), which leads to Route 5. This house contains a Rocket Grunt and a hole in the wall.
- **Ledge Trap:** Jumping down the ledges at (23, 18) and (24, 18) traps you in the western segment of the city. To escape, you must exit the city (e.g., north to Route 24) and re-enter.
- **Yard/Gym Trap:** The yard at (31,21) has a one-way entrance into the back of the Cerulean Gym. There is no exit from this part of the gym other than back into the yard, creating a loop.

### Underground Path (Route 5 to 6)
- An NPC mentioned that people often lose things in the Underground Path. This could be a hint for a hidden item.

## V. Current Tasks & Plans
- Get to Vermilion City to get HM01 Cut.
- Current path: Route 6 -> Vermilion City.
- **Reminder:** Before adding nodes/edges to the World Knowledge Graph, always check if they already exist to avoid errors.

- **Strength:** An NPC on the S.S. Anne B1F mentioned that the move STRENGTH can be used to move big rocks.