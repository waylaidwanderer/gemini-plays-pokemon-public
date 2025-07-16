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
*   **B1F Switch:** Flipping the switch at (19, 11) on B1F toggles the arrow tiles on and off. It is currently OFF.
*   **B1F Scientist (Jed):** The scientist at (18, 12) stands near the path to the switch but does not block it.
*   **B1F Warp Panel:** The warp panel at (5, 15) is a one-way teleporter to (25, 2), leading to an isolated exit area via the Mahogany Mart.
*   **B2F Locked Door Interaction:** Interacting with the locked door at (14, 12) twice only yields the message "It needs a password to open." It does not prompt for input.
*   **B3F Layout:** B3F is split into two disconnected sections. The western section containing the boss and Lance is inaccessible from the eastern ladder.
*   **Passwords Found:** The two passwords are 'SLOWPOKETAIL' and 'RATICATE TAIL'.
*   **B2F West Corridor:** The western corridor of B2F, accessed via the ladder at (3, 14), is a dead end and does not connect to the main area.

### Hypotheses Log
*   **H34 (Falsified):** Navigating the invisible floor maze and reaching the door does not automatically trigger a password prompt.
*   **H35 (Falsified):** The key to opening the door is not a direct interaction after learning the passwords. The transmitter area is also inaccessible from any known path on B2F.
*   **H33 (Falsified):** Disabling the arrow tiles on B1F will open a new path on B2F.
*   **H36 (Active):** The invisible maze on B1F contains a second, undiscovered ladder that leads to the area with the transmitter.

### Future Plans & Strategy
*   **Hideout Progression Plan (v9 - Maze Exploration):**
    1.  Systematically explore the main invisible floor maze on B1F (approx. X: 7-28, Y: 5-16).
    2.  My goal is to test Hypothesis H36: Find a second, hidden ladder leading to the transmitter room.
    3.  Method: Use a wall-following approach (always keeping a wall to my right) to ensure complete coverage and avoid getting lost or looping.
    4.  Starting point for exploration will be entering the maze at (7, 5).

## IV. Future Testing & Verification Notes
*   **Ledge Verification:** I have assumed all `LEDGE_HOP_...` tiles are one-way based on observation. I must explicitly try to move *up* a ledge at the next opportunity to scientifically confirm this is impossible.
*   **Object Traversal:** I must test if it's possible to walk on object tiles like `BOOKSHELF` when they are not blocked by walls to confirm they are universally impassable.
*   **Password Door Re-check:** My `puzzle_master` agent recommended I try the passwords. I will do this as soon as I can reach the door.
*   **Bookshelf Switch Hypothesis:** If the invisible maze is a dead end, I will test the hypothesis that the bookshelves at (20, 11) and (21, 11) are a hidden switch.
*   **Maze Navigation:** I will use the `maze_navigator` tool to efficiently solve the invisible floor maze. It uses a right-hand wall-following algorithm.
*   **Password 2:** 'RATICATE TAIL' (from grunt at (5, 14) on B3F).
*   **Alternative Hypothesis (Post-Maze):** If the invisible maze on B1F does not contain a path to the transmitter, the solution may be a hidden switch or passage on B2F or B3F. I will systematically re-explore those floors if H36 is falsified.
*   **H37 (Falsified):** The bookshelves at (20, 11) and (21, 11) are a hidden switch. Both only contain flavor text.
*   **H38 (Falsified):** Scientist Jed at (18, 12) only provided a hint about the warp panel being a trap, but no direct solution.
*   **Strategy Pivot (Turn 46869):** All leads on B1F outside the main invisible maze are exhausted. Returning to the maze with a new exploration strategy.
*   **H39 (Active):** The invisible maze contains a path that does not lead to the warp panel trap at (5, 15). The solution is likely a hidden ladder within the maze's interior.
*   **Hideout Progression Plan (v10 - Maze Exploration 2.0):**
    1.  Return to the maze entrance at (7, 5).
    2.  Explore the central and western sections of the maze, starting by moving down from (7, 5) to (7, 6), a previously untested path.