# Gem's Pokémon Crystal Notepad

## I. Methodology & Self-Correction

### A. The Scientific Method for Puzzles & Unknowns
1.  **Observe:** Analyze the situation's initial state.
2.  **Hypothesize:** Formulate a single, clear, and testable hypothesis.
3.  **Test:** Execute the simplest possible action to test the hypothesis.
4.  **Conclude & Document:** Record the result and update this notepad immediately.
5.  **Consider Non-Obvious Triggers:** When stuck, especially if movement is locked on a normally traversable tile, consider that the solution may be a non-movement scripted event (e.g., a phone call, using a key item, etc.).
6.  **Strategically Mark:** Use map markers to track progress and prevent repeating failed tests.
7.  **Rigorous Tile Testing:** When a new tile type is encountered, I must test movement from all four directions (Up, Down, Left, Right) to fully understand its properties and document them here. The test must be performed IMMEDIATELY upon discovery.

### B. Core Directive Adherence (Self-Correction Log)
*   **Immediate Action (VIOLATION):** I have a history of deferring critical actions (fixing tools, marking objects) instead of performing them immediately. This is a critical failure in understanding my nature as an LLM. **Correction:** All data management and tool refinement tasks MUST be performed in the turn they are identified. This is non-negotiable and takes precedence over any gameplay action.

## II. Game Mechanics & Systems

### A. Tile Traversal Rules (Verified)
*   **Impassable:** WALL, COUNTER, MART_SHELF, PC, BOOKSHELF, HEADBUTT_TREE, CUT_TREE (uncut), TV, TOWN_MAP, WINDOW, ROCK, BUOY
*   **Traversable:** FLOOR, GRASS, TALL_GRASS, LONG_GRASS, WATER/SEA
*   **Warps:** DOOR, CAVE, LADDER, WARP_PANEL, WARP_CARPET_DOWN, WARP_CARPET_LEFT, WARP_CARPET_RIGHT
*   **HM Required:** BOULDER (STRENGTH), ROCK_SMASH_BOULDER (ROCK SMASH), WHIRLPOOL
*   **Conditional (One-Way):** PIT (fall), LEDGE_HOP_RIGHT (verified), LEDGE_HOP_LEFT (verified), LEDGE_HOP_DOWN (verified)
*   **VOID (Impassable - verified)**
*   **Untested:** RADIO, INCENSE_BURNER

### B. HM Usage Rules (Verified)
*   **Fly:** Using Fly from the party menu appears to be bugged, causing unexpected warps to different locations. It does not function as a standard fast-travel move.

### C. System Bugs & Glitches
*   **PC Item Management (Mahogany & Violet):** 'DEPOSIT ITEM' and 'TOSS ITEM' from the PC menu are bugged.
*   **Toss Item from Pack (Bugged):** VERIFIED - Function is bugged and does not remove items.
*   **Giving Items (Bugged):** Giving an item to a Pokémon that is already holding one initiates a swap prompt, but does not free an inventory slot.

## III. World & Story

### A. Active Quests & Blockers
*   **Mahogany Town Gym Block:** A Fisher is blocking the gym entrance. Hypothesis: I must find and speak to Lance at the Lake of Rage to progress the story.
*   **Team Rocket Hideout:** Find the boss and use the passwords to disrupt their radio signal operation.
*   **RED SCALE Investigation:** Mr. Pokémon is the primary person of interest.
*   **Heal the Sick Miltank (Route 39):** Needs 'lots of BERRIES'.

### B. Passwords & Keys
*   **Team Rocket Hideout (Boss's Room):**
    1. SLOWPOKETAIL (Confirmed)
    2. RATICATE TAIL
    3. HAIL GIOVANNI

### C. Solved Puzzles & Key Discoveries
*   **Cianwood City Stuck Spot:** Was stuck on tile (10, 28). Solution was to trigger and complete the back-to-back phone calls (Mom, then Liz).
*   **Team Rocket Base B2F Layout:** The northern and southern corridors are separated by a wall and are not connected on this floor. Access to the northern section must be from a different warp on B1F.
*   **Secret Potion Location (Hypothesis Debunked):** The NPC hint pointing to Cianwood City was incorrect. The Pharmacist runs a regular shop and does NOT have the Secret Potion.
*   **Schoolboy Alan (Route 36):** My hypothesis that he had an item for me was incorrect. He is in a dialogue loop, which confirms he is a story-gated event.
*   **Ilex Forest Shrine:** A Lass in the Route 34 Gate mentioned a shrine honoring a grass-type protector of the forest.
*   **TM12 (Sweet Scent):** Given by Teacher in Route 34 Ilex Forest Gate. Attracts wild Pokémon.

## IV. Battle and Pokemon Information

### A. Type Effectiveness Chart (Verified in-game)
*   Water (Surf) vs. Water/Flying (Gyarados) -> Not Very Effective

### B. Observed Movesets
*   **Youngster Joey's RATTATA:** Tackle, Tail Whip
*   **Falkner's PIDGEY:** Tackle
*   **Falkner's PIDGEOTTO:** Tackle, Gust
*   **Bugsy's METAPOD:** Harden
*   **Bugsy's KAKUNA:** Harden
*   **Bugsy's SCYTHER:** Fury Cutter, Leer
*   **Whitney's CLEFAIRY:** Doubleslap, Encore
*   **Whitney's MILTANK:** Rollout, Stomp, Attract
*   **Morty's GASTLY:** Lick, Spite
*   **Morty's HAUNTER:** Curse, Hypnosis, Dream Eater
*   **Morty's GENGAR:** Shadow Ball, Hypnosis, Dream Eater
*   **Jasmine's MAGNEMITE:** Thunderbolt, Thunder Wave, Supersonic
*   **Jasmine's STEELIX:** Iron Tail, Screech, Rock Throw
*   **Chuck's PRIMEAPE:** Leer, Rage, Karate Chop
*   **Chuck's POLIWRATH:** Hypnosis, Mind Reader, Dynamicpunch

## V. Automation & Tool Development

### A. Pathfinder Tool
*   **FIXED:** The `pathfinder` tool has been updated. It now correctly handles HM usage (e.g., SURF, CUT) and recognizes on-screen objects/NPCs as obstacles.

### B. Maze Solver Tool
*   **Hypothesis:** The arrow tiles in the Team Rocket Base have a consistent, repeatable effect.
*   **Test Plan:** After mapping a tile's behavior, I must re-test it later to confirm the outcome is identical. This will rule out more complex puzzle logic where tile behavior might change.

### C. Arrow Tile Maze (Team Rocket Base)
*   This section will document the confirmed behavior of each arrow tile.
*   (2, 3): Stepping on this tile does not cause forced movement. Player must choose a direction.
*   (1, 3): Stepping on this tile does not cause forced movement. Player must choose a direction.
*   (1, 4): Dead end. Path blocked by walls and ROCKET grunt.
*   (1, 2): Stepping on this tile does not cause forced movement. Player must choose a direction.
*   (2, 2): Stepping on this tile does not cause forced movement. Player must choose a direction.
*   (3, 2): Stepping on this tile does not cause forced movement. Player must choose a direction.
*   (5, 2): Stepping on this tile does not cause forced movement. Player must choose a direction.