# Strategic Principles & Lessons Learned
- **Warp Navigation Lesson:** When setting a `navigation_goal` to a warp, the coordinates provided in `navigation_goal_coordinates` MUST be the coordinates of the warp tile on the *current* map, not the destination map. Verifying this against the `Map Events -> Warps` list is critical to avoid hallucinations and validation errors.
- CRITICAL LESSON - Trust Warp Data: My visual count of warps in the Kabuto Chamber was a hallucination. I must always trust the raw Game State Information's 'Map Events -> Warps' list over my own memory or visual assessment. Verify against the data.
- **CRITICAL LESSON - Verify Location:** I have repeatedly hallucinated my location after map transitions. I MUST verify my current map ID and coordinates from the Game State Information after every warp or map change before taking any other action.
- **CRITICAL LESSON - Trust Tool Failures:** When a trusted tool like `find_path` reports 'No path found', it is a strong signal that my own understanding of the game state (my location, the map layout) is fundamentally flawed. I must question my own assumptions before questioning the tool.
- **EXECUTION DISCIPLINE:** A plan is useless if not executed. I must ensure my actions perfectly match the plan articulated in my thoughts. A recent critique highlighted failures where I manually pressed buttons instead of calling my intended `select_battle_option` tool. I must always call the correct, existing tools for their intended purpose.
- **Pathfinding Tool Principles (Consolidated):**
  - **Trust the Tool's Data:** When a pathfinder's output (e.g., 'No path found') contradicts a visual assumption, trust the tool. Its analysis of raw map data is more reliable than visual interpretation. Verify the game state in-game before debugging a trusted tool.
  - **Debug Collision Failures Immediately:** If a pathfinder generates a path through a visible on-screen object (like an NPC), its collision logic (likely the `has_object` check) is critically flawed and must be debugged immediately.
  - **Account for Off-Screen Objects:** Pathfinders are blind to off-screen objects. For long-distance pathing, I must consult my map markers to manually plan around known off-screen obstacles to prevent interruptions.
