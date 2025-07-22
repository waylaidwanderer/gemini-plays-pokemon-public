# Gem's Pokémon Crystal Adventure Log

## Current Plan
1. Get the item ball at (48, 2) on Route 29.
2. Find the correct path through Route 29 to reach Cherrygrove City.
3. Buy Poké Balls in Cherrygrove City.
4. Find Mr. Pokémon's house, which is past Cherrygrove.
5. Get the item from Mr. Pokémon and return to Professor Elm.

## Game Mechanics & Systems
* **Money & Economy:** Currently have ¥3000.

## Battle and Pokemon Information
* **Party Composition:**
    * Vulcan (Cyndaquil), Lv. 5

## Area and Navigation Insights
* **Route 29:** Contains two main paths, north and south. The southern path is blocked by a series of one-way ledges that prevent westward travel. The northern path appears to be the correct way forward.

## Tile Traversal Rules (Systematic Testing)
*Method: To confirm a tile's properties, I must attempt to move onto it from all four adjacent, traversable tiles (Up, Down, Left, Right). A conclusion is only valid after all directions are tested.*

### Confirmed Mechanics:
*   **FLOOR:** Traversable.
*   **WALL:** Impassable.
*   **TALL_GRASS:** Traversable, wild Pokémon may appear.
*   **HEADBUTT_TREE:** Impassable. Confirmed by attempting to walk into them from multiple directions.
*   **LEDGE_HOP_RIGHT:** One-way traversal from left to right. Confirmed impassable from the right side (east).
*   **WARP_CARPET_DOWN:** Requires pressing 'Down' while standing on the tile to activate.

## Progress Tracking & Corrections
* **Failed Hypothesis:** The Cooltrainer at (50, 12) is not a required battle and does not block progress. His dialogue is generic.

## Hypotheses & Systematic Testing
*Method: To confirm a tile's properties, I must attempt to move onto it from all four adjacent, traversable tiles (Up, Down, Left, Right). A conclusion is only valid after all directions are tested.*

### Untested Mechanics:
*   **HEADBUTT_TREE:** Requires full directional testing.
*   **LEDGE_HOP_DOWN:** Requires full directional testing.
*   **STAIRS:** Untested.
*   **BOOKSHELF:** Untested.
*   **PC:** Untested.
*   **TV:** Untested.
*   **WINDOW:** Untested.