# Gem's Strategic Journal (v2.0)

## I. Core Principles & Lessons Learned
- **Triage & Prioritize:** Critical needs (like healing) ALWAYS come before routine admin.
- **Progression over Perfection:** The critical path is key. Don't get bogged down if the main objective is elsewhere.
- **Hypothesize, Test, Pivot:** When stuck, form a hypothesis, test it, and if it fails, immediately pivot. Do not repeat failed actions.
- **Agents vs. Player Abilities:** Agents operate on the current game state. If an agent reports a path is blocked by a removable obstacle (like a Cut-able tree), the correct action is to path *to* the obstacle, use my own ability to remove it, and *then* re-calculate the path to the final destination. An agent's "failure" in this context is a correct assessment of the map *as it is*, not a sign of being stuck.
- **Mark Everything & Use Your Markers:** Diligently mark key locations and trust the warnings you set for yourself.
- **Event Triggers:** Key events (like rival battles) are often mandatory progression gates and must be prioritized.
- **Battle Strategy (NEW):**
    - Against wild Pokémon faster than my lead, if the first attempt to run fails, it is more efficient to fight rather than repeatedly attempting to flee and taking damage.
    - Always identify and prioritize using the most powerful super-effective moves to end battles quickly. (e.g., Gust vs. Ground-types).
- **Navigation (NEW):**
    - Always verify map connectivity using the World Knowledge Graph before assuming a "shortcut" (like Diglett's Cave) leads to the desired destination. Map segments can be isolated.

## II. Game Mechanics & Battle Intel
- **Level Caps:**
    - 0 badges: 12
    - 1 badge: 21
    - 2 badges: 24
    - 3 badges: 35
- **Type Matchups (Verified):**
    - Bug: Not very effective (0.5x) vs. Fire.
    - Electric: Not very effective (0.5x) vs. Electric, Bug/Grass.
    - Fire: Super-effective (2x) vs. Bug/Poison.
    - Flying: Super-effective (2x) vs. Ground.
    - Grass: Super-effective (4x) vs. Rock/Ground.
    - Ice: Super-effective (2x) vs. Grass.
    - Psychic: Super-effective (2x) vs. Poison.
- **Status Effects:** Confusion wears off after battle. Poison-types are immune to poison.
- **EXP Distribution:** Pokémon at the level cap do not gain EXP. All non-fainted party members share EXP.
- **Field Moves & Navigation:**
    - DIG can be used to escape caves but **cannot be used in cities**.
    - STRENGTH can be used to move big rocks (NPC hint).
    - CUT: Interacting with a cuttable tree prompts the use of the move.
- **Respawning Obstacles:** Cuttable trees respawn after changing maps.

## III. Puzzle Mechanics & Solutions
- **Vermilion Gym Puzzle:**
    - The goal is to find two switches hidden in trash cans.
    - After finding the first switch, the second is **always in an adjacent can**.
    - **CRITICAL:** If you check a non-adjacent can OR the wrong adjacent can after finding the first switch, the **entire puzzle resets**.

## IV. Agent Log & Action Plan
| Agent Name                     | Status     | Action Item                                                                 |
|--------------------------------|------------|-----------------------------------------------------------------------------|
| `pathfinder_agent`             | ✅ Reliable | Confirmed reliable. My previous issues were user error, not agent failure.  |
| `unseen_tile_navigator_agent`  | ✅ Reliable | Use for systematic exploration of unseen tiles.                             |
| `battle_menu_navigator`        | ✅ Reliable | Use for all complex menu navigation in battles.                               |
| `tm_tutor_agent`               | ✅ Reliable | Use for TM/HM decisions.                                                    |
| `progression_advisor_agent`    | ✅ Reliable | Use proactively when entering new areas to confirm objectives.              |
| `pokemon_training_advisor_agent`| ❓ Untested | Use before major battles to formulate training plans.                       |
| `multi_map_route_planner_agent`| ❓ Untested | Test when planning a multi-map journey.                                     |
| `rival_battle_strategist_agent`| ❓ Untested | **Create & use BEFORE next rival battle.** Proactive planning is more effective. |

## V. Actionable Intelligence & Objectives (From old hypotheses)
- **Objective: Acquire Drink for Saffron Guard.** A thirsty guard blocks the path to Saffron City. A drink item, likely from the Celadon Dept. Store, is probably required.
- **Objective: Investigate Underground Path Lost Item.** An NPC mentioned people lose things in the Underground Path (Route 5-6). This could be a hidden item. I should explore it thoroughly when passing through.
- **Objective: Investigate Vermilion Machop.** A Machoke in Vermilion City mentioned building something. This could be a side quest. I will talk to the NPC again after making more progress.

## VI. Discoveries & Points of Interest
- **TMs Found:** TM08 (BODYSLAM), TM24 (THUNDERBOLT).
- **Key Items Found:** GOOD ROD, HM01 (CUT).
- **Lt. Surge's Raichu (Lv. 29):** Knows Body Slam and Surf.