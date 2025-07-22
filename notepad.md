# Game Objectives
*   **Primary:** Investigate the mysterious radio broadcast.
*   **Secondary:** Find a way to Goldenrod City.
*   **Tertiary:** Train my lower-level Pokémon.

# Core Lessons
*   **Automate Early:** Repetitive manual tasks are inefficient. If a problem is complex or requires multiple steps, create an agent or tool for it *immediately* instead of wasting turns on manual attempts.
*   **Document Immediately:** New discoveries (mechanics, items, NPC info) must be documented in the notepad or via map markers on the same turn they are learned. This is a higher priority than any in-game action.
*   **Trust Verified Tools:** A tool reporting 'no path' or providing unexpected data is giving critical, accurate information about the game state, not evidence of a bug. Trust the tools over assumptions.
*   **Be Flexible:** Fixating on a single path or strategy in the face of repeated failure is inefficient. Be quick to abandon a failed hypothesis and explore alternatives. If progress stalls, pivot to a different goal.
*   **No Glitches:** Never assume a game mechanic is a glitch. Investigate unexpected behavior with a scientific mindset to understand the underlying rules.

# Puzzles
## Route 36 National Park Gate
*   **Goal:** Enter the National Park.
*   **Hypothesis 1:** The warp at (0, 4) and (0, 5) is the entrance.
    *   **Test:** Attempted to move left onto the warp tile. Failed. Attempted to step off and back on. Failed.
    *   **Conclusion:** This is a one-way exit from the National Park, confirmed by multiple failed entry attempts.
*   **Hypothesis 2:** Talking to the Officer at (3, 2) from across the counter opens the path.
    *   **Test:** Spoke to the Officer from (3, 4).
    *   **Conclusion:** Failed. He only provided flavor text.
*   **Hypothesis 3:** Reading the Bug-Catching Contest sign at (6, 0) is required.
    *   **Test:** Interacted with the sign from (6, 1).
    *   **Conclusion:** Failed. Provided only informational text.
*   **Hypothesis 4:** The Officer must be interacted with from a different position (not across the counter).
    *   **Test:** Attempted to plot a path around the counter to (2, 2).
    *   **Conclusion:** Failed. I could not find a path behind the counter.
*   **Overall Conclusion:** The gatehouse is currently a dead end. The path to the National Park must be elsewhere.

## Mahogany Town Navigation
*   **Goal:** Investigate the mysterious radio broadcast in Mahogany Town.
*   **Analysis:** My previous conclusion of being trapped in southern Mahogany Town was incorrect. My `path_navigator` tool successfully found a path to the northern section. The eastern path to Route 44 is now blocked by a POKEFAN_M NPC, indicating a story-based roadblock.
*   **Plan:** The most logical step is to investigate other changes in town. A new 'Gramps' NPC has appeared at (7, 9). I will interact with him to see if he provides a clue to progress.

# Tile Mechanics Testing
*This section tracks experiments to understand how different tiles work.*

## Untested Hypotheses
*   **Hypothesis: `HEADBUTT_TREE` can be interacted with using the move Headbutt.**
    *   **Test:** Find a Pokémon that can learn Headbutt, teach it the move, stand next to a `HEADBUTT_TREE`, and use the move from the party menu.
    *   **Status:** Untested. Need to find the Headbutt TM/Tutor.

## Verified Tile Mechanics
### Traversable
*   `FLOOR`: Standard ground.
*   `TALL_GRASS`: Triggers wild encounters.
*   `ICE`: Slides player in the direction of movement until an obstacle is hit.

### Requires HM/Interaction
*   `WATER`: Requires SURF. Can only be entered by facing the tile and pressing 'A'.
*   `CUT_TREE`: Impassable, but can be cleared with HM01 CUT.
*   `CAVE`/`DOOR`/`STAIRCASE`/`LADDER`: Warp point.

### Impassable
*   `VOID`: Standard barrier.
*   `BUOY`: Confirmed impassable after attempting to move onto the tile.
*   `ROOF`/`TV`: Impassable.
*   `COUNTER`: Confirmed impassable after attempting to move onto the tile.
*   `WALL`: Standard impassable tile.
*   `HEADBUTT_TREE`: Impassable.

### Special Interaction
*   `FRUIT_TREE`: Can be interacted with by facing it and pressing 'A' to receive a BERRY.

### One-Way Traversal
*   `LEDGE_HOP_DOWN`: This tile is one-way. It can only be entered by moving down from the tile above. Attempting to move up onto it from below is impossible.
*   `LEDGE_HOP_LEFT`: Can only be moved left from.
*   `FLOOR_UP_WALL`: Can only be entered by moving up from the tile below.
*   `LEDGE_HOP_RIGHT`: This tile is one-way. It can only be entered by moving right from the tile to its left. Attempting to move left onto it from the right is impossible.
*   `WARP_CARPET_LEFT`: Confirmed one-way *exit* at Route36NationalParkGate (0, 4) & (0, 5). Attempts to use as an entrance have failed.
*   `WARP_CARPET_DOWN`: Confirmed one-way exit.

# Known Issues & Peculiarities
*   **`stun_npc` Ineffectiveness:** The `stun_npc` tool is ineffective on Youngster (ID 2) on Route 31. The stun was either overridden by a script or is ineffective on this specific NPC. Avoid using `stun_npc` on him.