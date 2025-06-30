# Gem's Pokémon Crystal Notepad

## I. Strategic Overview
- **Primary Objective:** My main goal is to get the Hive Badge from the Azalea Town Gym.

## II. Current Plan
1.  Navigate from my current position on Route 32 to the Union Cave entrance.
2.  The entrance is at (6, 79), so the target tile is (6, 78).
3.  Use the `path_finder` tool to calculate the route.
4.  Explore Union Cave to find the path to Azalea Town.

## III. Battle Intel
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

## IV. World Knowledge & Mechanics
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

## V. Tool Development & Reflection
- **path_finder:** The tool has had multiple bugs related to one-way ledges and impassable tiles. My debugging has been inefficient. I need to systematically verify game mechanics and ensure my code reflects my documented knowledge *before* running tests. The tool should now correctly handle all known tile types.
- **route_finder:** The tool initially had a bug where it only considered the first exit from a map. This has been fixed by iterating through all possible start nodes. A second bug was discovered where it did not account for intra-map travel; this has also been fixed.
- **battle_advisor:** The agent now correctly considers a Pokémon's moveset when making recommendations.
- **move_advisor:** I have not yet tested this agent. I must find an opportunity to use it.
- **World Knowledge Graph:** I must remember to check for existing nodes/edges before attempting to add new ones to avoid redundant operations.

## VI. Self-Critique & Improvement Plan
- **Debugging Inefficiency:** My trial-and-error approach to fixing the `path_finder` was slow and ineffective. I made multiple incorrect assumptions about tile mechanics (`COUNTER`, `FLOOR_UP_WALL`) without proper verification.
- **Action Plan:** Before modifying any tool, I MUST first verify the specific game mechanic through direct observation. I will then update my 'Tile Traversal Rules' section in the notepad. Only after the mechanic is fully documented will I implement the logic in my code. This will prevent repeated failures and align my tools with my verified knowledge.
- **Agent Testing:** I have neglected to test my `move_advisor` agent. I will look for the next opportunity (e.g., finding a new TM) to use it and evaluate its performance.
- **Knowledge Management:** I failed to check my World Knowledge Graph for an existing edge before trying to add a duplicate. I must remember to consult my existing knowledge bases before performing 'add' operations to avoid redundancy.