# Gem's Pokémon Crystal Adventure Log

## Current Plan
1. Interact with the Youngster on Route 29.
2. Test the `find_path_bfs` tool to navigate west towards Cherrygrove City.
3. Find Mr. Pokémon's house, which is past Cherrygrove.
4. Get the item from Mr. Pokémon and return to Professor Elm.

## Game Mechanics & Systems
* **Money & Economy:** Currently have ¥3000.
* **Interactions:** Interacting with a stunned NPC seems to automatically unstun them.

## Battle and Pokemon Information
* **Party Composition:**
    * Vulcan (Cyndaquil), Lv. 5

## Tile Traversal Rules (Systematic Testing)
*Method: To confirm a tile's properties, I must attempt to move onto it from all four adjacent, traversable tiles (Up, Down, Left, Right). A conclusion is only valid after all directions are tested.*

### Confirmed Mechanics:
*   **FLOOR:** Traversable.
*   **WALL:** Impassable.
*   **HEADBUTT_TREE:** Impassable.
*   **LEDGE_HOP_RIGHT:** One-way traversal from left to right. Impassable from right, above, or below.
*   **LEDGE_HOP_DOWN:** One-way traversal from top to bottom. Impassable from below, left, or right.
*   **WARP_CARPET_DOWN:** Requires pressing 'Down' while standing on the tile to activate.

### Untested Mechanics & Testing Plan:
*   **TALL_GRASS:** Appears traversable, but needs confirmation from all directions. *Plan: Walk into a patch from all 4 sides.*
*   **LEDGE_HOP_DOWN:** Hypothesis: Allows downward travel over the ledge. *Plan: Find a ledge and attempt to move down onto it, then attempt to move back up.*
*   **LEDGE_HOP_LEFT:** Hypothesis: Allows leftward travel over the ledge. *Plan: Find a ledge and attempt to move left onto it, then attempt to move back right.*
*   **VOID:** Appears impassable. *Plan: Attempt to walk into it from an adjacent tile.*