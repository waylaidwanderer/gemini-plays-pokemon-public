# Gem's Pokémon Crystal Notepad

## I. Strategic Overview

### Current Strategy
- **Primary Objective:** My main goal is to get the Hive Badge from the Azalea Town Gym.
- **Current Plan:** I am in Union Cave, exploring to find the path to Azalea Town.

### Reminders & Best Practices
- **Tool Failures:** I must be persistent in debugging my tools. I will not abandon a tool just because it fails; instead, I will perform a thorough, systematic, and incremental logical review. This is my highest priority.
- **Immediate Data Management:** I must update my World Knowledge Graph and Map Markers *immediately* upon discovering new information or transitions. Deferring these tasks is an invalid strategy.
- **Mark Dead Ends:** Mark all confirmed dead ends with '🚫' immediately after thorough exploration.
- **Agent Usage:** Use `battle_advisor` in all non-trivial battles to improve efficiency.

## II. Battle Intel

### Rival SILVA's Team
- CHIKORITA: Lv5 (Last seen in New Bark Town)

### Observed Movesets
- Wild Poliwag: BUBBLE
- Wild Hoothoot: TACKLE, GROWL, FLASH, FORESIGHT
- Wild Bellsprout: VINE WHIP, GROWTH
- Wild Caterpie: TACKLE, STRING SHOT
- Wild Ekans: LEER
- Wild Pidgey: SAND-ATTACK
- Wild Hoppip: TAIL WHIP, SYNTHESIS
- Wild Rattata: TACKLE, TAIL WHIP
- Wild Wooper: TAIL WHIP, WATER GUN
- Wild Zubat: LEECH LIFE
- Wild Sandshrew: SCRATCH, DEFENSE CURL
- Wild Geodude: TACKLE, DEFENSE CURL

### Type Effectiveness Chart (Verified)
- Normal is not very effective against Water.
- Normal is not very effective against Rock/Ground.
- Water is super effective against Rock/Ground.
- Water is super effective against Ground.

## III. World Knowledge & Mechanics

### Tile Traversal Rules (Verified)
- **Objects are impassable:** Most map objects act as walls.
- **Defeated Trainers:** Passability is inconsistent. Each must be tested.
- **WALL:** Impassable.
- **FLOOR:** Traversable.
- **TALL_GRASS / LONG_GRASS:** Traversable, triggers wild encounters.
- **LEDGE:** One-way downward traversal.
- **COUNTER:** Impassable.
- **DOOR/CAVE:** Warp tile, triggered by movement.
- **MART_SHELF/BOOKSHELF/TV/RADIO/PC/TOWN_MAP/WINDOW/PAINTING/STATUE/PILLAR:** Impassable scenery.
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
- **FLOOR_UP_WALL:** Impassable from above (one-way upward traversal).
- **unseen**: Impassable.

### Misc Mechanics
- HMs must be used from the PACK menu, not the Pokémon's party menu.

## IV. Tool Development Log
- **path_finder:** The tool is now functional. It correctly identifies impassable tiles, including one-way ledges and unseen areas.
- **route_finder:** The tool initially had a bug where it only considered the first exit from a map. This has been fixed by iterating through all possible start nodes. A second bug was discovered where it did not account for intra-map travel; this has also been fixed.
- **battle_advisor:** The agent now correctly considers a Pokémon's moveset when making recommendations.

## V. Unresolved Mysteries
- My Onix, Rocky, has 0 PP for Tackle. I need to check his status screen immediately after this battle to investigate.