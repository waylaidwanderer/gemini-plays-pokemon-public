## II. World Knowledge & Puzzles

### A. Solved Puzzles & Key Discoveries
*   **Red Gyarados Event (Lake of Rage):** Defeated the red Gyarados and obtained the RED SCALE.
*   **Cianwood City Stuck Spot:** Resolved by triggering back-to-back phone calls (Mom, then Liz) on tile (10, 28).
*   **Ilex Forest Shrine:** A Lass in the Route 34 Gate mentioned a shrine honoring a grass-type protector.
*   **TM12 (Sweet Scent):** Given by Teacher in Route 34 Ilex Forest Gate.
*   **Team Rocket Base Passwords:** SLOWPOKETAIL, HAIL GIOVANNI.
*   **Team Rocket Base B1F Secret Passage:** The 'door' at (10, 9) is opened by the Secret Switch at (19, 11).
*   **Team Rocket Base B2F Layout:** Northern and southern corridors are separate. Access to the north must be from a different warp on B1F.
*   **Mahogany Town:** No shop exists. The mart is a Team Rocket front, and the Poké Center has no vendor. Travel to another city is required for inventory management.
*   **Mahogany Town Story Lock:** FLY is disabled, forcing progression towards the Lake of Rage.
*   **Mahogany Mart Secret Ladder:** The warp to the hideout is not triggered by interaction, but by stepping onto the ladder tile at (7, 3).
*   **Team Rocket B1F Maze (Disguised Path):** The solution, hinted at by the ROCKET Grunt's dialogue ('Collect your courage and walk!'), is not a path through a wall, but a FLOOR tile at (3, 5) disguised to look like a wall. This creates a secret northern passage in the western maze area.

### B. Falsified Hypotheses & Dead Ends
*   **Mahogany Gym Blocker:** The Fisher did NOT move after the Lake of Rage event. Hypothesis that Lance's presence was the trigger is false.
*   **Secret Potion Location:** The hint for Cianwood City was incorrect; the Pharmacist runs a regular shop.
*   **Team Rocket B2F Southern Corridor:** The ROCKET at (21, 14) has non-progressive dialogue, confirming this path is a dead end.
*   **Team Rocket B1F Eastern Corridor:** The secret passage at (10, 9) and the entire eastern corridor lead to a dead-end loop.
*   **Team Rocket B1F Switch Function:** The switch at (19, 11) is not a toggle for the invisible maze. Interacting with the ROCKET at (2, 4) produces the same result regardless of the switch's on/off state.
*   **Team Rocket B1F Maze (Simple Pitfall):** Systematically exploring every floor tile in the western maze area revealed no pitfalls or warps other than the known dead-end ladder. Hypothesis that a simple pitfall was the solution is false.

### C. Solved Puzzles & Key Discoveries (Continued)
*   **Mahogany Gym Ice Puzzle:** Solved using a manual path. Defeated Gym Leader Pryce and obtained the Glacier Badge and TM16 (Icy Wind).
*   **Mysterious Radio Broadcast:** After defeating Pryce, received a call from Prof. Elm about a strange broadcast. The PokéGear radio confirms a Team Rocket broadcast. Next objective is to investigate the Goldenrod Radio Tower.

### D. Tool Development & Bugs
*   **bfs_pathfinder:** This tool is currently flawed. It does not correctly interpret one-way tiles like `LEDGE_HOP_DOWN` or `FLOOR_UP_WALL`, treating them as normal traversable tiles in any direction. This can cause it to fail to find a valid path or suggest an impossible one. It needs to be updated to account for tile-specific movement restrictions.

### E. Tool Development Bugs (Overwatch Feedback)
*   **`bfs_pathfinder`:** Still broken. The logic for one-way tiles is incorrect. Must be fixed before next use.
*   **`ice_puzzle_solver`:** Reported as unreliable. Needs to be tested, debugged, or deleted.
*   **`stun_npc`:** This tool was a hallucination and does not exist. Do not attempt to use it.

# Gem's Pokémon Crystal Notepad (REFACTORED)

## I. Game Mechanics & Systems

### A. Tile Traversal Rules
*   **Impassable:** WALL, COUNTER, MART_SHELF, PC, HEADBUTT_TREE, CUT_TREE (uncut), TV, TOWN_MAP, WINDOW, ROCK, BUOY, VOID, RADIO, INCENSE_BURNER, BOOKSHELF.
*   **Traversable:** GRASS, TALL_GRASS, LONG_GRASS, WATER/SEA (with Surf).
*   **Warps:** DOOR, CAVE, LADDER, WARP_CARPET_DOWN/LEFT/RIGHT, WARP_PANEL.
*   **HM Required:** BOULDER (STRENGTH), ROCK_SMASH_BOULDER (ROCK SMASH), WHIRLPOOL.
*   **One-Way:** PIT (fall), LEDGE_HOP_RIGHT/LEFT/DOWN, FLOOR_UP_WALL (one-way 'up' ledge).
*   **Special Movement:**
    *   ICE: Slide until hitting an obstacle (WALL, Object, VOID). FLOOR tiles are safe spots.
*   **Untested:** COMPUTER, BED, CABINET, SINK, PLANT, unknown tile types.

### B. System Bugs & Glitches (Verified)
*   'DEPOSIT ITEM', 'TOSS ITEM', and 'FLY' HM are bugged.
*   Giving/Tossing one item from a stack does not free an inventory slot.

### C. Item Usage Rules
*   Status/HP items can only be used on afflicted/damaged Pokémon.

## II. World Knowledge & Puzzles

### A. Solved Puzzles & Key Discoveries
*   **Lake of Rage:** Defeated Red Gyarados, got RED SCALE.
*   **Ilex Forest:** Got TM12 (Sweet Scent) from Teacher. Shrine honors a grass protector.
*   **Team Rocket Base:** Passwords are SLOWPOKETAIL, HAIL GIOVANNI. Secret door at (10, 9) on B1F opened by switch at (19, 11). B2F north/south corridors are separate. Disguised FLOOR tile at (3, 5) on B1F is the path through the maze.
*   **Mahogany Town:** No shop, mart is a front. FLY is disabled. Secret ladder to hideout is at (7, 3) in the mart.
*   **Mahogany Gym:** Defeated Pryce, got Glacier Badge & TM16.
*   **Radio Broadcast:** Prof. Elm called about a strange broadcast, confirmed on PokéGear.
*   **Stuck Event Solution:** Calling Prof. Elm was the trigger for the next phase of the scripted 'stuck' event in Violet City.

### B. Falsified Hypotheses & Dead Ends
*   **Mahogany Gym Blocker:** Fisher did not move after Lake of Rage event.
*   **Team Rocket Base:** ROCKET at (21, 14) B2F is a dead end. Eastern corridor on B1F is a loop. Switch at (19, 11) doesn't affect the maze trigger. No simple pitfall solution in the western maze.

## III. Maintenance & Status Log

### A. Tool Bugs & Status
*   **`bfs_pathfinder`:** Fixed in turn #61836. Should now correctly handle one-way tiles.
*   **`ice_puzzle_solver`:** UNRELIABLE. Needs testing and debugging.
*   **Hallucinated Tools:** `stun_npc` does not exist.

### B. Current Predicament: The 'Stuck' State
*   **Observation:** After a failed Fly attempt from Mahogany, I was warped to Violet City (31, 26). I am unable to move or use any warp items/moves.
*   **Hypothesis:** This is a scripted event. The solution is tied to the Team Rocket radio broadcast. The call to Prof. Elm was a necessary step.
*   **Current Plan:** Access the Radio function of the PokéGear, which may now be unlocked after the phone call.