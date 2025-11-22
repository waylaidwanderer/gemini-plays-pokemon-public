# Game Mechanics & Systems
- The Day/Night cycle is an important mechanic in this game, affecting events.
- Received 5 POKé BALLS from the scientist in Elm's Lab. I can now catch wild Pokémon.
- The PC in Pokémon Centers is used for Pokémon and item storage.
- BERRY trees grow new BERRIES every day.

# Current Quest: Explore Goldenrod Department Store
- **Objective:** Fully explore all floors of the Goldenrod Department Store.
- **Status:** Currently on the Roof (GoldenrodDeptStoreRoof).

# Key Items
- **HIVEBADGE:** From Bugsy. Allows traded POKéMON up to L30 to obey and enables the use of CUT outside of battle.
- **POKéDEX:** A high-tech encyclopedia from PROF. OAK to record POKéMON data.
- **HM05 FLASH:** Obtained from the Elder of Sprout Tower. Illuminates dark caves. Requires the Zephyr Badge to use outside of battle.
- **HM01 CUT:** Obtained from the charcoal maker in Ilex Forest. Allows cutting small trees outside of battle. Requires the Hive Badge.

# TMs
- **TM12 SWEET SCENT**
- **TM31 MUD-SLAP**
- **TM39 SWIFT**
- **TM49 FURY CUTTER**

# Consumable Items
- Received a BITTER BERRY from the tree at (16, 7) on Route 31.

# Strategic Lessons
- **Trust Tool Outputs:** My visual interpretation of the map is fallible. The pathfinding tool's analysis of the map data is the source of truth. If a trusted tool like `find_path` reports 'No path found', I must immediately discard my own hypothesis that a path exists and instead operate under the assumption the tool is correct. My first step should be to find the obstacle on the map that proves the tool right, not to debug the tool. The recent incident on Pokecenter2F, where I spent over 20 turns 'fixing' a correct tool because I failed to see an NPC blocker, is a critical example of this failure.
- **Automation Consistency:** I must consistently use my automation tools (like `select_battle_option`) to improve efficiency and reduce errors, especially when prompted by system critiques. Inconsistent use is a failure of strategy. For built-in tools, I must use them as designed (e.g., passing 'RUN' as an argument to `select_battle_option`) rather than manually scripting button presses.
- **Tool Maintenance & Verification:** If a tool produces an incorrect outcome or contradicts system information, I must not assume the problem is external. The tool is likely flawed and must be fixed immediately. Deferring tool maintenance is a critical failure.
- **Tool Consistency:** When one tool's logic is updated (like `find_path`), any other tools that use similar logic must be updated immediately to prevent conflicting results and strategic errors.
- **Tool Debugging Priority:** When a core tool like a pathfinder fails, debugging it becomes the absolute highest priority, superseding all gameplay goals. A systematic approach is required: 1. Confirm the tool is the problem, not a misunderstanding of the map (e.g., by testing a path manually). 2. Add targeted logging to trace execution and understand the algorithm's decision process. 3. Analyze logs to form a specific hypothesis about the bug before attempting a fix. Do not blindly refactor or revert without evidence.
- **Data Hygiene:** Map markers for resolved events (like collected items) must be deleted immediately to avoid confusion and wasted turns. When updating a marker for an object (e.g., after defeating a trainer), the old marker must be deleted to prevent redundant and conflicting information. Markers should also be linked to their corresponding `object_id` whenever possible to ensure they move with the object.

