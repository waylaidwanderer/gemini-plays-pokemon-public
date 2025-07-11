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
    *   `unknown` (in Ruins of Alph Ho-Oh Chamber at (3,3) and RuinsOfAlphOutside at (2,18)): A special tile type. In the Ho-Oh chamber, interacting with the puzzle from this tile triggers the puzzle. In RuinsOfAlphOutside, it appears to be a standard traversable floor tile.

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
*   **Ho-Oh Puzzle:** A 16-piece puzzle on a 6x6 grid. Goal is to assemble Ho-Oh in the central 4x4 area. I MUST use the `puzzle_analyst` agent the next time I attempt this puzzle.
*   **Ruins of Alph Southern Section:** This area is accessible by hopping down a one-way ledge. It contains two unexplored cave warps at (2, 29) and (6, 27), which are the only exits.

### Goldenrod Dept. Store Basement Puzzle
*   **Mechanic:** A dynamic box-pushing maze where Black Belts move and create/remove walls based on the player's position. The goal is to clear a path to the ladder at (17, 2).

## VI. Lessons Learned & Process Improvement
*   **Tool Maintenance:** My `pathfinder_v23` tool was critically flawed. I have now fixed it to account for Surf availability and one-way ledges. It is essential to fix faulty tools immediately to prevent getting stuck.
*   **Map Marker Consistency:** I must be more diligent about marking all significant events, especially defeated trainers and both sides of used warps, immediately after they occur.
*   **Immediate Action:** I must act on new information immediately. Deferring tasks like marking warps or fixing tools is an invalid and inefficient strategy.
*   **Hypothesis Testing:** When stuck, I must form multiple, alternative hypotheses and test them systematically to avoid confirmation bias. I will document these hypotheses in my notepad.
*   **Critical Failure Analysis:** I spent over 100 turns stuck in Ruins of Alph because I misread my map memory and incorrectly concluded that the ledge at (2, 19) led to a trap. This flawed premise led me to create and debug multiple faulty pathfinding tools, ignore my agent's correct advice, and waste time on incorrect hypotheses. The solution was simply to hop the ledge and walk out. This highlights a critical need to double-check my own observations and assumptions before building complex automation or dismissing agent advice.
*   **Critical Failure Analysis:** I spent over 100 turns stuck in Ruins of Alph because I misread my map memory and incorrectly concluded that the ledge at (2, 19) led to a trap. This flawed premise led me to create and debug multiple faulty pathfinding tools, ignore my agent's correct advice, and waste time on incorrect hypotheses. The solution was simply to hop the ledge and walk out. This highlights a critical need to double-check my own observations and assumptions before building complex automation or dismissing agent advice.
*   **Ruins of Alph Southern Section Failure:** I have spent many turns stuck in the southern part of Ruins of Alph. My repeated attempts to navigate to the cave warps at (6, 27) and (2, 29) have all failed due to misinterpreting the one-way `FLOOR_UP_WALL` ledges. This suggests my fundamental assumption about the exit path is wrong. New Hypothesis: The intended exit is via the cave warp at (6, 19) leading back to Union Cave, from which I might find another way out.