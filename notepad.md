# Gem's Pokémon Crystal Adventure Log

## Current Plan
1. Interact with the Fruit Tree at (12, 2) for a potential item.
2. Challenge the Cooltrainer M at (13, 4).
3. Use `find_reachable_unseen_tiles` to clear the rest of Route 29.
4. Proceed west through Route 29 to Cherrygrove City.
5. Find Mr. Pokémon's house.

## Future Plans
*   Consider creating a 'battle strategy' agent for more complex fights.

## Game Mechanics & Systems
*   **Held Items:** Pokémon can hold items and use them automatically in battle (e.g., Vulcan used a BERRY to restore HP).
*   **Money & Economy:** Currently have ¥3000.

## Battle and Pokemon Information
*   **Party Composition:**
    *   Vulcan (Cyndaquil), Lv. 6. Learned SMOKESCREEN.

## Tile Traversal Rules (Systematic Testing)
*Method: To confirm a tile's properties, I must attempt to move onto it from all four adjacent, traversable tiles (Up, Down, Left, Right). A conclusion is only valid after all directions are tested.*

### Confirmed Mechanics:
*   **FLOOR:** Traversable.
*   **WALL:** Impassable.
*   **COUNTER:** Impassable. Interacting with NPCs behind them requires facing the counter tile.
*   **HEADBUTT_TREE:** Impassable.
*   **LEDGE_HOP_DOWN:** One-way traversal from top to bottom. Impassable from below, left, or right.
*   **WARP_CARPET_DOWN:** Requires pressing 'Down' while standing on the tile to activate.
*   **DOOR:** Functions as a warp.

### Untested Mechanics & Testing Plan:
*   **TALL_GRASS:** Appears fully traversable, but needs confirmation from all directions. *Plan: Walk into a patch from all 4 sides.*
*   **LEDGE_HOP_LEFT/RIGHT:** Hypothesis: Allows one-way travel over the ledge. *Plan: Find an appropriate ledge and test movement from all four directions.*
*   **VOID:** Appears impassable. *Plan: Attempt to walk into it from an adjacent tile to confirm.*