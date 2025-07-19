# Gem's Pokémon Crystal Notepad

## I. Methodology & Self-Correction

### A. The Scientific Method for Puzzles & Unknowns
1.  **Observe:** Analyze the situation's initial state.
2.  **Hypothesize:** Formulate a single, clear, and testable hypothesis.
3.  **Test:** Execute the simplest possible action to test the hypothesis.
4.  **Conclude & Document:** Record the result and update this notepad immediately.
5.  **Pivot when Stuck:** If a hypothesis repeatedly fails or a path is confirmed blocked by a trusted tool (like `pathfinder`), I must abandon the approach and formulate a new, fundamentally different hypothesis (e.g., if an object interaction fails, consider an item use or an escape/re-entry strategy). I will not persist with a failed approach for more than 3-5 attempts.
6.  **Trust My Tools:** I will trust the output of my validated computational tools (e.g., `pathfinder`) and reasoning agents (`strategy_advisor`) over my own intuition. If a tool says a path is blocked, it is blocked. If I am stuck, I will consult my `strategy_advisor` before resorting to manual brute-force solutions.

### B. Core Directive Adherence (Self-Correction Log)
*   **Immediate Action (VIOLATION):** I have a history of deferring critical actions (fixing tools, marking objects, using agents) instead of performing them immediately. **Correction:** All data management and tool/agent use/refinement tasks MUST be performed in the turn they are identified. This is non-negotiable and takes precedence over any gameplay action.
*   **Trusting Documentation (VIOLATION):** I attempted to use the 'TOSS' item function despite my own notes verifying it is bugged. **Correction:** I must trust my own verified findings.

## II. Game Mechanics & Systems

### A. Tile Traversal Rules (Verified)
*   **Impassable:** WALL, COUNTER, MART_SHELF, PC, BOOKSHELF, HEADBUTT_TREE, CUT_TREE (uncut), TV, TOWN_MAP, WINDOW, ROCK, BUOY, VOID
*   **Traversable:** FLOOR, GRASS, TALL_GRASS, LONG_GRASS, WATER/SEA
*   **Warps:** DOOR, CAVE, LADDER, WARP_PANEL, WARP_CARPET_DOWN, WARP_CARPET_LEFT, WARP_CARPET_RIGHT
*   **HM Required:** BOULDER (STRENGTH), ROCK_SMASH_BOULDER (ROCK SMASH), WHIRLPOOL
*   **Conditional (One-Way):** PIT (fall), LEDGE_HOP_RIGHT, LEDGE_HOP_LEFT, LEDGE_HOP_DOWN
*   **Untested:** RADIO, INCENSE_BURNER, unknown (warp tile)

### B. System Bugs & Glitches (Verified)
*   **Item Management:**
    *   'DEPOSIT ITEM' and 'TOSS ITEM' from PC are bugged.
    *   'TOSS ITEM' from PACK is bugged.
    *   'FLY' HM is bugged and causes unpredictable warps.
*   **Toss Item from Pack (Bugged):** VERIFIED - Function is bugged and does not remove items.
*   **Giving Items (Bugged):** Giving an item to a Pokémon that is already holding one initiates a swap prompt, but does not free an inventory slot.

## III. World & Story

### A. Active Quests & Blockers
*   **Mahogany Town Gym Block:** A Fisher is blocking the gym entrance. Hypothesis: I must find and speak to Lance at the Lake of Rage to progress the story.
*   **Team Rocket Hideout:** Find the boss and use the passwords to disrupt their radio signal operation.
*   **RED SCALE Investigation:** Mr. Pokémon is the primary person of interest.
*   **Heal the Sick Miltank (Route 39):** Needs 'lots of BERRIES'.

### B. Passwords & Keys
*   **Team Rocket Hideout (Boss's Room):
    1. SLOWPOKETAIL (Confirmed)
    2. RATICATE TAIL
    3. HAIL GIOVANNI (Confirmed)

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
*   **Tool Distrust (VIOLATION):** I spent dozens of turns refusing to accept the correct output of my `pathfinder` tool, assuming it was broken when my own spatial reasoning was flawed. **Correction:** The output of a validated computational tool must be trusted over my own intuition. If a tool says a path is blocked, it is blocked.

### B. Maze Solver Tool & Arrow Tile Maze (Team Rocket Base)
*   This section will document the confirmed behavior of each arrow tile.
*   **Hypothesis:** The arrow tiles have a consistent, repeatable effect (e.g., stepping 'Down' on tile X always results in moving to tile Y).
*   **Test Plan:** 
    1. Move onto a new arrow tile and record the starting coordinate, input direction, and resulting coordinate.
    2. After mapping a tile's behavior, I must re-test it later by returning to the start coordinate and using the same input direction to confirm the outcome is identical. This will rule out more complex logic where tile behavior might change.
*   **Arrow Tile Data (Verified):**
    *   (3, 6) + Down -> (3, 7) (Normal movement, not an arrow tile)
    *   (3, 7) + Left -> (2, 7) (Normal movement, not an arrow tile)
    *   (2, 7) + Up -> (2, 6) (Normal movement, not an arrow tile)
    *   (2, 6) + Right -> (3, 6) (Normal movement, not an arrow tile)
    *   (3, 6) + Right -> (4, 6) (Normal movement, not an arrow tile)
    *   (4, 6) + Right -> (5, 6) (Normal movement, not an arrow tile)
    *   (5, 6) + Down -> (5, 7) (Normal movement, not an arrow tile)
    *   (5, 7) + Down -> (5, 8) (Normal movement, not an arrow tile)
    *   (5, 8) + Down -> (5, 9) (Normal movement, not an arrow tile)
    *   (5, 9) + Down -> (5, 10) (Normal movement, not an arrow tile)
    *   (5, 10) + Down -> (5, 11) (Normal movement, not an arrow tile)
    *   (5, 11) + Down -> (5, 12) (Normal movement, not an arrow tile)
    *   (5, 12) + Down -> (5, 13) (Normal movement, not an arrow tile)
    *   (5, 13) + Down -> (5, 14) (Normal movement, not an arrow tile)