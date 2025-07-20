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
*   **Tool Distrust (CRITICAL VIOLATION):** I spent dozens of turns refusing to accept the correct output of my `pathfinder` tool, assuming it was broken when my own spatial reasoning was flawed. This was a critical failure of my scientific method. **Correction:** The output of a validated computational tool is an extension of the game's ground truth. It MUST be trusted over my own intuition, ALWAYS. If a tool says a path is blocked, it is BLOCKED. My first action upon receiving such an output is to use diagnostic tools like `map_debugger` to understand *why* the path is blocked, not to assume the tool is broken. I will not repeat this mistake.
*   **Trusting Documentation (VIOLATION):** I attempted to use the 'DEPOSIT ITEM' PC function despite my own notes verifying it is bugged. **Correction:** I must trust my own verified findings.

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
*   **Giving Items (Bugged):** Giving an item to a Pokémon that is already holding one initiates a swap prompt, but does not free an inventory slot.

## III. World & Story

### A. Active Quests & Blockers
*   **Mahogany Town Gym Block:** A Fisher is blocking the gym entrance. Hypothesis: I must find and speak to Lance at the Lake of Rage to progress the story.
*   **Team Rocket Hideout:** Find the boss and use the passwords to disrupt their radio signal operation. The entrance is a secret stairway in the Mahogany Mart, revealed by interacting with the Pharmacist. The northern and southern corridors are separated by a wall and are not connected on this floor. Access to the northern section must be from a different warp on B1F. The entrance is a secret stairway in the Mahogany Mart, revealed by interacting with the Pharmacist.
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
*   **Team Rocket Base B1F Secret Passage:** The 'door' at (10, 9) is a secret passage, not a locked door. It is opened by activating the Secret Switch at (19, 11).

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
*   **Action Plan:** I must trust the output of my validated tools over my own intuition. The `map_debugger` tool was critical in diagnosing my own flawed perception, not a flaw in the tool.

### C. Agent & Tool Concepts (New)
*   **Tool Validation Agent:** An agent that takes a tool's code and a set of test cases (inputs and expected outputs) and runs them to verify the tool's correctness. This would have caught the multiple `pathfinder` bugs much faster.
*   **Behavioral Analyst:** An agent that takes my turn history as input to identify repetitive, non-progressive loops and suggest alternative strategies. This could have helped me break out of the Mt. Mortar cycle much faster.
*   **Dungeon Analyst Agent:** An agent that takes the map XML and warp data from multiple interconnected maps (like a cave system) as input. It would analyze the data to build a connectivity graph, identify partitioned or unreachable areas, and suggest an optimal exploration route to reveal the entire dungeon and find all exits. This would prevent wasting time in dead-end corridors like I did in the Team Rocket Base.

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

## VII. Side Quests & Rematches
*   **Picnicker Liz (Route 34):** Wants a rematch on Route 32.

### C. Team Rocket Base B1F Arrow Maze (Verified)
*   (1, 4) -> Forces movement 'Up' to (1, 3).
*   (1, 3) -> Normal floor tile.
*   (2, 3) -> Normal floor tile.
*   (3, 3) -> Normal floor tile.
*   (4, 3) -> Normal floor tile.
*   (5, 3) -> Normal floor tile.
*   (6, 3) -> Normal floor tile.
*   (7, 3) -> Normal floor tile.
*   (8, 3) -> Normal floor tile.
*   (9, 3) -> Normal floor tile.
*   (10, 3) -> Normal floor tile.
*   (11, 3) -> Normal floor tile.
*   (12, 3) -> Normal floor tile.
*   (13, 3) -> Normal floor tile.
*   (14, 3) -> Normal floor tile.
*   (15, 3) -> Normal floor tile.
*   (16, 3) -> Normal floor tile.

### D. Future Agent Development Queue
1. **Tool Validation Agent:** An agent that takes a tool's code and a set of test cases (inputs and expected outputs) and runs them to verify the tool's correctness. This would have caught the multiple `pathfinder` bugs much faster.
2. **Behavioral Analyst:** An agent that takes my turn history as input to identify repetitive, non-progressive loops and suggest alternative strategies. This could have helped me break out of the Mt. Mortar cycle much faster.
3. **Dungeon Analyst Agent:** An agent that takes the map XML and warp data from multiple interconnected maps (like a cave system) as input. It would analyze the data to build a connectivity graph, identify partitioned or unreachable areas, and suggest an optimal exploration route to reveal the entire dungeon and find all exits. This would prevent wasting time in dead-end corridors like I did in the Team Rocket Base.

### C. Solved Puzzles & Key Discoveries (New Entry)
*   **Team Rocket Base Layout (Key Discovery):** B2F and B3F are partitioned by walls. The eastern and western corridors are not connected on these floors. Access to the western sections must be from a different warp on B1F.