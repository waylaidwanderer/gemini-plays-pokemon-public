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
*   **Tool Distrust (CRITICAL VIOLATION):** I have repeatedly refused to accept the correct output of my `pathfinder` tool, assuming it was broken when my own spatial reasoning was flawed. This was a critical failure of my scientific method and resulted in dozens of wasted turns. **Correction:** This behavior is unacceptable and will not be repeated. From now on, validated tool output is ground truth.
*   **Goal Fixation (VIOLATION):** I remained fixated on exploring the partitioned eastern loop for too long, despite overwhelming evidence it was a dead end. **Correction:** If a primary goal is demonstrably blocked after 3-5 distinct, documented hypotheses fail, I MUST pivot to a secondary or exploratory goal. Progress must be maintained.

## II. Game Mechanics & Systems

### A. Tile Traversal Rules (Verified)
*   **Impassable:** WALL, COUNTER, MART_SHELF, PC, BOOKSHELF, HEADBUTT_TREE, CUT_TREE (uncut), TV, TOWN_MAP, WINDOW, ROCK, BUOY, VOID
*   **Traversable:** FLOOR, GRASS, TALL_GRASS, LONG_GRASS, WATER/SEA
*   **Warps:** DOOR, CAVE, LADDER, WARP_PANEL, WARP_CARPET_DOWN, WARP_CARPET_LEFT, WARP_CARPET_RIGHT
*   **HM Required:** BOULDER (STRENGTH), ROCK_SMASH_BOULDER (ROCK SMASH), WHIRLPOOL
*   **Conditional (One-Way):** PIT (fall), LEDGE_HOP_RIGHT, LEDGE_HOP_LEFT, LEDGE_HOP_DOWN
*   **Conditional (Special):** FLOOR_UP_WALL (ledge, can only be entered by moving 'Up' from below, can be exited in other directions).
*   **Untested:** RADIO, INCENSE_BURNER, unknown (TeamRocketBaseB2F), unknown (TeamRocketBaseB3F, traversable), unknown (MahoganyPokecenter1F), unknown (LakeOfRage), COMPUTER, BED, CABINET, SINK, PLANT, unknown (MountMortarB1F), unknown (Route42)

### B. System Bugs & Glitches (Verified)
*   **Item Management:**
    *   'DEPOSIT ITEM' and 'TOSS ITEM' from PC are bugged.
    *   'TOSS ITEM' from PACK is bugged.
    *   'FLY' HM is bugged and causes unpredictable warps.
    *   Using one item from a stack (e.g., a Potion) does not free an inventory slot. The entire stack must be gone to clear the slot.
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
    2. RATICATE TAIL (Unconfirmed)
    3. HAIL GIOVANNI (Confirmed)

### C. Solved Puzzles & Key Discoveries
*   **Cianwood City Stuck Spot:** Was stuck on tile (10, 28). Solution was to trigger and complete the back-to-back phone calls (Mom, then Liz).
*   **Team Rocket Base B2F Layout:** The northern and southern corridors are separated by a wall and are not connected on this floor. Access to the northern section must be from a different warp on B1F.
*   **Secret Potion Location (Hypothesis Debunked):** The NPC hint pointing to Cianwood City was incorrect. The Pharmacist runs a regular shop and does NOT have the Secret Potion.
*   **Schoolboy Alan (Route 36):** My hypothesis that he had an item for me was incorrect. He is in a dialogue loop, which confirms he is a story-gated event.
*   **Ilex Forest Shrine:** A Lass in the Route 34 Gate mentioned a shrine honoring a grass-type protector of the forest.
*   **TM12 (Sweet Scent):** Given by Teacher in Route 34 Ilex Forest Gate. Attracts wild Pokémon.
*   **Team Rocket Base B1F Secret Passage:** The 'door' at (10, 9) is a secret passage, not a locked door. It is opened by activating the Secret Switch at (19, 11).
*   **Team Rocket Base B1F Hidden Revive (Unobtainable):** The hidden Revive at (3, 11) is currently unobtainable. Systematic testing from all adjacent tiles and facings failed to trigger the item pickup, suggesting a story flag or other unmet condition is required.

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

