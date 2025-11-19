# Tile Traversal Notes
- WALL: Impassable.
- FLOOR: Traversable.
- STAIRCASE: Traversable, acts as a warp.
- BOOKSHELF: Impassable.
- TOWN_MAP: Impassable.
- TV: Impassable.
- WARP_CARPET_DOWN: Traversable, acts as a warp.
- DOOR: Traversable, acts as a warp.
- WATER: Impassable.
- HEADBUTT_TREE: Impassable.
- GROUND: Traversable, acts as a warp (at map edge).

# Current Plan
- Goal: Travel to Mr. Pokémon's house.
- Steps:
  1. Exit Professor Elm's Lab.
  2. Navigate through Route 29 to Cherrygrove City.
  3. Find the route leading to Mr. Pokémon's house.
- Tool: Building 'find_path' to automate navigation.
- TOWN_MAP: Readable, provides location info.