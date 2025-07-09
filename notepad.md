# Gem's Pokémon Crystal Notepad

## I. Strategic Plan
*   **Primary Goal: Find and defeat the Ecruteak City Gym Leader.**
    *   **Status:** Morty is likely back in the Ecruteak Gym after the Burned Tower event. Need to acquire Repels before returning.
*   **Secondary Goal: Acquire Repels to explore the Burned Tower safely.**
    *   **Status:** The Goldenrod Dept. Store does not sell Repels. New plan is to find a standard Poké Mart in Goldenrod City.
*   **Tertiary Goal: Investigate the mystery of the legendary beasts.**
    *   **Status:** Witnessed their awakening. Eusine is also tracking them.

## II. Game Systems & Mechanics

### Tile Traversal Protocol
- **Testing Mandate:** When a new, reachable tile type is seen, I MUST test it immediately.
- **Movement Test:** Attempt to move *into* and *out of* the tile from all 4 cardinal directions to verify passability.
- **Ledge Test:** For any ledge-like tile, I must attempt to move up/against the apparent direction of the ledge to confirm if it is a one-way path.

### Verified Tile Types
*   **Impassable:** `WALL`, `HEADBUTT_TREE`, `PILLAR`, `BOOKSHELF`, `TV`, `RADIO`, `TOWN_MAP`, `WINDOW`, `STATUE`, `TABLE`, `CHAIR`, `BIRD` (Farfetch'd), `MART_SHELF`, `BUOY`, `PC`, `LINK_CABLE`, `TRADE_MACHINE`, `INCENSE_BURNER`, `COUNTER`, `ROOF`, `CHIMNEY`, `SIGN`, `FLOWER`, `TREE_TOP`, `WATER_EDGE_UP`, `WATER_EDGE_DOWN`, `WATER_EDGE_LEFT`, `WATER_EDGE_RIGHT`, `VOID`.
*   **Traversable:** `FLOOR`, `GRASS`, `TALL_GRASS`, `LONG_GRASS`, `RAILING`, `PIPE_HORIZONTAL`, `PIPE_VERTICAL`.
*   **Warps:** `DOOR`, `CAVE`, `LADDER`, `STAIRCASE` (Move onto tile).
*   **One-Way Ledges:** 
    * `LEDGE_HOP_DOWN/LEFT/RIGHT`.
    * `FLOOR_UP_WALL`: A one-way ledge that can only be hopped **UP**.
*   **Special Requirement:** 
    * `CUT_TREE` (Requires HM01 Cut).
    * `WATER` (Requires HM03 Surf).
    * `BREAKABLE_ROCK` (Requires Rock Smash).
*   **Complex Tiles:**
    *   `WARP_CARPET_LEFT/RIGHT/DOWN`: Activated by pressing the indicated direction while standing on the tile.
    *   `Push-Down Trap`: A `FLOOR` tile that, when stepped on, pushes the player down one tile.

### Unverified Tile Types & Mechanics
*   **PIT:** A hole in the floor that appeared after the rival battle in the Burned Tower. It is the correct path to the basement, but its exact mechanics (one-way drop vs. two-way) are unconfirmed.

### Other Mechanics
*   **Object Impassability:** All Map Objects (NPCs, items, signs, etc.) are impassable.
*   **Item Effects:**
    *   **BERRY:** Restores 10 HP.
    *   **EVERSTONE:** Prevents evolution.
    *   **MOOMOO MILK:** Restores 100 HP.
    *   **HARD STONE:** Powers up rock-type moves.
    *   **PRZCUREBERRY:** Cures paralysis.
    *   **HYPER POTION:** Restores 200 HP.
*   **Haircuts:** Increases a Pokémon's happiness.

## III. Key Items & TMs
*   **COIN CASE**
*   **HM01 (CUT)**
*   **HM03 (SURF)**
*   **SQUIRTBOTTLE** (Used)
*   **TM08 (ROCK SMASH)**
*   **TM12 (SWEET SCENT)**
*   **TM28 (DIG)**
*   **TM45 (ATTRACT)**
*   **TM49 (FURY CUTTER)**

## IV. Untested Hypotheses
*   **Morty's Location:**
    *   **Hypothesis:** Morty has returned to the Ecruteak Gym.
    *   **Alternative:** Morty is not in the gym and is somewhere else in Ecruteak City, or has left the city entirely.
    *   **Test:** After acquiring Repels, I will return to Ecruteak City and check the Gym.
*   **Repel Location:**
    *   **Hypothesis 1 (Falsified):** Repels are sold in the Goldenrod Dept. Store. (Result: False. Checked all 6 floors).
    *   **Hypothesis 2:** Repels are sold in a standard Poké Mart in Goldenrod City.
    *   **Test:** Find the standard Mart in Goldenrod City and check its inventory.
*   **Goldenrod Dept. Store Basement Puzzle:**
    *   **Status:** Abandoned. Interacting with all four NPCs in the area did not open the path to the items, as confirmed by the pathfinder tool. The visual changes were misleading. Will return later if a key item or event is discovered elsewhere.