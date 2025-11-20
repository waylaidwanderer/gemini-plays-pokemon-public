# Game Mechanics & Systems
- The Day/Night cycle is an important mechanic in this game, affecting events.

# Current Quest: Find MR. POKEMON
- **Objective:** Get the item from MR. POKEMON for Professor Elm.
- **Status:** Explored a house on Route 30. Spoke to a POKEFAN_M who gave me a BERRY. Confirmed this is NOT MR. POKEMON.
- **Plan:** Leave this house and continue exploring Route 30 to find the correct location.

# Strategic Lessons
- Trust the provided game state information (especially the on-screen object list) over my own visual perception. My perception can be flawed, but the data is the source of truth.
- Do not assume a quest is complete without explicit in-game confirmation (like receiving a key item). Verify by re-interacting or exploring further if the initial interaction doesn't complete the objective.
- When a plan repeatedly fails or seems overly complex, I must question my root hypothesis.
- When I discover a new tile mechanic or game rule, I must immediately review and update any relevant custom tools.
- Trust the output of my tools. If `find_path` returns "No path found," it's a strong indicator that my assumption about the path is wrong, not that the tool is broken.
- Some maps can be partitioned, making certain areas inaccessible from others on the same floor.
- For moving NPCs, it's best to use the `stun_npc` tool to freeze them in place before attempting to interact.

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

# Battle Mechanics
- Pokémon holding a BERRY can automatically use it to heal themselves when their HP gets low in battle.
- Poisoned Pokémon lose 1 HP every four steps outside of battle.

# Object Mechanics
- **FRUIT_TREE**: An interactable object that functions as an obstacle. Likely provides a BERRY.

# Exploration Targets
- The `check_unseen_reachability` tool confirmed the following unseen tiles are reachable:
  - (38, 2), (39, 2), (40, 2), (41, 2), (42, 3), (43, 2), (44, 2), (45, 2)
  - (11, 6), (11, 7), (11, 8)
  - (10, 9), (9, 10), (11, 9), (9, 11)