# Gem's Pokémon Crystal Notepad

## I. Game Systems & Mechanics

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
    *   `FLOOR_UP_WALL`: A complex one-way ledge with specific traversal rules:
    *   You can move **UP** from a `FLOOR` tile onto a `FLOOR_UP_WALL` tile.
    *   You can move **DOWN** from a `FLOOR_UP_WALL` tile onto a `FLOOR` tile (this is the one-way jump).
    *   You can move horizontally between adjacent `FLOOR_UP_WALL` tiles.
    *   You **CANNOT** move **DOWN** from a `FLOOR` tile onto a `FLOOR_UP_WALL` tile.
    *   You **CANNOT** move **UP** from a `FLOOR_UP_WALL` tile into a `WALL` or other impassable tile.
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

## II. Blocked Paths & Story Gates
*   **Route 37 Trainer Blockade:** Twins Ann & Anne disguised as trees block the path north at (6, 12) and (7, 12).
*   **Goldenrod Underground Blockade:** A Super Nerd blocks the path south at (5, 31).

## III. Solved Puzzles & Completed Quests
*This section is for major, multi-step puzzles that have been fully resolved.*

## V. Area and Navigation Insights
*   **Route 32 Pier:** The pier is divided into multiple sections by one-way ledges. The easternmost section (where Cooltrainer M is) is a one-way path heading south. It does not connect directly to the main pier area where the other fishers are.

## IV. Strategic Plans

### Primary Goal: Defeat Olivine City Gym Leader
1.  **Travel to Olivine City.**
2.  **Locate the Gym Leader.** Rival SILVA mentioned she is at the Lighthouse.
3.  **Ascend the Lighthouse.** This seems to be a prerequisite to challenging the gym.
4.  **Challenge and defeat the Gym Leader.**

### Secondary Goal: Ascend the Olivine Lighthouse
1.  **Re-enter the Lighthouse.**
2.  **Systematically explore each floor.** I previously missed the way up, so I need to check every path and interaction point.
3.  **Look for hidden paths or puzzles.** There might be a trick to ascending that isn't obvious.

### Tertiary Goal: Heal the Miltank
1.  **Collect BERRIES.** I need to find Fruit Trees that have regrown their fruit.
2.  **Return to Route 39 Farmhouse.**
3.  **Give the BERRIES to the sick Miltank.**