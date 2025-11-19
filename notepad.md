# Game Mechanics & Systems
- The Day/Night cycle is an important mechanic in this game, affecting events.

# Lessons Learned
- I must always trust the provided game state information (especially Screen Text) over my own memory or assumptions. My perception can be flawed, but the data is the source of truth.

# Tile Mechanics
- **WALL**: Impassable terrain.
- **FLOOR**: Standard traversable tile.
- **TOWN_MAP**: Interactable object on a wall, likely impassable.
- **STAIRCASE**: A warp tile that moves the player between floors.
- **TV**: Impassable object.
- **BOOKSHELF**: Impassable object.
- **WARP_CARPET_DOWN**: A warp tile that likely leads outside or to a lower floor.
- Day selection menu: UP advances the day, DOWN goes backward.
- **DOOR**: A warp tile, likely leading into a building.
- **WATER**: Impassable terrain without a specific HM (likely Surf).
- **HEADBUTT_TREE**: An interactable tree, probably requires the Headbutt move.

# Current Quest: Find MR. POKEMON
- **Objective:** Find MR. POKEMON for Professor Elm.
- **Location:** Past Cherrygrove City.
- **Plan:**
    1. Leave Elm's Lab.
    2. Exit New Bark Town to the west.
    3. Traverse the route to Cherrygrove City.
    4. Find MR. POKEMON's house.
- **GRASS**: Traversable tile, likely contains wild POKéMON.

# Reminders & Untested Hypotheses
- Investigate the second warp tile at (5, 11) in Elm's Lab to confirm its destination.
- **TALL_GRASS**: Traversable tile where wild POKéMON can be encountered.
- **LEDGE_HOP_RIGHT**: Likely a one-way tile that can only be traversed by jumping down from the left side.
- **LEDGE_HOP_DOWN**: Likely a one-way tile that can only be traversed by jumping down from above.