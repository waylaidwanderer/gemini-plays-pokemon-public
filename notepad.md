# Gem's Pokémon Crystal Adventure Log

# I. Game Mechanics & Systems

## A. Tile Traversal Rules

### Confirmed Traversable:
*   **FLOOR:** Fully traversable.
*   **TALL_GRASS:** Traversable. Can trigger wild Pokémon encounters.
*   **DOOR:** Functions as a two-way warp.
*   **CAVE:** Functions as a warp.
*   **LADDER:** Functions as a two-way warp between floors.

### Warp Tiles:
*   **WARP_CARPET_DOWN:** One-way warp. Activated by pressing 'Down'.
*   **WARP_CARPET_LEFT:** One-way warp. Activated by moving onto the tile from the right.
*   **WARP_CARPET_RIGHT:** One-way warp. Activated by moving onto the tile from the left.

### Confirmed Impassable:
*   **WALL:** Impassable.
*   **COUNTER:** Impassable. Interact with NPCs from the front.
*   **PC:** Impassable. Functions as an object.
*   **VOID:** Impassable. Appears as a black abyss.
*   **CUT_TREE:** Impassable. Likely requires HM Cut.
*   **HEADBUTT_TREE:** Impassable. Likely requires HM Headbutt.
*   **SIGN:** Impassable. Functions as an object that can be interacted with for text.
*   **BOOKSHELF:** Impassable. Functions as an object that can be interacted with for text.
*   **BLACKBOARD:** Impassable. Functions as an object that can be interacted with for text.
*   **MART_SHELF:** Impassable. Functions as a wall.
*   **WATER:** Confirmed impassable. Blocks movement entirely.

### Confirmed One-Way:
*   **LEDGE_HOP_DOWN:** One-way traversal. Can only be entered from above.
*   **FLOOR_UP_WALL:** Confirmed one-way traversal. Can only be entered from below. Impassable from all other directions.

### Under Investigation:
*   **unknown:** Encountered this tile type when interacting with the Kabuto puzzle in the Ruins of Alph. Its properties are currently unknown as I am locked in the puzzle interface. Must investigate after completion.

# II. Battle Information

## A. Verified Type Matchups
*   Ghost-type Pokémon are immune to Normal-type moves.
*   Unown's Hidden Power can be super-effective against Fire-type Pokémon (observed against Vulcan). The specific type is unknown, but could be Water, Rock, or Ground.

# III. Badges & TMs
*   **Zephyr Badge:** Acquired from Falkner. Raises Pokémon's attack power and allows the use of HM05 (Flash) outside of battle.
*   **TM31 (Mud-Slap):** Received from Falkner.
*   **TM39:** Found in Union Cave B1F.

# IV. Phone Calls & Side Quests
*   Wade called about the Bug-Catching Contest at the National Park.

# V. New Discoveries & Lessons
*   **Ruins of Alph Puzzle:** Solving the Kabuto puzzle caused Unown to appear in the inner chambers. This seems to be the intended progression.
*   **SUPER_NERD at (4, 21) in Union Cave is not a trainer.** He is an NPC who gives a hint about Pokémon roars on Fridays. The western path is currently blocked by him.

# VI. Puzzle Solutions

## A. Ruins of Alph (Kabuto Puzzle)
*   **Hypothesis 1 (Failed):** The puzzle is solved by arranging the 16 pieces to form an image of the Pokémon Kabuto.
    *   **Test:** All pieces were arranged correctly into the Kabuto image.
    *   **Result:** The game did not automatically exit the puzzle screen.
    *   **Conclusion:** This hypothesis is incorrect.
*   **Hypothesis 2 (Failed):** After arranging the pieces, the 'Start' button must be pressed to confirm the solution.
    *   **Test:** Pressed 'Start' after arranging all pieces.
    *   **Result:** The puzzle interface did not close, and the puzzle was not solved.
    *   **Conclusion:** This hypothesis is incorrect.
