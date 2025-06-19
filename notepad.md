# Gem's Strategic Journal

## I. Core Principles & Lessons Learned
- **Progression over Perfection:** The critical path is key. Don't get bogged down in side rooms if the main objective is elsewhere.
- **Hypothesize, Test, Pivot:** When stuck, form a hypothesis, test it, and if it fails, immediately pivot. Do not repeat failed actions.
- **Trust the Game State & Agents:** The game data and agent outputs are the source of truth.
- **Mark Everything & Use Your Markers:** Diligently mark key locations and trust the warnings you set for yourself.
- **Event Triggers:** Key events (like the rival battle) are mandatory progression gates and must be prioritized.
- **Strategic Triage:** For simple, non-recurring tasks, manual execution is more efficient than prolonged, in-the-moment agent debugging. Note the failure and refine the agent later.

## II. Game Mechanics & Battle Intel
- **Type Matchups (Verified):**
    - **Bug:** Not very effective (0.5x) vs. Fire (Charmander).
    - **Electric:** Not very effective (0.5x) vs. Electric, Bug/Grass (Paras).
    - **Fire:** Super-effective (2x) vs. Bug/Poison (Venonat).
    - **Grass:** Super-effective (4x) vs. Rock/Ground.
    - **Ice:** Super-effective (2x) vs. Grass.
    - **Psychic:** Super-effective (2x) vs. Poison (Zubat).
- **Status Effects:** Confusion wears off after battle. Poison-types are immune to poison.
- **EXP Distribution:** Pokémon at the level cap do not gain EXP. All non-fainted party members share EXP.
- **Field Moves & Navigation:**
    - DIG can be used to escape caves but **cannot be used in cities**.
    - STRENGTH can be used to move big rocks (NPC hint).
    - **Dead End Definition:** An area is a 'dead end' ONLY if there is one reachable exit path (a single warp/warp group or map connection). An area with two or more exits is a thoroughfare.

## III. Agent Log & Action Plan
| Agent Name                     | Status     | Action Item                                                                 |
|--------------------------------|------------|-----------------------------------------------------------------------------|
| `pathfinder_agent`             | ✅ Reliable | Use for direct navigation to a known coordinate.                              |
| `unseen_tile_navigator_agent`  | ✅ Reliable | Use for systematic exploration of unseen tiles.                             |
| `battle_menu_navigator`        | ✅ Reliable | Use for all complex menu navigation in battles.                               |
| `tm_tutor_agent`               | ✅ Reliable | Use for TM/HM decisions.                                                    |
| `ship_explorer_agent`          | ❓ Untested | Test when I return to the S.S. Anne to find the Captain.                      |
| `multi_map_route_planner_agent`| ❓ Untested | Test when planning a multi-map journey.                                     |
| `progression_advisor_agent`    | ❓ Untested | Use when unsure about the next major story objective.                         |
| `menu_master_agent`            | ⚠️ Flawed   | **Refine Later.** Needs better context handling and sub-menu logic.           |
| `rival_battle_strategist_agent`| ❓ Untested | **Use after training.** Formulate a plan for the Pixel rematch.               |

## IV. Progression Log & Current Plans
- **Operation: Rematch Revenge (vs. Rival Pixel)**
  - **Objective:** Defeat Rival Pixel on the S.S. Anne to get to the Captain and obtain HM01 (Cut).
  - **Urgency:** The ship is departing soon.
  - **Recommended Team:** SPARKY (Lv24), CRAG (Lv23), NIGHTSHADE (Lv22), ECHO (Lv23), a new Diglett (Lv23), PULSAR (Lv23).
  - **Current Status:** Team acquired. Immediate priority is healing the party, then training CRAG, ECHO, and SUBTERRA to Lv. 23.
  - **Strategy:** Lead with SPARKY vs. Pidgeotto. Use Diglett as a hard counter for Jolteon. CRAG walls Pidgeotto/Raticate. Evolved ECHO (Golbat) handles Kadabra.
- **Underground Path (Route 5 to 6):** An NPC mentioned that people often lose things here. Could be a hint for a hidden item.
- **Vermilion City:** The building at (10,14) is the Pokémon Fan Club.

## V. Item Log
- **TMs Found:**
  - TM08 (BODYSLAM): Found in cabin (map_id: 102, (13,16)).
- **Key Items Found:**
  - GOOD ROD: Received from Fishing Guru's brother in Vermilion City (map_id: 163, (3,5)).