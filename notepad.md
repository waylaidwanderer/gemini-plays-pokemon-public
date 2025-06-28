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
- FLOOR: A standard traversable tile. **Correction:** This tile is NOT always traversable. I am currently blocked from moving from `FLOOR` to `FLOOR`.
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
- **Problem:** I am completely stuck at (3, 1). All movement attempts (Up, Down, Left, Right) have been blocked for multiple turns, even onto adjacent `FLOOR` tiles. This is accompanied by a major visual/state desync (screen shows Route 46, game state is Player's Neighbor's House).
- **Hypothesis:** The game is in a soft-locked state. Standard movement is impossible.
- **Failed Attempts:**
    1. Moving Up, Down, Left, or Right.
    2. Following the 'maze-solving' hint (walking into wall, turning right were both blocked).
    3. Using 'Start' and 'Select' buttons (no effect).
- **New Strategy:** Since movement is impossible, I must try other inputs. My next action will be to press 'A' to attempt to interact with the `TOWN_MAP` object directly in front of me. If that fails, I will systematically try interacting with every adjacent tile.