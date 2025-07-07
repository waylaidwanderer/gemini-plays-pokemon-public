# Gem's Pokémon Crystal Notepad

## I. Game Systems & Mechanics

### Tile Traversal Protocol
- **Testing Mandate:** When a new, reachable tile type is seen, I MUST test it immediately.
- **Movement Test:** Attempt to move *into* and *out of* the tile from all 4 cardinal directions to verify passability.
- **Ledge Test:** For any ledge-like tile, I must attempt to move up/against the apparent direction of the ledge to confirm if it is a one-way path.

### Verified Tile Types
*   **Impassable:** `WALL`, `HEADBUTT_TREE`, `PC`, `PILLAR`, `BOOKSHELF`, `TV`, `RADIO`, `TOWN_MAP`, `WINDOW`, `STATUE`, `TABLE`, `CHAIR`, `BIRD` (Farfetch'd), `CUT_TREE`, `VOID`, `MART_SHELF`, `COUNTER`, `COUNTER`
*   **Traversable:** `FLOOR`, `GRASS`, `TALL_GRASS` (Wild Encounters)
*   **Warps:** `DOOR`, `CAVE`, `LADDER` (Move onto tile), `STAIRCASE` (Move onto tile). Gatehouse warps are triggered by walking into the building side.
*   **One-Way Ledges:** `LEDGE_HOP_DOWN/LEFT/RIGHT`. Verified by attempting to move against the ledge direction.
*   **Complex Tiles:**
    *   `FLOOR_UP_WALL`: One-way ledge. Enter from below/sides. Cannot exit by moving up.
    *   `WARP_CARPET_LEFT`: Activated by pressing 'Left' while standing on the tile.
    *   `WARP_CARPET_DOWN`: Activated by pressing 'Down' while standing on the tile.

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
*   **SQUIRTBOTTLE:** A bottle for watering Pokémon. Needed for the strange tree on Route 36.
*   **TM45 (ATTRACT):** Makes full use of a POKéMON's charm.
*   **TM49 (Fury Cutter):** Gets stronger with each consecutive hit.

## III. Active Puzzles & Hypotheses

### Route 35 Phone Call Loop
*   **Obstacle:** Attempting to battle Camper Ivan at (4, 19) triggers a repetitive phone call about radio music, preventing the battle from starting. This is confirmed to be the only puzzle trigger.
*   **Confirmed Failure 1:** Defeating the nearby Lass (Picnicker Brooke) at (7, 20) has no effect on the puzzle. The phone call loop persists.
*   **Confirmed Failure 2:** Navigating the Pokégear by pressing 'Right' repeatedly fails due to the 'Whom do you want to call?' sub-menu on the Phone tab, which blocks further navigation. Exiting with 'B' is necessary but has led to a failure loop.
*   **Confirmed Failure 3:** The Pokégear menu does not wrap around. Pressing 'Left' from the Clock tab has no effect.

## IV. Agent & Tool Development
*   **`pathfinder_v1`:** My standard, consolidated pathfinding tool. Replaced and deleted `path_master_v24` and `maze_explorer_v8`.
*   **`nickname_genius` Testing:** Must use this agent the next time a Pokémon is caught to evaluate its performance.
*   **`quest_strategist`:** This agent should be used for getting unstuck on complex puzzles.
*   **`ui_navigator`:** Has been refined to understand the 'B' button is for backing out of sub-menus.

### Radio Tower Side Quests
*   **Buena's Password Show:** Received a BLUE CARD from Buena on the 2nd floor. I can earn points by giving her passwords from the radio and trade them for prizes.

## V. To-Do & Testing
*   **Agent Test:** Use `nickname_genius` after the next Pokémon capture to evaluate its performance.

## VI. Future Development Ideas
*   **Navigation Master Agent:** Create a high-level agent that takes a destination (e.g., a city name) and uses the `pathfinder_v1` tool to plot the full course, including navigating between maps and through warps.