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
    *   `LEDGE_HOP_DOWN`: A one-way ledge that can only be hopped **DOWN**. Attempting to move up against it fails.
    *   `LEDGE_HOP_DOWN/RIGHT`: A one-way ledge that can only be hopped in the specified direction.
    *   `LEDGE_HOP_LEFT`: A one-way ledge that can only be hopped **LEFT**.
    *   `FLOOR_UP_WALL`: A complex one-way ledge. You can move onto it from a tile below it, move horizontally between adjacent `FLOOR_UP_WALL` tiles, and move down *off* of it to a tile below. You cannot move up from this tile or down onto it from a standard `FLOOR` or `LADDER` tile.
*   **Special Requirement:**
    *   `CUT_TREE` (Requires HM01 Cut. These trees can respawn after being cut).
    *   `WATER` (Requires HM03 Surf. To initiate, face the water and press 'A').
    *   `BREAKABLE_ROCK` (Requires Rock Smash).
    *   `HEADBUTT_TREE` (Requires the move Headbutt. Confirmed that interacting without the move does nothing).
*   **Complex Tiles:**
    *   `WARP_CARPET_DOWN/LEFT/RIGHT`: Traversable. Activated by pressing the corresponding direction while standing on the tile to trigger a warp.
    *   `WARP_CARPET_DOWN`: Traversable. Activated by pressing 'Down' while standing on the tile to trigger a warp.
    *   `unknown` (Puzzle Trigger): In the Ruins of Alph puzzle chambers (Ho-Oh, Omanyte, Aerodactyl), standing on the tile at (3,3) and facing up to interact with the object at (3,2) activates the puzzle interface. In other locations, such as RuinsOfAlphOutside at (2,18), it functions as a standard traversable floor tile.

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

## II. Blocked Paths & Story Gates
*   **Route 37 Trainer Blockade:** Twins Ann & Anne disguised as trees block the path north at (6, 12) and (7, 12). This path is story-locked.
*   **Goldenrod Underground Blockade:** A Super Nerd blocks the path south at (5, 31). This path is story-locked.

## III. Puzzles & Hypotheses

### Ruins of Alph Sliding Puzzles
*   **General Mechanics:** These are 16-piece picture puzzles on a 6x6 grid. The goal is to assemble the image in the central 4x4 area. Pieces are picked up and placed, not slid.
*   **Ho-Oh Puzzle:** Solved by manually assembling the image.
*   **Omanyte Puzzle:** Solved by manually assembling the image.
*   **Aerodactyl Puzzle:**
    *   **Hypothesis (H1 - Disproven):** The puzzle is not solved by visually assembling the image.
    *   **Hypothesis (H2 - Disproven):** The solution is a magic square logic puzzle. The `puzzle_solver` agent provided an incorrect arrangement. This hypothesis has been tested and failed.
*   **Hypothesis (H3 - Active):** The puzzle must be solved by visually assembling the image of Aerodactyl. I will now attempt this.

### Goldenrod Dept. Store Basement Puzzle
*   **Mechanic:** A dynamic box-pushing maze where Black Belts move and create/remove walls based on the player's position. The goal is to clear a path to the ladder at (17, 2).

## IV. Process Improvement & Future Plans
*   **Immediate Data Management:** All data management tasks (notepad edits, marker placement, tool/agent definition) MUST be performed in the same turn they are identified. Deferring these tasks is a critical process failure.
*   **Hypothesis Testing:** When stuck, I must systematically test alternative hypotheses instead of getting locked into one approach. I will document these tests and their outcomes in my notepad.