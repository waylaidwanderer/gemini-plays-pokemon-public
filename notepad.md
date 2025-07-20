# Gem's Pokémon Crystal Notepad

## I. Methodology & Self-Correction

### A. The Scientific Method for Puzzles & Unknowns
1.  **Observe:** Analyze the situation's initial state.
2.  **Hypothesize:** Formulate a single, clear, and testable hypothesis.
3.  **Test:** Execute the simplest possible action to test the hypothesis.
4.  **Conclude & Document:** Record the result and update this notepad immediately.
5.  **Pivot when Stuck:** If a hypothesis repeatedly fails or a path is confirmed blocked by a trusted tool (like `pathfinder`), I must abandon the approach and formulate a new, fundamentally different hypothesis (e.g., if an object interaction fails, consider an item use or an escape/re-entry strategy). I will not persist with a failed approach for more than 3-5 attempts.
6.  **Falsify Hypotheses:** To avoid confirmation bias, after a test confirms a hypothesis (e.g., an arrow tile's behavior), I must attempt to disprove it. A key test will be to return to the same tile later and repeat the same action to ensure the outcome is consistent.
7.  **Trust My Tools:** I will trust the output of my validated computational tools (e.g., `pathfinder`) and reasoning agents (`strategy_advisor`) over my own intuition. If a tool says a path is blocked, it is blocked. If I am stuck, I will consult my `strategy_advisor` before resorting to manual brute-force solutions.

### B. Core Directive Adherence (Self-Correction Log)
*   **Immediate Action (VIOLATION):** I have a history of deferring critical actions (fixing tools, marking objects) instead of performing them immediately. **Correction:** All data management and tool/agent use/refinement tasks MUST be performed in the turn they are identified. This is non-negotiable and takes precedence over any gameplay action.
*   **Tool Debugging & Confirmation Bias (VIOLATION):** I repeatedly assumed my `pathfinder` tool was fixed after each single bug fix, failing to consider that multiple, independent bugs could exist concurrently. **Correction:** After fixing a tool, I must test it rigorously. If it fails again, I must assume another, different bug exists and continue the iterative refinement process.
*   **Trusting Documentation (VIOLATION):** I attempted to use the 'TOSS' item function despite my own notes verifying it is bugged. **Correction:** I must trust my own verified findings.
*   **Tool Distrust (VIOLATION):** I spent dozens of turns refusing to accept the correct output of my `pathfinder` tool, assuming it was broken when my own spatial reasoning was flawed. **Correction:** The output of a validated computational tool must be trusted over my own intuition. If a tool says a path is blocked, it is blocked.
*   **Trusting Documentation (VIOLATION):** I attempted to use the 'DEPOSIT ITEM' PC function despite my own notes verifying it is bugged. **Correction:** I must trust my own verified findings.

## II. Game Mechanics & Systems

### A. Tile Traversal Rules (Verified)
*   **Impassable:** WALL, COUNTER, MART_SHELF, PC, BOOKSHELF, HEADBUTT_TREE, CUT_TREE (uncut), TV, TOWN_MAP, WINDOW, ROCK, BUOY, VOID
*   **Traversable:** FLOOR, GRASS, TALL_GRASS, LONG_GRASS, WATER/SEA
*   **Warps:** DOOR, CAVE, LADDER, WARP_PANEL, WARP_CARPET_DOWN, WARP_CARPET_LEFT, WARP_CARPET_RIGHT
*   **HM Required:** BOULDER (STRENGTH), ROCK_SMASH_BOULDER (ROCK SMASH), WHIRLPOOL
*   **Conditional (One-Way):** PIT (fall), LEDGE_HOP_RIGHT, LEDGE_HOP_LEFT, LEDGE_HOP_DOWN, FLOOR_UP_WALL (move 'Up' only)
*   **Untested:** RADIO, INCENSE_BURNER, unknown (TeamRocketBaseB3F, traversable), unknown (MahoganyPokecenter1F), unknown (LakeOfRage)

### B. System Bugs & Glitches (Verified)
*   **Item Management:**
    *   'DEPOSIT ITEM' and 'TOSS ITEM' from PC are bugged.
    *   'TOSS ITEM' from PACK is bugged.
    *   'FLY' HM is bugged and causes unpredictable warps.
*   **Giving Items (Bugged):** Giving an item to a Pokémon that is already holding one initiates a swap prompt, but does not free an inventory slot.

## III. World & Story

### A. Active Quests & Blockers
*   **Mahogany Town Gym Block:** A Fisher is blocking the gym entrance. Hypothesis: I must find and speak to Lance at the Lake of Rage to progress the story.
*   **Team Rocket Hideout:** Find the boss and use the passwords to disrupt their radio signal operation. The entrance is a secret stairway in the Mahogany Mart, revealed by interacting with the Pharmacist.
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

### A. Tool Refinement Methodology
1.  **Immediate Action:** Any identified bug, flaw, or opportunity for improvement in a tool or agent MUST be addressed in the *immediate* turn. This task takes absolute precedence over any gameplay action.
2.  **Rigorous Testing:** After any modification, a tool must be subjected to a battery of tests to confirm the fix and check for unintended side effects. A single successful use case is not sufficient proof of correctness.
3.  **Iterative Refinement:** Assume that multiple, independent bugs may exist. If a tool fails after a fix, a new, unrelated bug is the most likely cause. The debugging process must be iterative and persistent.

### B. Pathfinder Tool
*   **FIXED (AGAIN):** The `pathfinder` tool has been updated to correctly handle one-way ledges (`LEDGE_HOP_...` and `FLOOR_UP_WALL` types) and water traversal (`can_surf` parameter). It is now considered reliable.

### C. Maze Solver Tool
*   The `maze_solver` tool is now available to navigate the Team Rocket Base arrow tile maze. Manual mapping is no longer necessary.

## VI. Future Development
### A. Agent Concepts
*   **Party Checker Tool:** A tool to check which Pokémon in my party are holding items. This would have prevented my recent inventory-solving failures.

## VII. Hypotheses & Tests
### A. Mahogany Gym Blocker
*   **Hypothesis:** The Fisher blocking the Mahogany Town Gym will move after I resolve the event with Lance at the Lake of Rage.
*   **Falsification Test:** If, after completing the Lake of Rage event, the Fisher is still blocking the gym, this hypothesis is false. The trigger must be something else. At that point, I must abandon this line of thinking and begin a systematic search for new clues in Mahogany Town and its surrounding routes.
*   **Fishing Guru (Lake of Rage):** Confirmed that "men wearing black" (Team Rocket) are causing the disturbance at the lake.
*   **Special Warps:**
    *   `WARP_CARPET_DOWN`: Activated by standing on the tile and pressing the 'Down' button. (Verified in Lake of Rage Magikarp House)

## VIII. Side Quests & Rematches
*   **Picnicker Liz (Route 34):** Wants a rematch on Route 32.

### B. Agent Concepts (New)
*   **Behavioral Analyst:** An agent that takes my turn history as input to identify repetitive, non-progressive loops and suggest alternative strategies. This could have helped me break out of the Mt. Mortar cycle much faster.

### C. Tile Testing To-Do
*   Test traversability of RADIO and INCENSE_BURNER tiles.
*   **Untested (TeamRocketBaseB3F):** COMPUTER, BED, CABINET, SINK, PLANT
*   **Team Rocket Base B1F Secret Passage:** The 'door' at (10, 9) is a secret passage, not a locked door. It is opened by activating the Secret Switch at (19, 11).