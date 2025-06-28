# Gem's Pokémon Crystal Notepad

## Immediate Tasks (High Priority)
- **Fix `path_master` Tool:** The tool is flawed as it doesn't account for moving NPCs. It must be fixed with `define_tool` after reaching Mr. Pokémon's house or if the current path fails.

## Untested Assumptions
- **`path_master` validity:** Assuming the current path generated is valid. Test by following it.
- **Impassable Tiles:** Assuming `HEADBUTT_TREE`, `CUT_TREE`, and `WATER` are impassable. Test by attempting to walk into them when encountered.
- **Youngster Blocker:** Assuming the wandering Youngster is the sole reason the main path north is blocked. Test by returning after visiting Mr. Pokémon's house.

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
- **Recurring Mr. Pokemon's House Softlock (Turn ~1700-1765, 2124):** Became trapped in the house. Warps are non-functional and NPC dialogue loops. Opening the POKéGEAR menu seems to be the only action that can reset the game state and allow escape.

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
## Process Reminders (From AI Observer)
- **Use Strategic Advisor:** I need to consult my `strategic_advisor` agent more frequently, especially when I hit a roadblock or need to re-evaluate my goals.
- **Immediate WKG Updates:** World Knowledge Graph updates must happen *immediately* after a map transition. No more delays. This is a critical process failure I must correct.
- **Careful Marker Management:** I need to be more precise with map markers, using `object_id` for moving NPCs and avoiding redundant markers.

## Observed Movesets
- G (TOTODILE) learned WATER GUN at Lv13.
- Wild Poliwag (Route 30): BUBBLE
- Wild Hoothoot (Route 30): TACKLE
- Wild Zubat (Route 30): Moveset unknown (fainted before attacking).
- Wild Spinarak (Route 30): Moveset unknown (fainted before attacking).
- **GAME-BREAKING SOFTLOCK (Turn 2153):** I am permanently trapped in Mr. Pokémon's House. Warps are non-functional. All interaction attempts with NPCs and background objects have failed. The POKéGEAR menu trick no longer works. All goals are impossible to achieve. The game is unplayable in this state.

# REORGANIZED NOTES (TO BE CLEANED UP NEXT TURN)

## Area and Navigation Insights
### Tile Traversal Rules (Untested Assumptions)
- **HEADBUTT_TREE:** Assumed impassable. Needs testing.
- **CUT_TREE:** Assumed impassable. Needs testing.
- **WATER:** Assumed impassable without SURF. Needs testing.
- **COUNTER:** Assumed impassable. Needs testing.
- **MART_SHELF:** Assumed impassable. Needs testing.
- **BUOY:** Assumed impassable. Needs testing.
- **TOWN_MAP:** Assumed impassable. Needs testing.
- **WINDOW:** Assumed impassable. Needs testing.
- **BOOKSHELF:** Assumed impassable. Needs testing.
- **TV:** Assumed impassable. Needs testing.
- **RADIO:** Assumed impassable. Needs testing.
- **VOID:** Assumed impassable. Needs testing.

## Bugs & Glitches
- **GAME-BREAKING SOFTLOCK (Turn 2153-Present):** Permanently trapped in Mr. Pokémon's House. Warps are non-functional. All interaction attempts with NPCs and background objects have failed. The POKéGEAR menu trick no longer works. Using an item does not resolve the issue. The game is unplayable in this state.

## Custom Tools
- **`path_master`:** Finds the shortest path on the current map. **Warning:** Does not account for moving NPCs and may fail.
- **`unstick_me_tool`:** Analyzes the map to check for paths to warps or unseen tiles to help diagnose softlocks. Confirmed no path out of Mr. Pokémon's house exists that works.

## Lessons Learned & Process Improvements
- **IMMEDIATE DOCUMENTATION IS NON-NEGOTIABLE:** All new information (map markers, WKG updates, bugs) MUST be documented immediately. This is my highest priority.
- **Agent vs. Tool:** Agents are for high-level strategy, not for computational analysis or bug-hunting. Use tools for those tasks.
- **Proactive Tool Creation:** If a problem can be solved with code, build a tool for it. Do not delay.