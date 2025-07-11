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
    * `FLOOR_UP_WALL`: A complex one-way ledge. Can be moved onto from a tile below, off of by moving down, and horizontally between adjacent `FLOOR_UP_WALL` tiles. Cannot move up from this tile.
*   **Special Requirement:** 
    * `CUT_TREE` (Requires HM01 Cut. These trees can respawn after being cut).
    * `WATER` (Requires HM03 Surf, but is currently blocked in Olivine City).
    * `BREAKABLE_ROCK` (Requires Rock Smash).
    * `HEADBUTT_TREE` (Requires the move Headbutt. Confirmed that interacting without the move does nothing).
*   **Complex Tiles:**
    *   `WARP_CARPET_DOWN/LEFT/RIGHT`: Activated by pressing the corresponding direction while standing on the tile.
    *   `PIT`: A hole in the floor that acts as a warp. Stepping on it triggers the warp.
    *   `unknown` (in Ruins of Alph Ho-Oh Chamber): A special tile that, when standing on it and interacting with the adjacent puzzle object at (3, 2), warps the player to a sliding block puzzle screen. Its behavior without interacting with the puzzle is currently unknown.

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

### Ruins of Alph Ho-Oh Puzzle
- **Mechanic:** A 16-piece puzzle on a 6x6 grid. The goal is to assemble the image of Ho-Oh in the central 4x4 area. Pieces are picked up from the border and placed into empty slots. A piece cannot be placed in an occupied slot; the existing piece must be moved first.
- **Strategy:**
    1.  Identify corner and edge pieces.
    2.  Assemble the outer frame of the 4x4 picture first.
    3.  Fill in the middle pieces last.
    4.  If a target slot is occupied, move the blocking piece to a temporary empty slot on the border.

## VII. Untested Hypotheses
*   **`CUT_TREE` Respawn Conditions:** A `CUT_TREE` at (8, 25) in Ilex Forest respawned. I need to test the exact conditions. Does it happen after a certain number of steps, after leaving the map, or after a certain amount of time? Next time I cut a tree near a map transition, I will immediately leave and re-enter the map to check if it has respawned.

## VIII. Current Plans
### Primary Goal: Solve Ruins of Alph Puzzles
*   **Problem:** I'm in the Ho-Oh Chamber and need to solve the puzzle to proceed.
*   **Hypothesis 1 (Failed):** Interacting with the puzzle object at (3, 2) from the adjacent tile (3, 1) will activate it. (Failed twice).
*   **Hypothesis 2 (Current):** Activation requires standing on one of the special floor tiles, (3, 3) or (4, 3), and *then* interacting with the puzzle object at (3, 2).
*   **Current Plan:**
    1.  Move to (3, 3).
    2.  Face the puzzle object at (3, 2).
    3.  Interact with the puzzle object.

## IX. Untested Hypotheses (Post-Reflection)
*   **`WARP_CARPET_DOWN` Traversability:** I need to test if `WARP_CARPET_DOWN` tiles are truly one-way. Next time I'm on one, I will attempt to move up, left, and right to confirm.
*   **Ho-Oh Puzzle Mechanics:** My current hypothesis is that this is a standard sliding puzzle where any border piece adjacent to an empty grid slot can be moved. An alternative hypothesis is that only *specific* border pieces are movable at any given time. To test this, after placing the next piece, I will try to pick up another adjacent border piece (like Piece #11 at position 24). If I can't, my current hypothesis is incomplete.