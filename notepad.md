# Gem's Pokémon Crystal Notepad

## I. Party & Rival

### My Team
- G (CROCONAW): Lv19. **NOTE: Out of PP for WATER GUN & SCRATCH.**
- HOOTHOOT (HOOTHOOT): Lv4
- HOOTIN (HOOTHOOT): Lv4
- ROCKY (ONIX): Lv6 (Traded for Bellsprout in Violet City)

### Rival SILVA's Team
- CHIKORITA: Lv5 (Last seen in New Bark Town)

## II. Game Mechanics & Systems

### PC Storage
- **Pokémon:** None
- **Items:** None

### Gifts & Trades
- Received POKéGEAR from Mom.
- Received a BERRY from a man on Route 30.
- Received 5 POKé BALLS from a scientist in Elm's Lab.
- Traded a Bellsprout for an Onix (ROCKY) in Violet City.
- Received HM05 (Flash) from the Elder in Sprout Tower.

### Observed Movesets
- G (CROCONAW): SCRATCH (0 PP), WATER GUN (0 PP), LEER, RAGE
- ROCKY (ONIX): TACKLE, SCREECH. **NOTE: Does not have any Rock-type moves.**
- Wild Poliwag: BUBBLE
- Wild Hoothoot: TACKLE
- Wild Bellsprout: VINE WHIP
- Wild Gastly: LICK, HYPNOSIS (Encountered in Sprout Tower)
- Wild Rattata: TACKLE (Encountered in Sprout Tower)

## III. Area & Navigation Insights

### Tile Traversal Rules (Verified)
- **Objects are impassable:** All map objects (items, trees, signs, defeated trainers etc.) act as as walls.
- **WALL:** Impassable.
- **FLOOR:** Traversable.
- **TALL_GRASS:** Traversable, triggers wild encounters.
- **LEDGE:** One-way downward traversal.
- **FLOOR_HOP_*_LEDGE:** One-way traversal in the specified direction.
- **COUNTER:** Impassable.
- **DOOR/CAVE:** Warp tile, triggered by movement.
- **MART_SHELF/BOOKSHELF/TV/RADIO/PC/TOWN_MAP/WINDOW/PAINTING:** Impassable scenery.
- **WATER/CUT_TREE/BUOY:** Impassable.
- **PILLAR:** An impassable scenery object.
- **VOID:** Impassable.
- **WARP_CARPET_*: Warp tile, direction-specific.
- **FRUIT_TREE:** Impassable object, may yield items.
- **LADDER:** A warp tile triggered by movement. Can be one-way (e.g., SproutTower2F (10, 14) is one-way down) or two-way.
- **STATUE:** An impassable scenery object.

## IV. Untested Hypotheses & To-Do
- **To-Do:** Test teaching Flash as soon as I exit Sprout Tower.

## Sprout Tower Escape Plan (V11 - The Pillar)
*All previous plans failed due to a buggy pathfinding tool and incorrect assumptions about the map layout. The tool is now fixed and has confirmed all known paths are blocked.*
Hypothesis: The central pillar is the key. The Sages' dialogue about it shaking is a major hint.
1. From my current position at (8, 14), navigate to the tile adjacent to the central pillar at (8, 7).
2. Face the pillar and interact with it.