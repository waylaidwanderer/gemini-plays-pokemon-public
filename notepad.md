# Game Objectives
*   **Primary:** Investigate the mysterious radio broadcast.
*   **Secondary:** Travel to Blackthorn City and challenge the Gym Leader.
*   **Tertiary:** Train my lower-level Pokémon.

# Core Lessons
*   **Automate Early:** Repetitive manual tasks are inefficient. If a problem is complex or requires multiple steps, create an agent or tool for it *immediately* instead of wasting turns on manual attempts.
*   **Document Immediately:** New discoveries (mechanics, items, NPC info) must be documented in the notepad or via map markers on the same turn they are learned. This is a higher priority than any in-game action.
*   **Trust Verified Tools:** A tool reporting 'no path' or providing unexpected data is giving critical, accurate information about the game state, not evidence of a bug. Trust the tools over assumptions.
*   **Be Flexible:** Fixating on a single path or strategy in the face of repeated failure is inefficient. Be quick to abandon a failed hypothesis and explore alternatives. If progress stalls, pivot to a different goal.

# Game Mechanics & Systems
*   **Inventory Management:** To free up an inventory slot, you must toss the *entire stack* of an item. Tossing a single item from a stack of multiple does not free up a slot.

# Tile Mechanics Testing
*This section tracks experiments to understand how different tiles work.*

### Untested Hypotheses
*   **Hypothesis: `PC` tiles are impassable.**
    *   **Test:** Attempt to walk into a `PC` tile.
    *   **Status:** Untested.
*   **Hypothesis: `HEADBUTT_TREE` can be interacted with using the move Headbutt.**
    *   **Test:** Stand next to a `HEADBUTT_TREE` and use Headbutt from the party menu.
    *   **Status:** Untested.
*   **Hypothesis: `LEDGE_HOP_RIGHT` is one-way.**
    *   **Test:** Attempt to move left onto a `LEDGE_HOP_RIGHT` tile from an adjacent `FLOOR` tile. 
    *   **Status:** Untested. Must test at next opportunity.

### Verified Tile Mechanics
*   **Traversable:**
    *   `FLOOR`: Standard ground.
    *   `TALL_GRASS`: Triggers wild encounters.
*   **Requires HM/Interaction:**
    *   `WATER`: Requires SURF. Can only be entered by facing the tile and pressing 'A'.
    *   `CUT_TREE`: Impassable, but can be cleared with HM01 CUT.
    *   `CAVE`/`DOOR`/`STAIRCASE`/`LADDER`: Warp point.
*   **Impassable:**
    *   `VOID`: Standard barrier.
    *   `BUOY`: Confirmed impassable after attempting to move onto the tile at (27, 16).
    *   `ROOF`/`TV`: Impassable.
    *   `COUNTER`: Confirmed impassable after attempting to move onto the tile at (3, 2).
    *   `WALL`: Standard impassable tile.
*   **Special Interaction:**
    *   `FRUIT_TREE`: Can be interacted with by facing it and pressing 'A' to receive a BERRY.
*   **One-Way Traversal:**
    *   `LEDGE_HOP_DOWN`: Can only be moved down from.
    *   `LEDGE_HOP_LEFT`: Can only be moved left from.
    *   `FLOOR_UP_WALL`: Can only be entered by moving up from the tile below.
*   **`WARP_CARPET_LEFT` Investigation:**
    *   **Conclusion:** All attempts to use this tile as an *entrance* have failed. It is highly likely a one-way *exit* from the connected area.
    *   **Failed Tests:**
        *   Walking onto the tile from the right.
        *   Standing on the tile, facing up, and pressing 'A'.
        *   Simply pressing 'A' on the tile.