# Gem's Pokémon Crystal Notepad

## Game Mechanics & Systems
### HM/TM Usage
### Evolution Methods
### Money & Economy
### Item Effects
### Day/Night Cycle
### Special Interactions
### PC Storage
- Pokémon:
- Items:

## Battle and Pokemon Information
### Type Effectiveness Chart
### Observed Movesets
### Pokémon Locations
### My Party
- G (TOTODILE): Lv7 (Scratch, Leer, Rage)

## Area and Navigation Insights
### Tile Traversal and Movement Rules
- FLOOR_HOP_RIGHT_LEDGE: A one-way tile that allows jumping over a ledge to the right.
- FLOOR_HOP_DOWN_LEDGE: A one-way tile that allows jumping over a ledge downwards.
- FLOOR_HOP_DOWN_OR_RIGHT_LEDGE: A one-way tile that allows jumping over a ledge either down or to the right.
- HEADBUTT_TREE: An impassable wall. Confirmed by attempting to walk into it.
- CUT_TREE: Assumed to be an impassable wall until I can test it with the HM Cut.

### Puzzle Solutions
### Resource Locations

## NPCs and Interactions
### Key Dialogue
### Interaction Rules
### Gifts and Trades
- Received POKéGEAR from Mom in New Bark Town.

## Obstacles and Solutions
### Character Blockades
### Key Item Requirements
### Event-Based Roadblocks

## Tracking Progress and Corrections
### Current Plan
- **Objective:** Reach Cherrygrove City.
- **Strategy:**
    1. My `find_path` tool has been repeatedly failing due to incorrect assumptions about tile mechanics.
    2. I have now confirmed that `HEADBUTT_TREE` tiles are impassable.
    3. I will update my `find_path` tool to treat all tree tiles as walls.
    4. After correcting the tool, I will use it to find a valid path to Cherrygrove City. If no path is found, I will use it to explore all remaining unseen tiles on the map.

### Misunderstandings & Corrections
- Corrected my assumption that tree tiles are walkable. They are impassable obstacles.

### Failed Hypotheses