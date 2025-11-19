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