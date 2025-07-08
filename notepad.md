# Gem's Pokémon Crystal Notepad

## I. Core Directives & Principles
*   **Act Immediately:** As an LLM, I have no concept of 'later'. Any task I decide on (agent/tool creation/refinement, documentation) MUST be performed in the current turn. Deferring tasks is a critical failure.

## II. Strategic Plan
*   **Primary Goal: Find and defeat the Ecruteak City Gym Leader.**
    *   **Status:** Just arrived in Ecruteak City. Need to locate the Gym.
*   **Secondary Goal: Investigate Team Rocket's activities.**
    *   **Status:** Last seen in Goldenrod City's underground. No current leads.
*   **Tertiary Goal: Train ELEKID.**
    *   **Plan:** Keep ELEKID in the party to gain experience from battles.

## III. Game Systems & Mechanics

### Tile Traversal Protocol
- **Testing Mandate:** When a new, reachable tile type is seen, I MUST test it immediately.
- **Movement Test:** Attempt to move *into* and *out of* the tile from all 4 cardinal directions to verify passability.
- **Ledge Test:** For any ledge-like tile, I must attempt to move up/against the apparent direction of the ledge to confirm if it is a one-way path.
- **Obvious Tile Test:** Even if a tile seems obviously impassable (e.g., WALL), I must attempt to walk into it once to be 100% certain.

### Verified Tile Types
*   **Impassable:** `WALL`, `HEADBUTT_TREE`, `PILLAR`, `BOOKSHELF`, `TV`, `RADIO`, `TOWN_MAP`, `WINDOW`, `STATUE`, `TABLE`, `CHAIR`, `BIRD` (Farfetch'd), `VOID`, `MART_SHELF`, `WATER` (without Surf), `BUOY`, `PC`, `LINK_CABLE`, `TRADE_MACHINE`, `INCENSE_BURNER`, `COUNTER`, `ROOF`, `CHIMNEY`, `SIGN`, `FLOWER`, `TREE_TOP`, `WATER_EDGE_UP`, `WATER_EDGE_DOWN`, `WATER_EDGE_LEFT`, `WATER_EDGE_RIGHT`.
*   **Traversable:** `FLOOR`, `GRASS`, `TALL_GRASS` (Wild Encounters), `LONG_GRASS` (Wild Encounters), `RAILING`, `PIPE_HORIZONTAL`, `PIPE_VERTICAL`.
*   **Warps:** `DOOR`, `CAVE`, `LADDER`, `STAIRCASE` (Move onto tile).
*   **One-Way Ledges:** 
    * `LEDGE_HOP_DOWN/LEFT/RIGHT`.
    * `FLOOR_UP_WALL`: A one-way ledge that can only be hopped **UP**. It is impassable from above (acts as a wall).
*   **Special Requirement:** `CUT_TREE` (Requires HM01 Cut).
*   **Complex Tiles:**
    *   `WARP_CARPET_LEFT/RIGHT/DOWN`: Activated by pressing the indicated direction while standing on the tile.
    *   `Push-Down Trap`: A `FLOOR` tile that, when stepped on, pushes the player down one tile.
    *   `Interactable Warp (FLOOR)`: Some FLOOR tiles that are also warps must be interacted with by pressing 'A' to trigger an event or text.

### Other Mechanics
*   **Object Impassability:** All Map Objects (NPCs, items, signs, etc.) are impassable and function as walls.
*   **Item Effects:**
    *   **BERRY:** Restores 10 HP.
    *   **EVERSTONE:** Prevents evolution.
    *   **MOOMOO MILK:** Restores 100 HP.
    *   **HARD STONE:** Powers up rock-type moves.
    *   **PRZCUREBERRY:** Cures paralysis.
    *   **HYPER POTION:** Restores 200 HP.
*   **Haircuts:** Increases a Pokémon's happiness.
*   **Pokégear Phone Menu:** Must press 'B' to cancel the 'Whom to call?' prompt before switching functions.

## IV. Key Items & TMs
*   **COIN CASE:** Allows playing at the Game Corner.
*   **HM01 (CUT):** Clears small trees. Requires Hive Badge.
*   **SQUIRTBOTTLE:** Used to clear the Sudowoodo on Route 36.
*   **TM08 (ROCK SMASH)**
*   **TM12 (SWEET SCENT)**
*   **TM28 (DIG)**
*   **TM45 (ATTRACT)**
*   **TM49 (FURY CUTTER)**

## V. Archive: Solved Puzzles & Failed Hypotheses
*   **Skepticism Reminder:** Not all NPCs are trainers. Do not waste turns trying to battle non-battling NPCs.
*   **Failure Log (Navigation):** The path to Ecruteak City is NOT east of Route 36 (leads to Violet City) or west of Route 36 (dead end). **Lesson: If a path repeatedly fails, abandon the hypothesis and explore other routes.**
*   **Failure Log (Pathfinder v7):** The tool's failures are often a symptom of my own flawed strategy (e.g., pathing into unseen areas). **Lesson: Verify my strategic assumptions before blaming the tool.**
*   **Hypothesis Failure (Radio Tower):** The Plain Badge does NOT grant access to the upper floors of the Radio Tower. The Black Belt at (0, 1) on 2F still blocks the path, citing an issue with the Director. (Turn #29187)