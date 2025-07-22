# Gem's Pokémon Crystal Adventure Log

## Current Plan
- Get the item ball on Route 29.
- Find the correct path through Route 29 to reach Cherrygrove City.
- Buy Poké Balls in Cherrygrove City.
- Find Mr. Pokémon's house, which is past Cherrygrove.
- Get the item from Mr. Pokémon and return to Professor Elm.

## Game Mechanics & Systems
* **Money & Economy:** Currently have ¥3000.

## Battle and Pokemon Information
* **Party Composition:**
    * Vulcan (Cyndaquil), Lv. 5

## Area and Navigation Insights
* **Route 29:** Contains two main paths, north and south. The southern path is blocked by a series of one-way ledges that prevent westward travel. The northern path appears to be the correct way forward.

## Tile Traversal Rules (Systematic Testing)
*   **FLOOR:** Traversable.
*   **WALL:** Impassable.
*   **TALL_GRASS:** Traversable, wild Pokémon may appear.
*   **HEADBUTT_TREE:** 
    *   Test 1: Attempted to move Up into (47, 6). Result: Blocked.
    *   Test 2: Attempted to move Right into (46, 7). Result: Blocked.
    *   Conclusion: Impassable from below and from the right. Further testing needed for other directions.
*   **LEDGE_HOP_RIGHT:**
    *   Test 1: Attempted to move Left into (43, 8). Result: Blocked.
    *   Test 2: Attempted to move Left into (43, 11). Result: Blocked.
    *   Test 3: Attempted to move Left into (43, 12). Result: Blocked.
    *   Conclusion: Confirmed impassable from the right side (east). Hypothesis: This is a one-way ledge allowing travel from left to right (west to east).
*   **LEDGE_HOP_DOWN:**
    *   Untested. Hypothesis: Allows downward travel over the ledge.

## Progress Tracking & Corrections
* **Failed Hypothesis:** The Cooltrainer at (50, 12) is not a required battle and does not block progress. His dialogue is generic.

## Hypotheses & Systematic Testing
*Method: To confirm a tile's properties, I must attempt to move onto it from all four adjacent, traversable tiles (Up, Down, Left, Right). A conclusion is only valid after all directions are tested.*

### Untested Mechanics:
*   **HEADBUTT_TREE:** Requires full directional testing.
*   **LEDGE_HOP_DOWN:** Requires full directional testing.