- **IMMEDIATE DATA & TOOL MAINTENANCE:** My absolute highest priority is maintaining a perfect, up-to-the-second internal state. Any task I decide on—adding, deleting, or fixing an agent, tool, marker, or notepad entry—MUST be performed in the CURRENT turn. This task is more important than any in-game action and must never be deferred. If a tool is flawed, a better one can be conceived, or it contradicts reality, fixing or creating it is the top priority, superseding all other objectives.
- **VERIFY POSITION & SEPARATE INPUTS:** After any interruption (battle, menu, etc.) and before any action, I MUST verify my current `(x, y)` coordinates in the Game State Information. I must NEVER mix directional inputs (Up, Down, Left, Right) and action inputs ('A', 'B') in the same turn. Movement/turning must happen in one turn, and interaction in the next.
- **DEFAULT TO AUTOMATION:** If a custom tool or built-in function exists for a task, I MUST use it by default instead of performing the action with manual button presses. Manual inputs are less efficient and more error-prone.
- **Agent Escalation for Debugging:** If I am struggling to debug a tool manually after a few attempts, I MUST escalate to the `python_code_debugger` agent. It can often identify logical flaws more quickly and efficiently than I can.
- **UI Automation Timing:** When automating UI interactions, simple button sequences can fail due to game engine lag or animation timing. Incorporate 'sleep' commands to ensure the UI is in the expected state before the next input is sent.
- **Tool Parameter Verification:** When calling a tool, especially one that automates actions like `select_move`, I must double-check all parameters, such as `autopress_buttons`, to ensure the call is correctly formatted and will execute as intended. A simple oversight can waste a turn.
- **Tool Definition Errors:** If `define_tool` fails with an 'identical script' error, it means the proposed change has already been successfully applied in a previous turn. Do not retry the same definition; proceed with the next action.
- **DEBUG TOOLS IMMEDIATELY:** If a trusted tool provides an output that contradicts obvious reality (e.g., 'No path found' to a clearly visible and reachable tile), the tool is broken. Debugging and fixing the tool becomes the absolute highest priority, superseding any other gameplay objective.
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
- **Tool Contradiction Analysis:** If two custom tools provide contradictory outputs, it is a strong indicator of a bug in one of them. I must immediately stop and debug the faulty tool to resolve the discrepancy instead of trusting one over the other.
- **Verify Root Assumptions:** When a plan fails, especially when a trusted tool like a pathfinder reports an issue, the root hypothesis about the map/mechanic is likely flawed. Do not repeatedly try minor variations of the failed plan. Instead, re-examine the map to find the contradiction and form a new, fundamentally different hypothesis (e.g., trying to go east instead of west when blocked).
- **Random Chance Strategy:** If a strategy based on random chance (like waiting for moving NPCs) fails repeatedly (3+ times), I must switch to a deterministic strategy (like proactively stunning them in favorable positions).
- **Agent Escalation:** When multiple self-generated hypotheses for a puzzle have failed, especially after getting stuck in a repetitive loop (like the stun-gun strategy), I must escalate to a more powerful problem-solving tool like an agent. Even if the agent's initial suggestions are not the final solution, they serve the critical purpose of breaking cognitive fixation and forcing a re-evaluation of the problem's root assumptions.
- **Herding Puzzles:** Interacting with an object (like the Farfetch'd) from an adjacent tile can trigger movement along a complex, pre-determined path, not just simple repulsion. The direction of approach is the key trigger.
- **Visual Path Verification:** Before executing a move, I must visually confirm the path on the ASCII map and game screen to avoid simple navigational errors like walking into walls. This supplements tool-based pathfinding.
- **Debugging Cycle Avoidance:** When a core tool repeatedly fails despite multiple fixes, the core algorithm is likely fundamentally flawed. I must avoid getting stuck in a loop of incremental, failing changes. The correct approach is to either replace the logic with a known-working version from another tool or re-implement it from first principles, rather than continuing with minor tweaks.
- **Puzzle State Changes:** Some puzzles, like the Goldenrod Dept. Store basement, may change their state based on triggers that are not immediately obvious, such as leaving and re-entering the area. If internal solutions fail, I must consider external actions as potential triggers.
- **Interaction Loops:** If repeated interaction with an NPC doesn't change the outcome, the solution lies elsewhere. Don't get stuck in an interaction loop; pivot to testing environmental or sequential triggers.
- **Interaction vs. Line of Sight:** If direct interaction with a trainer-like NPC results in a dialogue loop, the battle trigger is likely entering their line of sight. If both methods fail, they may not be a battlable trainer.
- **Positional Awareness:** Always verify my own coordinates and the coordinates of relevant NPCs before using a targeted tool like `stun_npc`. Wasting a turn on an unnecessary action is a failure of observation.
- **Notepad Edit Precision:** When using `notepad_edit` with the `replace` action, the `old_text` must be an exact match. If an edit fails because the text is not found, it's possible the change was already successfully applied in a previous turn. Verify the current notepad content before retrying.
- **Data Structure Verification:** Do not assume data structures, sorting order, or string casing within the game (e.g., inventory lists, item names). Always verify against direct observation before building automation that relies on it. A faulty assumption about data, like case-sensitivity, will lead to tool failure.
- **Blocked Movement vs. Battle Start:** A 'Movement Blocked' alert does not guarantee a wild battle has started. I must wait for the battle screen text to appear before assuming I am in a battle and pressing 'A' to advance dialogue. This prevents wasted turns from incorrect assumptions.
- **Tool Output for Autopress:** When a custom tool has `autopress_buttons: true`, its `print()` output MUST be a valid JSON array of strings. Any other text, such as debug statements, will corrupt the output and cause a JSON parsing error.
- **Verify Location After Transitions:** After any map transition (entering/exiting a building or route), I MUST immediately verify my current map ID and coordinates from the Game State Information to prevent severe hallucinations about my location.
- **Tool Debugging Logic:** When a tool fails repeatedly in a predictable way (e.g., always selecting the wrong item), the problem is likely a core logic or syntax error, not a simple timing issue. I must investigate the code itself rather than just tweaking parameters like sleep timers.
- **Execution Errors:** I must ensure my actions match my plan. A recent failure was caused by manually pressing buttons (`B`, `A`) instead of calling the intended tool, which wasted a turn and accomplished nothing. I must double-check that I am pressing the `tool` button when my plan is to use a tool.
- **Struggle Mechanic Failure:** Repeatedly selecting a 0 PP move does not trigger Struggle in this game. If a Pokémon runs out of PP, the only viable options are to switch out or use an item. Do not get stuck in a loop trying to force Struggle.
- **Tool Robustness:** Tools must be written to handle all likely edge cases. A tool failing because a target is already selected indicates a lack of robust design. Fixing such flaws immediately is critical to maintaining automation efficiency.
- **Proactive Automation:** I must not wait until a manual task becomes a major bottleneck before automating it. If I identify any repetitive, complex, or error-prone manual action, creating a tool or agent to handle it becomes an immediate high-priority task, superseding non-critical gameplay actions. Deferring automation is a strategic failure.
- **Resource Management:** Avoid inefficient battles (e.g., against high-defense, low-EXP opponents) that drain PP for minimal gain. Running away is often the more strategic option to conserve resources for more important fights or exploration.
- **Warp Carpet Anomaly:** The `WARP_CARPET_DOWN` tile at Union Cave (17, 3) was confusing. A manual 'Down' press failed due to a wall, but an automated path through the same tile succeeded in warping me. The exact mechanic is unclear and needs further investigation.
- **Tool Context Awareness:** Tools like `select_battle_option` are context-specific and will fail if used when the required UI (e.g., the main battle menu) is not visible. Always verify the game state before calling a context-dependent tool.
- **Agent UI Parsing Warning:** Agents can hallucinate the structure of a UI when parsing it from screen text. I must always verify an agent's core assumptions about the UI layout before trusting its code. Simple, robust parsing methods that rely on stable structural elements are superior to complex, brittle ones that rely on variable content.
- **Agent Code Verification:** Agent-provided code, especially for UI parsing, must be critically scrutinized. The agent may hallucinate UI elements or structure (e.g., PP counters on the same line as a move name). Always verify the agent's core assumptions against direct observation of the screen text before implementing its code. Simple, observation-based logic is often more robust and reliable.
- **Type Disadvantage Switching:** When a Pokémon is facing an opponent with a significant type advantage (e.g., Rock/Ground vs. Fighting), switching out is not just an option, it's a critical necessity to avoid taking massive damage or being knocked out. Preserving HP is key.
- **Interaction Pre-check:** Before pressing 'A' to interact with any NPC or object, I must first perform a pre-check: verify my character is standing on an adjacent tile AND is facing the target directly. Wasting a turn on a failed interaction due to poor positioning is a critical error.
- **Proactive Stunning:** To avoid wasting turns on failed interactions with moving NPCs, the default strategy must be to use `stun_npc` to freeze them in place *before* attempting to approach and talk to them.
- **Pathing Interruption:** Even short, automated paths can be interrupted by moving NPCs. Proactive stunning is the most reliable strategy to ensure path execution and successful interaction.
- **IMMEDIATE TOOL MAINTENANCE (Addendum):** Do not defer tool fixes. If a tool breaks in a specific context (like a battle menu), I must stay in that context and fix it immediately, even if it means taking damage or losing a turn. The context is critical for debugging and is lost once I leave.
- **Non-Battling NPCs:** Not all moving NPCs are trainers. If an NPC's dialogue repeats without initiating a battle after multiple interaction attempts (direct, line-of-sight), they are likely a non-battling character. Do not get stuck in an interaction loop; update markers and move on.
- **Trust the Pathfinder:** When the `find_path` tool reports 'No path found,' the path is genuinely blocked. My own visual assessment can be flawed. I must trust the tool's analysis of the map data and immediately pivot my strategy instead of questioning the tool.
- **`select_move` Workflow:** The tool's logic for calculating button presses is correct, but the `autopress_buttons` feature is unreliable due to game engine timing. The correct and verified workflow is: 1. Call the tool with `autopress_buttons: false`. 2. Manually input the button presses returned by the tool. 3. Press 'A' in the next turn to execute the move.

# Game Mechanics & Systems
- The Day/Night cycle is an important mechanic in this game, affecting events.
- Received 5 POKé BALLS from the scientist in Elm's Lab. I can now catch wild Pokémon.
- The PC in Pokémon Centers is used for Pokémon and item storage.
- BERRY trees grow new BERRIES every day.
- Healing at a Pokémon Center restores all HP and PP for the entire party and cures any status conditions.
- **Game State Updates:** The game's internal map data (like a `CUT_TREE` changing to a `FLOOR`) does not fully update until all on-screen text from the preceding action is cleared. Attempting to use tools like `find_path` before the overworld is fully interactive will result in the tool using stale data and failing.
- **HEADBUTT Mechanic:** The move HEADBUTT can be used outside of battle to shake certain trees (`HEADBUTT_TREE` tiles). This can cause sleeping Pokémon to fall out, providing a new method for encounters.
- **Environmental Obstacle Resets:** The CUT_TREE at (8, 25) in Ilex Forest reappeared after I left the map and returned. This suggests some environmental obstacles might reset upon re-entry.
- **Environmental Obstacle Resets:** The CUT_TREE at (8, 25) in Ilex Forest reappeared after I left the map and returned. This suggests some environmental obstacles might reset upon re-entry.
- **CRITICAL DATA VERIFICATION:** My memory of game mechanics or map layouts can be flawed. I must always trust the raw Game State Information (Map Memory, Map Events) over my own assumptions. If a plan fails, the first step is to re-verify all assumptions against the game data.
- **Warp vs. Map Edge:** I must distinguish between formal warp tiles (like doors, listed in Map Events) and map edge transitions (walking off the map). Hallucinating a warp where a transition exists can cause validation errors and flawed navigation plans. Always verify against the `Map Events -> Warps` list.
- **Battle Anomaly:** A wild battle terminated unexpectedly. After pressing 'A' on the main battle menu's 'FIGHT' option, I was returned to the overworld without any battle resolution. The cause is unknown.
- **Evolution Methods:** Some POKéMON, like MACHOKE, KADABRA, HAUNTER, and GRAVELer, evolve when traded.

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
- Ground-type moves have no effect on Flying-type Pokémon.

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
- **PC**: An interactable object used to access the Pokémon Storage System and personal item storage. Impassable.
- **LADDER**: A traversable warp tile that moves the player between floors.
- **FLOOR_UP_WALL**: Confirmed impassable when trying to move onto it from an adjacent tile above. My previous hypothesis that it was a one-way ledge was a hallucination.
- **WARP_CARPET_RIGHT**: A traversable warp tile at the edge of a map that transitions to the adjacent map on the right. To activate, you must attempt to move right from the carpet tile, effectively trying to walk 'off' the map.
- **WARP_CARPET_UP**: A traversable warp tile at the edge of a map that transitions to the adjacent map above. Must move up to activate. Confirmed that moving from this tile to a FLOOR tile below it is possible, so it is not a one-way ledge.
- **WARP_CARPET_DOWN**: A traversable warp tile at the edge of a map that transitions to the adjacent map below. Must move down to activate.
- **unseen**: A tile that has not yet been explored. Its properties are unknown until visited.
- **BUOY**: An object found in water. Appears to be impassable, functioning like a WALL tile within a WATER area.
- **WARP_CARPET_LEFT**: A traversable warp tile at the edge of a map that transitions to the adjacent map on the left. To activate, you must attempt to move left from the carpet tile, effectively trying to walk 'off' the map.
- **TEACHER / LASS / BIRD / OFFICER / YOUNGSTER / POKEFAN_M**: These NPC objects are impassable and function as walls.
- **FRUIT_TREE**: An impassable, interactable object. Gives one BERRY item (like PRZCUREBERRY) when interacted with for the first time. Subsequent interactions yield nothing.
- **CAVE**: A traversable warp tile that functions as an entrance to a cave.
- **VOID**: An impassable tile type found at the edges of some maps, functions as a wall.
- **GRASS**: Fully traversable tile, similar to TALL_GRASS. Wild POKéMON can be encountered here.
- **FLOWER**: Fully traversable decorative tile.
- **SIGN**: An impassable, interactable object. Functions as a wall.
- **To interact with objects** like ladders, signs, or switches, you must be standing on an adjacent tile and facing the object. Attempting to interact while standing *on* the object itself will fail.
- **Route 30's one-way ledges** (`LEDGE_HOP_DOWN`) make northbound travel from Cherrygrove City impossible. The route is effectively a one-way path when traveling south from Route 31. This is a critical piece of information for future navigation planning.
- **Verify Warp Coordinates:** Before setting a navigation goal that is a warp, I must verify its existence and coordinates in the 'Map Events -> Warps' list for the current map to avoid hallucinations and failed pathing.
- **Tool Logic Consistency:** When debugging, ensure that fixes are applied consistently across all relevant parts of the code. My `find_path` tool failed repeatedly because I fixed an 'unseen' tile check in one part of the algorithm but missed an identical flaw in another. A partial fix is not a fix.
- **SUPER_NERD**: Impassable NPC, functions as a wall.
- **`stun_npc` Tool:** The `stun_npc` tool can be effective for freezing moving NPCs to clear a path, as demonstrated with the Lass in Goldenrod City. While a previous attempt seemed to fail, this successful use case confirms its utility. It should be used proactively to prevent pathing interruptions.
- **Pathing to Impassable Objects:** When using a pathfinding tool to navigate to an impassable object (like an NPC, sign, or vending machine), the target coordinates must be a valid, traversable tile *adjacent* to the object, not the object's tile itself.
- **Warp Verification:** My navigation goals for warps can be hallucinations. I must always verify a warp's existence and coordinates against the 'Map Events -> Warps' list for the current map before setting it as a goal to avoid validation errors and failed plans.
- **PLANT**: A decorative object that functions as an impassable WALL tile.

# Current Quest: Journey to Ecruteak City
- **Objective:** Obtain the Fog Badge from the Ecruteak City Gym Leader.
- **Status:** Just defeated Whitney in Goldenrod. Need to heal at the Pokémon Center, then get the SQUIRTBOTTLE from the Flower Shop to clear the path on Route 36.

# Key Items
- **HIVEBADGE:** From Bugsy. Allows traded POKéMON up to L30 to obey and enables the use of CUT outside of battle.
- **POKéDEX:** A high-tech encyclopedia from PROF. OAK to record POKéMON data.
- **HM05 FLASH:** Obtained from the Elder of Sprout Tower. Illuminates dark caves. Requires the Zephyr Badge to use outside of battle.
- **HM01 CUT:** Obtained from the charcoal maker in Ilex Forest. Allows cutting small trees outside of battle. Requires the Hive Badge.
- **PLAINBADGE:** From Whitney. Boosts POKéMON's Speed and allows the use of STRENGTH outside of battle.

# TMs
- **TM02 HEADBUTT:** Received from a Rocker in Ilex Forest. Can be used to shake trees and find sleeping Pokémon.
- **TM12 SWEET Scent**
- **TM31 MUD-SLAP**
- **TM39 SWIFT**
- **TM45 ATTRACT**
- **TM49 FURY CUTTER**
- **TM08 ROCK SMASH:** Received from a man on Route 36 after defeating the Sudowoodo.

# NPC Dialogue
- **POKEFAN_M in Violet City House:** Traded Pokémon grow quickly but may disobey without the correct Gym Badge.
- Received MIRACLE SEED from a trainer on Route 32.
- **FIREBREATHER WALT on Route 35:** Said "I'm practicing my fire breathing." despite appearing as a FISHER sprite. Likely a Fire-type trainer.
- A POKEFAN_M in the Game Corner lost his COIN CASE in the UNDERGROUND. This is likely required to play the games.
- **Route 34 Gatehouse:** A Lass at (3, 5) mentioned a shrine in Ilex Forest honoring a 'protector' that 'watches over the FOREST from across time' and is likely a Grass-type POKéMON.
- **POKEFAN_F in Bill's House (Goldenrod):** Her son, BILL, is an expert on Pokémon and is at the Pokémon Center in ECRUTEAK CITY. Her husband is at the GAME CORNER.
- **LASS on Goldenrod Dept. Store 5F:** A lady gives away TMs on Sundays.
- **Scientist in Ruins of Alph Research Center:** Confirmed that the appearance of Pokémon in the ruins is a recent and incredible discovery that needs investigation. The UNOWN Pokémon are very similar to the drawings on the walls of the ruins, implying there are many different kinds.
- **Computer in Ruins of Alph Research Center:** Displays 'RUINS OF ALPH Exploration Year 10'.
- **Bookshelf at (6, 5) in Ruins of Alph Research Center:** contains books titled "Ancient Ruins…" and "Mysteries of the Ancients…".
- **Youngster in Route 32 Gatehouse:** Mentioned trying to move the stone panels in the ruins, wondering what they are.
- **Officer in Route 32 Gatehouse:** Said "RUINS OF ALPH".
- **Route 32 Sign at (13, 5):** Reads 'ROUTE 32, VIOLET CITY - AZALEA TOWN'.

# Crafting
- Kurt in Azalea Town can make special POKé BALLS from APRICORNS. I received a LURE BALL from him as an example.

# Puzzle Solutions
## Azalea Gym
- Gym Guide: The Gym Leader is BUGSY. His Bug POKéMON are weak to Fire and Flying-type moves.
- **Solution:** The gym puzzle involves finding two hidden floor switches. The first, located on the path to the right-side trainer, makes a new trainer appear on the left side. The second, on the path to the left-side trainer, makes another new trainer appear. The path to these trainers is not blocked by the Twins in the middle; it is possible to walk around the bottom of the gym. Defeating all trainers is not required to reach Bugsy.

## Goldenrod Department Store
- **Elevator:** The elevator is controlled by the panel at (3, 0). Interacting with the panel brings up a floor selection menu. After selecting a floor, you must walk onto the corresponding warp carpet to travel. The warp to B1F is at (1, 3) and the warp to 1F is at (2, 3).
- **B1F Box Puzzle:** My own movement is causing changes in the a map layout. A WALL at (5, 10) changed to a FLOOR after I moved. The Machop at (7, 7) is likely the key to solving the puzzle. The previous solution of leaving and returning the room seems to be only a partial trigger.

## Goldenrod Gym
- Gym Guide: This is a Normal-type gym. Fighting-type POKéMON are recommended.
- **Puzzle Mechanic:** The gym puzzle is solved by walking along the outer perimeter of the entrance room. The direction and sequence of these walks cause different trainers to appear and disappear, opening and closing paths. The correct sequence of perimeter walks and trainer battles is required to open the path to the main gym area.

## Goldenrod Underground Switch Room Puzzle
- **Failed Hypothesis:** The puzzle is solved by repeatedly entering and exiting the 'GoldenrodUndergroundSwitchRoomEntrances' area to cycle through different room configurations. (Failed after 5+ attempts, triggered a loop warning).
- **New Hypothesis:** The puzzle requires accessing the switch rooms from a different path. The main underground connects the north and south city entrances. I will re-enter the underground from the southern entrance in Goldenrod City and explore the lower level again, as my path was previously blocked and new events (Granny NPC) may have occurred.
- **Agent Hypothesis #1 (Full Traversal):** FAILED. Attempted to walk from the north entrance to the south entrance. Path was blocked by a SUPER_NERD at (3, 27) that appears only in the 'north entrance' configuration. This confirms a simple traversal is impossible.
- **Agent Hypothesis #2 (Defeat All Trainers):** FAILED. The SUPER_NERD at (3, 27) that blocks the path does not initiate a battle, only dialogue. This makes defeating all trainers impossible in this configuration.
- **Agent Hypothesis #3 (In-and-Out Ladders):** FAILED for northern ladder (3, 2). The blocking SUPER_NERD at (3, 27) did not move. Will proceed to test other accessible ladders.

## Ruins of Alph - Kabuto Chamber Puzzle
- **Clue:** "A POKéMON that hid on the sea floor. Eyes on its back scanned the area."
- **Solution:** The image is KABUTO.

# Obstacles and Solutions
- A strange tree blocks the road north of Goldenrod City (Route 35). It can be cleared using a SQUIRTBOTTLE, which is obtained from the Flower Shop after defeating Whitney. The Lass in the shop confirms this is the correct sequence of events.

# Held Items
- **QUICK CLAW:** Received from a Teacher in the National Park. When held by a Pokémon, it may allow them to attack first in battle.

# PC Inventory
- **Box 1:**
  - Hestia (MAGBY), Lv15, Female

# Automation Suite
## Built-in Tools
- `notepad_edit`: Edits the persistent notepad.
- `run_code`: Executes single-use Python code.
- `define_map_marker` / `delete_map_marker`: Manages map markers for data hygiene.
- `stun_npc`: Freezes NPCs to assist with pathing and interaction.
- `select_battle_option`: Selects main battle menu options (FIGHT, PKMN, PACK, RUN).
- `define_agent` / `delete_agent`: Manages custom reasoning agents.
- `define_tool` / `delete_tool`: Manages custom Python tools.
## Custom Tools (via `define_tool`)
- `find_path`: Finds a path from a start to an end coordinate on the current map.
- `select_item`: Automates selecting a specific item from the bag menu.
- `select_move`: Selects a move from the battle menu by name.
- `switch_pokemon`: Automates switching to a specific Pokémon in the party during a battle.
- `verify_reachability`: Checks a list of coordinates to see which are reachable from the player's current position.
## Custom Agents (via `define_agent`)
- `gym_puzzle_solver`: Generates simple, testable hypotheses for gym puzzles.
- `python_code_debugger`: Analyzes and corrects faulty Python scripts.

# Phone Calls
- Hiker ANTHONY (Route 33) has called multiple times for rematches and mentioned that timid DUNSPARCE can be found in DARK CAVE, away from stronger POKéMON.
- Youngster JOEY called for a rematch on Route 30. He also called to brag about his RATTATA and that he defeated a wild SPINARAK and a wild HOOTHOOT.

# Tool Development Lessons
- **Case-Insensitive Parsing:** When creating tools that parse UI text (like item or move names), all string comparisons must be made case-insensitive (e.g., by converting both strings to uppercase). The game's text can have subtle capitalization differences (like 'POKé BALL' vs 'POKÉ BALL') that will cause case-sensitive logic to fail catastrophically.
- **Pathing Over Warps:** Pathfinding tools must not treat all warp tiles as non-traversable. Some warps, like multi-tile WARP_CARPETS, are part of a valid path and must be treated as regular floor tiles unless they are the final destination.

# Ilex Forest
- **Objective:** Traverse the forest to reach Route 34.
- **Path:** The entrance is from Azalea Town, and the exit is at (1, 5).