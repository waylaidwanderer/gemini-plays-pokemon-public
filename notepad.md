# Gem's Pokémon Crystal Notepad

## Current Plan
- I am currently on Route 30, backtracking to Cherrygrove City after taking a wrong turn. My goal is to get back to the main path to continue towards Violet City.

## Party & Rival
### My Team
- G (TOTODILE): Lv12
- HOOTHOOT (HOOTHOOT): Lv3

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
- **HEADBUTT_TREE:** An impassable wall. (Requires Headbutt - Assumption)
- **CUT_TREE:** An impassable wall. (Requires HM Cut - Assumption)
- **COUNTER:** An impassable barrier.
- **DOOR:** A warp tile.
- **WATER:** An impassable tile without HM Surf. (Assumption)
- **MART_SHELF:** An impassable barrier.
- **BUOY:** An impassable tile in water.
- **TOWN_MAP:** Impassable object.
- **WINDOW:** Impassable object.
- **BOOKSHELF:** Impassable object.
- **TV:** Impassable object.
- **RADIO:** Impassable object.
- **VOID:** An impassable tile outside the map boundaries.
- **WARP_CARPET_DOWN:** A warp tile.

## Development & Strategy Notes
### Pathfinding Tool Issues
- My `pathfinder_pro` tool is excellent for static environments, but it cannot account for moving NPCs that are off-screen. When a calculated path is repeatedly blocked by a moving NPC, I must switch to manual navigation.

### Custom Agents & Tools (Ideas)
- **`unstick_me_tool` (Idea):** A tool that analyzes the map XML to find the nearest cluster of "unseen" tiles when I'm stuck, returning coordinates for a new navigation goal.
- **`dialogue_summarizer` (Idea):** An agent to extract key information from NPC conversations.

## Critical Reminders
- **IMMEDIATE DOCUMENTATION:** All new information MUST be documented in the notepad and via map markers *immediately*.
- **Proactive Agent Use:** I must use my `strategic_advisor` agent proactively to avoid getting stuck.
- **World Knowledge Graph:** I must add nodes and edges to my World Knowledge Graph immediately upon discovering new connections between maps.
### Discovered Traps & Puzzles
- **Route 30 Noob Trap:** The western path accessible by jumping the ledge near (4, 24) is a dead end. It's blocked by Youngster Mikey, forcing a full backtrack to the southern entrance.