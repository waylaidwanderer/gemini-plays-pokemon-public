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
- FLOOR: A standard traversable tile. **Correction:** This tile is NOT always traversable. Specifically, floor tiles with flowers are impassable walls.
- TALL_GRASS: A traversable tile that can trigger wild Pokémon encounters.
- LEDGE: Impassable from the bottom edge. Can be jumped down from the top edge.
- FLOOR_HOP_RIGHT_LEDGE: A one-way tile that allows jumping over a ledge to the right.
- FLOOR_HOP_LEFT_LEDGE: A one-way tile that allows jumping over a ledge to the left.
- FLOOR_HOP_DOWN_LEDGE: A one-way tile that allows jumping over a ledge downwards.
- FLOOR_HOP_DOWN_OR_RIGHT_LEDGE: A one-way tile that allows jumping over a ledge either down or to the right.
- FLOOR_HOP_DOWN_OR_LEFT_LEDGE: A one-way tile that allows jumping over a ledge either down or to the left.
- HEADBUTT_TREE: An impassable wall.
- CUT_TREE: An impassable wall. (Requires HM Cut - Assumption)
- COUNTER: An impassable barrier.
- DOOR: A warp tile.
- WATER: An impassable tile without HM Surf.
- MART_SHELF: An impassable barrier.
- BUOY: An impassable tile in water.
- TOWN_MAP: Impassable object.
- WINDOW: Impassable object.
- BOOKSHELF: Impassable object.
- TV: Impassable object.
- RADIO: Impassable object.
- WARP_CARPET_DOWN: A warp tile.

## Critical Issues & Current Plan
### Immobilized at (3, 1) in Player's Neighbor's House
- **Problem:** I am completely stuck at (3, 1). All movement attempts (Up, Down, Left, Right) and turning attempts have been blocked for multiple turns. This is accompanied by a major visual/state desync (screen shows Route 46, game state is Player's Neighbor's House).
- **Hypothesis:** The game is in a soft-locked state. Standard movement and interaction are impossible.
- **Failed Attempts:**
    1. Moving (Up, Down, Left, Right).
    2. Turning (by attempting to move).
    3. Maze-solving hint (failed as turning is impossible).
    4. Menu buttons ('Start', 'Select').
    5. Interaction button ('A' while facing TOWN_MAP).
- **New Strategy:** I have now systematically tested every standard input except for the 'B' button. My next action is to press 'B' to see if it can cancel or otherwise alter this glitched state.
- VOID: An impassable tile outside the map boundaries.
- WARP_CARPET_DOWN: A warp tile.
### Tool Limitations
- **pathfinder_pro is unreliable:** The tool cannot distinguish between visually different tiles of the same type (e.g., normal FLOOR vs. impassable flowered FLOOR). Do not use it on maps with such features; rely on manual pathing instead.