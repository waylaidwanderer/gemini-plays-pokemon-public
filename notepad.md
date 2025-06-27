# Gem's Pokémon Crystal Notepad

## Game Mechanics & Systems
### PC Storage
- Pokémon:
- Items:
### Gifts and Trades
- Received POKéGEAR from Mom in New Bark Town.

## Battle and Pokemon Information
### My Party
- G (TOTODILE): Lv8 (Scratch, Leer, Rage)

## Area and Navigation Insights
### Tile Traversal and Movement Rules
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

## NPCs and Interactions
- Youngster on Route 29 (27, 17) gives advice about keeping weak Pokémon out of the grass.

## Obstacles and Solutions
- Route 29 has many ledges that create one-way paths, requiring careful navigation to explore fully.

## Tracking Progress and Corrections
### Current Plan
- **Objective:** Find the correct path to Cherrygrove City to reach Mr. Pokémon's house.
- **Strategy:**
    1. Systematically explore all unseen areas of Route 29.
    2. The path appears to be through the northern part of the route.
    3. I will use my `find_path` tool to navigate to unseen areas and eventually to the exit.

### Misunderstandings & Corrections
- Corrected my assumption that tree tiles are walkable. They are impassable obstacles. My `find_path` tool has been updated to reflect this.