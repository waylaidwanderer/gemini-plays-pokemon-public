# Gem's Strategic Journal

## I. Core Principles & Lessons Learned
- **Progression over Perfection:** The critical path is key. Don't get bogged down if the main objective is elsewhere.
- **Hypothesize, Test, Pivot:** When stuck, form a hypothesis, test it, and if it fails, immediately pivot. Do not repeat failed actions.
- **Trust the Game State & Agents:** The game data and agent outputs are the source of truth.
- **Mark Everything & Use Your Markers:** Diligently mark key locations and trust the warnings you set for yourself.
- **Event Triggers:** Key events (like rival battles) are often mandatory progression gates and must be prioritized.
- **Strategic Triage:** For simple, non-recurring tasks, manual execution is more efficient than prolonged, in-the-moment agent debugging. Note the failure and refine the agent later.

## II. Game Mechanics & Battle Intel
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
    - CUT can be used by a fainted Pokémon (NPC hint).
    - **Dead End Definition:** An area is a 'dead end' ONLY if there is one reachable exit path. An area with two or more exits is a thoroughfare.

## III. Agent Log & Action Plan
| Agent Name                     | Status     | Action Item                                                                 |
|--------------------------------|------------|-----------------------------------------------------------------------------|
| `pathfinder_agent`             | ✅ Reliable | Use for direct navigation to a known coordinate.                              |
| `unseen_tile_navigator_agent`  | ✅ Reliable | Use for systematic exploration of unseen tiles.                             |
| `battle_menu_navigator`        | ✅ Reliable | Use for all complex menu navigation in battles.                               |
| `tm_tutor_agent`               | ✅ Reliable | Use for TM/HM decisions.                                                    |
| `pokemon_training_advisor_agent`| ✅ Reliable | Use to find optimal training spots before major battles.                       |
| `ship_explorer_agent`          | ❓ Untested | Test when I return to the S.S. Anne to find the Captain.                      |
| `multi_map_route_planner_agent`| ❓ Untested | Test when planning a multi-map journey.                                     |
| `progression_advisor_agent`    | ❓ Untested | Use when unsure about the next major story objective.                         |
| `rival_battle_strategist_agent`| ❓ Untested | **Use after training.** Formulate a plan for the Pixel rematch.               |
| `pokemon_training_advisor_agent`| ❓ Untested | Use to find optimal training spots before major battles.                       |

## IV. Current Objective: Operation Rematch Revenge (vs. Rival Pixel)
- **Primary Goal:** Heal my party at the Vermilion City Pokémon Center.
- **Secondary Goal:** Defeat Rival Pixel on the S.S. Anne to obtain HM01 (Cut).
- **Tertiary Goal:** Explore the eastern part of Route 11 after healing.
- **Status:** Team acquired. Immediate priority is healing, then training the team to Lv. 23-24.
- **Strategy:**
    - **Team:** SPARKY (Lv24), CRAG (Lv23), NIGHTSHADE (Lv22), ECHO (Lv23), SUBTERRA (Lv23), PULSAR (Lv23).
    - **Plan:** Lead with SPARKY vs. Pidgeotto. Use SUBTERRA as a hard counter for Jolteon. CRAG walls Pidgeotto/Raticate. Evolved ECHO (Golbat) handles Kadabra.

## V. Discoveries & Points of Interest
- **Underground Path (Route 5 to 6):** An NPC mentioned that people often lose things here. Could be a hint for a hidden item.
- **Vermilion City:** The building at (10,14) is the Pokémon Fan Club.
- **TMs Found:**
  - TM08 (BODYSLAM): Found in cabin (map_id: 102, (13,16)).
- **Key Items Found:**
  - GOOD ROD: Received from Fishing Guru's brother in Vermilion City (map_id: 163, (3,5)).