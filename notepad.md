# Gem's Pokémon Crystal Notepad

## I. Current Objectives & Plans
*   **Primary Goal:** Find and defeat the Olivine City Gym Leader.
*   **Secondary Goal:** Find a way to ascend the Olivine Lighthouse. My hypothesis is that the Gym Leader is at the top, and I need to help the sick Pokémon there.
*   **Tertiary Goal:** Find more BERRIES to heal the sick Miltank on Route 39.
*   **Current Plan:** After a long detour in the Ruins of Alph, I am now back on Route 32. My plan is to travel south, exploring the route incrementally, to reach Union Cave and eventually Olivine City.

## II. Game Systems & Mechanics

### Tile Traversal Protocol
- **Testing Mandate:** When a new, reachable tile type is seen, I MUST test it immediately.
- **Movement Test:** Attempt to move *into* and *out of* the tile from all 4 cardinal directions to verify passability.
- **Interaction Test:** If movement fails, I must attempt to interact with the tile by facing it and pressing 'A'.
- **Ledge Test:** For any ledge-like tile, I must attempt to move up/against the apparent direction of the ledge to confirm if it is a one-way path.

### Verified Tile Types
*   **Impassable:** `WALL`, `PILLAR`, `BOOKSHELF`, `TV`, `RADIO`, `TOWN_MAP`, `STATUE`, `TABLE`, `CHAIR`, `BIRD` (Farfetch'd), `MART_SHELF`, `BUOY`, `PC`, `LINK_CABLE`, `TRADE_MACHINE`, `INCENSE_BURNER`, `ROOF`, `CHIMNEY`, `SIGN`, `FLOWER`, `TREE_TOP`, `WATER_EDGE_UP`, `WATER_EDGE_DOWN`, `WATER_EDGE_LEFT`, `WATER_EDGE_RIGHT`, `VOID`, `COUNTER`, `FENCE`, `PC`, `LINK_RECEPTIONIST`, `WINDOW`, `WEIRD_TREE`, `PRINTER`.
*   **Traversable:** `FLOOR`, `GRASS`, `TALL_GRASS`, `LONG_GRASS`, `RAILING`, `PIPE_HORIZONTAL`, `PIPE_VERTICAL`.
*   **Warps:** `DOOR`, `CAVE`, `LADDER`, `STAIRCASE` (Move onto tile), `PIT` (Acts as a warp when stepped on).
*   **One-Way Ledges:**
    *   `LEDGE_HOP_DOWN`: A one-way ledge that can only be hopped **DOWN**.
    *   `LEDGE_HOP_DOWN/RIGHT`: A one-way ledge that can only be hopped in the specified direction.
    *   `LEDGE_HOP_LEFT`: A one-way ledge that can only be hopped **LEFT**.
    *   `FLOOR_UP_WALL`: A complex one-way ledge. You can move onto it from a tile below it, move horizontally between adjacent `FLOOR_UP_WALL` tiles, and move down *off* of it to a tile below. You cannot move up from this tile or down onto it.
*   **Special Requirement:**
    *   `CUT_TREE` (Requires HM01 Cut).
    *   `WATER` (Requires HM03 Surf).
    *   `BREAKABLE_ROCK` (Requires Rock Smash).
    *   `HEADBUTT_TREE` (Requires the move Headbutt).
*   **Complex Tiles:**
    *   `WARP_CARPET_DOWN/LEFT/RIGHT`: Traversable. Activated by pressing the corresponding direction while standing on the tile to trigger a warp.
    *   `WARP_CARPET_DOWN`: Traversable. Activated by pressing 'Down' while standing on the tile to trigger a warp.
    *   `unknown` (Puzzle Trigger): In the Ruins of Alph puzzle chambers, standing on the tile at (3,3) and interacting with the object at (3,2) activates the puzzle interface.

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

## III. Blocked Paths & Story Gates
*   **Route 37 Trainer Blockade:** Twins Ann & Anne disguised as trees block the path north at (6, 12) and (7, 12).
*   **Goldenrod Underground Blockade:** A Super Nerd blocks the path south at (5, 31).

## IV. Solved Puzzles & Completed Quests

### Ruins of Alph Sliding Puzzles
*   **General Mechanics:** These are 16-piece picture puzzles on a 6x6 grid. The goal is to assemble the image in the central 4x4 area.
*   **Ho-Oh Puzzle:** Solved.
*   **Omanyte Puzzle:** Solved.
*   **Aerodactyl Puzzle:** Solved. The key was to interact with the sign at (4,2) to see the target image, then arrange the pieces visually, not numerically.

### Goldenrod Dept. Store Basement Puzzle
*   **Mechanic:** A dynamic box-pushing maze where Black Belts move and create/remove walls based on the player's position.

## V. Puzzle Hypotheses & Logs

## VI. Process Improvement & Future Plans
*   **Immediate Data Management:** All data management tasks MUST be performed in the same turn they are identified.
*   **Hypothesis Testing:** When stuck, I must systematically test alternative hypotheses instead of getting locked into one approach. I will document these tests and their outcomes in my notepad.
*   **Tool Refinement:** Faulty tools must be refined immediately. This is a higher priority than any gameplay action.