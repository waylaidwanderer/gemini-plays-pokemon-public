# Gem's Pokémon Crystal Notepad

## I. Strategic Plan
*   **Primary Goal: Find and defeat the Ecruteak City Gym Leader.**
    *   **Status:** Currently inside the Burned Tower. Morty is likely at the Ecruteak Gym now that the legendary beast event is over.
*   **Secondary Goal: Systematically explore and mark every warp in the Burned Tower.**
    *   **Status:** Partially complete. I need to investigate the remaining unmarked warps on 1F.
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
*   **Warps:** `DOOR`, `CAVE`, `LADDER`, `STAIRCASE` (Move onto tile). Some `WALL` tiles can also function as warps, though the activation method is still unknown.
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

### Unverified Tile Types
*   **PIT:** A hole in the floor that appeared after the rival battle. Need to test if it's a one-way drop or leads somewhere specific.

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
*   **Hypothesis Failure (Radio Tower):** The Plain Badge does NOT grant access to the upper floors of the Radio Tower.
*   **Hypothesis Failure (Burned Tower 1F Warps):** The warps near the entrance at (5,5), (4,6), and (5,6) are not activated by stepping on them or interacting with them from the front. They are likely exit-only.
*   **Hypothesis Failure (Burned Tower Basement Access):** The western floor-warps/holes on 1F do not lead to new areas; they trigger a cutscene and reset my position. The central `PIT` tile is the correct path to the basement.

## V. Untested Hypotheses
*   **Morty's Location:**
    *   **Hypothesis:** Morty has returned to the Ecruteak Gym.
    *   **Alternative:** Morty is still in the Burned Tower or has moved to the Tin Tower now that the legendary beasts have been released.
    *   **Test:** After exploring the Burned Tower, I will go to the Ecruteak Gym. If he's not there, I will check the Tin Tower entrance again.
*   **Floor Holes:**
    *   **Hypothesis:** All the floor holes/warps on 1F lead to the same spot in the basement.
    *   **Alternative:** Each hole could lead to a different, isolated section of the basement.
    *   **Test:** Systematically fall through each unique hole and map out where I land.