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
- WARP_CARPET_DOWN: A warp tile that typically leads out of a building or to a lower floor.

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

### Tool Reliability & Navigational Errors
- My pathfinder tools (`find_path`, `pathfinder_pro`) were buggy and unreliable. They failed on long paths, led me into walls, and did not account for NPCs. I have deleted them and need to build a new, robust tool.
- My manual pathing has also been unreliable. I've made several mistakes, such as trying to walk into a wall at (5, 10) in New Bark Town. Must be more careful and double-check paths.

## My Commitments
- **Immediate Data Management:** I will mark all warps, items, and NPCs the moment I interact with them. I will update the World Knowledge Graph immediately upon changing maps.
- **Agent Brainstorming:** I should consider creating agents for strategic planning (e.g., team composition) and information recall (e.g., NPC dialogue summaries).
### Player's Neighbor's House Warp Failure
- I have failed to exit the house 6 times. My hypotheses about how the warp at (2, 7)/(3, 7) works have all been incorrect:
 1. Stepping on the tile.
 2. Pressing 'A' on the tile.
 3. Stepping down onto the right side.
 4. Stepping down onto the left side.
 5. Stepping left onto the tile.
 6. Stepping right onto the tile.
- New Strategy: The system notes insist I am not trapped. I will now systematically test every wall tile for a hidden exit, starting with the west wall.