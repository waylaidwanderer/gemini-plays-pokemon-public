# Gem's Pokémon Crystal Notepad

## I. Current Objectives
*   **Primary Goal:** Find and defeat the Olivine City Gym Leader.
*   **Secondary Goal:** Travel to Ecruteak City.
*   **Tertiary Goal:** Find the Coin Case.

## II. Game Systems & Mechanics

### Tile Traversal Protocol
- **Testing Mandate:** When a new, reachable tile type is seen, I MUST test it immediately.
- **Movement Test:** Attempt to move *into* and *out of* the tile from all 4 cardinal directions to verify passability.
- **Ledge Test:** For any ledge-like tile, I must attempt to move up/against the apparent direction of the ledge to confirm if it is a one-way path.

### Verified Tile Types
*   **Impassable:** `WALL`, `PILLAR`, `BOOKSHELF`, `TV`, `RADIO`, `TOWN_MAP`, `STATUE`, `TABLE`, `CHAIR`, `BIRD` (Farfetch'd), `MART_SHELF`, `BUOY`, `PC`, `LINK_CABLE`, `TRADE_MACHINE`, `INCENSE_BURNER`, `ROOF`, `CHIMNEY`, `SIGN`, `FLOWER`, `TREE_TOP`, `WATER_EDGE_UP`, `WATER_EDGE_DOWN`, `WATER_EDGE_LEFT`, `WATER_EDGE_RIGHT`, `VOID`, `COUNTER`, `FENCE`, `PC`, `LINK_RECEPTIONIST`, `WINDOW`.
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
*   **Complex Tiles:**
    *   `WARP_CARPET_DOWN/LEFT/RIGHT`: Activated by pressing the corresponding direction while standing on the tile.
    *   `PIT`: A hole in the floor that acts as a warp. Stepping on it triggers the warp.
    *   `2x1 warp tile`: A warp tile that seems to be stairs. Interaction method is currently unknown.
*   **Untested:** `unknown` (in Olivine City), `HEADBUTT_TREE`.

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
- **Behavior:** Interacting with them triggers a repeating dialogue loop ("my POKéMON are thinking.").
- **Conclusion:** This appears to be a story-based roadblock. Standard interactions have failed (A, B, Start, Select buttons; SQUIRTBOTTLE). Progress is likely gated behind another story event, possibly related to the Olivine City Gym. Will return later.

### Goldenrod Underground
- The path forward is blocked by a Super Nerd in a dialogue loop and a locked door in the northern section. I was unable to break the dialogue loop by pressing A, B, or Start, suggesting I am missing a prerequisite to proceed in this area.