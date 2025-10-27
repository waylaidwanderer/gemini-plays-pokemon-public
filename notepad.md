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

- **Route 29 Pathfinding Failure (West):**
  - **Hypothesis:** I can reach the Cooltrainer at (13, 4) from the eastern part of the upper path.
    - **Test:** Attempted to pathfind from (17, 3) to (13, 4) on turn 1141.
    - **Conclusion:** FAILED. The path is blocked by a one-way `LEDGE_HOP_RIGHT` that prevents westward movement from the upper plateau.
- **Route 29 Pathfinding Failure (West):**
  - **Hypothesis:** I can reach the Cooltrainer at (13, 4) from the eastern part of the upper path.
    - **Test:** Attempted to pathfind from (17, 3) to (13, 4) on turn 1141.
    - **Conclusion:** FAILED. The path is blocked by a one-way `LEDGE_HOP_RIGHT` that prevents westward movement from the upper plateau.
- **Route 29 Pathfinding Failure (South Ledges):**
  - **Hypothesis:** I can jump down the ledges to the south from the upper plateau at (17, 3).
    - **Test:** Attempted to pathfind from (17, 3) to (13, 5) on turn 1145.
    - **Conclusion:** FAILED. There is no direct path down from this part of the plateau.
- **Route 29 Pathfinding Failure (Lower Path West):**
  - **Hypothesis:** I can reach the western unseen area from the lower plateau at (24, 10).
    - **Test:** Attempted to pathfind from (24, 10) to (13, 12) on turn 1154.
    - **Conclusion:** FAILED. The path is blocked by `CUT_TREE` and `HEADBUTT_TREE` tiles, and the eastern path is blocked by one-way ledges. This area is a dead end.
- **Route 29 Pathfinding Failure (Lower Path West):**
  - **Hypothesis:** I can reach the western unseen area from the lower plateau at (24, 10).
    - **Test:** Attempted to pathfind from (24, 10) to (13, 12) on turn 1154. Confirmed impassable by attempting to walk into HEADBUTT_TREE on turn 1164.
    - **Conclusion:** FAILED. The path is blocked by `CUT_TREE` and `HEADBUTT_TREE` tiles, and the eastern path is blocked by one-way ledges. This area is a dead end.
- **`find_reachable_unseen_tiles` Tool Failure:**
  - **Observation:** The tool returned a list of unseen tiles that are not reachable from my current position on the isolated lower plateau of Route 29 (turn 1167).
  - **Hypothesis:** The tool is not correctly performing a reachability check (BFS/DFS) from the player's current position and is instead just identifying all unseen tiles adjacent to any seen tile on the map.
  - **Conclusion:** The tool is currently unreliable for finding explorable paths and needs to be fixed.