# Core Lessons
*   **Trust Verified Tools:** A tool reporting 'no path' is providing critical, accurate information about the game state, not evidence of a bug. My repeated failure to trust `pathfinder_v2`'s correct assessment of Route 46 was a major strategic error. I must trust my verified tools over my own assumptions.
*   **Question Assumptions, Not Tools:** If a path repeatedly fails, don't just blame the execution or the tool; question the premise of the path itself. My fixation on a northern path on Route 30 was a massive failure born from a flawed assumption.
*   **Be Flexible:** Fixating on a single path or strategy in the face of repeated failure is inefficient. I must be quicker to abandon a failed hypothesis and explore alternatives.

# Game Objectives
*   **Primary:** Investigate the red Gyarados at the Lake of Rage.
*   **Secondary:** Defeat Team Rocket in the Mahogany Town hideout.
*   **Tertiary:** Earn the Glacier Badge from Pryce in Mahogany Town.

# Development Pipeline
*   **Pathfinding Tool:** My `pathfinder_v2` tool has been debugged and verified. It correctly handles impassable terrain and one-way ledges.

# Tile Mechanics Testing
*This section tracks experiments to understand how different tiles work.*

### Untested Hypotheses
*   **Hypothesis: `PC` tiles are impassable.**
    *   **Test:** Attempt to walk into a `PC` tile.
    *   **Status:** Untested.
*   **Hypothesis: `HEADBUTT_TREE` can be interacted with using the move Headbutt.**
    *   **Test:** Stand next to a `HEADBUTT_TREE` and use Headbutt from the party menu.
    *   **Status:** Untested.
*   **Hypothesis: `WARP_CARPET_DOWN` has specific entry requirements.**
    *   **Conclusion:** The warp at (17, 31) in Union Cave 1F seems to be a one-way exit from Route 33. Will test entry from the Route 33 side when possible.

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

# Misc Notes & Reminders
*   **Bag is Full:** Cannot pick up the Rare Candy at (53, 12) on Route 27 until a slot is freed.
*   **Pending Rematch:** Fisher Ralph on Route 32.
*   **Violet Gym Warp:** The warp tile at (5, 15) inside the Violet City Gym is a one-way exit that returns the player to the front of the gym.

# Strategic Plans
*   **Route to Lake of Rage:**
    1.  Travel north from Cherrygrove City to Route 30.
    2.  Head east through Route 31 to Violet City. (Currently on Route 31)
    3.  Continue south through Route 32, Union Cave, and Route 33 to Azalea Town.
    4.  Pass through Ilex Forest to Route 34.
    5.  Travel north through Goldenrod City, Route 35, and the National Park to Route 36.
    6.  Head east on Route 36 and Route 37 to Ecruteak City.
    7.  Go east from Ecruteak through Route 42 to Mahogany Town.
    8.  From Mahogany Town, go north to the Lake of Rage.