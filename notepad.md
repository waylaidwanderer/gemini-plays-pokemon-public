# Game Mechanics & Systems
- The Day/Night cycle is an important mechanic in this game, affecting events.

# Current Quest: Return the MYSTERY EGG
- **Objective:** Get the MYSTERY EGG to Professor Elm.
- **Status:** Received MYSTERY EGG from MR. POKEMON and POKéDEX from PROF. OAK. Now returning to New Bark Town.
- **Plan:** Travel east through Route 29 to New Bark Town.

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

# Reminders & Untested Hypotheses
- Investigate the second warp tile at (5, 11) in Elm's Lab to confirm its destination.
- Investigate the properties of `LONG_GRASS` tiles when first encountered.
- Investigate unmarked warp at (31, 11) in Cherrygrove City.

# Battle Mechanics
- Pokémon holding a BERRY can automatically use it to heal themselves when their HP gets low in battle.
- Poisoned Pokémon lose 1 HP every four steps outside of battle.

# Object Mechanics
- **FRUIT_TREE**: An interactable object that functions as an obstacle. Likely provides a BERRY.

# Exploration Targets
- The `check_unseen_reachability` tool has confirmed the following unseen tiles are reachable: [[10, 8], [11, 8], [12, 8], [13, 8], [14, 8], [15, 8], [16, 8], [17, 8], [18, 9], [18, 10], [18, 11], [19, 14], [5, 15], [19, 15], [5, 16], [5, 18], [5, 19], [5, 20], [5, 21], [5, 24], [2, 25], [1, 26], [1, 27], [1, 28], [1, 29], [1, 30], [1, 31], [1, 32], [1, 33], [1, 34], [1, 35], [2, 37], [1, 36], [2, 38], [2, 39], [2, 40], [2, 41]]

# NPC Behavior
- YOUNGSTER (ID 5) on Route 30 has been defeated.
- YOUNGSTER (ID 1) at (5, 26) on Route 30 is an active trainer.

# Battle Lessons
- Accuracy-lowering moves like SMOKESCREEN are not a guaranteed defense. Opponents can still land hits.
- The auto-activation threshold for a held BERRY is likely below 25% HP.
- Do not mix directional and action buttons in a single input sequence.

# New Bark Town Exploration
- Investigate unmarked warp at (3, 11).
- Explore unseen areas of the town.

# Reminders & Untested Hypotheses
- Investigate the second warp tile at (5, 11) in Elm's Lab to confirm its destination.

# Menu Navigation
- For complex menu inputs (like on-screen keyboards), perform all directional movements in one turn and the final confirmation ('A' button) in the next. Do not mix directional and action buttons in the same input sequence to avoid errors.