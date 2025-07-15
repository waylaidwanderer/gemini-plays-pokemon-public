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

## III. Team Rocket Hideout Puzzle Log

*   **Objective:** Find the Team Rocket Boss and disable the radio signal.
*   **Main Obstacle:** A password-locked door on B2F at (14, 12) is blocking progress.

### Confirmed Facts & Discoveries
*   **B1F Switch:** Flipping the switch at (19, 11) on B1F toggles the arrow tiles on and off.
*   **B1F Scientist (Jed):** The scientist at (18, 12) stands near the path to the switch but does not block it.
*   **B1F Warp Panel:** The warp panel at (5, 15) is a one-way teleporter to (25, 2), leading to an isolated exit area via the Mahogany Mart.
*   **B2F Locked Door Interaction:** Interacting with the locked door at (14, 12) twice only yields the message "It needs a password to open." It does not prompt for input.
*   **B3F Layout:** B3F is split into two disconnected sections. The western section containing the boss and Lance is inaccessible from the eastern ladder.
*   **Passwords Found:** The two passwords are 'SLOWPOKETAIL' and 'RATICATE TAIL'.

### Hypotheses Log
*   **H27 (Disproven):** Interacting with Scientist Jed at (18, 12) after collecting the passwords does not trigger a new event. He only repeats his dialogue about the warp panel at (5, 15).
*   **H28 (Disproven):** Interacting with the switch at (19, 11) a second time does not trigger a new event. It only turns the arrow tiles off.
*   **H29 (Active):** Lance is waiting on B2F. I must find him and he will help open the locked door at (14, 12).

### Future Plans & Strategy
*   **Hideout Progression Plan (v4):**
    1.  Return to B2F via the ladder at (3, 14).
    2.  Locate Lance, who was last seen at (5, 13) on B2F.
    3.  Interact with Lance to see if he triggers the event to open the locked door at (14, 12).