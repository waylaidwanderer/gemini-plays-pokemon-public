# Gem's Pokémon Crystal Notepad

## I. Game Systems & Mechanics

### Tile Traversal Protocol
- **Testing Mandate:** When a new, reachable tile type is seen, I MUST test it immediately.
- **Movement Test:** Attempt to move *into* and *out of* the tile from all 4 cardinal directions to verify passability.
- **Ledge Test:** For any ledge-like tile, I must attempt to move up/against the apparent direction of the ledge to confirm if it is a one-way path.

### Verified Tile Types
*   **Impassable:** `WALL`, `HEADBUTT_TREE`, `PC`, `PILLAR`, `BOOKSHELF`, `TV`, `RADIO`, `TOWN_MAP`, `WINDOW`, `STATUE`, `TABLE`, `CHAIR`, `BIRD` (Farfetch'd), `CUT_TREE`, `COUNTER`, `VOID`, `MART_SHELF`
*   **Traversable:** `FLOOR`, `GRASS`, `TALL_GRASS` (Wild Encounters)
*   **Warps:** `DOOR`, `CAVE`, `LADDER` (Move onto tile), `STAIRCASE` (Move onto tile). Gatehouse warps are triggered by walking into the building side.
*   **One-Way Ledges:** `LEDGE_HOP_DOWN/LEFT/RIGHT`. Verified by attempting to move against the ledge direction.
*   **Complex Tiles:**
    *   `FLOOR_UP_WALL`: One-way ledge. Enter from below/sides. Cannot exit by moving up.
    *   `WARP_CARPET_DOWN`: One-way warp. Activated by pressing 'Down' while standing on the tile.

### Untested Tile Types (High Priority)
* `RAILING`: Located on the Goldenrod Dept. Store Roof.
* `PIPE_HORIZONTAL`
* `PIPE_VERTICAL`
* `WATER`
* `LINK_CABLE`: Located on Pokecenter2F.
* `TRADE_MACHINE`: Located on Pokecenter2F.

### Other Mechanics
*   **Item Effects:**
    *   **BERRY:** Restores 10 HP. Found at `FRUIT_TREE`s.
    *   **EVERSTONE:** Prevents evolution.
    *   **MOOMOO MILK:** Restores 100 HP.
*   **SLOWPOKETAIL:** Offered for sale on Route 32. Purpose unknown.
*   **Vending Machine Drinks:** Can refresh tired POKéMON.
*   **Hidden Items:** Must be interacted with from an adjacent tile.
*   **Haircuts:** Increases a Pokémon's happiness.
*   **Pokégear UI:** The Phone function has a sub-menu ('Whom do you want to call?'). This is a modal state. Directional buttons are DISABLED. You MUST press 'B' to exit this sub-menu and return to the main Pokégear navigation.

## II. Key Items & TMs
*   **COIN CASE:** Allows playing at the Game Corner. Found in the Goldenrod Underground.
*   **HM01 (CUT):** Clears small trees. Requires the Hive Badge.
*   **TM45 (ATTRACT):** Makes full use of a POKéMON's charm.
*   **TM49 (Fury Cutter):** Gets stronger with each consecutive hit.

## III. Active Puzzles & Hypotheses

### Route 35 Phone Call Loop
*   **Obstacle:** Attempting to battle Camper Ivan at (4, 19) triggers a repetitive phone call about radio music, preventing the battle from starting.
*   **Failed Hypothesis:** Simply pressing 'A' to dismiss the call and re-engage the trainer will work. (Failed multiple times).
*   **Primary Hypothesis:** The puzzle requires interacting with the Pokégear's radio function.
*   **Test Plan:** 1. Open Pokégear. 2. Navigate to the Radio function. 3. Try different stations or actions within the radio. 4. Exit the menu and attempt to battle Camper Ivan again.
*   **Alternative Hypothesis:** The battle with the nearby Lass at (7, 20) must be completed first.

### Goldenrod City Path Forward
*   **Obstacle:** The path east out of Goldenrod City is blocked by a strange tree (Sudowoodo).
*   **Primary Hypothesis:** A `SQUIRTBOTTLE` is required, as stated by the Pokefan F in the Route 35 Gatehouse.
*   **Alternative Hypothesis:** The tree can be cleared by other means, such as a Pokémon move (e.g., Headbutt) or by progressing a different quest line (e.g., the Radio Tower issue).
*   **Test Plan:** 1. Find the `SQUIRTBOTTLE` and attempt to use it. 2. If that fails or I cannot find it, I will return to the tree and try using Headbutt. 3. If both fail, I will prioritize the Radio Tower quest before returning to the tree.

## IV. Agent & Tool Development
*   **`maze_solver_v1` Limitation:** The tool can only see objects currently on screen. For it to navigate around off-screen obstacles (like NPCs), I MUST manually provide their coordinates using the `extra_impassable_coordinates` parameter. This is a user responsibility, not a code bug.
*   **`nickname_genius` Testing:** Must use this agent the next time a Pokémon is caught to evaluate its performance.
*   **`quest_strategist`:** This agent should be used for getting unstuck on complex puzzles.
*   **`ui_navigator`:** Has been refined to understand the 'B' button is for backing out of sub-menus.