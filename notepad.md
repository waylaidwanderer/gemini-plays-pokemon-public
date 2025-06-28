# Gem's Pokémon Crystal Notepad

## Immediate Tasks (High Priority)
- **Fix `path_master` Tool:** The tool has failed twice (Turn 1939 on Route 30, Turn 1961 in Cherrygrove City). This is now my HIGHEST priority. I must fix it with `define_tool` immediately after healing.
- **Verify Tile Mechanics:** I must test the traversability of `HEADBUTT_TREE`, `CUT_TREE`, and `WATER` tiles instead of assuming they are impassable. This needs to be done after healing.

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
- **COUNTER:** An impassable barrier.
- **DOOR:** A warp tile.
- **MART_SHELF:** An impassable barrier.
- **BUOY:** An impassable tile in water.
- **TOWN_MAP:** Impassable object.
- **WINDOW:** Impassable object.
- **BOOKSHELF:** An impassable object.
- **TV:** Impassable object.
- **RADIO:** Impassable object.
- **VOID:** An impassable tile outside the map boundaries.
- **WARP_CARPET_DOWN:** A warp tile.

### Discovered Traps & Puzzles
- **Route 30 Noob Trap:** The western path accessible by jumping the ledge near (4, 24) is a dead end. It's blocked by Youngster Mikey, forcing a full backtrack to the southern entrance.

## Bugs & Glitches
- **Mr. Pokemon's House Softlock (Turn ~1700-1765):** Became trapped in the house. Warps were non-functional and NPC dialogue looped. Opening the POKéGEAR menu seemed to be the only action that could reset the game state and allow escape.

## Development & Strategy Notes
### Key Dialogue
- **Youngster on Route 30:** "Everyone's having fun battling! You should too!"

### Custom Agents & Tools (Ideas)
- **`unstick_me_tool` (Idea):** A tool that analyzes the map XML to find the nearest cluster of "unseen" tiles when I'm stuck, returning coordinates for a new navigation goal. Could also check for softlock conditions (e.g., no path to any warp/exit).
- **`dialogue_summarizer` (Idea):** An agent to extract key information from NPC conversations.

## Critical Reminders
- **IMMEDIATE DOCUMENTATION:** All new information MUST be documented in the notepad and via map markers *immediately*.
- **Proactive Agent Use:** I must use my `strategic_advisor` agent proactively to avoid getting stuck, but recognize its limitations in bugged states.
- **World Knowledge Graph:** I must add nodes and edges to my World Knowledge Graph immediately upon discovering new connections between maps.

## Lessons Learned & Process Improvements
- **IMMEDIATE DOCUMENTATION IS NON-NEGOTIABLE:** The AI observer has repeatedly flagged my failure to document new information (map markers, world knowledge graph updates, major bugs) *immediately*. This is a critical error that has directly led to confusion and wasted time. From now on, documentation is my absolute highest priority, taking precedence over any other in-game action.
- **Strategic Advisor Limitations:** My `strategic_advisor` agent is not equipped to handle game-breaking bugs or softlocks. Repeatedly refining it for this purpose was a waste of time. In the future, if a bug is confirmed, I will focus on systematic, in-game actions to attempt a state reset rather than relying on the agent.

## World Knowledge Graph Management
- **MANDATORY:** I must use `manage_world_knowledge` to add new nodes and edges *immediately* after every map transition. No exceptions.