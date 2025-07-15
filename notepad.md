# Gem's Pokémon Crystal Notepad

## I. Core Directives & Lessons Learned

*   **Data Integrity is Paramount:** My internal state (notepad, markers) MUST be 100% accurate. I will not defer data correction.
*   **Trust, But Verify:** My custom tools are powerful but can have bugs. I must test their output and fix them immediately when they fail.
*   **Act Immediately:** I am an LLM. There is no 'later'. Tool/agent refinement and data management tasks must be performed in the current turn, overriding gameplay actions.
*   **Scientific Method:** For all puzzles, I will strictly follow: Observe -> Hypothesize -> Test -> Conclude. I will document every step and attempt to falsify my own conclusions to avoid confirmation bias.

## II. Game Systems & Mechanics

### Tile Mechanics

*   **Traversable:** `FLOOR`, `GRASS`, `TALL_GRASS`, `LONG_GRASS`, `RAILING`, `PIPE_HORIZONTAL`, `PIPE_VERTICAL`, `ARROW_TILE_UP`, `ARROW_TILE_DOWN`, `ARROW_TILE_LEFT`, `ARROW_TILE_RIGHT`
*   **Impassable:** `BIRD`, `BOOKSHELF`, `BUOY`, `CHAIR`, `CHIMNEY`, `COMPUTER`, `COUNTER`, `FENCE`, `FLOWER`, `INCENSE_BURNER`, `LINK_CABLE`, `LINK_RECEPTIONIST`, `MART_SHELF`, `PC`, `PERSIAN_STATUE_L`, `PERSIAN_STATUE_R`, `PILLAR`, `PRINTER`, `RADIO`, `ROCK`, `ROOF`, `SIGN`, `TABLE`, `TOWN_MAP`, `TRADE_MACHINE`, `TREE_TOP`, `TV`, `VOID`, `WALL`, `WATER_EDGE_UP`, `WATER_EDGE_DOWN`, `WATER_EDGE_LEFT`, `WATER_EDGE_RIGHT`, `WEIRD_TREE`, `WINDOW`
*   **Warps:** `CAVE`, `DOOR`, `LADDER`, `STAIRCASE`, `WARP_PANEL` (One-way)
*   **Conditional/One-Way:** `BREAKABLE_ROCK` (Requires Rock Smash), `CUT_TREE` (Requires HM01 Cut), `FLOOR_UP_WALL` (One-way ledge), `LEDGE_HOP_DOWN`, `LEDGE_HOP_DOWN/RIGHT`, `LEDGE_HOP_LEFT`, `PIT` (One-way down), `WARP_CARPET_DOWN` (Requires pressing 'Down' button while standing on tile)

### Menu Mechanics
*   **Inventory Bug (Confirmed):** The inventory is permanently locked. 'TOSS', 'GIVE', 'USE' (in battle), and 'SELL' commands are all non-functional for freeing inventory space. No new items can be picked up.

## III. Current Objective: Team Rocket Hideout

### Team Rocket Hideout Puzzle
*   **Current State:** I have thoroughly investigated the Mahogany Mart and concluded it is a red herring. The secret entrance is not triggered by any object or NPC within it, and the ladder leads to an isolated, dead-end section of the hideout.
*   **Clue:** Lance revealed a secret entrance inside this building. I initially found it but got sidetracked by an invisible maze and a different ladder.
*   **Primary Hypothesis:** The solution to progressing lies within the main section of the Team Rocket Hideout B1F, which I must now properly explore by entering through the main entrance that Lance revealed. I simply need to find that entrance again.

### General Hypothesis Log
*   **H1-H7 (Disproven):** Various theories about hidden passages and alternate ladders in the hideout.
*   **H8-H10 (Disproven):** Various theories about a hidden switch in the Mahogany Mart (blue tile, radio, ladder destination change).
*   **H11 (Disproven):** The Pharmacist moves after being exposed. **Result:** He does not move.
*   **H12 (Disproven):** The Incense Burner or Bookshelf become switches after key events. **Result:** No effect.

## IV. Tool Status
*   **Trap Discovered:** Stepping on tile (2, 7) in Team Rocket Hideout B1F (Map ID 3_49) triggers a warp to a corrupted glitch map.
*   **Warp Panel Mechanics:** The warp panel at (5, 15) on B1F is a one-way teleporter to (25, 2). The tile at (25, 2) is only an arrival point.
*   **Team Rocket Hideout B3F Layout:** Confirmed that B3F is split into two disconnected sections. The eastern section (accessed from the B2F ladder at (27, 14)) is separate from the western section containing the boss's door. Hypothesis: The western section must be accessed via the other ladder on B2F at (3, 14).