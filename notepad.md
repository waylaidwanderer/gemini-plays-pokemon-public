# Gem's Pokémon Crystal Adventure Log

## Current Plan
1. I am in the Guide Gent's house in Cherrygrove City.
2. My immediate goal is to talk to GRAMPS.
3. After, I will leave and explore the final building in the city, the Poké Mart at (31, 11).

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
*   **TALL_GRASS:** Appears traversable. *Plan: Walk into a patch from all 4 sides.*
*   **LEDGE_HOP_DOWN/LEFT/RIGHT:** Hypothesis: One-way traversal. *Plan: Find ledges and test movement from all four directions.*
*   **VOID:** Appears impassable. *Plan: Attempt to walk into it from an adjacent tile.*
*   **WATER/WATER_EDGE:** Hypothesis: Impassable without Surf. *Plan: Test by attempting to walk into it from an adjacent tile.*
*   **BOOKSHELF/RADIO/TV/WINDOW/TOWN_MAP:** Hypothesis: Impassable scenery. *Plan: Attempt to walk into them from adjacent tiles.*