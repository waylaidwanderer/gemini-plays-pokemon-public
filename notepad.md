# Gem's Pokémon Crystal Notepad

## I. Current Objectives
*   **Primary Goal:** Find and defeat the Olivine City Gym Leader.
*   **Secondary Goal:** Find BERRIES to heal the sick Miltank on Route 39.
*   **Tertiary Goal:** Find the Radio Card.

## II. Game Systems & Mechanics

### Tile Traversal Protocol
- **Testing Mandate:** When a new, reachable tile type is seen, I MUST test it immediately.
- **Movement Test:** Attempt to move *into* and *out of* the tile from all 4 cardinal directions to verify passability.
- **Ledge Test:** For any ledge-like tile, I must attempt to move up/against the apparent direction of the ledge to confirm if it is a one-way path.

### Verified Tile Types
*   **Impassable:** `WALL`, `PILLAR`, `BOOKSHELF`, `TV`, `RADIO`, `TOWN_MAP`, `STATUE`, `TABLE`, `CHAIR`, `BIRD` (Farfetch'd), `MART_SHELF`, `BUOY`, `PC`, `LINK_CABLE`, `TRADE_MACHINE`, `INCENSE_BURNER`, `ROOF`, `CHIMNEY`, `SIGN`, `FLOWER`, `TREE_TOP`, `WATER_EDGE_UP`, `WATER_EDGE_DOWN`, `WATER_EDGE_LEFT`, `WATER_EDGE_RIGHT`, `VOID`, `COUNTER`, `FENCE`, `PC`, `LINK_RECEPTIONIST`, `WINDOW`, `WEIRD_TREE`.
*   **Traversable:** `FLOOR`, `GRASS`, `TALL_GRASS`, `LONG_GRASS`, `RAILING`, `PIPE_HORIZONTAL`, `PIPE_VERTICAL`.
*   **Warps:** `DOOR`, `CAVE`, `LADDER`, `STAIRCASE` (Move onto tile).
*   **One-Way Ledges:** 
    * `LEDGE_HOP_DOWN/RIGHT`: A one-way ledge that can only be hopped in the specified direction.
    * `LEDGE_HOP_LEFT`: A one-way ledge that can only be hopped **LEFT**.
    * `FLOOR_UP_WALL`: A one-way ledge that can only be hopped **UP**.
*   **Special Requirement:** 
    * `CUT_TREE` (Requires HM01 Cut).
    * `WATER` (Requires HM03 Surf, but is currently blocked in Olivine City).
    * `BREAKABLE_ROCK` (Requires Rock Smash).
    * `HEADBUTT_TREE` (Requires the move Headbutt. Currently unable to test).
*   **Complex Tiles:**
    *   `WARP_CARPET_DOWN/LEFT/RIGHT`: Activated by pressing the corresponding direction while standing on the tile.
    *   `PIT`: A hole in the floor that acts as a warp. Stepping on it triggers the warp.
    *   `2x1 warp tile`: A warp tile that seems to be stairs. Interaction method is currently unknown.
*   **Untested:** `unknown` (in Olivine City).

### Other Mechanics
*   **Object Impassability:** All Map Objects (NPCs, items, signs, etc.) are impassable.
*   **Item Effects:**
    *   **BERRY:** Restores 10 HP.
    *   **MINT BERRY:** Cures sleep.
    *   **EVERSTONE:** Prevents evolution.
    *   **MOOMOO MILK:** Restores 100 HP.
    *   **HARD STONE:** Powers up rock-type moves.
    *   **PRZCUREBERRY:** Cures paralysis.
    *   **HYPER POTION:** Restores 200 HP.
    *   **ICE BERRY:** Heals burn.
*   **Haircuts:** Increases a Pokémon's happiness.

## III. Key Items, HMs & TMs
*   **Key Items:** SQUIRTBOTTLE, GOOD ROD, COIN CASE
*   **HMs:** HM01 (CUT), HM03 (SURF), HM04 (STRENGTH)
*   **TMs:** 
    * TM08 (ROCK SMASH)
    * TM12 (SWEET SCENT)
    * TM28 (DIG)
    * TM30 (SHADOW BALL) - Causes damage and may reduce SPCL.DEF.
    * TM45 (ATTRACT)
    * TM49 (FURY CUTTER)

## IV. Badges
*   **ZEPHYR BADGE**
*   **HIVE BADGE**
*   **PLAIN BADGE**
*   **FOG BADGE** (Allows use of SURF outside battle, makes Pokémon up to L50 obey)

## V. Blocked Paths & Story Gates
### Route 37 Trainer Blockade
- **Location:** (6, 12) and (7, 12).
- **Blockade:** Two trainers (Twins Ann & Anne) disguised as trees block the path north.
- **Behavior:** Interacting with them triggers a repeating dialogue loop.
- **Conclusion:** This path is story-locked. Progress is gated behind an unknown event. I will not attempt this path again until I have a clear reason to believe it is open.

### Goldenrod Underground Blockade
- **Location:** (5, 31).
- **Blockade:** A Super Nerd blocks the path south.
- **Behavior:** Interacting with him triggers a repeating dialogue loop ("I guess I have to do things fair and square…"). No battle occurs.
- **Conclusion:** This path is story-locked. I will not attempt this path again until I have a clear reason to believe it is open.

## VI. Puzzle Solutions & Observations
### Goldenrod Dept. Store Basement Puzzle
- **Mechanic:** This is a dynamic maze. My position on the map causes walls to appear or disappear and NPCs (Black Belts) to move, opening and closing paths. The goal is to reach the ladder at (17, 2).
- **Known Triggers:**
    1. Interacting with the Black Belt at (4, 8) makes him block the path west.
    2. Moving from (5, 8) to (5, 9) causes the WALL at (10, 13) to become a FLOOR tile.
    3. Moving from (8, 7) to (8, 8) causes the WALL at (11, 12) to become a FLOOR tile.
    4. Moving from (8, 8) to (8, 9) causes the WALL at (11, 13) to become a FLOOR tile.
- **Hypothesis:** A specific sequence of movements is required to open the path to the ladder.