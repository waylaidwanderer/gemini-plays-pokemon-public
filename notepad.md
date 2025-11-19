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
  1. Talk to residents in Elm's House.
  2. Navigate Route 29 to Cherrygrove City.
  3. Find Mr. Pokémon's house.
- Tool: 'find_path' is active.
- TOWN_MAP: Readable, provides location info.
- Tip: Growlithe found on Route 37 (Radio).

- Lesson: If movement is blocked on a traversable tile with no visible objects, check for open menus or full-screen interfaces (like the Town Map) consuming inputs.
- Next: Talk to Fisher NPC.
- Then: Head West to Route 29.