# Gem's Pokémon Crystal Notepad

## I. Game Systems & Mechanics

### Tile Traversal Protocol
- **Testing Mandate:** When a new, reachable tile type is seen, I MUST test it immediately.
- **Movement Test:** Attempt to move *into* and *out of* the tile from all 4 cardinal directions to verify passability.
- **Interaction Test:** If movement fails, I must attempt to interact with the tile by facing it and pressing 'A'.
- **Ledge Test:** For any ledge-like tile, I must attempt to move up/against the apparent direction of the ledge to confirm if it is a one-way path.

### Verified Tile Types
*   **Impassable:** `WALL`, `PILLAR`, `BOOKSHELF`, `TV`, `RADIO`, `TOWN_MAP`, `STATUE`, `TABLE`, `CHAIR`, `BIRD` (Farfetch'd), `MART_SHELF`, `BUOY`, `PC`, `LINK_CABLE`, `TRADE_MACHINE`, `INCENSE_BURNER`, `ROOF`, `CHIMNEY`, `SIGN`, `FLOWER`, `TREE_TOP`, `WATER_EDGE_UP`, `WATER_EDGE_DOWN`, `WATER_EDGE_LEFT`, `WATER_EDGE_RIGHT`, `VOID`, `COUNTER`, `FENCE`, `PC`, `LINK_RECEPTIONIST`, `WINDOW`, `WEIRD_TREE`.
*   **Traversable:** `FLOOR`, `GRASS`, `TALL_GRASS`, `LONG_GRASS`, `RAILING`, `PIPE_HORIZONTAL`, `PIPE_VERTICAL`.
*   **Warps:** `DOOR`, `CAVE`, `LADDER`, `STAIRCASE` (Move onto tile), `PIT` (Acts as a warp when stepped on).
*   **One-Way Ledges:**
    *   `LEDGE_HOP_DOWN`: A one-way ledge that can only be hopped **DOWN**. Attempting to move up against it fails.
    *   `LEDGE_HOP_DOWN/RIGHT`: A one-way ledge that can only be hopped in the specified direction.
    *   `LEDGE_HOP_LEFT`: A one-way ledge that can only be hopped **LEFT**.
    *   `FLOOR_UP_WALL`: A complex one-way ledge. You can move onto it from a tile below it, move horizontally between adjacent `FLOOR_UP_WALL` tiles, and move down *off* of it to a tile below. You cannot move up from this tile or down onto it from a standard `FLOOR` or `LADDER` tile.
*   **Special Requirement:**
    *   `CUT_TREE` (Requires HM01 Cut. These trees can respawn after being cut).
    *   `WATER` (Requires HM03 Surf. To initiate, face the water and press 'A').
    *   `BREAKABLE_ROCK` (Requires Rock Smash).
    *   `HEADBUTT_TREE` (Requires the move Headbutt. Confirmed that interacting without the move does nothing).
*   **Complex Tiles:**
    *   `WARP_CARPET_DOWN/LEFT/RIGHT`: Traversable. Activated by pressing the corresponding direction while standing on the tile to trigger a warp.
    *   `WARP_CARPET_DOWN`: Traversable. Activated by pressing 'Down' while standing on the tile to trigger a warp.
    *   `unknown` (in Ruins of Alph Puzzle Chambers): This tile type represents a special interaction point. In the Ho-Oh and Omanyte chambers, standing on the tile at (3,3) and interacting with the puzzle object at (3,2) triggers the puzzle. In RuinsOfAlphOutside at (2,18), it appears to be a standard traversable floor tile.

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

## II. Key Items, HMs & TMs
*   **Key Items:** SQUIRTBOTTLE, GOOD ROD, COIN CASE
*   **HMs:** HM01 (CUT), HM03 (SURF), HM04 (STRENGTH)
*   **TMs:** TM08 (ROCK SMASH), TM12 (SWEET SCENT), TM28 (DIG), TM30 (SHADOW BALL), TM45 (ATTRACT), TM49 (FURY CUTTER)

## III. Badges
*   **ZEPHYR BADGE**
*   **HIVE BADGE**
*   **PLAIN BADGE**
*   **FOG BADGE** (Allows use of SURF outside battle, makes Pokémon up to L50 obey)

## IV. Blocked Paths & Story Gates
*   **Route 37 Trainer Blockade:** Twins Ann & Anne disguised as trees block the path north at (6, 12) and (7, 12). This path is story-locked.
*   **Goldenrod Underground Blockade:** A Super Nerd blocks the path south at (5, 31). This path is story-locked.

## V. Puzzles & Hypotheses

### Ruins of Alph
*   **Ho-Oh Puzzle:** A 16-piece puzzle on a 6x6 grid. Goal is to assemble Ho-Oh in the central 4x4 area. Must be solved manually.
*   **Aerodactyl Puzzle:**
    *   **Observed Mechanics:**
        *   The cursor wraps around the edges of the 6x6 grid. Moving left from column 0 goes to column 5, and vice-versa. The same applies to rows 0 and 5.
        *   Movement from row 4 to row 5 is blocked. I tried moving down from (2,4) and it failed. I will need to navigate around this.
    *   **Hypothesis 1:** The puzzle is solved by visually assembling the image of Aerodactyl. This is my current working theory.
    *   **Hypothesis 2 (Alternative):** The puzzle logic might involve matching patterns on the edges of the pieces, not just the overall image.
    *   **Exit Strategy:** If I fail to solve this puzzle after ~20-30 more turns, I will test the hypothesis that these puzzles are optional. I will leave the chamber and re-explore Ruins of Alph Outside for an alternative path forward.

### Goldenrod Dept. Store Basement Puzzle
*   **Mechanic:** A dynamic box-pushing maze where Black Belts move and create/remove walls based on the player's position. The goal is to clear a path to the ladder at (17, 2).

## VI. Critical Lessons & Process Improvement
*   **The Ruins of Alph Failure (Turns 34777-34873):** I wasted over 100 turns due to a cascade of process failures:
    1.  **Confirmation Bias:** I incorrectly concluded I was trapped and that my `pathfinder` tool *must* be broken. I spent dozens of turns in a futile debugging loop instead of questioning my initial premise.
    2.  **Violation of Simple-First Principle:** I failed to test the most obvious, simple hypothesis—jumping the southern ledge—and instead pursued complex, incorrect solutions (DIG, Escape Rope, tool modification).
    3.  **Violation of Immediate Action:** I deferred tool fixes and notepad updates, which is an invalid strategy. All new information and necessary fixes must be handled in the same turn they are identified.
*   **Tool Maintenance Protocol:** When a tool fails, first verify user input. If the input is correct, perform a simple diagnostic test (e.g., pathing one tile). If that fails, then begin systematic debugging. Do not get stuck in a debugging loop; if a fix isn't apparent, abandon the tool and try a manual approach.