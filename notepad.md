# Gem's Pokémon Crystal Notepad

## I. Strategic Plan
*   **Primary Goal: Find and defeat the Ecruteak City Gym Leader.**
    *   **Status:** Currently inside the Burned Tower, where Morty has been seen.
*   **Secondary Goal: Systematically explore and mark every warp in the Burned Tower.**
    *   **Status:** Acknowledged as a high-priority task after repeated failures to do so.
*   **Tertiary Goal: Investigate the mystery of the Lake of Rage & the legendary beasts.**
    *   **Status:** Multiple NPCs have mentioned these events. Eusine is also in the Burned Tower searching for Suicune.

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
*   **Complex Tiles:**
    *   `WARP_CARPET_LEFT/RIGHT/DOWN`: Activated by pressing the indicated direction while standing on the tile.
    *   `Push-Down Trap`: A `FLOOR` tile that, when stepped on, pushes the player down one tile.

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
*   **Hypothesis Failure (Burned Tower Progression):** Progress on 1F is not achieved by crossing the central chasm. 
    *   **Test 1 (Hole Warps):** Stepping on or falling through the `FLOOR` tiles that are also warps (holes) on the west side of the chasm did not lead to the basement; they either triggered a cutscene and returned me to my original spot or had no effect. (Turns #29787 - #29798)
    *   **Test 2 (Rock Smash):** Using Rock Smash on the breakable rock at (4, 12) is not permitted. (Turn #29810)
    *   **Test 3 (Rival Proximity):** Standing at the edge of the chasm directly opposite Rival SILVA at (8, 13) did not trigger any event. (Turn #29817)
    *   **New Hypothesis:** Progress is likely achieved by interacting with the NPCs (Morty, Eusine) or by finding the correct warp among the many on this floor.
*   **Hypothesis Failure (Burned Tower Progression):** The floor warp at (7, 15) is not activated by stepping on it, standing on it, or interacting with it. It likely has a special, unknown activation condition.
*   **Hypothesis Failure (Burned Tower Progression):** The entrance warp at (5, 5) is not activated by stepping on it, standing on it, or interacting with it. It likely has a special, unknown activation condition.
*   **BREAKABLE_ROCK:** Requires Rock Smash to break.
*   **BREAKABLE_ROCK:** Requires Rock Smash to break.
*   **BREAKABLE_ROCK:** Requires Rock Smash to break.