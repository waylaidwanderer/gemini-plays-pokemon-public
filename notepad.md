# Gem's Pokémon Crystal Notepad

## I. Game Systems & Mechanics

### Tile Traversal Protocol
- **Testing Mandate:** When a new, reachable tile type is seen, I MUST test it immediately.
- **Movement Test:** Attempt to move *into* and *out of* the tile from all 4 cardinal directions to verify passability.
- **Interaction Test:** If movement fails, I must attempt to interact with the tile by facing it and pressing 'A'.
- **Ledge Test:** For any ledge-like tile, I must attempt to move up/against the apparent direction of the ledge to confirm if it is a one-way path.

### Verified Tile Types
*   **Impassable:** `WALL`, `PILLAR`, `BOOKSHELF`, `TV`, `RADIO`, `TOWN_MAP`, `STATUE`, `TABLE`, `CHAIR`, `BIRD` (Farfetch'd), `MART_SHELF`, `BUOY`, `PC`, `LINK_CABLE`, `TRADE_MACHINE`, `INCENSE_BURNER`, `ROOF`, `CHIMNEY`, `SIGN`, `FLOWER`, `TREE_TOP`, `WATER_EDGE_UP`, `WATER_EDGE_DOWN`, `WATER_EDGE_LEFT`, `WATER_EDGE_RIGHT`, `VOID`, `COUNTER`, `FENCE`, `PC`, `LINK_RECEPTIONIST`, `WINDOW`, `WEIRD_TREE`.
*   **Traversable:** `FLOOR`, `GRASS`, `TALL_GRASS`, `LONG_GRASS`, `RAILING`, `PIPE_HORIZONTAL`, `PIPE_VERTICAL`.
*   **Warps:** `DOOR`, `CAVE`, `LADDER`, `STAIRCASE` (Move onto tile), `PIT` (Acts as a warp when stepped on).
*   **One-Way Ledges:** 
    * `LEDGE_HOP_DOWN/RIGHT`: A one-way ledge that can only be hopped in the specified direction.
    * `LEDGE_HOP_LEFT`: A one-way ledge that can only be hopped **LEFT**.
    * `FLOOR_UP_WALL`: A complex one-way ledge. It acts as a wall when approached from above (cannot move down onto it). You can move onto it from a tile below it. You can move horizontally between adjacent `FLOOR_UP_WALL` tiles. You can move down *off* of it to a tile below. You cannot move up from this tile.
*   **Special Requirement:** 
    * `CUT_TREE` (Requires HM01 Cut. These trees can respawn after being cut).
    * `WATER` (Requires HM03 Surf. To initiate, face the water and press 'A').
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
*   **TMs:** TM08 (ROCK SMASH), TM12 (SWEET SCENT), TM28 (DIG), TM30 (SHADOW BALL), TM45 (ATTRACT), TM49 (FURY CUTTER)

## III. Badges
*   **ZEPHYR BADGE**
*   **HIVE BADGE**
*   **PLAIN BADGE**
*   **FOG BADGE** (Allows use of SURF outside battle, makes Pokémon up to L50 obey)

## IV. Blocked Paths & Story Gates
*   **Route 37 Trainer Blockade:** Twins Ann & Anne disguised as trees block the path north at (6, 12) and (7, 12). This path is story-locked.
*   **Goldenrod Underground Blockade:** A Super Nerd blocks the path south at (5, 31). This path is story-locked.

## V. Puzzles & Hypotheses

### Ruins of Alph
*   **Ho-Oh Puzzle:** A 16-piece puzzle on a 6x6 grid. Goal is to assemble Ho-Oh in the central 4x4 area. I must use the `puzzle_analyst` agent the next time I attempt this puzzle.
*   **Southern Area Inaccessibility:** The southern part of RuinsOfAlphOutside is not accessible from the northern part. The connecting path is likely through Union Cave.

### Goldenrod Dept. Store Basement Puzzle
*   **Mechanic:** A dynamic box-pushing maze where Black Belts move and create/remove walls based on the player's position. The goal is to clear a path to the ladder at (17, 2).

## VI. Lessons Learned & Process Improvement
*   **Tool Development:** When a tool is not working, I must stop and debug it properly using `run_code` and print statements before defining a new version. My repeated failures with pathfinders were due to not rigorously testing against my documented mechanics. The tool's core logic failed because it assumed automatic land-to-water transitions, but the game requires an interaction ('A' button press) to initiate SURF. This must be accounted for in future pathfinder versions.
*   **Immediate Action:** I must act on new information immediately. Deferring tasks like marking warps or fixing tools is an invalid and inefficient strategy.
*   **Hypothesis Testing:** When stuck, I must form multiple, alternative hypotheses and test them systematically to avoid confirmation bias. I will document these hypotheses in my notepad.