- **NPC Interactions:** Some interactions, like battling a trainer, can be multi-step. Ensure all initial dialogue is cleared with 'A' presses before the main event (like the battle) will trigger.
- **Pathfinding Logic:** If a path is repeatedly blocked or a tool reports 'No path found,' do not assume you are soft-locked. Re-examine the map visually for alternative routes like ledges or other one-way tiles that may have been missed.
- **Tile Mechanic Verification:** I must verify the mechanics of every tile type through direct observation and experimentation. Assumptions based on a tile's name can be wrong and lead to critical tool failures. I must never assume I know how a tile works until I have tested it.
- **Immediate Correction Principle:** If an in-game observation contradicts a hypothesis (e.g., a failed movement), my absolute highest priority is to immediately correct my internal knowledge base (notepad) and any related tools. Deferring this creates cascading errors.
- **Dialogue & Movement:** I must ensure all dialogue boxes are closed by pressing 'A' before attempting any movement inputs. Trying to move with text on screen will fail.
- **Marker Hygiene for Moving Objects:** When an object with a linked marker moves off-screen, the marker becomes stale. I must immediately delete the marker. A new marker should only be created if/when the object reappears at a new location.
- **Position Verification after Interruptions:** I must ALWAYS verify my current `(x, y)` coordinates in the Game State Information after ANY interruption (battle, phone call, menu, etc.) before planning my next move. Assuming a path plan has completed without verification is a critical failure.
- **Agent-based fixes must be verified in both simple and complex scenarios before a tool is considered fully functional. A fix for one case may not cover all failure conditions.
- **Marker Hygiene:** When creating map markers, I must ensure they are linked to the correct object_id and have accurate labels. Failure to do so degrades the quality of my map data and leads to confusion. Unlinked markers for moving objects are useless.
- **Problem-Solving Escalation:** When stuck on a puzzle after exhausting simple, self-generated hypotheses, I must escalate to a more powerful problem-solving tool, such as my custom agents. Repeating failed attempts is inefficient.
- **Exploration Before Puzzles:** Prioritize exploring all reachable areas of a new map before attempting complex puzzles to ensure all context and potential clues have been gathered.
- **Strategic Lessons (Updates from Self-Assessment):**
- **Tool Input Verification:** Before concluding a tool is broken (e.g., `find_path` returning 'No path found'), I must first verify that my inputs and assumptions are correct. Pathing to an 'unseen' tile is an invalid input, as the tool correctly treats them as impassable. My strategy must adapt to the tool's logic.
- **Tool Contradiction Analysis:** If two of my tools provide contradictory outputs, it's a strong indicator of a bug in one of them. I must immediately stop and debug the tools to resolve the discrepancy instead of trusting one over the other.
- **Verify Root Assumptions:** When a plan fails, especially when a trusted tool like a pathfinder reports an issue, the root hypothesis about the map/mechanic is likely flawed. Do not repeatedly try minor variations of the failed plan. Instead, re-examine the map to find the contradiction and form a new, fundamentally different hypothesis (e.g., trying to go east instead of west when blocked).
- **Pathfinding Failure as a Clue:** When a pathfinding tool repeatedly reports no path to a major area, it's a strong signal that a story-based trigger is required to proceed. Instead of trying minor path variations, I must pivot to finding the trigger event, often hinted at by recent NPC dialogue.
- **Random Chance Strategy:** If a strategy based on random chance (like waiting for moving NPCs) fails repeatedly (3+ times), I must switch to a deterministic strategy (like proactively stunning them in favorable positions).
- **Agent Escalation:** When multiple self-generated hypotheses for a puzzle have failed, especially after getting stuck in a repetitive loop (like the stun-gun strategy), I must escalate to a more powerful problem-solving tool like an agent. Even if the agent's initial suggestions are not the final solution, they serve the critical purpose of breaking cognitive fixation and forcing a re-evaluation of the problem's root assumptions.
- **TRUST THE TOOL, NOT YOUR EYES:** The pathfinder repeatedly reported 'No path found' to the item at (10, 15) because a WALL exists at (10, 14), a fact confirmed by the map data that I failed to see visually. This is the ultimate proof that the tool's analysis of the raw game data is more reliable than my visual interpretation. Future 'No path found' results must be treated as a discovery of a real, unseen obstacle, not as a tool bug.

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

# Available Tools & Agents
**Built-in Tools:**
- `notepad_edit`: Edits this notepad.
- `run_code`: Executes a single-use Python script.
- `define_agent` / `delete_agent`: Manages custom reasoning agents.
- `define_map_marker` / `delete_map_marker`: Manages map markers.
- `define_tool` / `delete_tool`: Manages custom tools.
- `stun_npc`: Freezes or unfreezes an NPC's movement.
- `select_battle_option`: Automatically selects a main battle menu option (FIGHT, PKMN, PACK, RUN).

**Custom Agents & Tools (Defined by me):**
- `gym_puzzle_solver` (Agent): Analyzes gym puzzle descriptions and failed hypotheses to generate new, simple, and testable solutions.
- `python_code_debugger` (Agent): Analyzes a Python script, its intended behavior, and a bug description to provide a corrected version of the code and an explanation of the fix.
- `find_path` (Tool): Finds a path from a start to an end coordinate on the current map using the A* algorithm.
- `find_reachable_unseen_tiles` (Tool): Finds all reachable unseen tiles on the current map.

