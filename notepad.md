# Gem's Pokémon Crystal Notepad

## I. Game Systems & Mechanics

### Tile Traversal Protocol
- **Testing Mandate:** When a new, reachable tile type is seen, I MUST test it immediately.
- **Movement Test:** Attempt to move *into* and *out of* the tile from all 4 cardinal directions to verify passability.
- **Ledge Test:** For any ledge-like tile, I must attempt to move up/against the apparent direction of the ledge to confirm if it is a one-way path.

### Verified Tile Types
*   **Impassable:** `WALL`, `PILLAR`, `BOOKSHELF`, `TV`, `RADIO`, `TOWN_MAP`, `STATUE`, `TABLE`, `CHAIR`, `BIRD` (Farfetch'd), `MART_SHELF`, `BUOY`, `PC`, `LINK_CABLE`, `TRADE_MACHINE`, `INCENSE_BURNER`, `ROOF`, `CHIMNEY`, `SIGN`, `FLOWER`, `TREE_TOP`, `WATER_EDGE_UP`, `WATER_EDGE_DOWN`, `WATER_EDGE_LEFT`, `WATER_EDGE_RIGHT`, `VOID`, `COUNTER`, `FENCE`, `PC`, `LINK_RECEPTIONIST`, `WINDOW`, `WEIRD_TREE`.
*   **Traversable:** `FLOOR`, `GRASS`, `TALL_GRASS`, `LONG_GRASS`, `RAILING`, `PIPE_HORIZONTAL`, `PIPE_VERTICAL`.
*   **Warps:** `DOOR`, `CAVE`, `LADDER`, `STAIRCASE` (Move onto tile).
*   **One-Way Ledges:** 
    * `LEDGE_HOP_DOWN/RIGHT`: A one-way ledge that can only be hopped in the specified direction.
    * `LEDGE_HOP_LEFT`: A one-way ledge that can only be hopped **LEFT**.
    * `FLOOR_UP_WALL`: A complex one-way ledge. Can be moved onto from a tile below, off of by moving down, and horizontally between adjacent `FLOOR_UP_WALL` tiles. Cannot move up from this tile.
*   **Special Requirement:** 
    * `CUT_TREE` (Requires HM01 Cut. These trees can respawn after being cut).
    * `WATER` (Requires HM03 Surf, but is currently blocked in Olivine City).
    * `BREAKABLE_ROCK` (Requires Rock Smash).
    * `HEADBUTT_TREE` (Requires the move Headbutt. Confirmed that interacting without the move does nothing).
*   **Complex Tiles:**
    *   `WARP_CARPET_DOWN/LEFT/RIGHT`: Activated by pressing the corresponding direction while standing on the tile.
    *   `PIT`: A hole in the floor that acts as a warp. Stepping on it triggers the warp.
    *   `unknown` (in Ruins of Alph Ho-Oh Chamber): A special tile that, when standing on it and interacting with the adjacent puzzle object at (3, 2), warps the player to a sliding block puzzle screen.

### Other Mechanics
*   **Object Impassability:** All Map Objects (NPCs, items, signs, etc.) are impassable.
*   **Item Effects:**
    *   **BERRY:** Restores 10 HP.
    *   **MINT BERRY:** Cures sleep.
    *   **EVERSTONE:** Prevents evolution.
    *   **MOOMOO MILK:** Restores 100 HP.
    *   **HARD STONE:** Powers up rock-type moves.
    *   **PRZCUREBERRY:** Cures paralysis.
    *   **HYPER POTION:** Restores 200 HP.
    *   **ICE BERRY:** Heals burn.
*   **Haircuts:** Increases a Pokémon's happiness.

## II. Key Items, HMs & TMs
*   **Key Items:** SQUIRTBOTTLE, GOOD ROD, COIN CASE
*   **HMs:** HM01 (CUT), HM03 (SURF), HM04 (STRENGTH)
*   **TMs:** 
    * TM08 (ROCK SMASH)
    * TM12 (SWEET SCENT)
    * TM28 (DIG)
    * TM30 (SHADOW BALL) - Causes damage and may reduce SPCL.DEF.
    * TM45 (ATTRACT)
    * TM49 (FURY CUTTER)

## III. Badges
*   **ZEPHYR BADGE**
*   **HIVE BADGE**
*   **PLAIN BADGE**
*   **FOG BADGE** (Allows use of SURF outside battle, makes Pokémon up to L50 obey)

## IV. Blocked Paths & Story Gates
### Route 37 Trainer Blockade
- **Location:** (6, 12) and (7, 12).
- **Blockade:** Two trainers (Twins Ann & Anne) disguised as trees block the path north.
- **Conclusion:** This path is story-locked. Progress is gated behind an unknown event.

### Goldenrod Underground Blockade
- **Location:** (5, 31).
- **Blockade:** A Super Nerd blocks the path south.
- **Conclusion:** This path is story-locked.

## V. Puzzle Solutions & Observations

### Ruins of Alph Ho-Oh Puzzle
- **Mechanic:** A 16-piece puzzle on a 6x6 grid. The goal is to assemble the image of Ho-Oh in the central 4x4 area.
- **Attempt 1 (Manual Trial-and-Error):**
    - **Hypothesis:** Place what appear to be corner pieces first to build a frame.
    - **Action:** Moved all pieces to the border, then attempted to place corners.
    - **Result:** Failed. The puzzle did not solve.
    - **Conclusion:** Simple visual identification is not reliable.
- **Attempt 2 (Agent-Assisted Strategy):**
    - **Hypothesis:** A systematic analysis of piece shapes will reveal the true corners and edges, leading to a correct solution.
    - **Action 1 (Define Agent):** Created the `puzzle_analyst` agent to classify pieces.
    - **Action 2 (Automated Data Gathering):** Used `run_code` to try and extract piece shape data automatically.
    - **Result:** Failed. The script could not find the puzzle data.
    - **Conclusion:** Puzzle piece data must be gathered manually.
- **Current Strategy (Manual Data Gathering):**
    1.  Systematically enter and exit the puzzle interface to view each of the 16 pieces without the cursor obstructing the view.
    2.  Record the shape of each piece as a boolean grid below.
    3.  Once all 16 pieces are documented, call the `puzzle_analyst` agent with the complete dataset.
    4.  Use the agent's output (classification of corners, edges, middles) to assemble the puzzle, starting with the frame.

### Puzzle Piece Shape Data
*   **Piece 5:** (Observed at puzzle coordinate (0,0)) - Shape: `[[true, true], [true, false]]`

### Goldenrod Dept. Store Basement Puzzle
- **Mechanic:** A dynamic box-pushing maze where Black Belts move and create/remove walls based on the player's position. The goal is to clear a path to the ladder at (17, 2).
- **Hypothesis:** A specific sequence of movements and interactions with the Black Belts is required to open the path.

## VI. Untested Hypotheses & Future Plans
*   **`CUT_TREE` Respawn Conditions:** A `CUT_TREE` at (8, 25) in Ilex Forest respawned. I need to test the exact conditions. Next time I cut a tree near a map transition, I will immediately leave and re-enter the map to check if it has respawned.
*   **`WARP_CARPET_DOWN` Traversability:** I need to test if `WARP_CARPET_DOWN` tiles are truly one-way. Next time I'm on one, I will attempt to move up, left, and right to confirm.
*   **Puzzle Solver Tool Idea:** If I get stuck on visual puzzles, I should define a `puzzle_solver` tool.
    - **Input:** A representation of the puzzle grid (e.g., a 2D array of piece IDs) and a target configuration.
    - **Output:** A sequence of moves (e.g., `["pick(x1,y1)", "place(x2,y2)"]`) to solve it.
    - **Logic:** This would require an algorithm like A* search or a similar pathfinding/planning algorithm to find the optimal sequence of moves. It is a computational task, perfect for a tool.