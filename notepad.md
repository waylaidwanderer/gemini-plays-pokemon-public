## Discoveries & Lessons Learned
- Deferring tasks, like placing map markers, is a process violation. Significant events must be documented *immediately* in the turn they occur.
- My `simple_battle_strategist` agent is underutilized and I will prioritize using it for all future wild battles to automate decision-making.
- When stuck for more than 5 turns on a puzzle, I must use the `hypothesis_generator` agent.
- Always check for existing map markers before creating a new one to avoid duplicates.

## General Discoveries
- My biggest obstacle is my own memory. I must only trust in-game observation.
- Stunning an NPC can break scripted events, causing dialogue loops.
- The 'Poké Ball machine' was a hallucination.
- The southern path on Route 29 is a dead end.
- The western path on Route 29 is blocked by CUT_TREEs and HEADBUTT_TREEs.
- Talking to Mom does NOT heal my Pokémon. This is a critical mechanic difference from other games.
- Resting in the player's bed does NOT heal Pokémon.
- Repeatedly interacting with an object (like a sign) without new results can lead to loops. I must dismiss dialogue before attempting to move.
- The 'Select' button on the nicknaming screen toggles between uppercase and lowercase keyboards.

## Game Mechanics & Systems
*PC Storage*: Currently empty.

## Battle and Pokemon Information
*My Party*: Ignis (QUILAVA) Lv14, Aether (PIDGEY) Lv3, EGG (TOGEPI) Lv5.
*Ignis learned EMBER at Lv12.*
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
- **LEDGE_HOP_DOWN**: One-way ledge. Can only be traversed by moving down onto it. (Verified)
- **LEDGE_HOP_LEFT**: One-way ledge. Can only be traversed by moving left onto it. (Verified)
- **LEDGE_HOP_RIGHT**: One-way ledge. Can only be traversed by moving right onto it. (Verified)
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
- **WARP_CARPET_DOWN**: Traversable, acts as a warp tile. (Verified)
- **WATER**: Impassable. (Verified by failed pathing attempts)
- **WINDOW**: Impassable. (Verified)
- **FLOOR_UP_WALL**: Appears to be impassable. (Hypothesis, needs verification)
- **WARP_CARPET_RIGHT**: Traversable, acts as a warp tile. (Verified)

## Puzzles, Hypotheses & Assumptions

### Current Investigations
- **Sprout Tower Navigation:**
  - **Observation:** Sprout Tower's lower floors are divided by a central pillar, creating an eastern and western section.
  - **Hypothesis 1:** The path to the third floor is on the eastern side of the tower.
  - **Test 1:** Attempted to find a path from the eastern ladder on 2F to the western side. Used pathfinder multiple times.
  - **Conclusion 1:** FAILED. No path exists across the 2F from the east side. The eastern section is a dead end for upward progression.
  - **Hypothesis 2:** I must exit the tower from the eastern section of 1F and re-enter to find a new path.
  - **Test 2:** Attempted to find a path from the eastern section of 1F to the main tower exit.
  - **Conclusion 2:** FAILED. No path exists from the eastern 1F section to the main exit.

### Past Investigations & Solved Puzzles
- **Fisher NPC Interaction Failure (New Bark Town):**
  - **Conclusion:** Moving NPCs can disrupt interactions. Stunning them first is a reliable solution.
- **Healing Methods (New Bark Town):**
  - **Conclusion:** Neither Mom nor the player's bed heals Pokémon in this game.
- **Nickname Screen Controls:**
  - **Conclusion:** The 'Select' button toggles the keyboard case.
- **Building Identification (Violet City):**
  - **Assumption:** Building at (21, 29) was the Gym. **(Confirmed to be a house with a trade NPC)**
- **Sprout Tower vs. Gym:**
  - **Assumption:** Sprout Tower is separate from the Gym. **(Confirmed)**
- **MR. POKEMON's House Location:**
  - **Assumption:** Located on Route 30. **(Confirmed)**

## Corrected Misunderstandings
- The 'Poké Ball machine' in Elm's lab was a hallucination.
- Hallucinated a warp at (9, 35) on Route 30. There is no warp there.
- Hallucinated a warp at (13, 9) on Route 30. The actual house entrance is at (17, 5).

## Core Principles & Lessons Learned
- I must NEVER defer fixing a broken tool or agent. It is always the highest priority, overriding any in-game objective.

## NPCs and Interactions
- An Officer in the Route 31 Gatehouse mentioned visiting SPROUT TOWER.
- An NPC in a house on Route 30 mentioned that Berries can be found by checking trees.

## Item Effects
- **PRZCUREBERRY**: Cures paralysis. (Hypothesis based on name)