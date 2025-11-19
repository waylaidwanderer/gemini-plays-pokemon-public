# Game Mechanics & Systems
- The Day/Night cycle is an important mechanic in this game, affecting events.

# Lessons Learned
- I must always trust the provided game state information (especially Screen Text) over my own memory or assumptions. My perception can be flawed, but the data is the source of truth.

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
- **LEDGE_HOP_RIGHT**: A one-way traversable tile. Can only be entered from the left, moving right. Impassable from other directions.
- **LEDGE_HOP_DOWN**: A one-way traversable tile. Based on observation, it can likely only be entered from above, moving down. Impassable from other directions.

# Current Quest: Find MR. POKEMON
- **Objective:** Find MR. POKEMON for Professor Elm.
- **Location:** Past Cherrygrove City.
- **Plan:**
    1. Find a path around the one-way ledges on Route 29.
    2. Traverse the route to Cherrygrove City.
    3. Find MR. POKEMON's house.

# Reminders & Untested Hypotheses
- Investigate the second warp tile at (5, 11) in Elm's Lab to confirm its destination.

# Strategic Lessons
- Before committing to a long path, I must verify my assumptions about the traversability of all tiles along the way. Trying to force a path through a tile that seems impassable based on its type or my prior observations is inefficient.