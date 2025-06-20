# Gem's Strategic Journal

## I. Core Principles & Lessons Learned
- **Triage & Prioritize:** Critical needs (like healing) ALWAYS come before routine admin.
- **Progression over Perfection:** The critical path is key. Don't get bogged down if the main objective is elsewhere.
- **Hypothesize, Test, Pivot:** When stuck, form a hypothesis, test it, and if it fails, immediately pivot. Do not repeat failed actions.
- **Agents vs. Player Abilities:** Agents operate on the current game state. If an agent reports a path is blocked by a removable obstacle (like a Cut-able tree), the correct action is to path *to* the obstacle, use my own ability to remove it, and *then* re-calculate the path to the final destination. An agent's "failure" in this context is a correct assessment of the map *as it is*, not a sign of being stuck.
- **Mark Everything & Use Your Markers:** Diligently mark key locations and trust the warnings you set for yourself.
- **Event Triggers:** Key events (like rival battles) are often mandatory progression gates and must be prioritized.

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
    - Grass: Super-effective (4x) vs. Rock/Ground.
    - Ice: Super-effective (2x) vs. Grass.
    - Psychic: Super-effective (2x) vs. Poison.
- **Status Effects:** Confusion wears off after battle. Poison-types are immune to poison.
- **EXP Distribution:** Pokémon at the level cap do not gain EXP. All non-fainted party members share EXP.
- **Field Moves & Navigation:**
    - DIG can be used to escape caves but **cannot be used in cities**.
    - STRENGTH can be used to move big rocks (NPC hint).
    - CUT: Interacting with a cuttable tree prompts the use of the move. The HM item in the bag is a shortcut, not a direct activation.
- **Battle Tactics:**
    - **Running from Battle:** If the first attempt to run from a wild Pokémon fails (likely due to lower Speed), it is more efficient to fight rather than repeatedly attempting to flee and taking damage.
- **Respawning Obstacles:** Cuttable trees respawn after changing maps (e.g., entering/leaving a building).

## III. Puzzle Mechanics & Solutions
- **Vermilion Gym Puzzle:**
    - The goal is to find two switches hidden in trash cans.
    - After finding the first switch, the second is **always in an adjacent can** (Up, Down, Left, or Right).
    - **CRITICAL:** If you check a non-adjacent can OR the wrong adjacent can after finding the first switch, the **entire puzzle resets**, and the location of the first switch is randomized again.

## IV. Agent Log & Action Plan
| Agent Name                     | Status     | Action Item                                                                 |
|--------------------------------|------------|-----------------------------------------------------------------------------|
| `pathfinder_agent`             | ✅ Reliable | Confirmed reliable. My previous issues were user error, not agent failure.  |
| `unseen_tile_navigator_agent`  | ✅ Reliable | Use for systematic exploration of unseen tiles.                             |
| `battle_menu_navigator`        | ✅ Reliable | Use for all complex menu navigation in battles.                               |
| `tm_tutor_agent`               | ✅ Reliable | Use for TM/HM decisions.                                                    |
| `pokemon_training_advisor_agent`| ❓ Untested | Use before major battles to formulate training plans.                       |
| `multi_map_route_planner_agent`| ❓ Untested | Test when planning a multi-map journey.                                     |
| `progression_advisor_agent`    | ❓ Untested | Use after getting Flash to confirm next steps.                              |
| `rival_battle_strategist_agent`| ❓ Untested | **Create & use BEFORE next rival battle.** Proactive planning is more effective. |
| `pokemon_locator_agent`        | ❓ Untested | Newly created. Test when needed.                                            |

## V. Current & Completed Operations
- **Operation: Thunder Badge (Complete)**
    - **Result:** Success. Defeated Lt. Surge and earned the Thunder Badge.
- **Operation: Sea Sick for Cut (Complete)**
    - **Result:** Success. Defeated Rival Pixel and obtained HM01 from the Captain.

## VI. Discoveries & Points of Interest
- **Underground Path (Route 5 to 6):** An NPC mentioned that people often lose things here. Could be a hint for a hidden item.
- **TMs Found:** TM08 (BODYSLAM) in S.S. Anne cabin.
- **Key Items Found:** GOOD ROD from Fishing Guru's brother.
- **TMs Found:** TM24 (THUNDERBOLT) from Lt. Surge.
- **Lt. Surge's Raichu (Lv. 29):** Knows Body Slam and Surf. Extremely dangerous physical and special coverage.

## VII. Unverified Assumptions & Hypotheses
- **Flash Requirement:** Assumed to be necessary for Rock Tunnel, but this has not been confirmed in-game. The AI walkthrough supports this.
- **Aide with Flash location:** Assumed to be on Route 2 in an area accessible with Cut.
- **Pokémon caught for Flash:** I assume my 20 caught Pokémon are sufficient to receive HM05.
- **Rock Tunnel Progression:** Assumed to be the only path forward. The thirsty guard on Route 5 might be passable another way.
- **Vermilion Machop:** Assumed to be flavor text, but could be a side quest trigger.
- **Thirsty Guard Item:** Assumed to be from Celadon City, but could be available elsewhere sooner.