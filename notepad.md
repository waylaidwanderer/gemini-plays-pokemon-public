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
    - CUT: Interacting with a cuttable tree prompts the use of the move. Using the HM from the item bag is only a shortcut to the teaching menu.
    - **Dead End Definition:** An area is a 'dead end' ONLY if there is one reachable exit path. An area with two or more exits is a thoroughfare.

## III. Agent Log & Action Plan
| Agent Name                     | Status     | Action Item                                                                 |
|--------------------------------|------------|-----------------------------------------------------------------------------|
| `pathfinder_agent`             | ✅ Reliable | Use for complex navigation. Avoid for simple, straight-line paths.          |
| `unseen_tile_navigator_agent`  | ✅ Reliable | Use for systematic exploration of unseen tiles.                             |
| `battle_menu_navigator`        | ✅ Reliable | Use for all complex menu navigation in battles.                               |
| `tm_tutor_agent`               | ✅ Reliable | Use for TM/HM decisions.                                                    |
| `pokemon_training_advisor_agent`| ❓ Untested | **Use IMMEDIATELY.** Formulate training plan for Route 11.                   |
| `ship_explorer_agent`          | ❓ Untested | Test when I return to the S.S. Anne to find the Captain.                      |
| `multi_map_route_planner_agent`| ❓ Untested | Test when planning a multi-map journey.                                     |
| `progression_advisor_agent`    | ❓ Untested | Use when unsure about the next major story objective.                         |
| `rival_battle_strategist_agent`| ❓ Untested | **Create & use BEFORE next rival battle.** Proactive planning is more effective. |

## IV. Operation: Sea Sick for Cut
- **Objective:** Obtain HM01 (Cut) from the S.S. Anne Captain. The Vermilion Gym is inaccessible without it.
- **Obstacle:** Rival Pixel is blocking the path to the Captain's quarters on the S.S. Anne. He must be defeated.
- **Status:** Team is healed. Ready to board the S.S. Anne and begin training/exploration.
- **Training Plan:**
    - **Location:** Trainers aboard the S.S. Anne will be the primary source of EXP.
    - **Target Level:** 24 for all active party members before facing Pixel.
- **Battle Plan (vs. Pixel on S.S. Anne):**
    - **Team:** SPARKY (Lv24), CRAG (Lv24), NIGHTSHADE (Lv24), ECHO (Lv24), SUBTERRA (Lv24), PULSAR (Lv24).
    - **Strategy:** Lead with SPARKY vs. Pidgeotto. Use SUBTERRA as a hard counter for Jolteon. CRAG walls Pidgeotto/Raticate. Evolved ECHO (Golbat) handles Kadabra. This plan will be refined with `rival_battle_strategist_agent` after training is complete.

## V. Discoveries & Points of Interest
- **Underground Path (Route 5 to 6):** An NPC mentioned that people often lose things here. Could be a hint for a hidden item.
- **Vermilion City:** The building at (10,14) is the Pokémon Fan Club.
- **TMs Found:**
  - TM08 (BODYSLAM): Found in cabin (map_id: 102, (13,16)).
- **Key Items Found:**
  - GOOD ROD: Received from Fishing Guru's brother in Vermilion City (map_id: 163, (3,5)).

- **Hypothesis:** Stun Spore may not work on Poison-type Pokémon in this ROM hack. Need to test this on another Poison-type to verify if it's a mechanic or just a miss.

## VI. System Mechanics & Quirks
- **Input Restriction:** The system does NOT allow mixing directional buttons (Up, Down, Left, Right) and action buttons (A, B) in the same `buttons_to_press` array for a single turn. This contradicts AI critiques about 'batching commands.' The system warning is the source of truth. Battle menu navigation must be done one *type* of button press per turn (e.g., all directional presses in one turn, all action presses in another).

- **Lt. Surge's Ace:** The Gym Guide warned that Lt. Surge's single Pokémon is extremely powerful and knows a strong water technique. This poses a significant threat to Ground-types like SUBTERRA.