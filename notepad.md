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
*   **Obstacle:** Attempting to battle Camper Ivan at (4, 19) triggers a repetitive phone call about radio music, preventing the battle from starting. This is confirmed to be the only puzzle trigger.
*   **Confirmed Failure 1:** Defeating the nearby Lass (Picnicker Brooke) at (7, 20) has no effect on the puzzle. The phone call loop persists.
*   **Confirmed Failure 2:** Navigating the Pokégear by pressing 'Right' repeatedly fails due to the 'Whom do you want to call?' sub-menu on the Phone tab, which blocks further navigation. Exiting with 'B' is necessary but has led to a failure loop.
*   **New Hypothesis:** The Pokégear menu may wrap around. Pressing 'Left' from the starting Clock tab might immediately navigate to the Radio tab, bypassing the Map and Phone tabs.
*   **Test Plan:** 1. Open the Start Menu. 2. Select POKéGEAR. 3. Once in the Pokégear (on the Clock tab), immediately press 'Left'. 4. If this accesses the Radio, interact with it. 5. Exit all menus and attempt to battle Camper Ivan again.

### Goldenrod SQUIRTBOTTLE Quest
*   **Primary Hypothesis:** I must find the flower shop lady's sister on Route 36 to receive the SQUIRTBOTTLE.
*   **Alternative Hypothesis:** The sister might not be the trigger. Progressing the Radio Tower quest (investigating the Director) might be the actual trigger for obtaining the SQUIRTBOTTLE, as it's another major unresolved plot point in Goldenrod City.
*   **Test Plan:** 1. Thoroughly explore Route 35 and the entrance to Route 36. 2. If the sister is not found, I will pivot my focus to the Radio Tower before returning to this quest.

## IV. Agent & Tool Development
*   **`path_master_v27`:** DELETED. This tool was consistently failing to find valid paths.
*   **`maze_solver_v1` Limitation:** The tool can only see objects currently on screen. For it to navigate around off-screen obstacles (like NPCs), I MUST manually provide their coordinates using the `extra_impassable_coordinates` parameter. This is a user responsibility, not a code bug.
*   **`nickname_genius` Testing:** Must use this agent the next time a Pokémon is caught to evaluate its performance.
*   **`quest_strategist`:** This agent should be used for getting unstuck on complex puzzles.
*   **`ui_navigator`:** Has been refined to understand the 'B' button is for backing out of sub-menus.