### B. Pathfinder Tool (FUNCTIONAL)
*   **Status:** The tool is working correctly. My repeated failures to trust its output were a major process violation.
*   **Incident Log:**
    *   **TeamRocketBaseB2F:** The tool correctly identified an impassable wall at Y=12 that I had failed to see.
    *   **TeamRocketBaseB3F:** The tool correctly identified an impassable WALL tile at (15, 8). I spent multiple turns debugging a functional tool because my own visual assessment of the map was wrong.
    *   **TeamRocketBaseB3F (Partitioned Map):** The tool's repeated failure to find a path between the eastern and western corridors confirmed that this floor is partitioned. My manual path tracing was flawed. The tool correctly identified that the sections are not connected on this floor.
*   **Action Plan:** I must trust the output of my validated tools over my own intuition. The `tool_debugger_agent` was critical in diagnosing my own flawed perception, not a flaw in the tool.

### C. Future Automation & Development Queue
1.  **Tool Validation Agent:** An agent that takes a tool's code and a set of test cases (inputs and expected outputs) and runs them to verify the tool's correctness.
2.  **Behavioral Analyst:** An agent that takes my turn history as input to identify repetitive, non-progressive loops and suggest alternative strategies.
3.  **Exploration Tool:** A tool to auto-path to unseen tiles.
4.  **Battle Advisor:** An agent to suggest moves based on known opponent rosters.
5.  **Area Scanner:** A computational tool that takes start/end coordinates for a rectangle and systematically moves through it, reporting back any tiles that cause forced movement (e.g., arrow tiles).
6.  **Pathfinder Refinement:** Investigate and refine the `pathfinder` tool's logic to improve pathing efficiency (see turn 59073).

## VI. Hypotheses & Falsification Tests

### A. Mahogany Gym Blocker
*   **Hypothesis:** The Fisher blocking the Mahogany Town Gym will move after I resolve the event with Lance at the Lake of Rage.
*   **Falsification Test:** If, after completing the Lake of Rage event, the Fisher is still blocking the gym, this hypothesis is false. The trigger must be something else. At that point, I must abandon this line of thinking and begin a systematic search for new clues in Mahogany Town and its surrounding routes.

### B. Mt. Mortar Invisible Barrier
*   **Hypothesis:** An invisible barrier blocks the entire northern one-way ledge on Mt. Mortar B1F.
*   **Falsification Test:** If I find a way to the northern area from a different path and can successfully walk south over that same ledge, the hypothesis is false. The blockage is likely an event trigger I haven't met.

### C. Route 42 Blockage
*   **Hypothesis:** The only path from Mahogany Town to Ecruteak City is through Mt. Mortar.
*   **Falsification Test:** After clearing inventory in Ecruteak, return to Route 42. Check if the Super Nerd at (47, 8) has moved or if there is an alternative way to access the northern water route. If another path exists, the hypothesis is false.

### D. Team Rocket B1F Maze Progression
*   **Current State:** The dialogue from the Grunt at (2, 4) confirms the existence of invisible 'traps'. My systematic exploration has revealed that these are not forced-movement arrow tiles, but likely one-way pitfall warps.
*   **Evolving Hypothesis:** The traps are floor tiles that warp the player to B2F, but only when entered from specific directions.
*   **Verified Behavior (Current Turn):**
    *   Moving DOWN onto tile (2, 13) from (2, 12) does NOT trigger a warp. This falsifies my previous assumption that this was a guaranteed pitfall.
*   **Revised Plan:**
    1. For each tile in the maze area, I must test entry from all four cardinal directions (North, South, East, West) to confirm the trigger conditions.
    2. I will move to an adjacent tile, then move back onto the test tile.
    3. I will record the outcome (warp or no warp) for each directional entry.
*   **Current Test:** I am at (2, 13). I have confirmed entry from the North is safe. I will now test entry from the East by moving to (3, 13) and then moving Left back to (2, 13).

## VII. Side Quests & Rematches
*   **Picnicker Liz (Route 34):** Wants a rematch on Route 32.