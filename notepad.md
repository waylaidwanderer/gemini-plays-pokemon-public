## Core Principles & Lessons Learned
- **IMMEDIATE ACTION:** I must perform tasks like placing markers, updating my notepad, and fixing tools *immediately*. Deferring tasks, like placing map markers, is a process violation. Significant events must be documented *immediately* in the turn they occur.
- **AGENT USAGE:** When stuck for more than 5 turns on a puzzle, I must use the `hypothesis_generator` agent. My `simple_battle_strategist` agent is underutilized and I will prioritize using it for all future wild battles to automate decision-making.
- **PUZZLE DOCUMENTATION:** My entire problem-solving process (observation, hypothesis, test, conclusion) for any puzzle must be documented in this notepad as it happens.
- **MAP MARKER DISCIPLINE:** I must always check for existing map markers before creating a new one to avoid duplicates.
- **TOOL MAINTENANCE:** I must NEVER defer fixing a broken tool or agent. It is always the highest priority, overriding any in-game objective.

## General Discoveries
- My biggest obstacle is my own memory. I must only trust in-game observation.
- Stunning an NPC can break scripted events, causing dialogue loops.
- The southern path on Route 29 is a dead end.
- The western path on Route 29 is blocked by CUT_TREEs and HEADBUTT_TREEs.
- Talking to Mom does NOT heal my Pokémon. This is a critical mechanic difference from other games.
- Resting in the player's bed does NOT heal Pokémon.
- Repeatedly interacting with an object (like a sign) without new results can lead to loops. I must dismiss dialogue before attempting to move.
- The 'Select' button on the nicknaming screen toggles between uppercase and lowercase keyboards.

## Future Agent Ideas
- **puzzle_solver_assistant:** An agent to manage and prioritize hypotheses for complex puzzles.
- **code_debugger:** An agent that takes code and an error message to suggest potential fixes.

## Game Mechanics & Systems
*PC Storage*: Currently empty.

## Battle and Pokemon Information
*Ignis learned EMBER at Lv12.*
*Ignis grew to Lv15 after defeating a wild Gastly.*
*Type Effectiveness Chart*: Ground is super-effective against Fire. (Verified in battle vs Falkner's Pidgey's MUD-SLAP).

## Area and Navigation Insights

### Tile Traversal and Movement Rules
- **BOOKSHELF**: Impassable. (Verified)
- **COUNTER**: Impassable. (Verified by observation)
- **CUT_TREE**: Impassable, requires a specific ability/item to remove. (Verified)
- **DOOR**: Traversable, acts as a warp tile. (Verified)
- **FLOOR**: Traversable. (Verified)
- **HEADBUTT_TREE**: Impassable. (Verified by observation)
- **LADDER**: Traversable, acts as a warp tile. (Verified)
- **LEDGE_HOP_DOWN/LEFT/RIGHT**: One-way traversal.
- **LONG_GRASS**: Traversable, contains wild Pokémon. (Verified by encounters on Route 30)
- **MART_SHELF**: Impassable. (Verified by pathfinder consistently treating it as a wall)
- **PC**: Impassable. Interacting from an adjacent tile can trigger events. (Verified)
- **RADIO**: Impassable. (Verified by attempting to walk on it)
- **STAIRCASE**: Traversable, acts as a warp tile. (Verified)
- **TALL_GRASS**: Traversable, contains wild Pokémon. (Verified)
- **TOWN_MAP**: Impassable. (Verified by observation)
- **TV**: Impassable. (Verified)
- **VOID**: Impassable. (Verified)
- **WALL**: Impassable. (Verified)
- **WARP_CARPET_DOWN/RIGHT**: Traversable warp.
- **WATER**: Impassable. (Verified by failed pathing attempts)
- **WINDOW**: Impassable. (Verified)
- **FLOOR_UP_WALL**: Appears to be impassable. (Hypothesis, needs verification)

### Past Investigations & Solved Puzzles
- **Fisher NPC Interaction Failure (New Bark Town):** Conclusion: Moving NPCs can disrupt interactions. Stunning them first is a reliable solution.
- **Healing Methods (New Bark Town):** Conclusion: Neither Mom nor the player's bed heals Pokémon in this game.
- **Nickname Screen Controls:** Conclusion: The 'Select' button toggles the keyboard case.
- **Building Identification (Violet City):** Assumption: Building at (21, 29) was the Gym. (Confirmed to be a house with a trade NPC)
- **Sprout Tower vs. Gym:** Assumption: Sprout Tower is separate from the Gym. (Confirmed)
- **MR. POKEMON's House Location:** Assumption: Located on Route 30. (Confirmed)
- **Sprout Tower Puzzle - Ladder Interaction:** Hypothesis: Ladders must be interacted with from an adjacent tile, not by standing on them. Test: Move to (17, 4), face up towards the ladder at (17, 3), and press 'A'. Conclusion: SUCCESS. This triggered the warp back to 2F, confirming this is the correct interaction method for this type of ladder.
- **Sprout Tower Puzzle - 1F Sage Interaction:** Hypothesis (from Agent): Defeating the Sage on 2F triggered a new event or NPC on 1F. Test: Spoke to the Sage at (7, 4) on 1F. Conclusion: FAILED. The Sage repeated his original dialogue about the HM. This hypothesis is debunked.

### Corrected Misunderstandings
- The 'Poké Ball machine' in Elm's lab was a hallucination.
- Hallucinated a warp at (9, 35) on Route 30. There is no warp there.
- Hallucinated a warp at (13, 9) on Route 30. The actual house entrance is at (17, 5).
- **CRITICAL HALLUCINATION (Turn 2667):** Believed I was on Sprout Tower 2F at (17, 3) when I was actually on Sprout Tower 1F at (17, 2).
- **CRITICAL HALLUCINATION (Turn 2886):** Believed I was on Sprout Tower 2F at (6, 4) when I was actually on Sprout Tower 1F at (6, 3).
- **Pathfinder Tool Issue:** The pathfinder was flagged as faulty. I have since fixed it by adding dynamic debug prints to better diagnose future issues.

- **Hypothesis 4 (Agent):** Defeating the Sage on 2F triggered a new event or NPC on 1F. (DEBUNKED)
- **Hypothesis 5 (Agent):** One of the southern wall tiles of the central pillar is an interactable switch.

- **Hypothesis 2 (Agent): Use Key Item on wall.**
  - **Test:** Opened Key Items pocket while facing the wall at (4, 1).
  - **Conclusion:** FAILED. The Key Items pocket is empty. Hypothesis is debunked.

### Sprout Tower Puzzle - New Hypotheses (from Agent - Turn 3252)
After exhausting all previous hypotheses, the `hypothesis_generator` provided the following new ideas:
1.  **Defeating the Sage on 2F removes the wall at x=4.** (FAILED. The wall is still impassable.)
2.  An item or switch appeared on the tile where the Sage was defeated. (Testing by pressing A on (9, 3))
3.  The defeated Sage must be spoken to again to open the path.
4.  The ladder at (6,4) is now the correct path forward.
- **Hypothesis (from Agent):** The defeated Sage must be spoken to again to open the path.
  - **Test:** Move to (11, 3), face the Sage at (12, 3), and press 'A'.