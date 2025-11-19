# Tile Traversal Notes
- WALL: Impassable.
- FLOOR: Traversable.
- TALL_GRASS: Traversable (Wild Pokemon risk).
- LONG_GRASS: Traversable (Wild Pokemon risk).
- STAIRCASE: Traversable, acts as a warp.
- BOOKSHELF: Impassable.
- TOWN_MAP: Impassable.
- TV: Impassable.
- WARP_CARPET_DOWN: Traversable, acts as a warp.
- DOOR: Traversable, acts as a warp.
- WATER: Impassable.
- HEADBUTT_TREE: Impassable.
- GROUND: Traversable, acts as a warp (at map edge).
- BACKGROUND_OBJECTS: Impassable (Signs, etc.).

# Current Plan
- Goal: Reach Cherrygrove City.
- Problem: South path blocked at (13, 14). North path blocked by Cut Tree at (21, 11).
- Plan: Backtrack East to (31, 14), go North through gap at (31, 13), East to x=36. Then North to Row 7 and West to bypass Cut Tree. Note: Dead End at (13, 14) [Wall]., North to Row 8, then West to bypass trees.

# Notes
- Tip: Growlithe found on Route 37 (Radio).
- Tip: Pokémon hide in the grass (Cooltrainer M, Route 29).
- Lesson: If movement is blocked on a traversable tile with no visible objects, check for open menus or full-screen interfaces.
- Defeated L2 Rattata at (33, 7) for 16 XP.