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

### Cianwood Gym Puzzle
*   **Confirmed Mechanic:** Movement on the side paths (x=1 and x=8) is the PRIMARY mechanism for changing the state of the gym (making trainers/boulders appear, disappear, or move).
*   **Hypothesis 1 (Trainers - INVALIDATED):** Defeating trainers causes boulders to appear or disappear. This was invalidated as interacting with the trainers yielded no battle.
*   **Hypothesis 2 (Statue Switches - INVALIDATED):** The statues at the gym entrance are switches. This was invalidated as interacting with both statues only displayed the gym name.
*   **Hypothesis 3 (Agent Assistance - INVALIDATED):** The `gym_puzzle_advisor` agent, even after multiple refinements, has repeatedly suggested battling trainers who are not battle-ready or moving into walls. The agent is fundamentally unable to solve this dynamic puzzle. It will not be used for this gym.
*   **Hypothesis 4 (Western Path - INVALIDATED):** The western side path (x=1) is a dead end. Full exploration yielded no path forward.
*   **Current Working Hypothesis (Eastern Path):** The solution must involve exploring the eastern side path (x=8), which remains untouched.

### Future Plans & Untested Theories
*   **Tool Idea (`gym_state_tester`):** Create a tool that takes a sequence of moves as input and executes them, reporting back if any map objects appear, disappear, or move. This would automate testing the side paths.
*   **Alternative Puzzle Hypothesis 1 (Step Count - INVALIDATED):** The puzzle is not based on total steps taken. Walking 50 steps at the entrance caused no changes.
*   **Alternative Puzzle Hypothesis 2 (Facing Direction):** The trigger might depend on the direction the player is facing when stepping onto a specific trigger tile. **Test:** Step onto a known trigger tile like (1, 14) while facing different cardinal directions.
*   **Alternative Puzzle Hypothesis 2 (Facing Direction):** The trigger might depend on the direction the player is facing when stepping onto a specific tile. **Test:** Step onto a known trigger tile like (1, 14) while facing different cardinal directions.