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

# Game Mechanics & Systems
*   **Inventory Management:** To free up an inventory slot, you must toss the *entire stack* of an item. Tossing a single item from a stack of multiple does not free up a slot.

# Puzzles
## National Park Gate Puzzle (Route 36)
*   **Hypothesis 1:** The warp at (0, 4) is the entrance.
    *   **Test:** Attempted to move left onto the warp tile.
    *   **Conclusion:** Failed. This seems to be a one-way exit.
*   **Hypothesis 2:** Talking to the Officer at (3, 2) opens the path.
    *   **Test:** Spoke to the Officer.
    *   **Conclusion:** Failed. He only provided flavor text.

# Tool Development
*   **path_plotter:** A BFS pathfinding tool. It has been refined to account for on-screen objects as impassable obstacles.

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

### Special Interaction
*   `FRUIT_TREE`: Can be interacted with by facing it and pressing 'A' to receive a BERRY.

### One-Way Traversal
*   `LEDGE_HOP_DOWN`: This tile is one-way. It can only be entered by moving down from the tile above. Attempting to move up onto it from below is impossible.
*   `LEDGE_HOP_LEFT`: Can only be moved left from.
*   `FLOOR_UP_WALL`: Can only be entered by moving up from the tile below.
*   `LEDGE_HOP_RIGHT`: This tile is one-way. It can only be entered by moving right from the tile to its left. Attempting to move left onto it from the right is impossible.
*   `WARP_CARPET_LEFT`: Confirmed one-way *exit* at Route36NationalParkGate (0, 4). Attempts to use as an entrance have failed.
*   `WARP_CARPET_DOWN`: Confirmed one-way exit.

# Known Issues & Peculiarities
*   **`stun_npc` Ineffectiveness:** The `stun_npc` tool is ineffective on Youngster (ID 2) on Route 31. The stun was either overridden by a script or is ineffective on this specific NPC. Avoid using `stun_npc` on him.

# Corrections
*   **Verified:** Tile (31, 26) in Violet City is a standard `FLOOR` tile. My previous belief of it being a 'glitched warp' was a hallucination.