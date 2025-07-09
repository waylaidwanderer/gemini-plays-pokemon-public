# Gem's Pokémon Crystal Notepad

## I. Strategic Plan
*   **Primary Goal: Find and defeat the Ecruteak City Gym Leader.**
    *   **Status:** Morty is back in the Ecruteak Gym. I am currently inside, trying to solve the gym's invisible path puzzle to reach him.
*   **Secondary Goal: Investigate the mystery of the legendary beasts.**
    *   **Status:** Witnessed their awakening in the Burned Tower. Eusine is also tracking them.
*   **Tertiary Goal: Acquire Repels to explore safely.**
    *   **Status:** This is a low priority. I will buy them if I find a Poké Mart that sells them.

## II. Game Systems & Mechanics

### Tile Traversal Protocol
- **Testing Mandate:** When a new, reachable tile type is seen, I MUST test it immediately.
- **Movement Test:** Attempt to move *into* and *out of* the tile from all 4 cardinal directions to verify passability.
- **Ledge Test:** For any ledge-like tile, I must attempt to move up/against the apparent direction of the ledge to confirm if it is a one-way path.

### Verified Tile Types
*   **Impassable:** `WALL`, `HEADBUTT_TREE`, `PILLAR`, `BOOKSHELF`, `TV`, `RADIO`, `TOWN_MAP`, `WINDOW`, `STATUE`, `TABLE`, `CHAIR`, `BIRD` (Farfetch'd), `MART_SHELF`, `BUOY`, `PC`, `LINK_CABLE`, `TRADE_MACHINE`, `INCENSE_BURNER`, `ROOF`, `CHIMNEY`, `SIGN`, `FLOWER`, `TREE_TOP`, `WATER_EDGE_UP`, `WATER_EDGE_DOWN`, `WATER_EDGE_LEFT`, `WATER_EDGE_RIGHT`, `VOID`, `COUNTER`.
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
    *   `WARP_CARPET_DOWN`: Activated by pressing 'Down' while standing on the tile.
    *   `PIT`: A hole in the floor that acts as a warp. Stepping on it triggers the warp.

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

## IV. Puzzle Solutions
*   **Ecruteak Gym Maze:**
    *   **Primary Hypothesis:** The gym contains an invisible path. Stepping off the path onto `PIT` tiles warps the player back to the start. The safe path is revealed or changed by following a specific sequence of steps, which also causes new trainers to appear.
    *   **Evidence:** I successfully bypassed a known warp at (4, 14) by following a long, specific path. New trainers (Granny, Sage) have appeared after I reached new areas.
    *   **Alternative Hypothesis:** The warps could be directional (i.e., their destination depends on the direction from which you enter the tile).
    *   **Test Plan for Alternative Hypothesis:** Find a safe tile adjacent to a known warp `PIT`. Step onto the `PIT` from one direction (e.g., 'Up'). Reset. Approach the same `PIT` from a different direction (e.g., 'Left'). If the destination is different, the hypothesis is confirmed. If it's the same, it's likely false.
    *   **Confirmed Failure:** Attempting to battle the final Granny at (7, 5) results in a dialogue loop. Pressing 'B' exits the loop. This is not the way forward.
**New Strategy:** Systematically test every single unmarked `PIT` warp, marking its source and destination, to build a complete map of the maze's connections. The system warning about unmarked warps confirms this is the correct approach.
    *   **Untested Assumption:** All `PIT` tiles lead back to the start at (4, 14).
    *   **Test for Assumption:** The next time I step on an unmarked `PIT`, I must verify the landing coordinates. If it's not (4, 14), the gym is more complex than I thought.
*   **FOG BADGE** (Allows use of SURF outside battle, makes Pokémon up to L50 obey)
*   **TM30 (SHADOW BALL)**