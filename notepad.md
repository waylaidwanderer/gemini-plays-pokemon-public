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

*   **Primary Objective:** Find the Team Rocket Boss and disable the radio signal.
*   **Hypothesis Log:**
    *   **H1 (Disproven):** A hidden passage exists in the wall on B2F at Y=12. **Test:** Systematically interacted with every wall tile from (8, 12) to (3, 12). **Result:** No passage found. All tiles were solid walls.
    *   **H2 (Disproven):** An alternate ladder on B1F leads to the northern section of B2F. **Test:** All ladders on B1F have been explored. All lead to disconnected or previously explored sections.
    *   **H3 (Disproven):** Stunning Scientist Jed allows passage. **Test:** Used stun_npc on Jed at (18, 12) but could not walk through his tile.
    *   **H4 (Disproven):** Intentionally triggering the security cameras will unlock a new path. **Test:** Systematically moved in front of multiple security cameras ((8, 15), (22, 15), (24, 5)). **Result:** No event was triggered.
    *   **H5 (Disproven):** The "arrow tile puzzle" does not exist. The tiles are impassable WALLs. My analysis was based on a hallucination.
    *   **H6 (Disproven):** The ROCKET at (2, 4) triggers a glitch warp. **Test:** Interacted with the ROCKET. **Result:** Triggered a scripted event with dialogue confirming an invisible trap maze. The warp was part of the script, not a glitch.
*   **H7 (Current):** There is an invisible maze of floor traps. I must navigate it to reach the switch at (19, 11). Evidence is the ROCKET's dialogue.
*   **Passwords:**
    *   Password 1: SLOWPOKETAIL
    *   Password 2: RATICATE TAIL

## IV. Tool Status
*   **reliable_pathfinder:** This tool had a bug where it would path through `WARP_PANEL` tiles, causing accidental teleportation. I have implemented a fix to treat `WARP_PANEL` as impassable.
*   **Trap Discovered:** Stepping on tile (2, 7) in Team Rocket Hideout B1F (Map ID 3_49) triggers a warp to a corrupted glitch map. This is a trap, not a path forward.