## Discoveries & Lessons Learned
- Deferring tasks, like placing map markers, is a process violation. Significant events must be documented *immediately* in the turn they occur.
- My `simple_battle_strategist` agent is underutilized and I will prioritize using it for all future wild battles to automate decision-making.

## Discoveries & Lessons Learned
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
*My Party*: Ignis (CYNDAQUIL) Lv12, Aether (PIDGEY) Lv3.
*Ignis learned EMBER at Lv12.*
*Type Effectiveness Chart*: To be built based on battle observations.

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
- **WATER**: Impassable without a specific ability (like Surf). (Hypothesis, needs verification by attempting to walk on it)
- **WINDOW**: Impassable. (Verified)

## Puzzles & Hypotheses
- **Fisher NPC Interaction Failure (New Bark Town):**
  - **Observation:** Attempting to interact with the moving Fisher NPC failed, even when adjacent and facing him.
  - **Hypothesis:** The NPC's movement at the exact moment of interaction caused the input to fail.
  - **Test:** Used the `stun_npc` tool to freeze the Fisher in place and interacted again.
  - **Conclusion:** The interaction was successful, confirming the hypothesis. Moving NPCs can disrupt interactions.
- **Healing Methods:**
  - **Hypothesis 1:** Talking to Mom will heal my Pokémon.
    - **Test:** Spoke to Mom at various locations in PlayersHouse1F.
    - **Conclusion:** FAILED. Mom's dialogue does not trigger a heal in this game.
  - **Hypothesis 2:** Resting in the player's bed will heal Pokémon.
    - **Test 1:** Interacted from the side at (1, 4), facing left.
    - **Test 2:** Interacted from below at (1, 4), facing up.
    - **Test 3:** Interacted from directly below at (1, 5), facing up.
    - **Conclusion:** FAILED. Multiple interaction attempts from different positions and facings yielded no result. The bed does not heal Pokémon.
- **Nickname Screen Controls:**
  - **Observation:** Directional inputs did not move the cursor from the starting 'A' position.
  - **Hypothesis 1:** Movement on the screen is broken.
    - **Test:** Press 'Right' once.
    - **Conclusion:** FAILED. Cursor did not move. This falsifies the idea that only vertical movement is broken.
  - **Hypothesis 2:** The 'Select' button might change the input mode.
    - **Test:** Press 'Select' once.
    - **Conclusion:** SUCCESS. The keyboard switched to lowercase and the cursor became movable. The 'Select' button toggles the keyboard case.

## Untested Assumptions
- MR. POKEMON's house is located on Route 30 itself, not a connecting route. (Tested and confirmed)

## Corrected Misunderstandings
- The 'Poké Ball machine' in Elm's lab was a hallucination.
- Hallucinated a warp at (9, 35) on Route 30. There is no warp there.
- Hallucinated a warp at (13, 9) on Route 30. The actual house entrance is at (17, 5).
## Core Principles & Lessons Learned
- I must NEVER defer fixing a broken tool or agent. It is always the highest priority, overriding any in-game objective.
## NPCs and Interactions
- An NPC in a house on Route 30 mentioned that Berries can be found by checking trees.
## Untested Assumptions (Turn 1819)
- **Assumption:** The path to Violet City continues north on Route 30.
- **Alternative Hypothesis:** The path might be on a different route entirely, or require an HM on a previous route. 
- **Test:** If a full exploration of Route 30 yields no path, I will return to Cherrygrove City and Route 29 to search for alternate paths.

## To-Do/Test
- **WATER Tile:** Explicitly try to walk on a WATER tile to confirm it's impassable.
- **Route 30 Northern Path:**
  - **Hypothesis:** The northern path on Route 30 leads to Violet City.
  - **Test:** Explored the entire northern corridor, including both the western and eastern ends.
  - **Conclusion:** FAILED. The northern path is a dead end.
- **Western Ledge Path:**
  - **Hypothesis:** The path west over the ledges leads to Violet City.
  - **Test:** Explored the entire path after jumping down the ledges.
  - **Conclusion:** FAILED. This path is a small loop that leads to a dead end with a sign, forcing a return to the main path.
## NPCs and Interactions
- An Officer in the Route 31 Gatehouse mentioned visiting SPROUT TOWER.
- **WARP_CARPET_RIGHT**: Traversable, acts as a warp tile. (Verified)

## Untested Assumptions (Turn 2132)
- **Assumption:** The building at (21, 29) is the Violet City Gym.
  - **Alternative Hypothesis:** It could be another important building like a Pokémon School, a Mart, or a regular house.
  - **Test:** Enter the building to identify it.
- **Assumption:** Sprout Tower is a separate location from the Gym.
  - **Alternative Hypothesis:** Sprout Tower could be the Gym itself, or a prerequisite challenge before the Gym.
  - **Test:** Find both locations and observe any connections or NPC dialogue that links them.
*Type Effectiveness Discovery*: Ground is super-effective against Fire. (Verified in battle vs Falkner's Pidgey's MUD-SLAP).

## Untested Assumptions (Turn 2391)
- **Assumption:** Sprout Tower is in the northwest part of Violet City.
  - **Alternative Hypothesis:** It could be in the northeast, or accessible via a path I haven't found yet, perhaps even requiring me to leave and re-enter the city from a different route.
- **Assumption:** The path to Azalea Town is south of Violet City.
  - **Alternative Hypothesis:** The path could be west, or require passing *through* Sprout Tower or another location first.