# Gem's Pokémon Crystal Adventure Log

## Current Plan
1. Explore the Route 29/46 Gatehouse.
   - Interact with the Youngster.
   - Investigate and mark all three unexplored warps.
2. Use `find_reachable_unseen_tiles` on Route 29 to fully explore it.
3. Proceed west through Route 29 to Cherrygrove City.
4. Find Mr. Pokémon's house.

## Game Mechanics & Systems
* **Money & Economy:** Currently have ¥3000.

## Battle and Pokemon Information
* **Party Composition:**
    * Vulcan (Cyndaquil), Lv. 5

## Tile Traversal Rules (Systematic Testing)
*Method: To confirm a tile's properties, I must attempt to move onto it from all four adjacent, traversable tiles (Up, Down, Left, Right). A conclusion is only valid after all directions are tested.*

### Confirmed Mechanics:
*   **FLOOR:** Traversable.
*   **WALL:** Impassable.
*   **COUNTER:** Impassable.
*   **HEADBUTT_TREE:** Impassable.
*   **LEDGE_HOP_RIGHT:** One-way traversal from left to right. Impassable from right, above, or below.
*   **LEDGE_HOP_DOWN:** One-way traversal from top to bottom. Impassable from below, left, or right.
*   **WARP_CARPET_DOWN:** Requires pressing 'Down' while standing on the tile to activate.

### Untested Mechanics & Testing Plan:
*   **TALL_GRASS:** Appears traversable, but needs confirmation from all directions. *Plan: Walk into a patch from all 4 sides.*
*   **LEDGE_HOP_LEFT:** Hypothesis: Allows leftward travel over the ledge. *Plan: Find a ledge and attempt to move left onto it, then attempt to move back right.*
*   **VOID:** Appears impassable. *Plan: Attempt to walk into it from an adjacent tile.*
*   **DOOR:** Appears to function as a warp. *Plan: Walk into one to confirm.*