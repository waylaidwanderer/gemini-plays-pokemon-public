# Gem's Pokémon Crystal Notepad

## Current Plan
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
- FLOOR: A standard traversable tile. **Correction:** Tiles with this type can be impassable. Specifically, FLOOR tiles with flower graphics are impassable barriers.
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

## Development & Strategy Notes
### Pathfinding Tool
- **Status:** The `pathfinder_pro` tool is now robust and reliable after several refinements.
### Custom Agents
- **`strategic_advisor`:** An agent that takes my current party, location, and goals to suggest the next best course of action. I should use this more often.
- **`dialogue_summarizer`:** (Idea) An agent to extract key information from NPC conversations.
### Untested Assumptions
- **Running vs. Fighting:** I have been assuming running from wild battles is always optimal. This saves time but yields no EXP. I need to test if battling some wild encounters is a better long-term strategy for leveling.

## Critical Reminders
- **IMMEDIATE DOCUMENTATION:** All new information (NPC names, item locations, etc.) MUST be documented in the notepad and via map markers *immediately*, even during battles or cutscenes. No exceptions.
- **DOCUMENT BLOCKED PATHS:** Any time my movement is blocked by a wall or obstacle, I MUST immediately place a `🚫` map marker at that location to avoid repeating the mistake.
- **CLEAN UP MARKERS:** I must delete old or redundant markers (like '⚔️' after a trainer is defeated and marked with '☠️') to avoid clutter.
## Critical Reminders (Updated)
- **Check for Ledges:** Always check for ledges before planning a path. They are one-way and can trap me.