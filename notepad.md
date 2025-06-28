# Gem's Pokémon Crystal Notepad

## Party & Rival
### My Team
- G (TOTODILE): Lv13
- HOOTHOOT (HOOTHOOT): Lv3
- HOOTIN (HOOTHOOT): Lv4

### Rival SILVA's Team
- CHIKORITA: Lv5 (Last seen in New Bark Town)

## Game Mechanics & Systems
### PC Storage
- Pokémon: None
- Items: None

### Gifts and Trades
- Received POKéGEAR from Mom in New Bark Town.
- Received a BERRY from a man on Route 30.
- Received 5 POKé BALLS from a scientist in Elm's Lab.

## Area and Navigation Insights
### Tile Traversal and Movement Rules
- **Objects are impassable:** All map objects (items, trees, signs, etc.) act as walls.
- **WALL:** An impassable barrier.
- **FLOOR:** A standard traversable tile.
- **TALL_GRASS:** A traversable tile that can trigger wild Pokémon encounters.
- **LEDGE:** Impassable from the bottom edge. Can be jumped down from the top edge.
- **FLOOR_HOP_RIGHT_LEDGE:** A one-way tile that allows jumping over a ledge to the right.
- **FLOOR_HOP_LEFT_LEDGE:** A one-way tile that allows jumping over a ledge to the left.
- **FLOOR_HOP_DOWN_LEDGE:** A one-way tile that allows jumping over a ledge downwards.
- **FLOOR_HOP_DOWN_OR_RIGHT_LEDGE:** A one-way tile that allows jumping over a ledge either down or to the right.
- **FLOOR_HOP_DOWN_OR_LEFT_LEDGE:** A one-way tile that allows jumping over a ledge either down or to the left.
- **COUNTER:** An impassable barrier.
- **DOOR:** A warp tile.
- **MART_SHELF:** An impassable barrier.
- **BUOY:** An impassable tile in water.
- **TOWN_MAP:** Impassable object.
- **WINDOW:** Impassable object.
- **BOOKSHELF:** An impassable object.
- **TV:** Impassable object.
- **RADIO:** Impassable object.
- **VOID:** An impassable tile outside the map boundaries.
- **WARP_CARPET_DOWN:** A warp tile that activates when facing down.
- **FRUIT_TREE:** An impassable object that can sometimes yield items.
- **WATER:** Confirmed impassable.
- **CUT_TREE:** Confirmed impassable.
- **CAVE:** A warp tile that leads to another map.
- **PC:** An impassable, interactive object. Must be interacted with from the tile below, while facing up.
- **WARP_CARPET_LEFT:** A warp tile that activates when facing left.

### Untested Tile Mechanics
- **FLOOR_UP_WALL:** Present in Dark Cave. Appears to be a one-way wall traversable only from below. Needs to be tested.

### Discovered Traps & Puzzles
- **Route 30 Noob Trap:** The western path accessible by jumping the ledge near (4, 24) is a dead end. It's blocked by Youngster Mikey, forcing a full backtrack to the southern entrance.

## Critical Reminders
- **IMMEDIATE DOCUMENTATION:** All new information MUST be documented in the notepad and via map markers *immediately*.
- **Proactive Agent Use:** I must use my `strategic_advisor` agent proactively to avoid getting stuck, but recognize its limitations in bugged states.
- **World Knowledge Graph:** I must add nodes and edges to my World Knowledge Graph immediately upon discovering new connections between maps.

## World Knowledge Graph Management
- **MANDATORY:** I must use `manage_world_knowledge` to add new nodes and edges *immediately* after every map transition. No exceptions.

## Process Reminders (From AI Observer)
- **Use Strategic Advisor:** I need to consult my `strategic_advisor` agent more frequently, especially when I hit a roadblock or need to re-evaluate my goals.
- **Immediate WKG Updates:** World Knowledge Graph updates must happen *immediately* after a map transition. No more delays. This is a critical process failure I must correct.
- **Careful Marker Management:** I need to be more precise with map markers, using `object_id` for moving NPCs and avoiding redundant markers.

## Observed Movesets
- G (TOTODILE) learned WATER GUN at Lv13.
- Wild Poliwag (Route 30): BUBBLE
- Wild Hoothoot (Route 30): TACKLE
- Wild Zubat (Route 30): Moveset unknown (fainted before attacking).

### Custom Agents & Tools (Ideas)

### Tile Traversal and Movement Rules (Additions)
- **COUNTER:** An impassable barrier, often found in buildings.

### Trades
- A Youngster in Kyle's House (Violet City) will trade a Bellsprout for an Onix.

## Critical Reminders & Process Improvements
- **IMMEDIATE DOCUMENTATION:** All new information MUST be documented in the notepad and via map markers *immediately*.
- **Proactive Agent Use:** I must use my `strategic_advisor` agent more frequently to avoid getting stuck.
- **World Knowledge Graph:** I must add nodes and edges to my World Knowledge Graph immediately upon discovering new connections between maps.
- **Untested Tile Mechanics:** I need to make a plan to return to Dark Cave to test the `FLOOR_UP_WALL` tile.
## Tool Development
- **path_master:** The tool is critically bugged. It does not understand one-way tiles like ledges and `FLOOR_HOP` tiles. This needs to be the top priority to fix.