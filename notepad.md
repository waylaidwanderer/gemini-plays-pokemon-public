## Core Principles & Lessons Learned
- **IMMEDIATE ACTION:** I must perform tasks like placing markers, updating my notepad, and fixing tools *immediately*. Deferring tasks, like placing map markers, is a process violation. Significant events must be documented *immediately* in the turn they occur.
- **AGENT USAGE:** When stuck for more than 5 turns on a puzzle, I must use the `hypothesis_generator` agent. My `simple_battle_strategist` agent is underutilized and I will prioritize using it for all future wild battles to automate decision-making.
- **PUZZLE DOCUMENTATION:** My entire problem-solving process (observation, hypothesis, test, conclusion) for any puzzle must be documented in this notepad as it happens.
- **MAP MARKER DISCIPLINE:** I must always check for existing map markers before creating a new one to avoid duplicates.
- **TOOL MAINTENANCE:** I must NEVER defer fixing a broken tool or agent. It is always the highest priority, overriding any in-game objective.

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

## Puzzles, Hypotheses & Assumptions

### Current Investigation: Sprout Tower Navigation
- **Problem:** I am trapped in the eastern sections of Sprout Tower 1F and 2F. There is no visible path to the western sections or the main tower exit from these areas.
- **Failed Hypotheses Log:**
  1. The path to 3F is on the eastern side of 2F. (FAILED)
  2. A direct path exists across 2F from east to west. (FAILED)
  3. I must exit the tower from the eastern 1F section. (FAILED)
  4. The central pillar is interactive. (FAILED)
  5. A path exists on 1F to cross from east to west. (FAILED)
- **Current Hypotheses (from Agent):**
  1. An NPC in the eastern sections must be defeated/spoken to, creating a path.
  2. There is a hidden switch/object on the eastern side of 2F.
  3. A wall in the eastern sections is a secret passage.

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

## NPCs and Interactions
- An Officer in the Route 31 Gatehouse mentioned visiting SPROUT TOWER.
- An NPC in a house on Route 30 mentioned that Berries can be found by checking trees.

## Item Effects
- **PRZCUREBERRY**: Cures paralysis. (Hypothesis based on name)

## Corrected Misunderstandings
- **CRITICAL HALLUCINATION (Turn 2667):** Believed I was on Sprout Tower 2F at (17, 3) when I was actually on Sprout Tower 1F at (17, 2). All plans based on being on 2F were invalid. Corrected my position and plan based on the actual game state.
### Current Investigation: Sprout Tower Navigation (continued)
- **New Hypotheses (from Agent, Turn 2697):**
  1. The pillar can be pushed by walking directly into it. (FAILED - Walking into the pillar at (11, 5) did not move it.) (FAILED - Walking into the pillar at (11, 5) did not move it.)
  2. The pillar sways or moves in response to the player's movement, creating a temporary path.
  3. A specific tile on the floor adjacent to the pillar acts as a trigger when stepped on.

## Sprout Tower Puzzle Update (Turn 2707)
- **New Hypothesis:** The Sage's dialogue about the 'flexible pillar' was a trigger that has now made the pillar passable. My previous pathfinding attempts were made *before* this trigger.
- **Corrected Hallucinations (Recent):**
  - I hallucinated an exit warp on 2F (Turn 2704). The exit is on 1F.
  - I hallucinated a path south of the pillar on 2F (Turn 2686). The pathfinder's debug output confirmed a WALL blocks it.
  - I was on 1F when I thought I was on 2F (Turn 2667).
- **Procedural Correction:** I will no longer use `overwrite` for large notepad edits. I will use `append` for new entries and focused `replace` for corrections to avoid data loss.