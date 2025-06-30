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
- Wild Hoppip: TAIL WHIP

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

### Untested Assumptions & Planned Experiments
- **Union Cave Entrance (Route 32):** The warp at (6, 79) is confirmed to be an EXIT ONLY due to a one-way ledge at (6, 80). The main entrance must be elsewhere.
- **WATER:** Inferred impassable without SURF. (Test: attempt to walk into it)
- **CUT_TREE:** Inferred impassable without CUT. (Test: attempt to walk into it)
- **HEADBUTT_TREE:** Inferred impassable without HEADBUTT. (Test: attempt to walk into it and interact)

## IV. Tool & Agent Development

### Process Reminders
- **Mark ALL NPCs:** To prevent pathfinding errors, I must place a map marker for every single NPC I encounter, not just defeated trainers or special characters. This is crucial for remembering off-screen obstacles.

### Tool & Agent Ideas
- **Navigation Analyst Tool:** A tool that parses map XML when `path_finder` fails. It would analyze the start and end points to identify potential blockers like one-way ledges, impassable tile types, or permanent obstacles from map markers, and then suggest reasons for the path failure.
- **Training Spot Suggester (Agent):** An agent that takes my party's levels and types and suggests the best route/area to grind based on known wild Pokémon encounters and trainer data.