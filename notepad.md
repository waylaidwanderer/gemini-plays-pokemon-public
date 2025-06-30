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
- Wild Gastly: LICK, HYPNOSIS
- Wild Rattata: TACKLE
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
- **FLOOR_HOP_DOWN_LEDGE:** One-way traversal downward.
- **FLOOR_HOP_RIGHT_LEDGE:** One-way traversal to the right.
- **FLOOR_HOP_DOWN_OR_RIGHT_LEDGE:** One-way traversal down or right.
- **WARP_CARPET_DOWN:** Warp tile, triggered by movement.
- **VOID:** Impassable.
- **BUOY:** Impassable scenery.
- **WATER:** Confirmed impassable without SURF.
- **CUT_TREE:** Confirmed impassable without CUT.

### Untested Assumptions & Planned Experiments
- **Union Cave Entrance (Route 32):** The warp at (6, 79) is confirmed to be an EXIT ONLY due to a one-way ledge at (6, 80). The main entrance must be elsewhere.
- **HEADBUTT_TREE:** Inferred impassable without HEADBUTT. (Test: attempt to walk into the one at (11, 20) and interact).

## IV. Tool & Agent Development

### Implemented Tools & Agents
- **path_finder (Tool):** A* pathfinding.
- **navigation_analyst (Tool):** Analyzes failed pathfinding attempts.
- **training_spot_suggester (Agent):** Suggests best training locations.

## Action Items from Critique (Turn 6601)
- **Marker Fix:** Mark the exit warp at (3, 7) in the Route 32 Pokémon Center (ID: 10_13) as '🚪 To Route 32 (11, 74)' as soon as I return there.
- **LONG_GRASS:** Inferred to function like TALL_GRASS. (Test: attempt to walk through it and see if it triggers encounters).