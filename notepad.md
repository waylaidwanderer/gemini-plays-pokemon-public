# Gem's Pokémon Crystal Notepad

## I. Game Plan & Goals

### Strategic Notes
- **Party Imbalance:** My party is too reliant on G (Croconaw). The Azalea Town Gym is Bug-type, so I must train my two Hoothoots, whose Flying-type attacks will be super-effective. Current plan is to train on Route 32.
- **Onix's Moveset:** My Onix (ROCKY) lacks a Rock-type move. For now, rely on G and use ROCKY for defensive switching or to use SCREECH.
- **Party Full:** My party is full with the addition of the Egg. I can't catch any new Pokémon until I deposit one in the PC.

## II. Battle Intel

### Rival SILVA's Team
- CHIKORITA: Lv5 (Last seen in New Bark Town)

### Observed Movesets
- Wild Poliwag: BUBBLE
- Wild Hoothoot: TACKLE, GROWL, FLASH
- Wild Bellsprout: VINE WHIP, GROWTH
- Wild Caterpie: TACKLE, STRING SHOT
- Wild Ekans: (unknown)
- Wild Hoppip: TAIL WHIP, SYNTHESIS

## III. World Knowledge & Mechanics

### Tile Traversal Rules (Verified)
- **Objects are impassable:** All map objects (items, trees, signs, NPCs, defeated trainers etc.) act as walls.
- **WALL:** Impassable.
- **FLOOR:** Traversable.
- **TALL_GRASS:** Traversable, triggers wild encounters.
- **LEDGE:** One-way downward traversal.
- **COUNTER:** Impassable.
- **DOOR/CAVE:** Warp tile, triggered by movement.
- **MART_SHELF/BOOKSHELF/TV/RADIO/PC/TOWN_MAP/WINDOW/PAINTING/STATUE/PILLAR:** Impassable scenery.
- **FLOOR_UP_WALL:** One-way traversal. Can only be entered from below (moving up). Impassable from above.
- **LADDER:** Traversable (acts as FLOOR on docks).
- **FLOOR_ALLOW_HOP_DOWN:** One-way traversal downward. (Mechanics need re-verification due to system update.)
- **FLOOR_ALLOW_HOP_RIGHT:** One-way traversal to the right. (Mechanics need re-verification due to system update.)
- **FLOOR_ALLOW_HOP_DOWN_OR_RIGHT:** One-way traversal down or right. (Mechanics need re-verification due to system update.)
- **SYSTEM UPDATE:** All `FLOOR_HOP_*_LEDGE` tiles have been renamed to `FLOOR_ALLOW_HOP_*`. Old assumptions about their behavior are invalid and must be re-learned.
- **WARP_CARPET_DOWN:** Warp tile, triggered by movement.
- **VOID:** Impassable.
- **BUOY:** Impassable scenery.
- **WATER:** Confirmed impassable without SURF.
- **CUT_TREE:** Confirmed impassable without CUT.

## IV. Tool & Agent Development

### Implemented Tools & Agents
- **path_finder (Tool):** A* pathfinding.

## Action Items from Critique (Turn 6601)

- **LONG_GRASS:** Inferred to function like TALL_GRASS. (Test: attempt to walk through it and see if it triggers encounters).
- **HEADBUTT_TREE:** Impassable by walking. (Hypothesis: may be interactable with the HEADBUTT move).
- Wild Rattata: TACKLE, TAIL WHIP

## V. Action Items
- **CRITICAL:** Mark the Union Cave side of the warp at (17, 3) immediately after this battle.