# Tile Mechanics
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
- **CAVE**: A traversable warp tile leading into a cave.
- **LADDER**: A traversable warp tile that moves the player between floors.
- **FLOOR_UP_WALL**: A one-way ledge that is impassable from above. Confirmed that moving from a FLOOR tile at (5, 23) down to a FLOOR_UP_WALL tile at (5, 24) is impossible. This tile can only be traversed from below (moving up).
- **WARP_CARPET_RIGHT**: A traversable warp tile at the edge of a map that transitions to the adjacent map on the right. To activate, you must attempt to move right from the carpet tile, effectively trying to walk 'off' the map.
- **WARP_CARPET_DOWN**: A traversable warp tile at the edge of a map that transitions to the adjacent map below. Must move down to activate.
- **WARP_CARPET_UP**: A traversable warp tile at the edge of a map that transitions to the adjacent map above. Must move up to activate.
- **VOID**: Impassable terrain that appears to be an empty space off the edge of the map.
- **unseen**: A tile that has not yet been explored. Its properties are unknown until visited.
- **BUOY**: An object found in water. Appears to be impassable, functioning like a WALL tile within a WATER area.

# Object Mechanics
- **TEACHER / LASS / BIRD / OFFICER / YOUNGSTER**: These NPC objects are impassable and function as walls.
- **FRUIT_TREE**: An impassable, interactable object. Gives one BERRY item (like PRZCUREBERRY) when interacted with for the first time. Subsequent interactions yield nothing.

# NPC Dialogue
- **POKEFAN_M in Violet City House:** Traded Pokémon grow quickly but may disobey without the correct Gym Badge.
- Received MIRACLE SEED from a trainer on Route 32.

# Crafting
- Kurt in Azalea Town can make special POKé BALLS from APRICORNS. I received a LURE BALL from him as an example.

# Azalea Gym Info
- Gym Guide: The Gym Leader is BUGSY. His Bug POKéMON are weak to Fire and Flying-type moves.
- **Puzzle Solution:** The gym puzzle involves finding two hidden floor switches. The first, located on the path to the right-side trainer, makes a new trainer appear on the left side. The second, on the path to the left-side trainer, makes another new trainer appear. The path to these trainers is not blocked by the Twins in the middle; it is possible to walk around the bottom of the gym. Defeating all trainers is not required to reach Bugsy.

# Puzzle Mechanics
- **Herding Puzzles:** Interacting with an object (like the Farfetch'd) from an adjacent tile can trigger movement along a complex, pre-determined path, not just simple repulsion. The direction of approach is the key trigger.
- **Visual Path Verification:** Before executing a move, I must visually confirm the path on the ASCII map and game screen to avoid simple navigational errors like walking into walls. This supplements tool-based pathfinding.
- **Debugging Cycle Avoidance:** When a core tool repeatedly fails despite multiple fixes, the core algorithm is likely fundamentally flawed. I must avoid getting stuck in a loop of incremental, failing changes. The correct approach is to either replace the logic with a known-working version from another tool or re-implement it from first principles, rather than continuing with minor tweaks.
- **Positional Hallucination:** I must be extremely careful about my perceived location. If a path fails or the game state seems contradictory, my first assumption should be that I have hallucinated my position, not that the game or my tools are broken. I must always verify my `(x, y)` and `map_id` against the Game State Information before making critical navigation decisions.
- **Movement Interruption:** If a planned movement is interrupted (e.g., by bumping into an NPC), my final position may not be what I intended. I must always verify my actual final coordinates in the Game State Information before proceeding with the next action, rather than assuming the plan completed successfully.

# Game Corner Info
- A POKEFAN_M lost his COIN CASE in the UNDERGROUND. This is likely required to play the games.

# Puzzle Solving Strategy
- **Problem-Solving Escalation:** If a simple, systematic approach (like brute-forcing every tile) fails repeatedly (e.g., 5+ times), it is fundamentally the wrong approach. I must stop, document the failed strategy, and escalate to a more powerful problem-solving method (like my `gym_puzzle_solver` agent) instead of continuing the failed strategy.