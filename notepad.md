# Gem's Strategic Journal

## I. Core Principles & Lessons Learned
- **Triage & Prioritize:** Critical needs (like healing a near-fainted party) ALWAYS come before routine admin.
- **Progression over Perfection:** The critical path is key. Don't get bogged down if the main objective is elsewhere.
- **Hypothesize, Test, Pivot:** When stuck, form a hypothesis, test it, and if it fails, immediately pivot. Do not repeat failed actions.
- **Trust the Game State & Agents:** The game data and agent outputs are the source of truth.
- **Mark Everything & Use Your Markers:** Diligently mark key locations and trust the warnings you set for yourself.
- **Event Triggers:** Key events (like rival battles) are often mandatory progression gates and must be prioritized.
- **Strategic Triage:** For simple, non-recurring tasks, manual execution is more efficient than prolonged, in-the-moment agent debugging. Note the failure and refine the agent later.

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
    - CUT: Interacting with a cuttable tree prompts the use of the move. The HM item in the bag is a shortcut to the Pokémon selection screen, not a direct activation.
- **Dead End Definition:** An area is a 'dead end' ONLY if there is one reachable exit path. An area with two or more exits is a thoroughfare.

## III. Agent Log & Action Plan
| Agent Name                     | Status     | Action Item                                                                 |
|--------------------------------|------------|-----------------------------------------------------------------------------|
| `pathfinder_agent`             | ✅ Reliable | Confirmed reliable. Agent correctly identified an unreachable target. My previous assumption was incorrect. |
| `gym_puzzle_solver_agent`      | ✅ Reliable | Use for systematic puzzle solving.                             |
| `unseen_tile_navigator_agent`  | ✅ Reliable | Use for systematic exploration of unseen tiles.                             |
| `battle_menu_navigator`        | ✅ Reliable | Use for all complex menu navigation in battles.                               |
| `tm_tutor_agent`               | ✅ Reliable | Use for TM/HM decisions.                                                    |
| `pokemon_training_advisor_agent`| ❓ Untested | Use before major battles to formulate training plans.                       |
| `ship_explorer_agent`          | ❓ Untested | Test if I ever need to explore a large, multi-floor area again.             |
| `multi_map_route_planner_agent`| ❓ Untested | Test when planning a multi-map journey.                                     |
| `progression_advisor_agent`    | ❓ Untested | Use when unsure about the next major story objective.                         |
| `rival_battle_strategist_agent`| ❓ Untested | **Create & use BEFORE next rival battle.** Proactive planning is more effective. |

## IV. Current Operation
- **Operation: Thunder Badge**
    - **Objective:** Defeat Lt. Surge and earn the Thunder Badge.
    - **Obstacle:** The gym has an electric barrier puzzle that must be solved by finding two switches hidden in trash cans.
    - **Status:** Puzzle-solving in progress. Party is injured, retreating to heal.
    - **Intel:** Lt. Surge uses a single, extremely powerful Pokémon that knows a strong Water-type move. The level cap is 24.

## V. Completed Operations
- **Operation: Sea Sick for Cut**
    - **Objective:** Obtain HM01 (Cut) from the S.S. Anne Captain.
    - **Result:** Success. Defeated Rival Pixel and obtained HM01 from the Captain.

## VI. Discoveries & Points of Interest
- **Underground Path (Route 5 to 6):** An NPC mentioned that people often lose things here. Could be a hint for a hidden item.
- **Vermilion City:** The building at (10,14) is the Pokémon Fan Club.
- **TMs Found:**
  - TM08 (BODYSLAM): Found in cabin (map_id: 102, (13,16)).
- **Key Items Found:**
  - GOOD ROD: Received from Fishing Guru's brother in Vermilion City (map_id: 163, (3,5)).
- **Hypothesis:** Stun Spore may not work on Poison-type Pokémon in this ROM hack. Need to test this on another Poison-type to verify if it's a mechanic or just a miss.

## VII. System Mechanics & Quirks
- **Input Restriction:** The system does NOT allow mixing directional buttons (Up, Down, Left, Right) and action buttons (A, B) in the same `buttons_to_press` array for a single turn. Battle menu navigation must be done one *type* of button press per turn (e.g., all directional presses in one turn, all action presses in another).

- **Respawning Obstacles:** Cuttable trees respawn after changing maps (e.g., entering/leaving a building).

- **Pathfinder Agent Post-Mortem:** The agent was correct all along. My repeated attempts to path to a tile *behind* an impassable obstacle (the respawned tree) were the source of the 'path not found' errors. This was a critical user error, not a tool failure. Lesson: Always verify the target tile is reachable *before* pathing, and trust the agent's negative results as valid information about the game state.