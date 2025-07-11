# Gem's Pokémon Crystal Notepad

## I. Current Objectives
*   **Primary Goal:** Find and defeat the Olivine City Gym Leader.
*   **Secondary Goal:** Find BERRIES to heal the sick Miltank on Route 39.
*   **Tertiary Goal:** Solve the Ruins of Alph puzzles.

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
    * `FLOOR_UP_WALL`: A complex one-way ledge. Can be moved onto from a tile below, off of by moving down, and horizontally between adjacent `FLOOR_UP_WALL` tiles. Cannot move up from this tile.
*   **Special Requirement:** 
    * `CUT_TREE` (Requires HM01 Cut. These trees can respawn after being cut).
    * `WATER` (Requires HM03 Surf, but is currently blocked in Olivine City).
    * `BREAKABLE_ROCK` (Requires Rock Smash).
    * `HEADBUTT_TREE` (Requires the move Headbutt. Confirmed that interacting without the move does nothing).
*   **Complex Tiles:**
    *   `WARP_CARPET_DOWN/LEFT/RIGHT`: Activated by pressing the corresponding direction while standing on the tile.
    *   `PIT`: A hole in the floor that acts as a warp. Stepping on it triggers the warp.
    *   `unknown` (in Ruins of Alph Ho-Oh Chamber): A special tile that, when standing on it and interacting with the adjacent puzzle object at (3, 2), warps the player to a sliding block puzzle screen. Its general traversability is unknown.

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
- **Conclusion:** This path is story-locked. Progress is gated behind an unknown event.

### Goldenrod Underground Blockade
- **Location:** (5, 31).
- **Blockade:** A Super Nerd blocks the path south.
- **Conclusion:** This path is story-locked.

## VI. Puzzle Solutions & Observations
### Goldenrod Dept. Store Basement Puzzle
- **Mechanic:** A dynamic box-pushing maze where Black Belts move and create/remove walls based on the player's position. The goal is to clear a path to the ladder at (17, 2).
- **Hypothesis:** A specific sequence of movements and interactions with the Black Belts is required to open the path.

### Ruins of Alph Ho-Oh Puzzle
- **Mechanic:** A 16-piece puzzle on a 6x6 grid. The goal is to assemble the image of Ho-Oh in the central 4x4 area. Pieces are picked up from the border and placed into empty slots. A piece cannot be placed in an occupied slot; the existing piece must be moved first.
- **Status:** First attempt at solving the puzzle failed. The game did not auto-complete, indicating an incorrect arrangement. Currently in the process of disassembling the incorrect solution to start over.
- **Strategy (Revised):** 
    1.  Move all 16 pieces to the outer border to get a clear view of each one.
    2.  Carefully re-identify corner and edge pieces.
    3.  Assemble the outer frame of the 4x4 picture first, verifying each piece's fit.
    4.  Fill in the four middle pieces last.
    5.  If a target slot is occupied, move the blocking piece to a temporary empty slot on the border.

## VII. Untested Hypotheses
*   **`CUT_TREE` Respawn Conditions:** A `CUT_TREE` at (8, 25) in Ilex Forest respawned. I need to test the exact conditions. Does it happen after a certain number of steps, after leaving the map, or after a certain amount of time? Next time I cut a tree near a map transition, I will immediately leave and re-enter the map to check if it has respawned.
*   **`WARP_CARPET_DOWN` Traversability:** I need to test if `WARP_CARPET_DOWN` tiles are truly one-way. Next time I'm on one, I will attempt to move up, left, and right to confirm.
*   **Ho-Oh Puzzle Alternate Solutions:** If a second, careful visual assembly of the Ho-Oh image fails, my alternative hypothesis is that the solution is non-obvious (e.g., arranging by color, leaving a gap, etc.). I will test this only after a second standard attempt fails.