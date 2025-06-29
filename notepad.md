# Gem's Pokémon Crystal Notepad

## Party & Rival
### My Team
- G (CROCONAW): Lv18
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
- Traded a Bellsprout for an Onix (ROCKY) in Violet City.
- Received HM05 (Flash) from the Elder in Sprout Tower.

### Observed Movesets
- G (CROCONAW): WATER GUN, SCRATCH, LEER, RAGE
- Wild Poliwag: BUBBLE
- Wild Hoothoot: TACKLE
- Wild Bellsprout: VINE WHIP
- Wild Gastly: Encountered in Sprout Tower. No attacks seen.

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
- **WATER/CUT_TREE/BUOY:** Impassable.
- **PILLAR:** Impassable.
- **VOID:** Out-of-bounds, impassable.
- **WARP_CARPET_*: Warp tile, direction-specific.
- **FRUIT_TREE:** Impassable object, may yield items.
- **LADDER:** A warp tile. Automatically triggers a warp when stepped on. Confirmed to be a two-way warp, allowing travel both up and down between floors.

### Sprout Tower Layout
- The central pillar divides all floors, making east-west travel impossible on any single floor. To navigate the tower, one must ascend on one side, find the correct ladder down on the other side, and repeat as necessary. The key is using the different ladders to switch between the east and west sections of the tower.

## Future Plans & Untested Hypotheses
- **Hypothesis:** Can Onix learn Flash (HM05)?
- **Testing Plan:** Explicitly walk into every new tile type from all four directions to confirm traversability and document it.
- Wild Rattata: Encountered in Sprout Tower.