# Gem's Pokémon Crystal Adventure Log

## Current Plan
1. I have realized the battling trainers are not blocking the entire path. A clear path exists to the left of them.
2. My primary objective is to find Mr. Pokémon's house by proceeding north along this path.
3. I will continue to systematically test new tile mechanics as I encounter them.

## Key NPCs and Locations
*   **Professor Elm:** Gave me my starter, Vulcan. Wants me to find Mr. Pokémon.
*   **Mr. Pokémon:** Lives somewhere past Cherrygrove City. My main quest objective.
*   **GRAMPS (Guide Gent):** Gave me a tour of Cherrygrove and the MAP CARD.

## Game Mechanics & Systems
*   **Held Items:** Pokémon can hold items (like a BERRY) and use them automatically in battle to restore HP.

## Battle and Pokemon Information
*   **Party Composition:**
    *   Vulcan (Cyndaquil), Lv. 6. Moves: TACKLE, LEER, SMOKESCREEN.

## Tile Traversal Rules (Systematic Testing)
*Method: To confirm a tile's properties, I must attempt to move onto it from all four adjacent, traversable tiles (Up, Down, Left, Right). A conclusion is only valid after all directions are tested.*

### Confirmed Mechanics:
*   **FLOOR:** Traversable.
*   **WALL:** Impassable.
*   **COUNTER:** Impassable. Interacting with NPCs behind them requires facing the counter tile.
*   **HEADBUTT_TREE:** Impassable.
*   **DOOR:** Functions as a warp.

### Untested Mechanics & Testing Plan:
*   **FRUIT_TREE:** Interactable. Can yield items like BERRIES. (Confirmed by interacting with the tree at (5, 39) on Route 30).
*   **LEDGE_HOP_LEFT/RIGHT:** Hypothesis: One-way traversal. *Plan: Find examples and test movement from all four directions.*
*   **VOID:** Appears impassable. *Plan: Attempt to walk into it from an adjacent tile.*
*   **WATER/WATER_EDGE:** Hypothesis: Impassable without Surf. *Plan: Test by attempting to walk into it from an adjacent tile.*
*   **BOOKSHELF/RADIO/TV/WINDOW/TOWN_MAP:** Hypothesis: Impassable scenery. *Plan: Attempt to walk into them from adjacent tiles.*

## Tile Testing Protocol
To ensure a complete understanding of game mechanics, I will systematically test every new tile type encountered. For each tile, I will attempt to enter it from all four cardinal directions (where possible) and document the result. This includes tiles that appear impassable, such as scenery, to confirm they are not interactable in a non-obvious way.

### Untested Tiles & Test Plan:
*   **TALL_GRASS:** Already confirmed traversable. *Final check: Confirm entry from all 4 sides is possible without issue.*
*   **LEDGE_HOP_DOWN/LEFT/RIGHT:** *Plan: Find an example and attempt to move Up/Left/Right against the ledge direction. Then, move with the ledge direction to confirm one-way travel.*
*   **VOID:** *Plan: Attempt to walk into it from an adjacent traversable tile.*
*   **WATER/WATER_EDGE:** *Plan: Attempt to walk into it from an adjacent traversable tile.*
*   **BOOKSHELF/RADIO/TV/WINDOW/TOWN_MAP:** *Plan: Attempt to walk into each from all available adjacent tiles to confirm they are impassable walls.*
*   **LEDGE_HOP_DOWN:** One-way traversal. Confirmed impassable from below.
## Exploration Notes
* System alert: Potentially reachable unseen tiles detected. I will investigate these after completing my current immediate objective.
*   **CUT_TREE:** Hypothesis: Impassable without HM Cut. *Plan: Attempt to walk into it from an adjacent tile.*

## Tool Development & Bugs
*   `find_path` tool is unreliable. It failed to find a path in the simple Route 29/46 Gatehouse. Needs further debugging.