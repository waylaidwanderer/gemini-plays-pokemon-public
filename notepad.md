# Gem's Pokémon Crystal Notepad

## I. Game Systems & Mechanics

### Tile Traversal Protocol
- **Testing Mandate:** When a new, reachable tile type is seen, I MUST test it immediately.
- **Movement Test:** Attempt to move *into* and *out of* the tile from all 4 cardinal directions. Document results.
- **Interaction Test:** If movement fails, I must attempt to interact with the tile by facing it and pressing 'A'. Document results.
- **Ledge Test:** For any ledge-like tile, I must attempt to move against the apparent direction of the ledge to confirm if it is a one-way path. Document results.

### Verified Tile Types
*   **Impassable (Verified):** `WALL`, `PILLAR`, `BOOKSHELF`, `TV`, `RADIO`, `TOWN_MAP`, `STATUE`, `TABLE`, `CHAIR`, `BIRD` (Farfetch'd), `MART_SHELF`, `PC`, `LINK_CABLE`, `TRADE_MACHINE`, `INCENSE_BURNER`, `ROOF`, `CHIMNEY`, `SIGN`, `FLOWER`, `TREE_TOP`, `WATER_EDGE_UP`, `WATER_EDGE_DOWN`, `WATER_EDGE_LEFT`, `WATER_EDGE_RIGHT`, `VOID`, `COUNTER`, `FENCE`, `LINK_RECEPTIONIST`, `WEIRD_TREE`, `PRINTER`, `BUOY`, `WINDOW`.
*   **Traversable (Verified):** `GRASS`, `TALL_GRASS`, `LONG_GRASS`, `RAILING`, `PIPE_HORIZONTAL`, `PIPE_VERTICAL`, `CUT_TREE` (becomes traversable after using CUT), `FLOOR`.
*   **Warps (Verified):** `DOOR`, `CAVE`, `LADDER`, `STAIRCASE` (Move onto tile), `PIT` (Acts as a one-way warp when stepped on).
*   **One-Way Ledges (Verified):**
    *   `LEDGE_HOP_DOWN`: A one-way ledge that can only be hopped **DOWN**.
    *   `LEDGE_HOP_DOWN/RIGHT`: A one-way ledge that can only be hopped in the specified direction.
    *   `LEDGE_HOP_LEFT`: A one-way ledge that can only be hopped **LEFT**.
    *   `FLOOR_UP_WALL`: A complex one-way ledge. Can move **UP** from `FLOOR` to `FLOOR_UP_WALL`. Can move **DOWN** from `FLOOR_UP_WALL` to `FLOOR` (the jump). Cannot move **DOWN** from `FLOOR` to `FLOOR_UP_WALL`.
*   **Special Requirement (Verified):**
    *   `WATER` (Requires HM03 Surf, must be used from adjacent `FLOOR` tile).
    *   `BREAKABLE_ROCK` (Requires Rock Smash).
*   **Complex Tiles (Verified):**
    *   `WARP_CARPET_DOWN`: Traversable. Activated by pressing 'Down' while standing on the tile to trigger a warp.
    *   `WARP_CARPET_DOWN/LEFT/RIGHT`: Traversable. Activated by pressing the corresponding direction while standing on the tile to trigger a warp.
    *   `WARP_CARPET_LEFT`: Traversable. Activated by pressing 'Left' while standing on the tile to trigger a warp.

### Other Mechanics
*   **Object Impassability:** All Map Objects (NPCs, items, signs, etc.) are impassable.
*   **Haircuts:** Increases a Pokémon's happiness.

## II. Strategic Plans & Hypotheses

### Current Quest: The Secret Medicine
*   **Goal:** Find the special medicine in Cianwood City to cure the sick Ampharos in the Olivine Lighthouse.
*   **Current Hypothesis:** The medicine will be given to me after defeating the Cianwood City Gym Leader. This is the most common method of story progression in Pokémon games.
*   **Alternative Hypothesis:** The medicine is held by an NPC I haven't spoken to yet, or is hidden behind a boulder that requires ROCK SMASH.

### Verified Conclusions
*   The Olivine Lighthouse has no further upward paths. It is a dead end for now.
*   The sea route directly south of the Olivine City pier is blocked by buoys.
*   There is no pharmacy or obvious medicine-related building in Cianwood City. All buildings have been explored.

### Untested Hypotheses
*   **WHIRLPOOL Mechanics:** My rival mentioned the Whirl Islands are blocked by whirlpools. I need to test a `WHIRLPOOL` tile to see if it requires a specific HM. I will use my `pathfinder` to navigate to an adjacent tile and then interact with it.

### Cianwood Gym Puzzle
### Cianwood Gym Puzzle
*   **Hypothesis 1 (Trainers):** Defeating trainers causes boulders to appear or disappear, changing the gym layout. This was invalidated as interacting with the trainers yielded no battle.
*   **Hypothesis 2 (Statue Switches - INVALIDATED):** The statues at the gym entrance might be switches.
    *   **Test 1 (Left Statue @ 3,15):** Interacting with the statue only displayed the gym name.
    *   **Test 2 (Right Statue @ 6,15):** Interacting with the statue also only displayed the gym name.
    *   **Conclusion:** The statues are not switches. This hypothesis is fully invalid.
*   **New Hypothesis (Side Paths):** The solution to the puzzle may involve exploring the side paths of the gym that I have not yet fully traversed. I will start by exploring the leftmost path.
*   **Hypothesis 3 (Agent Advice - INVALIDATED):** The `gym_puzzle_advisor` repeatedly suggested battling Black Belt Yoshi at (3, 12). 
    *   **Test 1 & 2:** Interacting with Yoshi only resulted in dialogue, with no battle initiated. This was tested before and after moving on the side paths.
    *   **Conclusion:** The agent's logic is flawed for this dynamic puzzle. It cannot be relied upon for this gym. My own manual exploration based on the 'side path' hypothesis is the only strategy that has produced observable changes in the gym.