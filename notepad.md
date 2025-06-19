# Gem's Strategic Journal

## I. Core Principles & Lessons Learned
- **Progression over Perfection:** Prioritize main thoroughfares and staircases. The critical path is key.
- **Hypothesize, Test, Pivot:** When stuck, form a hypothesis, test it, and if it fails, immediately pivot. Do not repeat failed actions.
- **Trust the Game State & Agents:** The game data and agent outputs are the source of truth.
- **Mark Everything & Use Your Markers:** Diligently mark key locations and trust the warnings you set for yourself.
- **Event Triggers:** Key events (like the rival battle) are mandatory progression gates and must be prioritized.

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

## III. Agent Log & Action Plan
| Agent Name                     | Status     | Action Item                                                                 |
|--------------------------------|------------|-----------------------------------------------------------------------------|
| `pathfinder_agent`             | ✅ Reliable | Use for direct navigation to a known coordinate.                              |
| `unseen_tile_navigator_agent`  | ✅ Reliable | Use for systematic exploration of unseen tiles.                             |
| `battle_menu_navigator`        | ✅ Reliable | Use for all complex menu navigation in battles.                               |
| `ship_explorer_agent`          | ❓ Untested | **IMMEDIATE PRIORITY:** Test after this battle to find the Captain.         |
| `tm_tutor_agent`               | ❓ Untested | **IMMEDIATE PRIORITY:** Use after this battle to decide who learns TM08.    |
| `multi_map_route_planner_agent`| ❓ Untested | Test when planning a multi-map journey.                                     |

## IV. Progression Log & Current Plans
- **S.S. Anne Strategy:**
  - **Priority 1: Defeat Rival Pixel.** This battle is a mandatory event blocking access to the Captain.
  - **Priority 2: Find the Captain.** He is sick and in his cabin. Obtaining HM01 (Cut) from him is the main objective.
  - The ship is departing soon, adding urgency.
- **Current Battle Plan (vs. Rival Pixel):**
  - **Opponent:** Raticate (Lv20)
  - **Active Pokémon:** Sparky (Lv24)
  - **Strategy:** Use THUNDERPUNCH for maximum damage.
- **Underground Path (Route 5 to 6):** An NPC mentioned that people often lose things here. Could be a hint for a hidden item.
- **Vermilion City:** The building at (10,14) is the Pokémon Fan Club.

## V. Item Log
- **TMs Found:**
  - TM08 (BODYSLAM): Found in cabin (map_id: 102, (13,16)).
- **Key Items Found:**
  - GOOD ROD: Received from Fishing Guru's brother in Vermilion City (map_id: 163, (3,5)).