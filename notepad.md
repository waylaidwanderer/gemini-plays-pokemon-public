# Game Mechanics & Systems
- The Day/Night cycle is an important mechanic in this game, affecting events.

# Lessons Learned
- I must always trust the provided game state information (especially Screen Text) over my own memory or assumptions. My perception can be flawed, but the data is the source of truth.

# Tile Mechanics
- **WALL**: Impassable terrain.
- **FLOOR**: A standard traversable tile.
- **TOWN_MAP**: An interactable object on a wall; impassable.
- **STAIRCASE**: A warp tile that moves the player between floors.
- **TV**: An impassable object.
- **BOOKSHELF**: An impassable object.
- **WARP_CARPET_DOWN**: A warp tile that leads outside or to a lower floor.
- **DOOR**: A warp tile leading into or out of a building.
- **WATER**: Impassable terrain without a specific HM (likely Surf).
- **HEADBUTT_TREE**: An interactable tree, probably requires the Headbutt move. Impassable.
- **TALL_GRASS**: A traversable tile where wild POKéMON can be encountered.
- **LEDGE_HOP_RIGHT**: A one-way tile that can only be traversed by jumping down from the left side.

# Current Quest: Find MR. POKEMON
- **Objective:** Find MR. POKEMON for Professor Elm.
- **Location:** Past Cherrygrove City.
- **Plan:**
    1. Leave Elm's Lab.
    2. Exit New Bark Town to the west.
    3. Traverse the route to Cherrygrove City.
    4. Find MR. POKEMON's house.

# Reminders & Untested Hypotheses
- Investigate the second warp tile at (5, 11) in Elm's Lab to confirm its destination.
- **LEDGE_HOP_DOWN**: Likely a one-way tile that can only be traversed by jumping down from above.