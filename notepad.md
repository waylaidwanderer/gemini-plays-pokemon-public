# Gem's Pokémon Crystal Adventure Log

## Current Plan
1. I am in Cherrygrove City. My goal is to find Mr. Pokémon's house.
2. I will start by exploring the city, investigating buildings and talking to NPCs.
3. The Pokémon Center is at (29, 3). I should visit it to heal and mark the warp.
4. Another unmarked building is at (31, 11).

## Future Plans
*   Consider creating a 'battle strategy' agent for more complex fights.

## Game Mechanics & Systems
*   **Held Items:** Pokémon can hold items (like a BERRY) and use them automatically in battle to restore HP.

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
*   **DOOR:** Functions as a warp.

### Untested Mechanics & Testing Plan:
*   **TALL_GRASS:** Appears fully traversable, but needs confirmation from all directions. *Plan: Walk into a patch from all 4 sides.*
*   **LEDGE_HOP_LEFT/RIGHT:** Hypothesis: Allows one-way travel over the ledge. I have observed being unable to move onto these from the wrong direction. *Plan: Find an appropriate ledge and test movement from all four directions to confirm.*
*   **VOID:** Appears impassable. *Plan: Attempt to walk into it from an adjacent tile to confirm.*