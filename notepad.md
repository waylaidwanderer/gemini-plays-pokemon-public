## Discoveries & Lessons Learned
- My biggest obstacle is my own memory. I must only trust in-game observation.
- Stunning an NPC can break scripted events, causing dialogue loops.
- The 'Poké Ball machine' was a hallucination.
- The southern path on Route 29 is a dead end.
- The western path on Route 29 is blocked by CUT_TREEs and HEADBUTT_TREEs.
- Talking to Mom does NOT heal my Pokémon. This is a critical mechanic difference from other games.
- Resting in the player's bed does NOT heal Pokémon.

## Game Mechanics & Systems
*PC Storage*: Currently empty.

## Battle and Pokemon Information
*My Party*: Ignis (CYNDAQUIL) Lv8.
*Type Effectiveness Chart*: To be built based on battle observations.

## Area and Navigation Insights

### Tile Traversal and Movement Rules
- **BOOKSHELF**: Impassable. (Verified)
- **COUNTER**: Impassable. (Verified by observation)
- **CUT_TREE**: Impassable, requires a specific ability/item to remove. (Verified)
- **DOOR**: Traversable, acts as a warp tile. (Verified)
- **FLOOR**: Traversable. (Verified)
- **HEADBUTT_TREE**: Impassable. (Verified by observation)
- **LEDGE_HOP_DOWN**: One-way ledge. Can only be traversed by moving down onto it. (Verified)
- **LEDGE_HOP_LEFT**: One-way ledge. Can only be traversed by moving left onto it. (Verified)
- **LEDGE_HOP_RIGHT**: One-way ledge. Can only be traversed by moving right onto it. (Verified)
- **PC**: Impassable. Interacting from an adjacent tile can trigger events. (Verified)
- **STAIRCASE**: Traversable, acts as a warp tile. (Verified)
- **TALL_GRASS**: Traversable, contains wild Pokémon. (Verified)
- **TOWN_MAP**: Impassable. (Verified by observation)
- **TV**: Impassable. (Verified)
- **VOID**: Impassable. (Verified)
- **WALL**: Impassable. (Verified)
- **WARP_CARPET_DOWN**: Traversable, acts as a warp tile. (Verified)
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
- **Route 29 Pathfinding Failure:**
  - **Hypothesis 1:** The `find_path_to_target` tool is broken.
    - **Test:** Ran the tool multiple times with different logic and debug prints (Turns 1062-1078).
    - **Conclusion:** FAILED. The tool was functioning correctly. The path was physically impassable.
  - **Hypothesis 2:** The path to Cherrygrove is directly west past the Cooltrainer at (13, 4).
    - **Test:** Attempted to pathfind to the trainer (Turn 1141).
    - **Conclusion:** FAILED. The path is blocked by a one-way `LEDGE_HOP_RIGHT` that cannot be climbed from the east.
- **Route 29 Pathfinding Failure:**
  - **Hypothesis 1:** The `find_path_to_target` tool is broken.
    - **Test:** Ran the tool multiple times with different logic and debug prints (Turns 1062-1078).
    - **Conclusion:** FAILED. The tool was functioning correctly. The path was physically impassable.
  - **Hypothesis 2:** The path to Cherrygrove is directly west past the Cooltrainer at (13, 4).
    - **Test:** Attempted to pathfind to the trainer (Turn 1141).
    - **Conclusion:** FAILED. The path is blocked by a one-way `LEDGE_HOP_RIGHT` that cannot be climbed from the east.