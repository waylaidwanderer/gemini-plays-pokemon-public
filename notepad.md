# Gem's Pokémon Crystal Notepad

## Game Mechanics & Systems
### PC Storage
- Pokémon:
- Items:
### Gifts and Trades
- Received POKéGEAR from Mom in New Bark Town.
- Received a BERRY from a man on Route 30. He said they can be found on trees.

## Area and Navigation Insights
### Tile Traversal and Movement Rules
- **Objects are impassable:** All map objects (items, trees, signs, etc.) act as walls.
- WALL: An impassable barrier.
- FLOOR: A standard traversable tile.
- TALL_GRASS: A traversable tile that can trigger wild Pokémon encounters.
- LEDGE: Impassable from the bottom edge. Can be jumped down from the top edge.
- FLOOR_HOP_RIGHT_LEDGE: A one-way tile that allows jumping over a ledge to the right.
- FLOOR_HOP_LEFT_LEDGE: A one-way tile that allows jumping over a ledge to the left.
- FLOOR_HOP_DOWN_LEDGE: A one-way tile that allows jumping over a ledge downwards.
- FLOOR_HOP_DOWN_OR_RIGHT_LEDGE: A one-way tile that allows jumping over a ledge either down or to the right.
- FLOOR_HOP_DOWN_OR_LEFT_LEDGE: A one-way tile that allows jumping over a ledge either down or to the left.
- HEADBUTT_TREE: An impassable wall. Confirmed by attempting to walk into it.
- CUT_TREE: An impassable wall. Requires the HM Cut to pass. (Assumption)
- COUNTER: An impassable barrier, similar to a WALL.
- DOOR: A warp tile that typically leads into or out of a building.
- WATER: An impassable tile without the HM Surf. (Confirmed)
- MART_SHELF: An impassable barrier, similar to a WALL.
- BUOY: An impassable tile found in water. (Assumption)
- TOWN_MAP: Impassable object.
- WINDOW: Impassable object.
- BOOKSHELF: Impassable object.
- TV: Impassable object.
- RADIO: Impassable object.

## NPCs and Interactions
- Youngster on Route 29 (27, 17) gives advice about keeping weak Pokémon out of the grass.

## Obstacles and Solutions
- Route 29 has many ledges that create one-way paths, requiring careful navigation to explore fully.

## Tracking Progress and Corrections
### Current Plan
- **Objective:** Return the MYSTERY EGG to Professor Elm.
- **Strategy:**
    1. Travel from Cherrygrove City back to New Bark Town via Route 29.
    2. Go to Elm's Lab.

### Misunderstandings & Corrections
- Corrected my assumption that tree tiles are walkable. They are impassable obstacles. My `find_path` tool has been updated to reflect this.

## My Commitments
- **Immediate Data Management:** I will mark all warps, items, and NPCs the moment I interact with them. I will update the World Knowledge Graph immediately upon changing maps.

## Tool Reliability
- My pathfinder tools (`find_path`, `pathfinder_pro`) are buggy and unreliable. They failed to find valid paths and led me into walls. Need to debug or create a more robust version.