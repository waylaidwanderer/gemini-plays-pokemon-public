# Gem's Strategic Journal

## I. Core Principles & Lessons Learned
- **Progression over Perfection:** The main goal is to move forward. If a path is blocked, note it and find another way. Prioritize main thoroughfares and staircases over exhaustive side-room clearing.
- **Hypothesize, Test, Pivot:** When stuck, form a hypothesis, test it, and if it fails, immediately pivot. Do not repeat failed actions.
- **Trust the Game State & Agents:** The game data and agent outputs are the source of truth. A `path_found: false` result is a critical and accurate indicator that the target is in an unreachable map segment, not that the agent failed.
- **Mark Everything & Use Your Markers:** Diligently mark key locations, and more importantly, *trust* the warnings you set for yourself.
- **Event Triggers:** Some key events (like the rival battle on the S.S. Anne) are mandatory progression gates and must be prioritized.

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
    - **Unseen Tile Navigation:** To explore an unseen tile, you must navigate to a *traversable adjacent tile*, not the unseen tile itself. The `unseen_tile_navigator_agent` handles this automatically.

## III. Agent Log & Testing Plan
- **Reliable Agents:**
    - `pathfinder_agent`: Returns the shortest path to a single coordinate.
    - `unseen_tile_navigator_agent`: Calculates the shortest path to the nearest 'Reachable Unseen Tile'.
    - `battle_menu_navigator`: Calculates the precise button sequence to navigate battle menus.
- **Agents to Test ASAP:**
    - `ship_explorer_agent`: Refined prompt to prioritize ascending paths. **Action Item: Test on S.S. Anne to find the path to the rival/captain.**
    - `tm_tutor_agent`: Untested. **Action Item: Use to decide who learns TM08 (BODYSLAM) or another TM at the next opportunity.**
    - `multi_map_route_planner_agent`: Untested.

## IV. Progression Log & Current Plans
- **S.S. Anne Strategy:**
  - **Priority 1: Find and defeat Rival Pixel.** The rival battle is a mandatory event blocking access to the Captain. It likely occurs on an upper floor hallway.
  - **Priority 2: Find the Captain.** He is sick and in his cabin. Obtaining HM01 (Cut) from him is the main objective.
  - The ship will be departing soon, adding urgency. The critical path is ascending the main staircases.
- **Underground Path (Route 5 to 6):** An NPC mentioned that people often lose things here. Could be a hint for a hidden item.
- **Vermilion City:** The building at (10,14) is the Pokémon Fan Club.

## V. Item Log
- **TMs Found:**
  - TM08 (BODYSLAM): Found in cabin (map_id: 102, (13,16)).
- **Key Items Found:**
  - GOOD ROD: Received from Fishing Guru's brother in Vermilion City (map_id: 163, (3,5)).