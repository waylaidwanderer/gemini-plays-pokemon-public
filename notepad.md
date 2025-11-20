# Game Mechanics & Systems
- The Day/Night cycle is an important mechanic in this game, affecting events.

# Current Quest: Find MR. POKEMON
- **Objective:** Find MR. POKEMON for Professor Elm.
- **Location:** Past Cherrygrove City.
- **Plan:**
    1. Find a path around the one-way ledges on Route 29.
    2. Traverse the route to Cherrygrove City.
    3. Find MR. POKEMON's house.

# Strategic Lessons
- I must always trust the provided game state information (especially Screen Text) over my own memory or assumptions. My perception can be flawed, but the data is the source of truth.
- When a plan repeatedly fails or seems overly complex, I must question my root hypothesis. For example, assuming a path-blocking NPC is always a trainer is a false constraint that led to wasted time. I must verify foundational assumptions before building complex strategies on top of them.
- When I discover a new tile mechanic or game rule, I must immediately review and update any relevant custom tools (like `find_path`) to incorporate the new logic. A reactive approach to tool maintenance is inefficient and leads to repeated failures.
- My tools are only as reliable as I make them. I must test them against *all* known game mechanics after creation or modification.
- Not all NPCs who block a path are trainers. If interaction leads to looped dialogue instead of a battle, they are likely a non-battling NPC and I should move on.

# Tile Mechanics
- **WALL**: Impassable terrain.
- **FLOOR**: A standard, fully traversable tile.
- **TOWN_MAP**: An interactable object on a wall; impassable.
- **STAIRCASE**: A traversable warp tile that moves the player between floors.
- **TV**: An impassable object.
- **BOOKSHELF**: An impassable object.
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

# Reminders & Untested Hypotheses
- Investigate the second warp tile at (5, 11) in Elm's Lab to confirm its destination.

# Battle Mechanics
- Pokémon holding a BERRY can automatically use it to heal themselves when their HP gets low in battle.

# Tile Mechanics Update
- **WARP_CARPET_DOWN**: A traversable warp tile. If normal movement down is blocked, pressing the 'Down' button directly on the tile may trigger the warp.

# Object Mechanics
- **FRUIT_TREE**: An interactable object that functions as an obstacle. Likely provides a BERRY.

# Reminders & Untested Hypotheses
- Investigate the properties of `LONG_GRASS` tiles when first encountered.

# Strategic Lessons
- Trust the output of my tools. If `find_path` returns "No path found," it's a strong indicator that my assumption about the path is wrong, not that the tool is broken. I must re-evaluate the map layout.

# Exploration Targets
- The `check_unseen_reachability` tool confirmed the following unseen tiles are reachable:
  - (38, 2), (39, 2), (40, 2), (41, 2), (42, 3), (43, 2), (44, 2), (45, 2)
  - (11, 6), (11, 7), (11, 8)
  - (10, 9), (9, 10), (11, 9), (9, 11)

# Pokecenter2F Notes
- The northern rooms on this floor, containing warps at (5,0), (9,0), and (13,2), are inaccessible from the main southern area.

# Tile Mechanics
- **DOOR**: A traversable warp tile leading into or out of a building.