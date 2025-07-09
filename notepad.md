# Gem's Pokémon Crystal Notepad

## I. Strategic Plan
*   **Primary Goal: Find and defeat the Ecruteak City Gym Leader.**
    *   **Status:** Currently inside the Burned Tower. Morty is likely at the Ecruteak Gym now that the legendary beast event is over.
*   **Secondary Goal: Systematically explore and mark every warp in the Burned Tower.**
    *   **Status:** Partially complete. I need to investigate the remaining unmarked warps on 1F and B1F. Currently paused to acquire Repels.
*   **Tertiary Goal: Investigate the mystery of the Lake of Rage & the legendary beasts.**
    *   **Status:** Witnessed the awakening of Raikou, Entei, and Suicune. Eusine is also tracking them.

## II. Game Systems & Mechanics

### Tile Traversal Protocol
- **Testing Mandate:** When a new, reachable tile type is seen, I MUST test it immediately.
- **Movement Test:** Attempt to move *into* and *out of* the tile from all 4 cardinal directions to verify passability.
- **Ledge Test:** For any ledge-like tile, I must attempt to move up/against the apparent direction of the ledge to confirm if it is a one-way path.

### Verified Tile Types
*   **Impassable:** `WALL`, `HEADBUTT_TREE`, `PILLAR`, `BOOKSHELF`, `TV`, `RADIO`, `TOWN_MAP`, `WINDOW`, `STATUE`, `TABLE`, `CHAIR`, `BIRD` (Farfetch'd), `VOID`, `MART_SHELF`, `BUOY`, `PC`, `LINK_CABLE`, `TRADE_MACHINE`, `INCENSE_BURNER`, `COUNTER`, `ROOF`, `CHIMNEY`, `SIGN`, `FLOWER`, `TREE_TOP`, `WATER_EDGE_UP`, `WATER_EDGE_DOWN`, `WATER_EDGE_LEFT`, `WATER_EDGE_RIGHT`.
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
*   **PIT:** A hole in the floor that appeared after the rival battle. It is the correct path to the basement, but its exact mechanics (one-way drop vs. two-way) are unconfirmed.
*   **Floor Holes (Burned Tower):** These do not function as simple fall-through warps. Stepping on the hole at (14, 14) did not consistently cause a fall (Attempt 1: wild battle, Attempt 2: moved to (14, 15)). The western floor holes at (4,14) and (5,14) also seem to trigger a cutscene and reset position rather than leading to a new area.
*   **Wall-Warps (Burned Tower):** The activation method for these is unknown.
    *   **Failed Hypothesis 1:** Moving into the wall-warp tile does not work.
    *   **Failed Hypothesis 2:** Pressing the directional button towards the warp from an adjacent floor tile does not work.

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

## IV. Archive: Solved Puzzles & Failed Hypotheses
*   **Solved (Radio Tower Access):** The Plain Badge does NOT grant access to the upper floors.
*   **Solved (Burned Tower Basement Access):** The central `PIT` tile is the correct path to the basement after the rival battle.

## V. Untested Hypotheses
*   **Morty's Location:**
    *   **Hypothesis:** Morty has returned to the Ecruteak Gym.
    *   **Alternative:** Morty is still in the Burned Tower or has moved to the Tin Tower.
    *   **Test:** After exploring the Burned Tower, I will go to the Ecruteak Gym. If he's not there, I will check the Tin Tower entrance again.