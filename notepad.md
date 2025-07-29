# Gem's Pokémon Crystal Adventure Log

# I. Core Directives & Lessons Learned
*   **Proactive Data Management:** All new information must be recorded *immediately*. Data management is the highest priority.
*   **Trust Your Tools:** Once a tool is verified, its output must be trusted. If a tool reports no path, the area is unreachable. Stop re-testing and change high-level strategy.
*   **Mark Warps Immediately:** Mark both the entrance and exit of any warp immediately upon transitioning between maps. This is non-negotiable.
*   **Avoid Repetitive Failures:** If a sequence of actions fails repeatedly, document it, and deliberately pivot to a new strategy. Do not get stuck in loops.
*   **Verify Location:** Always verify current map and coordinates before planning any navigation, especially after a map transition or interruption.
*   **Link NPC Markers:** All map markers for NPCs or movable objects MUST be linked to their `object_id` to ensure data integrity.
*   **Fix Tools Immediately:** If a tool produces a verifiable error (e.g., generates an invalid path, crashes, or returns incorrect information), fixing it becomes the absolute highest priority, superseding any gameplay objective.

## B. Tile Traversal Rules
*   **Traversable:** TALL_GRASS, LONG_GRASS, DOOR, WARP_CARPET_DOWN, LADDER, FLOOR.
*   **Impassable (Verified):** WALL, WINDOW, CUT_TREE, SIGN, BOOKSHELF, BLACKBOARD, MART_SHELF, BUOY, TV, TOWN_MAP, RADIO, INCENSE_BURNER, BIRD, HEADBUTT_TREE, FRUIT_TREE, COMPUTER, PRINTER, VOID.
*   **Special Interaction (Impassable but Interactable):**
    *   **PC:** Impassable. Interact by standing below it at (X, Y+1), facing up, and pressing 'A'.
    *   **COUNTER:** Impassable. Interact with NPCs behind it by standing in front of the counter and pressing 'A'.
*   **One-Way Traversal:**
    *   LEDGE_HOP_DOWN: Can only be entered from above.
    *   LEDGE_HOP_RIGHT: Can only be entered from the left.
    *   LEDGE_HOP_LEFT: Can only be entered from the right.
*   **Special Interaction (Warp):**
    *   **CAVE:** Can act as a one-way warp. The tile at Route 33 (11, 9) is a confirmed one-way entrance to Union Cave (17, 31). The tile at Route 32 (6, 79) is a confirmed one-way entrance to Union Cave (17, 3). Should be treated as impassable for pathfinding.
    *   **WARP_CARPET_RIGHT:** Requires being on the tile, facing the direction of the warp, and then pressing the directional button again.
    *   **WARP_CARPET_LEFT:** Requires being on the tile, facing the direction of the warp, and then pressing the directional button again.
*   **Special Interaction (Weird Walls):**
    *   **FLOOR_UP_WALL:** A special tile type found in Union Cave. Movement onto this tile from an adjacent FLOOR tile is blocked. This was confirmed at (6, 17) -> (6, 18). It acts as a wall if approached from below (Y+1), but can be walked on from the sides or above. Essentially, it's a one-way ledge from above.
*   **Special Interaction (Fishing):**
    *   WATER: Impassable to walk on, but can be fished in with a rod.
*   **VOID:** Impassable. Confirmed by attempting to move left from (0, 33).

# II. Battle Information

## A. Verified Type Matchups
*   Ghost has NO EFFECT on Normal.
*   Normal has NO EFFECT on Ghost.
*   Unown's Hidden Power (type unknown) can be super-effective against Fire.

## B. Trainer Rosters
*   **Falkner (Violet City):** Pidgey (Lv7), Pidgeotto (Lv9).
*   **Bugsy (Azalea Town):** Metapod (Lv14), Kakuna (Lv14), Scyther (Lv16).
*   **Fisher Justin (Route 32):** Magikarp (Lv5), Magikarp (Lv5), Magikarp (Lv15), Magikarp (Lv5).

# III. Story & Quests

## A. Current Quest
*   **Current Quest:** Solve the Ruins of Alph puzzles.

## B. NPC Hints & Lore
*   A Fisher in Union Cave at (14, 19) mentioned that strange roars can be heard from deep within the cave on weekends.
*   WADE on Route 31 will share BERRIES if I visit him.
*   Hiker Anthony called and said there are tons of DUNSPARCE in DARK CAVE, especially in areas without strong POKéMON.

# IV. Tool Status & Available Agents
*   **Python Tools (Current Status: Confirmed Non-functional):** Direct testing via `run_code` has confirmed the Python sandbox is not running. All Python-based tools (`pathfinder`, `unseen_tile_checker`, `run_code`) are unusable until the environment is fixed.
*   **Reasoning Agents (Functional):** The following agents are available for strategic analysis:
    *   **battle_strategist:** Recommends the best action in a battle.
    *   **exploration_strategist:** Recommends the most strategic unseen tile to explore (requires manual reachability check).
    *   **quest_strategist:** Brainstorms hypotheses to overcome stalled quests.

# VI. Key Items & HMs
*   **OLD ROD:** Received from the Fishing Guru in the Route 32 Pokémon Center.

# VII. Held Items
*   **POISON BARB:** Received from FRIEDA on Route 32 on a Friday. Boosts the power of poison-type moves.
*   **MIRACLE SEED:** Received from Cooltrainer M on Route 32. Boosts the power of grass-type moves.

# X. Contingency Plans
*   **Route 32 North Path Failure:** My primary assumption is that the path to Route 36 is north through Route 32. If this path is blocked or proves to be a dead end, my contingency plan is to return to the southern part of Route 32 and explore it thoroughly to see if it leads to an alternative route to Goldenrod City.

# XIV. Battle Mechanics (Newly Observed)
*   **Wrap:** Traps the target for several turns, preventing them from switching or fleeing.