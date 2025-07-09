# Gem's Pokémon Crystal Notepad

## I. Strategic Plan
*   **Primary Goal: Find and defeat the Ecruteak City Gym Leader.**
    *   **Status:** Morty is back in the Ecruteak Gym. I am currently inside, ready to challenge him.
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

## IV. Untested Hypotheses & Puzzle Solutions
*   **Goldenrod Dept. Store Basement Puzzle:**
    *   **Status:** Abandoned. This is a sequential puzzle based on NPC interaction. Interacting with all four NPCs in a specific order is required to move the boxes. However, the visual changes are misleading, and the path to the items remains blocked in the collision data. The puzzle appears unsolvable at this time and may require an external trigger or key item.
*   **Radio Tower Progression:**
    *   **Hypothesis:** Progression in the Radio Tower is linked to the radio function in the Pokégear, as hinted by multiple NPCs.
    *   **Current Status:** The radio function is not available in my Pokégear. I must be missing the Radio Card. My current goal is to find this card by exploring the tower and speaking to all NPCs.
    *   **Known Hints:**
        - A Teacher mentioned that lullabies on the radio can make Pokémon sleep.
        - Buena mentioned her "PASSWORD SHOW".
*   **Goldenrod Underground Exploration:** Confirmed that the underground area is not related to obtaining the Radio Card. Both northern and southern sections have been fully explored. All paths are blocked by non-interactive or looping NPCs. This area is a confirmed dead end for the Radio Card quest.