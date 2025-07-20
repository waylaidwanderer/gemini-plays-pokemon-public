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
*   **Deferred Documentation (VIOLATION):** I failed to immediately update my notepad's incident log after each of the `pathfinder` tool's catastrophic failures. This is a critical process violation. **Correction:** All tool failures must be documented immediately to maintain an accurate internal state.

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

### B. Pathfinder Tool (CRITICALLY FAILED - DO NOT USE)
*   **Status:** The tool is fundamentally broken. It has repeatedly generated invalid paths or failed to find obvious ones. It is completely unreliable and must not be used for navigation until it is rebuilt from scratch.
*   **Incident Log:**
    *   **TeamRocketBaseB3F (Failure 1):** Generated a path through a solid WALL tile at (21, 15).
    *   **TeamRocketBaseB3F (Failure 2):** Generated a path through a solid WALL tile at (18, 11).
    *   **TeamRocketBaseB3F (Failure 3, 4, 5):** Returned 'No path found' for a simple, visually unobstructed path from (15, 12) to (10, 10), even after multiple supposed 'fixes' from the debugger agent. The A* implementation is fundamentally broken.
*   **Action Plan:** The tool requires a complete rewrite. Manual navigation is the only reliable option for now.

### C. Tool Debugger Agent (FAILED)
*   **Status:** The agent has repeatedly failed to identify the root cause of the pathfinder's bugs, providing multiple incorrect 'fixes'. It is currently unreliable for debugging complex code.

### D. Future Automation & Development Queue
1.  **Debugging Orchestrator Agent:** An agent that can manage the entire debugging loop: take a failing tool and a test case, use the debugger agent to get a fix, apply the fix, and re-test, reporting the final outcome. This would automate the tedious process I just went through.
2.  **Systematic Debugger Agent:** A more advanced version of the current debugger agent with a more structured prompt, forcing it to check for common error classes in a specific order (e.g., syntax, data parsing, logical fallacies) to avoid getting stuck on surface-level fixes.
3.  **Tool Validation Agent:** An agent that takes a tool's code and a set of test cases (inputs and expected outputs) and runs them to verify the tool's correctness.
4.  **Behavioral Analyst:** An agent that takes my turn history as input to identify repetitive, non-progressive loops and suggest alternative strategies.
5.  **Exploration Tool:** A tool to auto-path to unseen tiles.
6.  **Battle Advisor:** An agent to suggest moves based on known opponent rosters.

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
*   **Current Progress:** I have confirmed pitfalls at (2, 13) and (3, 13). I have successfully navigated south along the western wall to (1, 14).
*   **Current Plan:** Continue systematic, one-tile-at-a-time exploration south and east from my current position at (1, 14) to find a safe path to the ladder at (3, 14).

### E. Team Rocket Boss Location
*   **Hypothesis:** The Team Rocket boss is located behind the locked door at (10, 9) on B3F.
*   **Falsification Test:** If, after reaching the door, there is no password prompt, no visible switch, and no interaction possible, this hypothesis is false. The path forward must be on a different floor or via a hidden passage I have missed. My next step would be a full, systematic re-exploration of B1F and B2F.

## VII. Side Quests & Rematches
*   **Picnicker Liz (Route 34):** Wants a rematch on Route 32.