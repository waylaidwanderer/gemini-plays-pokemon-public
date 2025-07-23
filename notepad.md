# Gem's Pokémon Crystal Adventure Log

## Current Plan & Strategy
1.  **Objective:** My primary goal is to find Mr. Pokémon.
2.  **Strategic Pivot:** My exploration of Route 46 has confirmed it is a one-way path from a later area and not a viable route to Mr. Pokémon's house. My previous hypothesis was incorrect.
3.  **New Path:** I am now backtracking from Route 46 to return to Route 30. The path to Mr. Pokémon must be through the battling trainers on Route 30, or there is another trigger I have missed.
4.  **Tool Deletion:** My custom navigation tools (`find_path`, `find_reachable_unseen_tiles`) were fundamentally flawed. I have deleted them to prevent further wasted turns. I will rely on manual navigation until I can build a reliable tool.

## Guiding Principle: Immediate Action
As an LLM, I have no concept of 'later'. Any task I identify, especially tool maintenance or data management, must be performed in the current turn. Deferring actions is a critical failure.

## Key NPCs and Locations
*   **Professor Elm:** Gave me my starter, Vulcan. Wants me to find Mr. Pokémon.
*   **Mr. Pokémon:** Lives somewhere north of Cherrygrove City, likely past the battling trainers on Route 30.
*   **GRAMPS (Guide Gent):** Gave me a tour of Cherrygrove and the MAP CARD.

## Game Mechanics & Systems
*   **Held Items:** Pokémon can hold items (like a BERRY) and use them automatically in battle to restore HP.

## Battle and Pokemon Information
*   **Party Composition:**
    *   Vulcan (Cyndaquil), Lv. 8. Moves: TACKLE, LEER, SMOKESCREEN.
*   **Type Matchups Observed:**
    *   Normal (Tackle) is "not very effective" against Rock/Ground (Geodude).

## Tile Traversal Rules (Systematic Testing)
*Method: To confirm a tile's properties, I must attempt to move onto it from all four adjacent, traversable tiles (Up, Down, Left, Right). A conclusion is only valid after all directions are tested.*

### Confirmed Mechanics:
*   **FLOOR:** Traversable.
*   **WALL:** Impassable.
*   **COUNTER:** Impassable. Interacting with NPCs behind them requires facing the counter tile.
*   **HEADBUTT_TREE:** Impassable.
*   **DOOR:** Functions as a warp.
*   **LEDGE_HOP_DOWN:** Confirmed one-way traversal. Impassable from below. Player can only move down from this tile.

### Untested Mechanics & Testing Plan:
*   **FRUIT_TREE:** Interactable (Confirmed at (5, 39) on Route 30).
*   **CUT_TREE:** Hypothesis: Impassable without HM Cut. *Plan: Attempt to walk into it from an adjacent tile.*
*   **TALL_GRASS:** Confirmed traversable.
*   **LEDGE_HOP_LEFT:** Hypothesis: One-way traversal from right to left. *Plan: Attempt to walk onto it from the left.*
*   **WARP_CARPET_DOWN:** Appears to function as a two-way warp. *Plan: Confirm by attempting to walk back up from the destination map.*
*   **FLOOR_UP_WALL:** Encountered on Route 46. Hypothesis: A floor tile that appears visually connected to a wall above it. *Plan: Test traversability from all sides.*

## Agent Ideas (Future Development)
*   **Strategy Agent:** Could take party/opponent info and suggest battle plans.
*   **Exploration Agent:** Could prioritize navigation goals based on a list of unseen tiles and primary objectives.
*   **Pathfinding Tool:** A new, robust pathfinding tool is a high priority for future development. It must correctly handle all ledge types.