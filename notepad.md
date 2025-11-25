# Strategic Principles & Lessons Learned
- **IMMEDIATE DATA & TOOL MAINTENANCE:** My absolute highest priority is maintaining a perfect, up-to-the-second internal state. Any task I decide on, such as adding, deleting, or fixing an agent, tool, marker, or notepad entry, MUST be performed in the CURRENT turn. This task is more important than any in-game action and must never be deferred.
- **IMMEDIATE TOOL MAINTENANCE:** If a tool is flawed, a better one can be conceived, or a hallucinated tool needs to be replaced, this is the absolute highest priority. I must define, refine, or delete the necessary tool in the current turn, not defer it as a goal or a future task. This prevents repeated manual errors and enforces my 'DEFAULT TO AUTOMATION' principle.
- **VERIFY POSITION & SEPARATE INPUTS:** After any interruption (battle, menu, etc.) and before any action, I MUST verify my current `(x, y)` coordinates in the Game State Information. I must NEVER mix directional inputs (Up, Down, Left, Right) and action inputs ('A', 'B') in the same turn. Movement/turning must happen in one turn, and interaction in the next.
- **DEFAULT TO AUTOMATION:** If a custom tool or built-in function exists for a task, I MUST use it by default instead of performing the action with manual button presses. Manual inputs are less efficient and more error-prone.
- **UI Automation Timing:** When automating UI interactions, simple button sequences can fail due to game engine lag or animation timing. Incorporate 'sleep' commands to ensure the UI is in the expected state before the next input is sent.
- **Tool Parameter Verification:** When calling a tool, especially one that automates actions like `select_move`, I must double-check all parameters, such as `autopress_buttons`, to ensure the call is correctly formatted and will execute as intended. A simple oversight can waste a turn.
- **Tool Definition Errors:** If `define_tool` fails with an 'identical script' error, it means the proposed change has already been successfully applied in a previous turn. Do not retry the same definition; proceed with the next action.
- **DEBUG TOOLS IMMEDIATELY:** If a trusted tool provides an output that contradicts obvious reality (e.g., 'No path found' to a clearly visible and reachable tile), the tool is broken. Debugging and fixing the tool becomes the absolute highest priority, superseding any other gameplay objective.
- **TRUST DATA OVER INTUITION:** My custom tools (especially pathfinders) analyze the raw game data, which is the absolute source of truth. My visual interpretation of the screen or my memory can be flawed. If a tool reports 'No path found' or provides contradictory information, I must treat its output as the discovery of a fact about the game state (e.g., a hidden wall, a flawed assumption), not as a bug in the tool itself. I must always verify my root assumptions against the game data before pursuing complex solutions.
- **Tool & Knowledge Base Maintenance:** If a tool is flawed or an in-game observation contradicts a hypothesis, my absolute highest priority is to immediately correct the tool or my internal knowledge base (notepad). Deferring maintenance is a critical failure.
- **Tool Consistency:** When one tool's logic is updated (like `find_path`), any other tools that use similar logic must be updated immediately to prevent conflicting results and strategic errors.
- **Tool Debugging Priority:** When a core tool like a pathfinder fails, debugging it becomes the absolute highest priority, superseding all gameplay goals. A systematic approach is required: 1. Confirm the tool is the problem, not a misunderstanding of the map (e.g., by testing a path manually). 2. Add targeted logging to trace execution and understand the algorithm's decision process. 3. Analyze logs to form a specific hypothesis about the bug before attempting a fix. Do not blindly refactor or revert without evidence.
- **Data Hygiene:** Map markers for resolved events (like collected items) must be deleted immediately to avoid confusion and wasted turns. When updating a marker for an object (e.g., after defeating a trainer), the old marker must be deleted to prevent redundant and conflicting information. Markers should also be linked to their corresponding `object_id` whenever possible to ensure they move with the object.
- **NPC Interactions:** Some interactions, like battling a trainer, can be multi-step. Ensure all initial dialogue is cleared with 'A' presses before the main event (like the battle) will trigger.
- **Pathfinding Logic:** If a path is repeatedly blocked or a tool reports 'No path found,' do not assume you are soft-locked. Re-examine the map visually for alternative routes like ledges or other one-way tiles that may have been missed.
- **Dialogue & Movement:** I must ensure all dialogue boxes are closed by pressing 'A' before attempting any movement inputs. Trying to move with text on screen will fail.
- **Marker Hygiene for Moving Objects:** When an object with a linked marker moves off-screen, the marker becomes stale. I must immediately delete the marker. A new marker should only be created if/when the object reappears at a new location.
- **Agent-based fixes must be verified in both simple and complex scenarios before a tool is considered fully functional. A fix for one case may not cover all failure conditions.
- **Marker Hygiene:** When creating map markers, I must ensure they are linked to the correct object_id and have accurate labels. Failure to do so degrades the quality of my map data and leads to confusion. Unlinked markers for moving objects are useless.
- **Problem-Solving Escalation:** When stuck on a puzzle after exhausting simple, self-generated hypotheses, I must escalate to a more powerful problem-solving tool, such as my custom agents. Repeating failed attempts is inefficient.
- **Exploration Before Puzzles:** Prioritize exploring all reachable areas of a new map before attempting complex puzzles to ensure all context and potential clues have been gathered.
- **Tool Input Verification:** Before concluding a tool is broken (e.g., `find_path` returning 'No path found'), I must first verify that my inputs and assumptions are correct. Pathing to an 'unseen' tile is an invalid input, as the tool correctly treats them as impassable. My strategy must adapt to the tool's logic.
- **Tool Contradiction Analysis:** If two of my tools provide contradictory outputs, it's a strong indicator of a bug in one of them. I must immediately stop and debug the a to resolve the discrepancy instead of trusting one over the other.
- **Verify Root Assumptions:** When a plan fails, especially when a trusted tool like a pathfinder reports an issue, the root hypothesis about the map/mechanic is likely flawed. Do not repeatedly try minor variations of the failed plan. Instead, re-examine the map to find the contradiction and form a new, fundamentally different hypothesis (e.g., trying to go east instead of west when blocked).
- **Random Chance Strategy:** If a strategy based on random chance (like waiting for moving NPCs) fails repeatedly (3+ times), I must switch to a deterministic strategy (like proactively stunning them in favorable positions).
- **Agent Escalation:** When multiple self-generated hypotheses for a puzzle have failed, especially after getting stuck in a repetitive loop (like the stun-gun strategy), I must escalate to a more powerful problem-solving tool like an agent. Even if the agent's initial suggestions are not the final solution, they serve the critical purpose of breaking cognitive fixation and forcing a re-evaluation of the problem's root assumptions.
- **Herding Puzzles:** Interacting with an object (like the Farfetch'd) from an adjacent tile can trigger movement along a complex, pre-determined path, not just simple repulsion. The direction of approach is the key trigger.
- **Visual Path Verification:** Before executing a move, I must visually confirm the path on the ASCII map and game screen to avoid simple navigational errors like walking into walls. This supplements tool-based pathfinding.
- **Debugging Cycle Avoidance:** When a core tool repeatedly fails despite multiple fixes, the core algorithm is likely fundamentally flawed. I must avoid getting stuck in a loop of incremental, failing changes. The correct approach is to either replace the logic with a known-working version from another tool or re-implement it from first principles, rather than continuing with minor tweaks.
- **Puzzle State Changes:** Some puzzles, like the Goldenrod Dept. Store basement, may change their state based on triggers that are not immediately obvious, such as leaving and re-entering the area. If internal solutions fail, I must consider external actions as potential triggers.
- **Interaction Loops:** If repeated interaction with an NPC doesn't change the outcome, the solution lies elsewhere. Don't get stuck in an interaction loop; pivot to testing environmental or sequential triggers.
- **Trust Pathfinder Output:** If `find_path` reports 'No path found' to a seemingly reachable location, trust the tool. It is analyzing the raw map data and has likely identified an obstacle or layout issue (like one-way paths or impassable terrain) that is not immediately obvious. Re-examine the map visually to understand the blockage instead of assuming the tool is bugged.
- **Interaction vs. Line of Sight:** If direct interaction with a trainer-like NPC results in a dialogue loop, the battle trigger is likely entering their line of sight. If both methods fail, they may not be a battlable trainer.
- **Positional Awareness:** Always verify my own coordinates and the coordinates of relevant NPCs before using a targeted tool like `stun_npc`. Wasting a turn on an unnecessary action is a failure of observation.
- **EXECUTION DISCIPLINE:** A plan is useless if not executed. I recently failed by stating my intent to use automation tools but then manually pressing buttons, directly contradicting my own strategy. This is a critical failure. I MUST ensure my actions in `buttons_to_press` or `tools_to_call` perfectly match the plan articulated in my thoughts. Defaulting to automation is not optional; it is a core principle.
- **Notepad Edit Precision:** When using `notepad_edit` with the `replace` action, the `old_text` must be an exact match. If an edit fails because the text is not found, it's possible the change was already successfully applied in a previous turn. Verify the current notepad content before retrying.
- **Data Structure Verification:** Do not assume data structures or sorting order within the game (e.g., inventory lists). Always verify against direct observation before building automation that relies on it. A faulty assumption about data will lead to tool failure.
- **Blocked Movement vs. Battle Start:** A 'Movement Blocked' alert does not guarantee a wild battle has started. I must wait for the battle screen text to appear before assuming I am in a battle and pressing 'A' to advance dialogue. This prevents wasted turns from incorrect assumptions.
- **Tool Output for Autopress:** When a custom tool has `autopress_buttons: true`, its `print()` output MUST be a valid JSON array of strings. Any other text, such as debug statements, will corrupt the output and cause a JSON parsing error.
- **Verify Location After Transitions:** After any map transition (entering/exiting a building or route), I must immediately verify my current map ID and coordinates from the Game State Information to prevent severe hallucinations about my location.
- **Tool Debugging Logic:** When a tool fails repeatedly in a predictable way (e.g., always selecting the wrong item), the problem is likely a core logic or syntax error, not a simple timing issue. I must investigate the code itself rather than just tweaking parameters like sleep timers.
- **Execution Errors:** I must ensure my actions match my plan. A recent failure was caused by manually pressing buttons (`B`, `A`) instead of calling the intended tool, which wasted a turn and accomplished nothing. I must double-check that I am pressing the `tool` button when my plan is to use a tool.
- **Struggle Mechanic Failure:** Repeatedly selecting a 0 PP move does not trigger Struggle in this game. If a Pokémon runs out of PP, the only viable options are to switch out or use an item. Do not get stuck in a loop trying to force Struggle.
- **Tool Robustness:** Tools must be written to handle all likely edge cases. A tool failing because a target is already selected indicates a lack of robust design. Fixing such flaws immediately is critical to maintaining automation efficiency.
- **Proactive Automation:** I must not wait until a manual task becomes a major bottleneck before automating it. If I identify any repetitive, complex, or error-prone manual action, creating a tool or agent to handle it becomes an immediate high-priority task, superseding non-critical gameplay actions. Deferring automation is a strategic failure.
- **Verify Location After Transitions:** After any map transition (entering/exiting a building or route), I MUST immediately verify my current map ID and coordinates from the Game State Information to prevent severe hallucinations about my location.

# Game Mechanics & Systems
- The Day/Night cycle is an important mechanic in this game, affecting events.
- Received 5 POKé BALLS from the scientist in Elm's Lab. I can now catch wild Pokémon.
- The PC in Pokémon Centers is used for Pokémon and item storage.
- BERRY trees grow new BERRIES every day.
- Healing at a Pokémon Center restores all HP and PP for the entire party and cures any status conditions.
- **Game State Updates:** The game's internal map data (like a `CUT_TREE` changing to a `FLOOR`) does not fully update until all on-screen text from the preceding action is cleared. Attempting to use tools like `find_path` before the overworld is fully interactive will result in the tool using stale data and failing.
- **HEADBUTT Mechanic:** The move HEADBUTT can be used outside of battle to shake certain trees (`HEADBUTT_TREE` tiles). This can cause sleeping Pokémon to fall out, providing a new method for encounters.
- **Environmental Obstacle Resets:** The CUT_TREE at (8, 25) in Ilex Forest reappeared after I left the map and returned. This suggests some environmental obstacles might reset upon re-entry.
- **CRITICAL DATA VERIFICATION:** My memory of game mechanics or map layouts can be flawed. I must always trust the raw Game State Information (Map Memory, Map Events) over my own assumptions. If a plan fails, the first step is to re-verify all assumptions against the game data.
- **Warp vs. Map Edge:** I must distinguish between formal warp tiles (like doors, listed in Map Events) and map edge transitions (walking off the map). Hallucinating a warp where a transition exists can cause validation errors and flawed navigation plans. Always verify against the `Map Events -> Warps` list.

# Battle Mechanics
- Pokémon holding a BERRY can automatically use it to heal themselves when their HP gets low in battle.
- Poisoned Pokémon lose 1 HP every four steps outside of battle and remain poisoned after a wild battle concludes.
- Accuracy-lowering moves like SMOKESCREEN are not a guaranteed defense.
- The auto-activation threshold for a held BERRY is likely below 25% HP.
- Grass-type moves (like VINE WHIP) are not very effective against Fire-types.
- Normal-type moves have no effect on Ghost-type Pokémon.
- Normal-type moves (like TACKLE) are not very effective against Rock/Ground-types (like GEODUDE).
- Flying-type moves (like PECK) are not very effective against Rock/Ground-types (like GEODUDE).
- Fire-type moves (like EMBER) are not very effective against Rock/Ground-types (like GEODUDE).
- A single high-level Pokémon cannot carry an entire under-leveled team through a major battle like a Gym.
- Levels Over Type Advantage: A significant level disparity can completely negate type advantages. My Lv8 ROCKY was one-shot by a move it should have resisted, proving that raw power from a higher level is a critical factor.
- Low-HP Threat: A low-HP Pokémon with a status move like Hypnosis is still a major threat. Prioritize eliminating it quickly, even if it means using a stronger Pokémon and not spreading EXP optimally, to avoid having the whole team disabled.
- Type Immunity vs. Level Disparity: Type immunity (e.g., Flying vs. Ground) is not a guaranteed defense against a much higher-level opponent. A significant level gap means the opponent can still knock out the immune Pokémon with its other, non-resisted moves.
- **Pathfinding Failure as a Clue:** When a pathfinding tool repeatedly reports no path to a major area, it's a strong signal that a story-based trigger is required to proceed or the map layout is not what it seems. Instead of assuming the tool is bugged or trying minor path variations, I must re-evaluate my root assumptions about the map's traversability and pivot to finding the trigger event, often hinted at by recent NPC dialogue.

# Menu Navigation
- For complex menu inputs (like on-screen keyboards), perform all directional movements in one turn and the final confirmation ('A' button) in the next. Do not mix directional and action buttons in the same input sequence to avoid errors.
- In the party screen, the 'SWITCH' option is used to reorder Pokémon. The 'MOVE' option is for reordering a Pokémon's moves. Confusing these leads to menu loops.
- The main battle menu options are laid out in a 2x2 grid: FIGHT (top-left), PKMN (top-right), PACK (bottom-left), RUN (bottom-right). Navigating from FIGHT requires 'Right' for PKMN and 'Down' for PACK.

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
- **FLOOR_UP_WALL**: Confirmed impassable when trying to move onto it from an adjacent tile above. My previous hypothesis that it was a one-way ledge was a hallucination.
- **WARP_CARPET_RIGHT**: A traversable warp tile at the edge of a map that transitions to the adjacent map on the right. To activate, you must attempt to move right from the carpet tile, effectively trying to walk 'off' the map.
- **WARP_CARPET_UP**: A traversable warp tile at the edge of a map that transitions to the adjacent map above. Must move up to activate. Confirmed that moving from this tile to a FLOOR tile below it is possible, so it is not a one-way ledge.
- **WARP_CARPET_DOWN**: A traversable warp tile at the edge of a map that transitions to the adjacent map below. Must move down to activate.
- **unseen**: A tile that has not yet been explored. Its properties are unknown until visited.
- **BUOY**: An object found in water. Appears to be impassable, functioning like a WALL tile within a WATER area.
- **WARP_CARPET_LEFT**: A traversable warp tile at the edge of a map that transitions to the adjacent map on the left. To activate, you must attempt to move left from the carpet tile, effectively trying to walk 'off' the map.
- **TEACHER / LASS / BIRD / OFFICER / YOUNGSTER**: These NPC objects are impassable and function as walls.
- **FRUIT_TREE**: An impassable, interactable object. Gives one BERRY item (like PRZCUREBERRY) when interacted with for the first time. Subsequent interactions yield nothing.
- **CAVE**: A traversable warp tile that functions as an entrance to a cave.
- **To interact with objects** like ladders, signs, or switches, you must be standing on an adjacent tile and facing the object. Attempting to interact while standing *on* the object itself will fail.
- **Route 30's one-way ledges** (`LEDGE_HOP_DOWN`) make northbound travel from Cherrygrove City impossible. The route is effectively a one-way path when traveling south from Route 31. This is a critical piece of information for future navigation planning.
- **Verify Warp Coordinates:** Before setting a navigation goal that is a warp, I must verify its existence and coordinates in the 'Map Events -> Warps' list for the current map to avoid hallucinations and failed pathing.
- **VOID**: An impassable tile type found at the edges of some maps, functions as a wall.
- **GRASS**: Fully traversable tile, similar to TALL_GRASS. Wild POKéMON can be encountered here.
- **FLOWER**: Fully traversable decorative tile.
- **SIGN**: An impassable, interactable object. Functions as a wall.

# Available Tools & Agents

## Custom Agents
- `gym_puzzle_solver`: Analyzes gym puzzle descriptions and failed hypotheses to generate new, simple, and testable solutions.
- `python_code_debugger`: Analyzes a Python script, its intended behavior, and a bug description to provide a corrected version of the code and an explanation of the fix.

## Custom Tools
- `find_path`: Finds a path from a start to an end coordinate on the current map using the BFS algorithm.
- `find_reachable_unseen_tiles`: Finds all reachable unseen tiles on the current map.
- `select_move`: Selects a move from the battle menu by name.
- `switch_pokemon`: Automates switching to a specific Pokémon in the party during a battle.
- `select_item`: Automates selecting a specific item from the bag menu. It takes the target item's name and the current screen text as input. It must be state-aware, calculating moves relative to the current cursor position.

## Built-in Tools
- `select_battle_option`: Automatically selects the requested main battle menu option (FIGHT, PKMN, PACK, RUN).

# Current Quest: Train for Whitney Rematch
- **Objective:** Defeat Whitney at the Goldenrod Gym.
- **Status:** In Union Cave, training GIBRALTAR. Currently heading to Azalea Town to heal.

# Key Items
- **HIVEBADGE:** From Bugsy. Allows traded POKéMON up to L30 to obey and enables the use of CUT outside of battle.
- **POKéDEX:** A high-tech encyclopedia from PROF. OAK to record POKéMON data.
- **HM05 FLASH:** Obtained from the Elder of Sprout Tower. Illuminates dark caves. Requires the Zephyr Badge to use outside of battle.
- **HM01 CUT:** Obtained from the charcoal maker in Ilex Forest. Allows cutting small trees outside of battle. Requires the Hive Badge.

# TMs
- **TM02 HEADBUTT:** Received from a Rocker in Ilex Forest. Can be used to shake trees and find sleeping Pokémon.
- **TM12 SWEET Scent**
- **TM31 MUD-SLAP**
- **TM39 SWIFT**
- **TM49 FURY CUTTER**

# NPC Dialogue
- **POKEFAN_M in Violet City House:** Traded Pokémon grow quickly but may disobey without the correct Gym Badge.
- Received MIRACLE SEED from a trainer on Route 32.
- **FIREBREATHER WALT on Route 35:** Said "I'm practicing my fire breathing." despite appearing as a FISHER sprite. Likely a Fire-type trainer.
- A POKEFAN_M in the Game Corner lost his COIN CASE in the UNDERGROUND. This is likely required to play the games.
- **Phone Calls:**
    - Youngster JOEY called for a rematch on Route 30.
    - Hiker ANTHONY called for a rematch on Route 33.
    - Hiker ANTHONY called, mentioning that lots of timid DUNSPARCE can be found in DARK CAVE. He has called for a rematch on Route 33 multiple times.
    - Juggler IRWIN called, just to introduce himself.

# Crafting
- Kurt in Azalea Town can make special POKé BALLS from APRICORNS. I received a LURE BALL from him as an example.

# Puzzle Solutions

## Azalea Gym
- Gym Guide: The Gym Leader is BUGSY. His Bug POKéMON are weak to Fire and Flying-type moves.
- **Solution:** The gym puzzle involves finding two hidden floor switches. The first, located on the path to the right-side trainer, makes a new trainer appear on the left side. The second, on the path to the left-side trainer, makes another new trainer appear. The path to these trainers is not blocked by the Twins in the middle; it is possible to walk around the bottom of the gym. Defeating all trainers is not required to reach Bugsy.

## Goldenrod Department Store
- **Elevator:** The elevator is controlled by the panel at (3, 0). Interacting with the panel brings up a floor selection menu. After selecting a floor, you must walk onto the corresponding warp carpet to travel. The warp to B1F is at (1, 3) and the warp to 1F is at (2, 3).
- **B1F Box Puzzle:** My own movement is causing changes in the map layout. A WALL at (5, 10) changed to a FLOOR after I moved. The Machop at (7, 7) is likely the key to solving the puzzle. The previous solution of leaving and returning the room seems to be only a partial trigger.

## Goldenrod Gym
- Gym Guide: This is a Normal-type gym. Fighting-type POKéMON are recommended.
- **Puzzle Mechanic:** The gym puzzle is solved by walking along the outer perimeter of the entrance room. The direction and sequence of these walks cause different trainers to appear and disappear, opening and closing paths. The correct sequence of perimeter walks and trainer battles is required to open the path to the main gym area.

# Obstacles and Solutions
- A strange tree blocks the road north of Goldenrod City (Route 35). It can be cleared using a SQUIRTBOTTLE, which is obtained from the Flower Shop after defeating Whitney. The Lass in the shop confirms this is the correct sequence of events.

# Held Items
- **QUICK CLAW:** Received from a Teacher in the National Park. When held by a Pokémon, it may allow them to attack first in battle.

# Goldenrod Department Store Directory
- 1F: SERVICE COUNTER
- 2F: TRAINER'S MARKET
- 3F: BATTLE COLLECTION
- 4F: MEDICINE BOX
- 5F: TM CORNER
- 6F: TRANQUIL SQUARE
- ROOFTOP LOOKOUT

## Goldenrod Dept. Store B1F Box Puzzle Log
- **Hypothesis 1:** The puzzle solution involves interacting with the Machop at (7, 7).
  - **Test:** Path to (6, 7) and press 'A' on the Machop.
  - **Result:** Machop gave dialogue ("MACHOKE: Maaacho!") but the map layout did not change. Path to the item at (14, 2) remained blocked.
  - **Conclusion:** Hypothesis failed. Simple interaction with the Machop is not the solution.
- **Hypothesis 2:** Interacting with the static Black Belt at (4, 8) will solve the puzzle, based on his dialogue about being watched.
  - **Test:** Path to (5, 8), face left, and press 'A'.
  - **Result:** Black Belt gave new dialogue ("Come on, kid, scoot!"). Map layout did not change immediately.
  - **Conclusion:** Interaction is a necessary step, but not the complete solution. The next step is to follow his instruction to "scoot."
- **Hypothesis 3 (Agent):** Defeating the moving Black Belt at (9, 11) is the trigger.
  - **Test 1:** Walk into his line of sight.
  - **Result:** No battle triggered. He moved past me.
  - **Conclusion:** Hypothesis sub-test failed. Line of sight is not the trigger.
- **Hypothesis 3 (Agent):** Defeating the moving Black Belt at (9, 11) is the trigger.
  - **Test 2:** Interact with him directly.
  - **Result:** Confirmed! Interaction triggered dialogue ("Hey, kid! You're holding us up!") and caused the map layout to change, opening the path to the east.
  - **Conclusion:** The puzzle is solved by a sequence of interactions and movement.
- **Puzzle State Changes:** Some puzzles, like the Goldenrod Dept. Store basement, may change their state based on triggers that are not immediately obvious, such as leaving and re-entering the area. If internal solutions fail, I must consider external actions as potential triggers.
- **Tool Logic Consistency:** When writing tool scripts, ensure that data comparisons (like finding list indices) are performed using a single, consistent frame of reference. Using different versions of a list (e.g., one with a cursor marker and one without) for the same logical operation can lead to subtle, hard-to-diagnose bugs. This was the root cause of the `select_move` tool failure.

# PC Inventory
- **Box 1:**
  - Hestia (MAGBY), Lv15, Female
- **Conclusion:** My Onix (Rocky) is NOT in the PC. My memory was a hallucination based on the Pokedex entry. My new plan is to travel to Union Cave to catch a Geodude as a replacement counter for Whitney.
- **VERIFY PARTY/PC STATUS:** Before using the PC to deposit or withdraw a Pokémon, I must first verify the current composition of both my party and the relevant PC box to prevent hallucinations and wasted actions based on a faulty internal state.

# Azalea Town Investigation Log
- **Hypothesis 1:** The Team Rocket Grunt at the Slowpoke Well is the story trigger.
  - **Test:** Interact with the object at (18, 9).
  - **Result:** It was a Slowpoke, not a Grunt. Dialogue was "Yawn?".
  - **Conclusion:** Hypothesis failed due to a hallucination. The trigger is not a Grunt.
- **Hypothesis 2:** Kurt will provide information about the Slowpoke situation.
  - **Test:** Talk to Kurt at (3, 2) in his house.
  - **Result:** Kurt's dialogue was only about making Poké Balls from Apricorns.
  - **Conclusion:** Hypothesis failed. Kurt is not the immediate trigger for the Slowpoke Well event.
- **Hypothesis 3:** A Youngster at (8, 9) might have information.
  - **Test:** Talk to the Youngster.
  - **Result:** He mentioned that the 'CHARCOAL MAN's POKéMON can CUT down trees.' This is a major clue.
  - **Conclusion:** The Charcoal Man, likely found at the Charcoal Kiln (21, 13), is the next person to investigate.
- **Hypothesis 4:** The Black Belt at (2, 3) in the Charcoal Kiln is the 'Charcoal Man'.
  - **Test:** Talk to the Black Belt.
  - **Result:** His dialogue ('You chased off TEAM ROCKET...') contradicts the current game state.
  - **Conclusion:** Hypothesis failed. He is not the immediate story trigger.
- **Hypothesis 5:** The Youngster at (6, 4) in the Charcoal Kiln is the 'Charcoal Man' or has information.
  - **Test:** Talk to the Youngster.
  - **Result:** He gave me CHARCOAL as a thank you, but no information about the Slowpoke situation.
  - **Conclusion:** Hypothesis failed. He is not the immediate story trigger.
- **State-Aware Automation:** Any tool that navigates a list-based UI (like the party menu or move list) MUST be state-aware. It must identify the current cursor position (e.g., from a '▶' marker) and calculate relative movements ('Up'/'Down') rather than assuming a fixed starting point. This prevents catastrophic failures when the UI state is not what's expected.
- **CRITICAL LOCATION VERIFICATION:** After any map transition (entering/exiting a building, changing routes), I MUST immediately verify my current map ID and coordinates from the Game State Information. This is the only way to prevent severe hallucinations about my location, which has been a recurring critical failure.
- **EXECUTION DISCIPLINE:** A plan is useless if not executed. I must ensure my actions perfectly match the plan articulated in my thoughts. Defaulting to automation is not optional; it is a core principle.
- **Resource Management:** Avoid inefficient battles (e.g., against high-defense, low-EXP opponents) that drain PP for minimal gain. Running away is often the more strategic option to conserve resources for more important fights or exploration.
- Ground-type moves have no effect on Flying-type Pokémon.
- **Warp Carpet Anomaly:** The `WARP_CARPET_DOWN` tile at Union Cave (17, 3) was confusing. A manual 'Down' press failed due to a wall, but an automated path through the same tile succeeded in warping me. The exact mechanic is unclear and needs further investigation.

# Tile & Object Mechanics
- **LONG_GRASS**: Fully traversable tile. Wild POKéMON can be encountered here.

# Strategic Principles & Lessons Learned
- **VERIFY PARTY/PC STATUS:** Before using the PC or party menu to deposit, withdraw, or switch a Pokémon, I must first verify the current composition of both my party and the relevant PC box to prevent hallucinations and wasted actions based on a faulty internal state.
- **Proactive Automation:** I must not wait until a manual task becomes a major bottleneck before automating it. If I identify any repetitive, complex, or error-prone manual action, creating a tool or agent to handle it becomes an immediate high-priority task, superseding non-critical gameplay actions. Deferring automation is a strategic failure.
- **Verify Location After Transitions:** After any map transition (entering/exiting a building or route), I MUST immediately verify my current map ID and coordinates from the Game State Information to prevent severe hallucinations about my location.

# Strategic Principles & Lessons Learned
- **Tool Context Awareness:** Tools like `select_battle_option` are context-specific and will fail if used when the required UI (e.g., the main battle menu) is not visible. Always verify the game state before calling a context-dependent tool.
- **Agent UI Parsing Warning:** Agents can hallucinate the structure of a UI when parsing it from screen text. I must always verify an agent's core assumptions about the UI layout before trusting its code. Simple, robust parsing methods that rely on stable structural elements are superior to complex, brittle ones that rely on variable content.

# Strategic Principles & Lessons Learned
- **Agent Code Verification:** Agent-provided code, especially for UI parsing, must be critically scrutinized. The agent may hallucinate UI elements or structure (e.g., PP counters on the same line as a move name). Always verify the agent's core assumptions against direct observation of the screen text before implementing its code. Simple, observation-based logic is often more robust and reliable.

# Strategic Principles & Lessons Learned
- **UI Automation Timing:** Simple button sequences can fail due to game engine lag or animation timing. I must incorporate 'sleep' commands or wait a full turn after opening a new menu before sending subsequent inputs to ensure the UI is in the expected state.

# Game Mechanics & Systems
- **Battle Anomaly:** A wild battle terminated unexpectedly. After pressing 'A' on the main battle menu's 'FIGHT' option, I was returned to the overworld without any battle resolution. The cause is unknown.