*   **Hypothesis 3 (Confirmed):** The 'B' button exits the puzzle interface without solving it.
    *   **Test:** Pressed 'B' after arranging all pieces.
    *   **Result:** The puzzle interface closed, returning me to the chamber. The puzzle was not marked as solved.
    *   **Conclusion:** The puzzle is either optional, or the solution is not simply arranging the pieces. Abandoning the puzzle to explore other paths.
*   **Hypothesis 4 (Confirmed):** The true solution was to use the unmarked warp at (4, 0) in the puzzle chamber after arranging the pieces. This led to the inner chamber where Unown appeared.

# VII. Custom Tools & Agents
*   `find_path_to_target`: Finds the shortest path from the player's current position to a specified target coordinate.
*   `find_reachable_unseen_tiles`: Finds all unseen tiles that are reachable from the player's current position.
*   `battle_strategist`: Recommends the best action in a battle.
*   `exploration_strategist`: Recommends the next best tile to explore based on the primary goal.
*   `team_composition_advisor`: Recommends a team composition for a specific opponent type.
*   `kabuto_puzzle_solver`: Analyzes the Kabuto puzzle grid from a raw text input and provides the full sequence of moves to solve it.
*   `script_debugger`: Analyzes faulty Python scripts and provides debugging plans.

# VIII. Reflection Log & Untested Assumptions

## A. 50-Turn Reflection (Turn 5735)
*   **Immediate Action Mandate (Failure):** I continue to fail to perform data management tasks immediately. I deferred marking the Research Center warp and fixing my pathfinder. This must be my top priority to correct.
*   **Untested Assumption 1:** The main path to Azalea Town is south from Route 32.
    *   **Alternative Hypothesis:** The path is through a different, unexplored part of Union Cave or the Ruins of Alph.
    *   **Test:** Proceed south on Route 32. If a dead end is reached, the assumption is false.
*   **Untested Assumption 2:** The unmarked warp at (7, 5) on the Ruins of Alph Outside map is just another puzzle chamber.
    *   **Alternative Hypothesis:** It is a shortcut or the main path forward.
    *   **Test:** Enter the warp.

# IX. Story Clues & Hints
*   **Strange Tree:** Gramps in the Route 36 Gatehouse mentioned a 'strange tree' blocking a road, which might be why fewer people are visiting the Ruins of Alph. This could be the path forward.
*   Wade has called multiple times about the Bug-Catching Contest at the National Park today.

# X. Tool Development & Debugging Log

## A. `find_reachable_unseen_tiles`
*   **Logical Flaw Identified (Turn 6001):** The single-stage BFS logic is critically flawed, returning all theoretically passable unseen tiles, including those on inaccessible 'islands'. This led to impossible navigation goals. The tool is being rewritten to use a two-stage BFS to find only the unseen tiles bordering the currently known, reachable area.

# XI. Exploration Notes
*   **Ruins of Alph Outside (Central Plaza):** This area is a dead end. The southern and eastern paths are unreachable, and the warp at (13, 20) is an entrance only. The only way forward seems to be through one of the interior buildings.
*   **New Plan:** Re-investigate the Ruins of Alph Research Center.
*   Wade has called multiple times about the Bug-Catching Contest at the National Park today.
*   **Fix Implemented (Turn 5915):** The two-stage BFS was flawed. Re-implemented a single-stage BFS to find all *truly* reachable unseen tiles, not just adjacent ones. This should prevent the `exploration_strategist` from receiving impossible targets.
*   Wade has called multiple times about the Bug-Catching Contest at the National Park today.
*   **Hypothesis 5 (Failed):** Interacting with the ancient replicas after solving the puzzle will trigger an event.
    *   **Test:** Interacted with both the left and right replicas after solving the Kabuto puzzle.
    *   **Result:** Both interactions yielded only generic descriptive text.
    *   **Conclusion:** The replicas are not interactive post-puzzle. This chamber appears to be fully explored.
*   Wade has called multiple times about the Bug-Catching Contest at the National Park today.