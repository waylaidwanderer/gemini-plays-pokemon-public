# Strategic Principles & Lessons Learned
- **DEBUG TOOLS IMMEDIATELY:** If a trusted tool provides an output that contradicts obvious reality (e.g., 'No path found' to a clearly visible and reachable tile), the tool is broken. Debugging and fixing the tool becomes the absolute highest priority, superseding any other gameplay objective.
- **TRUST DATA OVER INTUITION:** My custom tools (especially pathfinders) analyze the raw game data, which is the absolute source of truth. My visual interpretation of the screen or my memory can be flawed. If a tool reports 'No path found' or provides contradictory information, I must treat its output as the discovery of a fact about the game state (e.g., a hidden wall, a flawed assumption), not as a bug in the tool itself. I must always verify my root assumptions against the game data before pursuing complex solutions.
- **Automation Consistency:** I must consistently use my automation tools (like `select_battle_option`) to improve efficiency and reduce errors, especially when prompted by system critiques. Inconsistent use is a failure of strategy. For built-in tools, I must use them as designed (e.g., passing 'RUN' as an argument to `select_battle_option`) rather than manually scripting button presses.
- **Tool & Knowledge Base Maintenance:** If a tool is flawed or an in-game observation contradicts a hypothesis, my absolute highest priority is to immediately correct the tool or my internal knowledge base (notepad). Deferring maintenance is a critical failure.
- **Tool Consistency:** When one tool's logic is updated (like `find_path`), any other tools that use similar logic must be updated immediately to prevent conflicting results and strategic errors.
- **Tool Debugging Priority:** When a core tool like a pathfinder fails, debugging it becomes the absolute highest priority, superseding all gameplay goals. A systematic approach is required: 1. Confirm the tool is the problem, not a misunderstanding of the map (e.g., by testing a path manually). 2. Add targeted logging to trace execution and understand the algorithm's decision process. 3. Analyze logs to form a specific hypothesis about the bug before attempting a fix. Do not blindly refactor or revert without evidence.
- **Data Hygiene:** Map markers for resolved events (like collected items) must be deleted immediately to avoid confusion and wasted turns. When updating a marker for an object (e.g., after defeating a trainer), the old marker must be deleted to prevent redundant and conflicting information. Markers should also be linked to their corresponding `object_id` whenever possible to ensure they move with the object.
- **NPC Interactions:** Some interactions, like battling a trainer, can be multi-step. Ensure all initial dialogue is cleared with 'A' presses before the main event (like the battle) will trigger.
- **Pathfinding Logic:** If a path is repeatedly blocked or a tool reports 'No path found,' do not assume you are soft-locked. Re-examine the map visually for alternative routes like ledges or other one-way tiles that may have been missed.
- **Tile Mechanic Verification:** I must verify the mechanics of every tile type through direct observation and experimentation. Assumptions based on a tile's name can be wrong and lead to critical tool failures. I must never assume I know how a tile works until I have tested it.
- **Dialogue & Movement:** I must ensure all dialogue boxes are closed by pressing 'A' before attempting any movement inputs. Trying to move with text on screen will fail.
- **Marker Hygiene for Moving Objects:** When an object with a linked marker moves off-screen, the marker becomes stale. I must immediately delete the marker. A new marker should only be created if/when the object reappears at a new location.
- **Agent-based fixes must be verified in both simple and complex scenarios before a tool is considered fully functional. A fix for one case may not cover all failure conditions.
- **Marker Hygiene:** When creating map markers, I must ensure they are linked to the correct object_id and have accurate labels. Failure to do so degrades the quality of my map data and leads to confusion. Unlinked markers for moving objects are useless.
- **Problem-Solving Escalation:** When stuck on a puzzle after exhausting simple, self-generated hypotheses, I must escalate to a more powerful problem-solving tool, such as my custom agents. Repeating failed attempts is inefficient.
- **Exploration Before Puzzles:** Prioritize exploring all reachable areas of a new map before attempting complex puzzles to ensure all context and potential clues have been gathered.
- **Tool Input Verification:** Before concluding a tool is broken (e.g., `find_path` returning 'No path found'), I must first verify that my inputs and assumptions are correct. Pathing to an 'unseen' tile is an invalid input, as the tool correctly treats them as impassable. My strategy must adapt to the tool's logic.
- **Tool Contradiction Analysis:** If two of my tools provide contradictory outputs, it's a strong indicator of a bug in one of them. I must immediately stop and debug the tools to resolve the discrepancy instead of trusting one over the other.
- **Verify Root Assumptions:** When a plan fails, especially when a trusted tool like a pathfinder reports an issue, the root hypothesis about the map/mechanic is likely flawed. Do not repeatedly try minor variations of the failed plan. Instead, re-examine the map to find the contradiction and form a new, fundamentally different hypothesis (e.g., trying to go east instead of west when blocked).
- **Random Chance Strategy:** If a strategy based on random chance (like waiting for moving NPCs) fails repeatedly (3+ times), I must switch to a deterministic strategy (like proactively stunning them in favorable positions).
- **Agent Escalation:** When multiple self-generated hypotheses for a puzzle have failed, especially after getting stuck in a repetitive loop (like the stun-gun strategy), I must escalate to a more powerful problem-solving tool like an agent. Even if the agent's initial suggestions are not the final solution, they serve the critical purpose of breaking cognitive fixation and forcing a re-evaluation of the problem's root assumptions.
- **Herding Puzzles:** Interacting with an object (like the Farfetch'd) from an adjacent tile can trigger movement along a complex, pre-determined path, not just simple repulsion. The direction of approach is the key trigger.
- **Visual Path Verification:** Before executing a move, I must visually confirm the path on the ASCII map and game screen to avoid simple navigational errors like walking into walls. This supplements tool-based pathfinding.
- **Debugging Cycle Avoidance:** When a core tool repeatedly fails despite multiple fixes, the core algorithm is likely fundamentally flawed. I must avoid getting stuck in a loop of incremental, failing changes. The correct approach is to either replace the logic with a known-working version from another tool or re-implement it from first principles, rather than continuing with minor tweaks.
- **VERIFY POSITION & SEPARATE INPUTS:** After any interruption (battle, menu, etc.) and before any action, I MUST verify my current `(x, y)` coordinates in the Game State Information. I must NEVER mix directional inputs (Up, Down, Left, Right) and action inputs ('A', 'B') in the same turn. Movement/turning must happen in one turn, and interaction in the next.
- **Puzzle State Changes:** Some puzzles, like the Goldenrod Dept. Store basement, may change their state based on triggers that are not immediately obvious, such as leaving and re-entering the area. If internal solutions fail, I must consider external actions as potential triggers.
- **Interaction Loops:** If repeated interaction with an NPC doesn't change the outcome, the solution lies elsewhere. Don't get stuck in an interaction loop; pivot to testing environmental or sequential triggers.
- **Trust Pathfinder Output:** If `find_path` reports 'No path found' to a seemingly reachable location, trust the tool. It is analyzing the raw map data and has likely identified an obstacle or layout issue (like one-way paths or impassable terrain) that is not immediately obvious. Re-examine the map visually to understand the blockage instead of assuming the tool is bugged.
- **Interaction vs. Line of Sight:** If direct interaction with a trainer-like NPC results in a dialogue loop, the battle trigger is likely entering their line of sight. If both methods fail, they may not be a battlable trainer.
- **Positional Awareness:** Always verify my own coordinates and the coordinates of relevant NPCs before using a targeted tool like `stun_npc`. Wasting a turn on an unnecessary action is a failure of observation.
- **Team Leveling Strategy:** A single high-level Pokémon cannot carry an entire under-leveled team through a major battle like a Gym. I must ensure my whole team is adequately leveled and balanced before challenging a Gym Leader.
- **Levels Over Type Advantage:** A significant level disparity can completely negate type advantages. My Lv8 ROCKY was one-shot by a move it should have resisted, proving that raw power from a higher level is a critical factor.
- **Low-HP Threat:** A low-HP Pokémon with a status move like Hypnosis is still a major threat. Prioritize eliminating it quickly, even if it means using a stronger Pokémon and not spreading EXP optimally, to avoid having the whole team disabled.
- **Type Immunity vs. Level Disparity:** Type immunity (e.g., Flying vs. Ground) is not a guaranteed defense against a much higher-level opponent. A significant level gap means the opponent can still knock out the immune Pokémon with its other, non-resisted moves.
- **Positional & Data Verification:** I must ALWAYS verify my current `(x, y)` coordinates AND map ID in the Game State Information after ANY interruption (battle, phone call, map transition, menu, etc.) before planning my next move. My memory of map layouts or my location can be flawed; the game state is the absolute source of truth. Assuming a transition has occurred or a path has completed without verification is a critical failure.
- **Pathfinding Failure as a Clue:** When a pathfinding tool repeatedly reports no path to a major area, it's a strong signal that a story-based trigger is required to proceed or the map layout is not what it seems. Instead of assuming the tool is bugged or trying minor path variations, I must re-evaluate my root assumptions about the map's traversability and pivot to finding the trigger event, often hinted at by recent NPC dialogue.
- **Proactive Object Marking:** I must mark any unidentified object as soon as it appears on screen. Waiting until it blocks my path is inefficient and reactive.
- **Trainer Line of Sight:** Assume a trainer can see you unless their facing direction and the path geometry make it impossible. When party health is critical, do not risk walking near trainers; find a guaranteed safe path or backtrack.
- **Data Hygiene:** When creating map markers, I must ensure they are linked to the correct object_id and have accurate labels, including the correct trainer type. Failure to do so degrades the quality of my map data and leads to confusion.
- **Interaction Loops:** If repeated, varied interaction with an NPC (e.g., from different directions, or testing line-of-sight) yields no new result, they are likely non-interactive for progression or have already served their purpose. I must abandon the interaction and explore other options to avoid wasting time in a loop.
- **Follow Documented Strategy:** My documented strategies and principles in the notepad are useless if I don't follow them. I must review relevant notes before making major decisions, especially for gym battles. A single high-level Pokémon cannot carry an under-leveled team, and attempting to do so after documenting this principle is a critical strategic failure.
- **Training Strategy:** The wild POKéMON on Route 35 (around Lv12-14) are currently too strong for my low-level party members. Attempting to grind here is inefficient and leads to frequent trips to the POKéMON Center. A better strategy is to train on an earlier route with weaker wild POKéMON, such as Route 32.
- **Pathfinding must account for all known obstacles, both on-screen (from map data) and off-screen (from map markers).**
- **Cautious Training:** Even with a type advantage, a low-level Pokémon is still vulnerable. Be prepared to switch out or use healing items if they take significant damage, rather than risking a faint for a small amount of EXP.
- **Accuracy-lowering moves** like SAND-ATTACK can turn a simple training battle into a high-risk situation. If an opponent repeatedly uses such moves, consider switching to a Pokémon with a move that doesn't check accuracy or running away to avoid wasting resources.
- **Separate Inputs:** I must be careful to separate directional inputs (Up, Down, Left, Right) from action inputs ('A', 'B') into separate turns, especially in menus, to avoid input errors.
- **IMMEDIATE DATA & TOOL MAINTENANCE:** My absolute highest priority is maintaining a perfect, up-to-the-second internal state. Any task I decide on, such as adding, deleting, or fixing an agent, tool, marker, or notepad entry, MUST be performed in the CURRENT turn. This task is more important than any in-game action and must never be deferred.
- **Notepad Edit Precision:** When using `notepad_edit` with the `replace` action, the `old_text` must be an exact match. If an edit fails, it's better to use a smaller, more unique line of text as the anchor for replacement rather than a large, complex block which is prone to mismatch errors.
- **Resilience & Stat-lowering moves:** Do not underestimate low-level opponents. A resilient Pokémon can withstand multiple hits from a higher-level attacker. Furthermore, repeated use of stat-lowering moves (like TAIL WHIP) can quickly turn an easy battle into a risky situation by neutralizing a level advantage.
- **Efficient Traversal:** When the primary goal is to traverse an area with frequent wild encounters (like a cave), using a Repel is more time and resource-efficient than fighting or running from every battle.

# Game Mechanics & Systems
- The Day/Night cycle is an important mechanic in this game, affecting events.
- Received 5 POKé BALLS from the scientist in Elm's Lab. I can now catch wild Pokémon.
- The PC in Pokémon Centers is used for Pokémon and item storage.
- BERRY trees grow new BERRIES every day.

# Current Quest: Defeat Whitney
- **Objective:** Defeat Whitney, the Goldenrod Gym Leader.
- **Status:** Training in Union Cave.
- **Sub-task:** Investigate unmarked warp at (33, 9) in Goldenrod City after dealing with Whitney.

# Key Items
- **HIVEBADGE:** From Bugsy. Allows traded POKéMON up to L30 to obey and enables the use of CUT outside of battle.
- **POKéDEX:** A high-tech encyclopedia from PROF. OAK to record POKéMON data.
- **HM05 FLASH:** Obtained from the Elder of Sprout Tower. Illuminates dark caves. Requires the Zephyr Badge to use outside of battle.
- **HM01 CUT:** Obtained from the charcoal maker in Ilex Forest. Allows cutting small trees outside of battle. Requires the Hive Badge.

# TMs
- **TM12 SWEET Scent**
- **TM31 MUD-SLAP**
- **TM39 SWIFT**
- **TM49 FURY CUTTER**

# Consumable Items
- Received a BITTER BERRY from the tree at (16, 7) on Route 31.

# Battle Mechanics
- Pokémon holding a BERRY can automatically use it to heal themselves when their HP gets low in battle.
- Poisoned Pokémon lose 1 HP every four steps outside of battle.
- Accuracy-lowering moves like SMOKESCREEN are not a guaranteed defense.
- The auto-activation threshold for a held BERRY is likely below 25% HP.
- Bug-type moves (like LEECH LIFE) are not very effective against Fire-types.
- Grass-type moves (like VINE WHIP) are not very effective against Fire-types.
- Normal-type moves have no effect on Ghost-type Pokémon.
- Normal-type moves (like TACKLE) are not very effective against Rock/Ground-types (like GEODUDE).

# Menu Navigation
- For complex menu inputs (like on-screen keyboards), perform all directional movements in one turn and the final confirmation ('A' button) in the next. Do not mix directional and action buttons in the same input sequence to avoid errors.
- In the party screen, the 'SWITCH' option is used to reorder Pokémon. The 'MOVE' option is for reordering a Pokémon's moves. Confusing these leads to menu loops.

# Available Tools & Agents
**Built-in Tools:**
- `notepad_edit`: Edits this notepad.
- `run_code`: Executes a single-use Python script.
- `define_agent` / `delete_agent`: Manages custom reasoning agents.
- `define_map_marker` / `delete_map_marker`: Manages map markers.
- `define_tool` / `delete_tool`: Manages custom tools.
- `stun_npc`: Freezes or unfreezes an NPC's movement.
- `select_battle_option`: Automatically selects a main battle menu option. Must be called with the `option_to_select` argument (e.g., `option_to_select: "FIGHT"`). Options are FIGHT, PKMN, PACK, RUN.

**Custom Agents & Tools (Defined by me):**
- `gym_puzzle_solver` (Agent): Analyzes gym puzzle descriptions and failed hypotheses to generate new, simple, and testable solutions.
- `python_code_debugger` (Agent): Analyzes a Python script, its intended behavior, and a bug description to provide a corrected version of the code and an explanation of the fix.
- `find_path` (Tool): Finds a path from a start to an end coordinate on the current map using the BFS algorithm.
- `find_reachable_unseen_tiles` (Tool): Finds all reachable unseen tiles on the current map.
- `stealth_pathfinder` (Tool): Finds a path while avoiding a given list of forbidden tiles.

# NPC Dialogue
- **POKEFAN_M in Violet City House:** Traded Pokémon grow quickly but may disobey without the correct Gym Badge.
- Received MIRACLE SEED from a trainer on Route 32.
- **FIREBREATHER WALT on Route 35:** Said "I'm practicing my fire breathing." despite appearing as a FISHER sprite. Likely a Fire-type trainer.
- A POKEFAN_M in the Game Corner lost his COIN CASE in the UNDERGROUND. This is likely required to play the games.
- Youngster JOEY called, wanting a rematch. He's on Route 30.
- Youngster JOEY called again, confirming he's on Route 30 for a rematch.
- Youngster JOEY called a third time for a rematch on Route 30.

# Crafting
- Kurt in Azalea Town can make special POKé BALLS from APRICORNS. I received a LURE BALL from him as an example.

# Puzzle Solutions

## Azalea Gym
- Gym Guide: The Gym Leader is BUGSY. His Bug POKéMON are weak to Fire and Flying-type moves.
- **Solution:** The gym puzzle involves finding two hidden floor switches. The first, located on the path to the right-side trainer, makes a new trainer appear on the left side. The second, on the path to the left-side trainer, makes another new trainer appear. The path to these trainers is not blocked by the Twins in the middle; it is possible to walk around the bottom of the gym. Defeating all trainers is not required to reach Bugsy.

## Goldenrod Department Store
- **Elevator:** The elevator is controlled by the panel at (3, 0). Interacting with the panel brings up a floor selection menu. After selecting a floor, you must walk onto the corresponding warp carpet to travel. The warp to B1F is at (1, 3) and the warp to 1F is at (2, 3).
- **B1F Box Puzzle:** Leaving the room and returning clears the central path, but does not grant access to the items in the side alcoves. The full solution is currently unknown, and the items may be inaccessible for now. The clue is the workers' dialogue about working 'behind the scenes'.

## Goldenrod Gym
- Gym Guide: This is a Normal-type gym. Fighting-type POKéMON are recommended.
- **Puzzle Mechanic:** The gym puzzle is solved by walking along the outer perimeter of the entrance room. The direction and sequence of these walks cause different trainers to appear and disappear, opening and closing paths. The correct sequence of perimeter walks and trainer battles is required to open the path to the main gym area.

# Obstacles and Solutions
- A strange tree blocks the road north of Goldenrod City (Route 35). It can be cleared using a SQUIRTBOTTLE, which is obtained from the Flower Shop after defeating Whitney. The Lass in the shop confirms this is the correct sequence of events.

# Held Items
- **QUICK CLAW:** Received from a Teacher in the National Park. When held by a Pokémon, it may allow them to attack first in battle.

# Tile & Object Mechanics
- **WALL**: Impassable terrain.
- **FLOOR**: A standard, fully traversable tile.
- **STAIRCASE**: A traversable warp tile that moves the player between floors.
- **TOWN_MAP**: An interactable object on a wall; impassable.
- **TV**: An impassable object.
- **BOOKSHELF**: An impassable object.
- **WINDOW**: An impassable object, functions like a wall.
- **RADIO**: An impassable object.
- **DOOR**: A traversable warp tile leading into or out of a building.
- **WATER**: Impassable terrain without a specific HM (likely Surf).
- **HEADBUTT_TREE**: An interactable tree, probably requires the Headbutt move. Impassable.
- **TALL_GRASS**: Fully traversable tile. Wild POKéMON can be encountered here.
- **LEDGE_HOP_RIGHT**: A one-way traversable tile. Can only be entered from the left, moving right.
- **LEDGE_HOP_DOWN**: A one-way traversable tile. Can only be entered from above, moving down.
- **LEDGE_HOP_LEFT**: A one-way traversable tile. Can only be entered from the right, moving left.
- **CUT_TREE**: An impassable tree that likely requires the HM move Cut to remove.
- **COUNTER**: Impassable terrain, usually a barrier in front of an NPC.
- **MART_SHELF**: Impassable terrain, functions like a wall.
- **LONG_GRASS**: Fully traversable tile. Wild POKéMON can be encountered here.
- **PC**: An interactable object used to access the Pokémon Storage System and personal item storage.
- **LADDER**: A traversable warp tile that moves the player between floors.
- **FLOOR_UP_WALL**: Confirmed impassable when trying to move onto it from an adjacent tile above. Its behavior when approached from other directions is untested. It may be a one-way ledge. My pathfinding tools currently treat it as a WALL to be safe.
- **WARP_CARPET_RIGHT**: A traversable warp tile at the edge of a map that transitions to the adjacent map on the right. To activate, you must attempt to move right from the carpet tile, effectively trying to walk 'off' the map.
- **WARP_CARPET_UP**: A traversable warp tile at the edge of a map that transitions to the adjacent map above. Must move up to activate. Confirmed that moving from this tile to a FLOOR tile below it is possible, so it is not a one-way ledge.
- **unseen**: A tile that has not yet been explored. Its properties are unknown until visited.
- **BUOY**: An object found in water. Appears to be impassable, functioning like a WALL tile within a WATER area.
- **WARP_CARPET_DOWN**: A traversable warp tile at the edge of a map that transitions to the adjacent map below. Must move down to activate.
- **VOID**: Impassable terrain that appears to be an empty space off the edge of the map.
- **WARP_CARPET_LEFT**: A traversable warp tile at the edge of a map that transitions to the adjacent map on the left. To activate, you must attempt to move left from the carpet tile, effectively trying to walk 'off' the map.
- **TEACHER / LASS / BIRD / OFFICER / YOUNGSTER**: These NPC objects are impassable and function as walls.
- **FRUIT_TREE**: An impassable, interactable object. Gives one BERRY item (like PRZCUREBERRY) when interacted with for the first time. Subsequent interactions yield nothing.
- **Check Movesets:** Before switching a low-level or unfamiliar Pokémon into battle for training, I must first check its moveset to ensure it has at least one attacking move. Switching in a Pokémon that can't fight (like Jubilee) is a wasted turn and puts them at risk.

# General Object Interaction
- To interact with objects like ladders, signs, or switches, you must be standing on an adjacent tile and facing the object. Attempting to interact while standing *on* the object itself will fail.
- **VOID**: Impassable terrain that appears to be an empty space off the edge of the map.
- **CAVE**: A traversable warp tile that functions as an entrance to a cave.
- LADDER: A traversable warp tile that moves the player between floors.

# Strategic Principles & Lessons Learned
- Menu Navigation: Always verify the order of items in the `Inventory` list from the game state *before* navigating menus to avoid wasting significant time on simple actions. The in-game sort order may not match the data's alphabetical sort.
- **Inefficient Strategies:** When a strategy proves inefficient or clumsy (like fumbling through menus mid-battle), I must pivot immediately to a more direct solution (like switching to a stronger Pokémon) instead of persisting with the flawed approach. I must actively identify and challenge false constraints that limit my strategic options.
- Bug-type moves (like LEECH LIFE) are not very effective against Fire-types.