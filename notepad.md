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
- **LADDER**: Traversable warp. Must be activated by moving *onto* the tile from an adjacent tile, not by pressing 'A' while standing on it. (Verified by Overwatch critique)
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

### [ARCHIVED] Sprout Tower 2F Pillar Puzzle

- **Untestable Hypotheses:**
  - A switch or path on the 3rd floor of Sprout Tower opens the western section of the 2nd floor.
  - All other trainers on Sprout Tower 2F must be defeated before the Sage at (12, 3) will trigger the event again.
- **Debunked Hypotheses:**
  - Use Key Item on wall.
  - Defeating the Sage on 2F removes the wall at x=4.
  - An item or switch appeared on the tile where the Sage was defeated.
  - The defeated Sage must be spoken to again to open the path.

  - Pressing 'interact' while facing the eastern wall of the pillar will cause it to move.
  - The pillar's 'flexible' nature means it can be pushed.
  - Examining the floor tiles directly adjacent to the pillar reveals a hidden switch.
  - The wall blocking the western section is an illusion or has a hidden switch.
  - The effect of interacting with the Sage at (12,3) is different depending on which adjacent tile the player stands on.
  - Stepping on a specific tile inside the temporarily passable central pillar triggers the opening of the western wall.
  - An NPC on the 1st floor has new dialogue or an item that allows passage after interacting with the Sage.

  - Interacting with the Sage from a different adjacent tile (e.g., from the south at (12, 4)) triggers the event.
  - Interacting with the Sage at (12, 3) multiple times in a row is required to trigger the event.
  - Interacting with the central pillar first, and then immediately interacting with the Sage at (12, 3), will trigger the event.

### Corrected Misunderstandings
- The 'Poké Ball machine' in Elm's lab was a hallucination.
- Hallucinated a warp at (9, 35) on Route 30. There is no warp there.
- Hallucinated a warp at (13, 9) on Route 30. The actual house entrance is at (17, 5).
- **CRITICAL HALLUCINATION (Turn 2667):** Believed I was on Sprout Tower 2F at (17, 3) when I was actually on Sprout Tower 1F at (17, 2).
- **CRITICAL HALLUCINATION (Turn 2886):** Believed I was on Sprout Tower 2F at (6, 4) when I was actually on Sprout Tower 1F at (6, 3).
- **Pathfinder Tool Issue:** The pathfinder was flagged as faulty. I have since fixed it by adding dynamic debug prints to better diagnose future issues.

- **Hypothesis 4 (Agent):** Defeating the Sage on 2F triggered a new event or NPC on 1F. (DEBUNKED)
- **Hypothesis 5 (Agent):** One of the southern wall tiles of the central pillar is an interactable switch.

### [ARCHIVED] Sprout Tower 2F Pillar Puzzle

- **Untestable Hypotheses:**
  - A switch or path on the 3rd floor of Sprout Tower opens the western section of the 2nd floor.
  - All other trainers on Sprout Tower 2F must be defeated before the Sage at (12, 3) will trigger the event again.
- **Debunked Hypotheses:**
  - Use Key Item on wall.
  - Defeating the Sage on 2F removes the wall at x=4.
  - An item or switch appeared on the tile where the Sage was defeated.
  - The defeated Sage must be spoken to again to open the path.

  - Pressing 'interact' while facing the eastern wall of the pillar will cause it to move.
  - The pillar's 'flexible' nature means it can be pushed.
  - Examining the floor tiles directly adjacent to the pillar reveals a hidden switch.
  - The wall blocking the western section is an illusion or has a hidden switch.
  - The effect of interacting with the Sage at (12,3) is different depending on which adjacent tile the player stands on.
  - Stepping on a specific tile inside the temporarily passable central pillar triggers the opening of the western wall.
  - An NPC on the 1st floor has new dialogue or an item that allows passage after interacting with the Sage.

  - Interacting with the Sage from a different adjacent tile (e.g., from the south at (12, 4)) triggers the event.
  - Interacting with the Sage at (12, 3) multiple times in a row is required to trigger the event.
  - Interacting with the central pillar first, and then immediately interacting with the Sage at (12, 3), will trigger the event.

## Future Agent Ideas (from reflection)
- **performance_analyst:** An agent to analyze my recent turns and suggest improvements based on my core principles.
- **gym_prep_advisor:** An agent to help plan long-term goals, like what level my Pokemon should be for the next gym.

## NPCs and Interactions
- YOUNGSTER at (5, 18) in Violet City mentioned a 'wiggly tree' that 'squirms and dances'. This is likely a hint about how to interact with HEADBUTT_TREEs.

## Future Agent Ideas (from reflection)
- **pathfinder_diagnostician:** An agent to analyze the pathfinder's debug grid to suggest fixes or identify the cause of pathing failures.

- **WARP_CARPET_DOWN**: Traversable, acts as a warp tile. (Verified)

### Sprout Tower Puzzle - New Hypotheses (from Agent - Turn 3590)
1. All other Sages on Sprout Tower 2F must be defeated before interacting with the Sage at (12, 3).
2. The interaction with the Sage at (12, 3) only makes the pillar passable during a specific time of day (e.g., night).
3. The player must have a specific Pokémon in the first slot of their party when interacting with the Sage at (12, 3). (DEBUNKED - Switched lead to Aether, no effect.)
4. The floor tiles in the room with the Sage at (12,3) contain a visual pattern or clue that needs to be followed or replicated.
### Sprout Tower Puzzle - New Hypotheses (from Agent - Turn 3654)
1. Defeating every Sage on the 2nd floor causes the central pillar to become passable.
2. Exiting the 2nd floor (e.g., by going down to 1F) and then returning resets the pillar puzzle, allowing the Sage at (12, 3) to trigger it again.
3. After the initial event, the trigger NPC changes; interacting with a different Sage on the 2nd floor now makes the pillar passable.
- **CRITICAL HALLUCINATION (Turn 3658):** Believed I was on Sprout Tower 2F at (6, 4) after climbing a ladder, but was actually still on Sprout Tower 1F at (6, 3). This invalidated my entire plan.
### Sprout Tower Puzzle - New Hypotheses (from Agent - Turn 3673)
1. The central pillar can be moved or made passable by interacting with it directly.
2. The Sage at (12, 3) will make the pillar passable if spoken to from a different adjacent tile, such as from the north (12, 2) or south (12, 4).
3. A hidden switch exists on the floor in the accessible eastern area which, when activated, makes the pillar passable.