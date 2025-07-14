# Gem's Pokémon Crystal Notepad

## I. Core Directives & Lessons Learned

*   **Data Integrity is Paramount:** My internal state (notepad, markers) MUST be 100% accurate. I will not defer data correction. Assumptions must be rigorously tested before being recorded as fact.
*   **Trust Automation:** My custom tools are more reliable than my manual analysis. I must prioritize using them to avoid unforced errors.
*   **Act Immediately:** I am an LLM. There is no 'later'. Tool/agent refinement and data management tasks must be performed in the current turn, overriding gameplay actions.
*   **Scientific Method:** For all puzzles, I will strictly follow: Observe -> Hypothesize -> Test -> Conclude. I will document every step and attempt to falsify my own conclusions to avoid confirmation bias.

## II. Game Systems & Mechanics

### Verified Tile Types

**Traversable:**
*   `FLOOR`
*   `GRASS`
*   `TALL_GRASS`
*   `LONG_GRASS`
*   `RAILING`
*   `PIPE_HORIZONTAL`
*   `PIPE_VERTICAL`

**Impassable:**
*   `BIRD`
*   `BOOKSHELF`
*   `BUOY`
*   `CHAIR`
*   `CHIMNEY`
*   `COUNTER`
*   `FENCE`
*   `FLOWER`
*   `INCENSE_BURNER`
*   `LINK_CABLE`
*   `LINK_RECEPTIONIST`
*   `MART_SHELF`
*   `PC`
*   `PILLAR`
*   `PRINTER`
*   `RADIO`
*   `ROCK`
*   `ROOF`
*   `SIGN`
*   `TABLE`
*   `TOWN_MAP`
*   `TRADE_MACHINE`
*   `TREE_TOP`
*   `TV`
*   `VOID`
*   `WALL`
*   `WATER_EDGE_UP`
*   `WATER_EDGE_DOWN`
*   `WATER_EDGE_LEFT`
*   `WATER_EDGE_RIGHT`
*   `WEIRD_TREE`
*   `WINDOW`

**Warps:**
*   `CAVE`
*   `DOOR`
*   `LADDER`
*   `STAIRCASE`
*   `WARP_CARPET_DOWN` (Requires 'Down' to activate)
*   `WARP_PANEL` (One-way teleporter)

**Conditional / One-Way:**
*   `BREAKABLE_ROCK` (Requires Rock Smash)
*   `CUT_TREE` (Requires HM01 Cut)
*   `FLOOR_UP_WALL` (One-way ledge, hoppable from above)
*   `LEDGE_HOP_DOWN`
*   `LEDGE_HOP_DOWN/RIGHT`
*   `LEDGE_HOP_LEFT`
*   `PIT` (One-way down)

## III. Current Investigation: Team Rocket Hideout

*   **Objective:** Find the secret Team Rocket entrance in Mahogany Town, as per Lance's instructions, and disable the radio signal.
*   **Key Discoveries:** The hideout entrance is in the Mahogany Mart. A switch at (19, 11) on B1F disables the security cameras. Both ladders on B1F are either dead ends or one-way exits. Interacting with Scientist Jed at (18, 12) causes him to move temporarily, but he blocks the path again.

### Passwords
*   **Password 1:** SLOWPOKETAIL (from Rocket Girl on B3F)

### Floor Puzzle - Team Rocket Hideout B2F
*   **Mechanics:** This appears to be another state-based sequence puzzle. Stepping on specific tiles triggers changes to objects on the floor (Poke Balls, Voltorbs, and Grunts appearing/disappearing).
*   **Known Triggers:**
    *   Stepping from (1, 15) to (1, 16) makes the Poke Ball at (3, 10) disappear.
    *   Stepping from (5, 16) to (5, 15) makes the Poke Ball at (3, 10) reappear.
    *   Stepping from (8, 13) to (9, 13) makes the Poke Ball at (3, 10) disappear.
    *   Stepping from (15, 13) to (14, 13) makes the ROCKET grunt at (21, 14) disappear.

## IV. Battle Discoveries & Type Chart

### Verified Type Interactions
*   **Water (Surf) vs. Gyarados (Water/Flying):** Observed as "not very effective". This contradicts standard type charts. Need to investigate further.

## V. Open Investigations

### Inventory Management Bug
*   **Observation:** All menu-based attempts to free an inventory slot (`TOSS`, `GIVE`, `DEPOSIT`) have failed, resulting in a menu loop.
*   **Primary Hypothesis:** The only way to free an inventory slot is to consume an item during a battle. **Test:** Initiate a battle and use a Potion.
*   **Alternative Hypothesis #1:** The issue is story-related and will resolve after defeating the hideout's leader. **Test:** Ignore the bug and all item pickups, focusing solely on finding the path to the boss.
*   **Alternative Hypothesis #2:** The issue is a deliberate mechanic, like an "inventory jammer." **Test:** Search for a machine, a generator, or a switch that could be responsible for this effect and interact with it.
*   **Alternative Hypothesis #3:** The inventory issue is a temporary story mechanic, not a bug. It may resolve automatically after defeating the hideout's leader. **Test:** If other hypotheses fail, ignore all item pickups and focus solely on finding the path to the boss.