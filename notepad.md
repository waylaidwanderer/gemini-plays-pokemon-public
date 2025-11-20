# Game Mechanics & Systems
- The Day/Night cycle is an important mechanic in this game, affecting events.

# Current Quest: Challenge the Violet City Gym
- **Objective:** Travel to Violet City and defeat the Gym Leader.
- **Status:** Just finished the catching tutorial on Route 29.
- **Plan:** Travel west through Route 29 to Cherrygrove City, then north to Route 30 and beyond.

# Key Items
- **MYSTERY EGG:** An egg from MR. POKEMON for PROF. ELM to study.
- **POKéDEX:** A high-tech encyclopedia from PROF. OAK to record POKéMON data.

# Strategic Lessons
- Trust the provided game state information over my own visual perception.
- Do not assume a quest is complete without explicit in-game confirmation.
- When a plan repeatedly fails, I must question my root hypothesis.
- When I discover a new tile mechanic or game rule, I must immediately review and update any relevant custom tools.
- Trust the output of my tools. If `find_path` returns "No path found," it's a strong indicator that my assumption about the path is wrong, not that the tool is broken.
- Some maps can be partitioned, making certain areas inaccessible from others on the same floor.
- **CRITICAL:** Before pathfinding near a moving NPC, ALWAYS use `stun_npc` to freeze them first. This is far more efficient than manual tracking.
- **CRITICAL:** When using `notepad_edit` with the "replace" action, the `old_text` must be an EXACT match. Copy from system suggestions if available to avoid errors.

# Tile Mechanics
- **WALL**: Impassable terrain.
- **FLOOR**: A standard, fully traversable tile.
- **TOWN_MAP**: An interactable object on a wall; impassable.
- **STAIRCASE**: A traversable warp tile that moves the player between floors.
- **TV**: An impassable object.
- **BOOKSHELF**: An impassable object.
- **WINDOW**: An impassable object, functions like a wall.
- **RADIO**: An impassable object.
- **WARP_CARPET_DOWN**: A traversable warp tile that leads outside or to a lower floor.
- **DOOR**: A traversable warp tile leading into or out of a building.
- **WATER**: Impassable terrain without a specific HM (likely Surf).
- **HEADBUTT_TREE**: An interactable tree, probably requires the Headbutt move. Impassable.
- **TALL_GRASS**: Fully traversable tile. Wild POKéMON can be encountered here.
- **LEDGE_HOP_RIGHT**: A one-way traversable tile. Can only be entered from the left, moving right.
- **LEDGE_HOP_DOWN**: A one-way traversable tile. Can only be entered from above, moving down.
- **LEDGE_HOP_LEFT**: A one-way traversable tile. Can only be entered from the right, moving left.
- **CUT_TREE**: An impassable tree that likely requires the HM move Cut to remove.
- **COUNTER**: Impassable terrain, usually a barrier in front of an NPC.
- **VOID**: Impassable, appears to be an empty space off the edge of the map.
- **MART_SHELF**: Impassable terrain, functions like a wall.

# Battle Mechanics
- Pokémon holding a BERRY can automatically use it to heal themselves when their HP gets low in battle.
- Poisoned Pokémon lose 1 HP every four steps outside of battle.
- Accuracy-lowering moves like SMOKESCREEN are not a guaranteed defense. Opponents can still land hits.
- The auto-activation threshold for a held BERRY is likely below 25% HP.

# Object Mechanics
- **FRUIT_TREE**: An interactable object that functions as an obstacle. Likely provides a BERRY.

# Exploration Targets
- The `check_unseen_reachability` tool has confirmed the following unseen tiles are reachable on Route 29: [[38, 2], [39, 2], [40, 2], [41, 2], [42, 3], [43, 2], [44, 2], [45, 2], [4, 15], [5, 15], [6, 15], [7, 15]]

# NPC Behavior
- YOUNGSTER (ID 5) on Route 30 has been defeated.
- YOUNGSTER (ID 1) at (5, 26) on Route 30 is an active trainer.

# Menu Navigation
- For complex menu inputs (like on-screen keyboards), perform all directional movements in one turn and the final confirmation ('A' button) in the next. Do not mix directional and action buttons in the same input sequence to avoid errors.

# Game Systems Update
- Received 5 POKé BALLS from the scientist in Elm's Lab. I can now catch wild Pokémon.

# Archived Objectives
## Finding Mom
- **Hypothesis 1:** Mom is at her usual spot (7, 4). **Result:** Failed. She was not there.
- **Hypothesis 2:** Mom is upstairs. **Result:** Failed. She was not there.
- **Hypothesis 3:** Mom's appearance is triggered by attempting to leave the house. **Result:** Failed.
- **Hypothesis 4:** Mom's appearance is triggered by attempting to leave New Bark Town. **Result:** Failed. I successfully transitioned to Route 29 without her appearing. I have put this objective on hold.