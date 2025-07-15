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
*   **Warps:** `CAVE`, `DOOR`, `LADDER`, `STAIRCASE`, `WARP_CARPET_DOWN` (Requires 'Down'), `WARP_PANEL` (One-way)
*   **Conditional/One-Way:** `BREAKABLE_ROCK` (Requires Rock Smash), `CUT_TREE` (Requires HM01 Cut), `FLOOR_UP_WALL` (One-way ledge), `LEDGE_HOP_DOWN`, `LEDGE_HOP_DOWN/RIGHT`, `LEDGE_HOP_LEFT`, `PIT` (One-way down)

### Menu Mechanics
*   **Inventory Bug (Confirmed):** The inventory is permanently locked. 'TOSS', 'GIVE', 'USE' (in battle), and 'SELL' commands are all non-functional for freeing inventory space. No new items can be picked up.

## III. Current Objective: Team Rocket Hideout

### Team Rocket Hideout Puzzle
*   **Current State:** I am in the isolated eastern section of the Team Rocket Hideout B1F. This area is a one-way path from the main hideout, leading only to the Mahogany Mart. It's a red herring.
*   **Clue:** Lance revealed a secret entrance inside the Mahogany Mart. I have not yet used this entrance.
*   **Primary Hypothesis:** The solution to progressing lies within the main section of the Team Rocket Hideout B1F, which I must now properly explore by entering through the main entrance that Lance revealed.
*   **Secondary Hypothesis:** I have missed a key interaction with a switch or NPC in the main B1F area, such as the security camera system or the arrow tile switch.

### General Hypothesis Log
*   **H1 (Disproven):** A hidden passage exists in the wall on B2F. **Result:** No passage found.
*   **H2 (Disproven):** An alternate ladder on B1F leads to a new section. **Result:** All ladders explored led to known areas.
*   **H3 (Disproven):** Stunning Scientist Jed allows passage. **Result:** Could not walk through stunned NPC.
*   **H4 (Disproven):** Triggering security cameras unlocks a path. **Result:** No event triggered.
*   **H5 (Disproven):** Arrow tiles are a puzzle. **Result:** They are impassable WALLs.
*   **H6 (Confirmed):** There is an invisible maze on B1F. I successfully navigated it.
*   **H7 (Disproven):** The locked door on B2F requires a password from Lance on B3F. **Result:** B3F is a dead end.
*   **H8 (Disproven):** The secret entrance is a hidden switch on the blue tile at (1, 2) in the mart. **Result:** Interaction and movement tests failed.
*   **H9 (Disproven):** The Radio at (0, 1) in the mart is the switch. **Result:** Interaction opened the Pokédex.
*   **H10 (Disproven):** The ladder at (7, 3) in the mart changes its destination after the Pharmacist dialogue. **Result:** It still leads to the isolated B1F area.

## IV. Tool Status
*   **Trap Discovered:** Stepping on tile (2, 7) in Team Rocket Hideout B1F (Map ID 3_49) triggers a warp to a corrupted glitch map.
*   **Warp Panel Mechanics:** The warp panel at (5, 15) is a one-way teleporter to (25, 2). The tile at (25, 2) is only an arrival point.