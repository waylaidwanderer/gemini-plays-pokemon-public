# Gem's Pokémon Crystal Notepad

## Current Plan
- Finish exploring Cherrygrove City.
- Travel to Violet City to challenge the first Gym.

## Party & Rival
### My Team
- G (TOTODILE): Lv10

### Rival SILVA's Team
- CHIKORITA: Lv5 (Last seen in New Bark Town)

## Game Mechanics & Systems
### PC Storage
- Pokémon: 
- Items: 
### Gifts and Trades
- Received POKéGEAR from Mom in New Bark Town.
- Received a BERRY from a man on Route 30.
- Received 5 POKé BALLS from a scientist in Elm's Lab.

## Area and Navigation Insights
### Tile Traversal and Movement Rules
- **Objects are impassable:** All map objects (items, trees, signs, etc.) act as walls.
- WALL: An impassable barrier.
- FLOOR: A standard traversable tile. **Correction:** This tile is NOT always traversable (e.g., flowered floor tiles are impassable).
- TALL_GRASS: A traversable tile that can trigger wild Pokémon encounters.
- LEDGE: Impassable from the bottom edge. Can be jumped down from the top edge.
- FLOOR_HOP_RIGHT_LEDGE: A one-way tile that allows jumping over a ledge to the right.
- FLOOR_HOP_LEFT_LEDGE: A one-way tile that allows jumping over a ledge to the left.
- FLOOR_HOP_DOWN_LEDGE: A one-way tile that allows jumping over a ledge downwards.
- FLOOR_HOP_DOWN_OR_RIGHT_LEDGE: A one-way tile that allows jumping over a ledge either down or to the right.
- FLOOR_HOP_DOWN_OR_LEFT_LEDGE: A one-way tile that allows jumping over a ledge either down or to the left.
- HEADBUTT_TREE: An impassable wall. (Requires Headbutt - Assumption)
- CUT_TREE: An impassable wall. (Requires HM Cut - Assumption)
- COUNTER: An impassable barrier.
- DOOR: A warp tile.
- WATER: An impassable tile without HM Surf. (Assumption)
- MART_SHELF: An impassable barrier.
- BUOY: An impassable tile in water.
- TOWN_MAP: Impassable object.
- WINDOW: Impassable object.
- BOOKSHELF: Impassable object.
- TV: Impassable object.
- RADIO: Impassable object.
- VOID: An impassable tile outside the map boundaries.
- WARP_CARPET_DOWN: A warp tile.

## Game Development Tasks
### Pathfinding Tool Development
- **Goal:** Create a new, reliable pathfinding tool using `define_tool`.
- **Problem:** The current `pathfinder_pro` is unreliable because it cannot distinguish between visually different tiles of the same type (e.g., normal FLOOR vs. impassable flowered FLOOR).
- **Plan:**
  1. The new tool's Python script must parse the `map_xml_string` more carefully.
  2. It needs to identify not just the `type` but also check for other attributes or child elements within a `<Tile>` that might indicate impassability.
  3. I will need to experiment to see what distinguishes these impassable floor tiles in the XML data.

### Custom Agent Ideas
- **`strategic_advisor`:** An agent that takes my current party, location, and goals to suggest the next best course of action (e.g., where to train, what items to buy).
- **`dialogue_summarizer`:** An agent to extract key information, quests, or hints from NPC conversations to avoid missing critical details.