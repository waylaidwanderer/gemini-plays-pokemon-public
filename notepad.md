# Gem's Pokémon Crystal Notepad

## Current Plan
- My `strategic_advisor` recommended I capture a Geodude from Dark Cave to prepare for the Violet City Gym. My immediate goal is to travel to Dark Cave on Route 31.

## Party & Rival
### My Team
- G (TOTODILE): Lv12
- HOOTHOOT (HOOTHOOT): Lv3

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

### Tile Testing Plan
- Systematically test each tile type on the current map to confirm traversability. Document findings.
- **CRITICAL:** Pay close attention to visually distinct tiles even if they share the same type name (e.g., decorative flowers on `FLOOR` tiles on Route 30 are impassable).

## Development & Strategy Notes
### Pathfinding Tool Issues
- **My Misunderstanding:** My manual assessment of Route 30 was incorrect. The only way to proceed north is via a long southern detour around the central part of the map. My `pathfinder_pro` tool was correctly identifying this path all along. My repeated failures were due to distrusting the tool and attempting to find a non-existent shortcut. The tool is functioning correctly, and its output must be trusted.

### Custom Agents & Tools (Ideas)
- **`unstick_me_tool` (Idea):** A tool that analyzes the map XML to find the nearest cluster of "unseen" tiles when I'm stuck, returning coordinates for a new navigation goal. This would be better than a reasoning-based agent.
- **`dialogue_summarizer` (Idea):** An agent to extract key information from NPC conversations.

## Untested Assumptions
- **Running vs. Fighting:** I am currently testing if battling some wild encounters is a better long-term strategy for leveling than always running. Initial results show small EXP gains. I need more data to form a conclusion.

## Critical Reminders
- **IMMEDIATE DOCUMENTATION:** All new information (NPC names, item locations, etc.) MUST be documented in the notepad and via map markers *immediately*, even during battles or cutscenes. No exceptions.
- **Proactive Agent Use:** I must use my `strategic_advisor` agent proactively to avoid getting stuck, not just as a last resort.
- **CLEAN UP MARKERS:** I must delete old or redundant markers to avoid clutter. Redundant markers are those that simply state information available from the tile type (e.g., 'Blocked by wall').

### Type Effectiveness Chart
- Normal vs. Water: NOT VERY EFFECTIVE (Observed: G's Scratch vs. wild Poliwag)