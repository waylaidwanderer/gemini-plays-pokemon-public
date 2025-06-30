# Gem's Pokémon Crystal Notepad

## I. Strategic Overview

### Current Strategy
- **Primary Objective:** My main goal is to get the Hive Badge from the Azalea Town Gym. 
- **Current Plan:** I am completely stuck in Violet City. My attempts to reach the southern exit have failed repeatedly. I am now pivoting to a full exploration of the city to find any alternative path forward.

### Reminders & Best Practices
- **Tool Failures:** I must be persistent in debugging my tools. I will not abandon a tool just because it fails; instead, I will perform a thorough, systematic, and incremental logical review.
- **Mark Dead Ends:** Mark all confirmed dead ends with '🚫' immediately.

## II. Untested Assumptions
- The south exit is the only way to Route 32. (Test: Explore all of Violet City)
- The `path_finder` tool's A* logic is sound, and bugs are data-related. (Test: Continue systematic, incremental testing)
- The Lass NPC is a solid obstacle. (Test: Attempt to walk through her)
- HEADBUTT_TREEs are interactable with a move. (Test: Use HEADBUTT from the party menu when available)

## III. Battle Intel

### Rival SILVA's Team
- CHIKORITA: Lv5 (Last seen in New Bark Town)

### Observed Movesets
- Wild Poliwag: BUBBLE
- Wild Hoothoot: TACKLE, GROWL, FLASH, FORESIGHT
- Wild Bellsprout: VINE WHIP, GROWTH
- Wild Caterpie: TACKLE, STRING SHOT
- Wild Ekans: (unknown)
- Wild Hoppip: TAIL WHIP, SYNTHESIS
- Wild Rattata: TACKLE, TAIL WHIP
- Wild Wooper: TAIL WHIP, WATER GUN

### Type Effectiveness Chart (Verified)
- Normal is not very effective against Water.
- Normal is not very effective against Rock/Ground.

## IV. World Knowledge & Mechanics

### Tile Traversal Rules (Verified)
- **Objects are impassable:** Most map objects (items, trees, signs, active NPCs, etc.) act as walls.
- **Defeated Trainers:** Passability is inconsistent. Each must be tested.
- **WALL:** Impassable.
- **FLOOR:** Traversable.
- **TALL_GRASS / LONG_GRASS:** Traversable, triggers wild encounters.
- **LEDGE:** One-way downward traversal.
- **COUNTER:** Impassable.
- **DOOR/CAVE:** Warp tile, triggered by movement.
- **MART_SHELF/BOOKSHELF/TV/RADIO/PC/TOWN_MAP/WINDOW/PAINTING/STATUE/PILLAR:** Impassable scenery.
- **FLOOR_UP_WALL:** One-way traversal. Can only be entered from below (moving up).
- **WARP_CARPET_DOWN:** Warp tile, triggered by movement.
- **WARP_CARPET_RIGHT:** Warp tile, triggered by movement.
- **VOID:** Impassable.
- **BUOY:** Impassable scenery.
- **CUT_TREE:** Impassable without CUT.
- **WATER:** Impassable without SURF.
- **HEADBUTT_TREE:** Impassable by walking.
- **FLOOR_ALLOW_HOP_DOWN:** One-way traversal downward.
- **FLOOR_ALLOW_HOP_LEFT:** One-way traversal to the left.
- **FLOOR_ALLOW_HOP_RIGHT:** One-way traversal to the right.
- **FLOOR_ALLOW_HOP_DOWN_OR_RIGHT:** One-way traversal down or right.

### Misc Mechanics
- HMs must be used from the PACK menu, not the Pokémon's party menu.

## V. Tool Development Log
- **path_finder:** ABANDONED. The tool is fundamentally broken after numerous, systematic debugging attempts failed to resolve its inefficient pathing. Further effort is halting game progress. I will proceed with careful manual navigation until a new approach for automated pathfinding is developed.
- **route_finder:** The tool initially had a bug where it only considered the first exit from a map. This has been fixed by iterating through all possible start nodes. A second bug was discovered where it did not account for intra-map travel; this has also been fixed.