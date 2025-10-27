## Discoveries & Lessons Learned
- My biggest obstacle is my own memory. I must only trust in-game observation.
- Stunning an NPC can break scripted events, causing dialogue loops.
- The 'Poké Ball machine' was a hallucination.
- The southern path on Route 29 is a dead end.
- The western path on Route 29 is blocked by CUT_TREEs and HEADBUTT_TREEs.
- Talking to Mom does NOT heal my Pokémon. This is a critical mechanic difference from other games.
- Resting in the player's bed does NOT heal Pokémon.
- Repeatedly interacting with an object (like a sign) without new results can lead to loops. I must dismiss dialogue before attempting to move.

## Game Mechanics & Systems
*PC Storage*: Currently empty.
*Key Items*:
- BERRY: Heals a Pokémon.
- MYSTERY EGG: An egg received from MR. POKEMON to be delivered to PROF. ELM.
- POKéDEX: A hi-tech encyclopedia that records data on Pokémon.

## Battle and Pokemon Information
*My Party*: Ignis (CYNDAQUIL) Lv9.
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

- **Route 29 Pathfinding Failure (South Ledges):**
  - **Hypothesis:** I can jump down the ledges to the south from the upper plateau at (17, 3).
    - **Test:** Attempted to pathfind from (17, 3) to (13, 5) on turn 1145.
    - **Conclusion:** FAILED. There is no direct path down from this part of the plateau.
- **Route 29 Pathfinding Summary:**
  - The southern path is a dead end. (Verified)
  - The western path from the lower plateau is blocked by `CUT_TREE` and `HEADBUTT_TREE` tiles. (Verified)
  - The eastern path from the upper plateau is blocked by one-way `LEDGE_HOP_RIGHT` tiles. (Verified)
- **`find_reachable_unseen_tiles` Tool Status:**
  - **Initial State:** The tool was unreliable, incorrectly identifying unreachable tiles as reachable.
  - **Fix:** Replaced the flawed logic with a Breadth-First Search (BFS) starting from the player's position, incorporating correct ledge traversal rules.
  - **Current Status:** The tool is now considered fixed and reliable for exploration planning.
- **Pokecenter2F (Cherrygrove City):** This floor is dedicated to link features (Trade Machine, Battle Machine, Time Capsule). All services are currently unavailable, making the entire floor a dead end for now.

## Untested Assumptions
- MR. POKEMON's house is located on Route 30 itself, not a connecting route. (Tested and confirmed)

## Corrected Misunderstandings
- The 'Poké Ball machine' in Elm's lab was a hallucination.
- Hallucinated a warp at (9, 35) on Route 30. There is no warp there.
- Hallucinated a warp at (13, 9) on Route 30. The actual house entrance is at (17, 5).