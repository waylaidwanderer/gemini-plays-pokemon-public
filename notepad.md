# Gem's Pokémon Crystal Notepad

## I. Game Systems & Mechanics

### Tile Traversal Protocol
- **Testing Mandate:** When a new, reachable tile type is seen, I MUST test it immediately.
- **Movement Test:** Attempt to move *into* and *out of* the tile from all 4 cardinal directions to verify passability.
- **Ledge Test:** For any ledge-like tile, I must attempt to move up/against the apparent direction of the ledge to confirm if it is a one-way path.

### Verified Tile Types
*   **Impassable:** `WALL`, `PILLAR`, `BOOKSHELF`, `TV`, `RADIO`, `TOWN_MAP`, `STATUE`, `TABLE`, `CHAIR`, `BIRD` (Farfetch'd), `MART_SHELF`, `BUOY`, `PC`, `LINK_CABLE`, `TRADE_MACHINE`, `INCENSE_BURNER`, `ROOF`, `CHIMNEY`, `SIGN`, `FLOWER`, `TREE_TOP`, `WATER_EDGE_UP`, `WATER_EDGE_DOWN`, `WATER_EDGE_LEFT`, `WATER_EDGE_RIGHT`, `VOID`, `COUNTER`, `FENCE`, `PC`, `LINK_RECEPTIONIST`, `WINDOW`, `WEIRD_TREE`.
*   **Traversable:** `FLOOR`, `GRASS`, `TALL_GRASS`, `LONG_GRASS`, `RAILING`, `PIPE_HORIZONTAL`, `PIPE_VERTICAL`.
*   **Warps:** `DOOR`, `CAVE`, `LADDER`, `STAIRCASE` (Move onto tile), `PIT` (Acts as a warp when stepped on).
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
*   **Route 37 Trainer Blockade:** Twins Ann & Anne disguised as trees block the path north at (6, 12) and (7, 12). This path is story-locked.
*   **Goldenrod Underground Blockade:** A Super Nerd blocks the path south at (5, 31). This path is story-locked.

## V. Puzzles & Exploration Notes

### Ruins of Alph
*   **Ho-Oh Puzzle:** A 16-piece puzzle on a 6x6 grid. Goal is to assemble Ho-Oh in the central 4x4 area. Currently on hold due to difficulty.
    *   **Unique Piece Shapes (Observed):** `[[true, true], [false, true]]`, `[[true, false], [true, true]]`, `[[false, true], [true, true]]`, `[[true, true], [true, false]]`.
*   **Ruins of Alph Ledges:** Some ledges in RuinsOfAlphOutside, like the one at (2, 19), lead to small grassy areas. These are not traps; a path out exists at (2, 21).
*   **Southern Area Inaccessibility:** The southern part of RuinsOfAlphOutside is not accessible from the northern part. The connecting path is likely through Union Cave.

### Goldenrod Dept. Store Basement Puzzle
*   **Mechanic:** A dynamic box-pushing maze where Black Belts move and create/remove walls based on the player's position. The goal is to clear a path to the ladder at (17, 2).
*   **Hypothesis:** A specific sequence of movements and interactions with the Black Belts is required to open the path.

## VI. Untested Hypotheses & Future Plans
*   **`CUT_TREE` Respawn Conditions:** A `CUT_TREE` at (8, 25) in Ilex Forest respawned. I need to test the exact conditions. Next time I cut a tree near a map transition, I will immediately leave and re-enter the map to check if it has respawned.
*   **Puzzle Solver Tool Idea:** If I get stuck on visual puzzles, I should define a `puzzle_solver` tool.
    - **Input:** A representation of the puzzle grid (e.g., a 2D array of piece IDs) and a target configuration.
    - **Output:** A sequence of moves (e.g., `["pick(x1,y1)", "place(x2,y2)"]`) to solve it.
    - **Logic:** This would require an algorithm like A* search or a similar pathfinding/planning algorithm to find the optimal sequence of moves. It is a computational task, perfect for a tool.