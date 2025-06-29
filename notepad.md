# Gem's Pokémon Crystal Notepad

## Party & Rival
### My Team
- G (TOTODILE): Lv17
- HOOTHOOT (HOOTHOOT): Lv4
- HOOTIN (HOOTHOOT): Lv4
- ROCKY (ONIX): Lv6 (Traded for Bellsprout in Violet City)

### Rival SILVA's Team
- CHIKORITA: Lv5 (Last seen in New Bark Town)

## Game Mechanics & Systems
### PC Storage
- Pokémon: None
- Items: None

### Gifts and Trades
- Received POKéGEAR from Mom.
- Received a BERRY from a man on Route 30.
- Received 5 POKé BALLS from a scientist in Elm's Lab.
- Traded a Bellsprout for an Onix in Violet City.
- Received HM05 (Flash) from the Elder in Sprout Tower.

### Observed Movesets
- G (TOTODILE): WATER GUN (Learned at Lv13), SCRATCH, LEER, RAGE
- Wild Poliwag: BUBBLE
- Wild Hoothoot: TACKLE
- Wild Bellsprout: VINE WHIP
- Wild Gastly: No attacks seen (fainted too fast).

## Area and Navigation Insights
### Tile Traversal Rules (Verified)
- **Objects are impassable:** All map objects (items, trees, signs, defeated trainers etc.) act as walls.
- **WALL:** Impassable.
- **FLOOR:** Traversable.
- **TALL_GRASS:** Traversable, triggers wild encounters.
- **LEDGE:** One-way downward traversal.
- **FLOOR_HOP_*_LEDGE:** One-way traversal in the specified direction.
- **COUNTER:** Impassable.
- **DOOR/CAVE:** Warp tile.
- **MART_SHELF/BOOKSHELF/TV/RADIO/PC/TOWN_MAP/WINDOW/PAINTING:** Impassable scenery.
- **WATER/CUT_TREE/BUOY/PILLAR:** Impassable.
- **VOID:** Out-of-bounds, impassable.
- **WARP_CARPET_*: Warp tile, direction-specific.
- **FRUIT_TREE:** Impassable object, may yield items.
- **LADDER:** A warp tile. Automatically triggers a warp when stepped on. Can be one-way.

### Sprout Tower Layout
- The central pillar on the first and second floors divides the area. The only way to cross is on the third floor. There are two ladders connecting 2F and 3F: one at (10, 14) and another at (6, 4). The ladder at (6, 4) on 3F appears to be a one-way path down.

## Future Plans & Untested Hypotheses
- **Hypothesis:** Can Onix learn Flash (HM05)?
- **Testing Plan:** Explicitly walk into every new tile type from all four directions to confirm traversability.

## Tool/Agent Development
- **Agent Idea (`pokemon_evaluator`):** An agent to suggest the best lead Pokémon and moves for a given battle based on type matchups and known movesets.