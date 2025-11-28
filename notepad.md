# Core Principles
- **TRUST THE GAME STATE OVER MEMORY:** After experiencing severe hallucinations, it is a critical, non-negotiable directive to always trust the raw Game State Information as the absolute source of truth. My own memory or interpretation of events is unreliable and must be discarded if it contradicts the game state. My hierarchy of truth is: 1) Raw Game State, 2) Verified Tool Outputs, 3) My own interpretation (least reliable).

# Strategic Principles & Lessons Learned
- **TRUST, BUT VERIFY: THE HIERARCHY OF TRUTH:** My own memory and visual assessment are unreliable and prone to hallucinations. I must operate under a strict hierarchy of truth: 1) Raw Game State Information is the absolute, unquestionable source of truth. 2) The output of verified, trusted tools (like pathfinders) is the next most reliable source, as they analyze the raw data. 3) My own interpretation is the least reliable and must ALWAYS be challenged and verified against the game state data before acting. If a tool's output contradicts my visual assessment, the tool is correct until proven otherwise by direct in-game evidence.
- **EXECUTION DISCIPLINE:** A plan is useless if not executed. I must ensure my actions perfectly match the plan articulated in my thoughts. I must always call the correct, existing tools for their intended purpose.
- **IMMEDIATE DATA & TOOL MAINTENANCE:** My absolute highest priority is maintaining a perfect, up-to-the-second internal state. Any task I decide on—adding, deleting, or fixing an agent, tool, marker, or notepad entry—MUST be performed in the CURRENT turn. This task is more important than any in-game action and must never be deferred. If a tool is flawed, a better one can be conceived, or it contradicts reality, fixing or creating it is the top priority, superseding all other objectives.
- **VERIFY POSITION & SEPARATE INPUTS:** After any interruption (battle, menu, etc.) and before any action, I MUST verify my current `(x, y)` coordinates in the Game State Information. I must NEVER mix directional inputs (Up, Down, Left, Right) and action inputs ('A', 'B') in the same turn. Movement/turning must happen in one turn, and interaction in the next.
- **DEFAULT TO AUTOMATION:** If a custom tool or built-in function exists for a task, I MUST use it by default instead of performing the action with manual button presses. Manual inputs are less efficient and more error-prone.
- **MAP MARKER & DATA HYGIENE:** Maintaining an accurate world model is a critical, non-negotiable priority. 1) **Consult First:** Before any interaction or navigation, I MUST consult my map markers to avoid repeating actions or making routing errors based on old information. 2) **Link Immediately:** When creating a marker for an object, it MUST be linked to its `object_id` immediately. 3) **Update Promptly:** Markers must be updated immediately after an event (e.g., marking a trainer as 'defeated' with ☠️, deleting markers for collected items with ✅). Old markers must be deleted when new ones are created for the same object. 4) **Handle Stale Data:** If an object with a linked marker moves off-screen, the marker becomes stale and must be deleted. A new marker should only be created if the object reappears.
- **Agent Escalation for Debugging:** If I am struggling to debug a tool manually after a few attempts, I MUST escalate to the `python_code_debugger` agent. It can often identify logical flaws more quickly and efficiently than I can.
- **UI Automation Timing:** When automating UI interactions, simple button sequences can fail due to game engine lag or animation timing. Incorporate 'sleep' commands to ensure the UI is in the expected state before the next input is sent.
- **Tool Definition Errors:** If `define_tool` fails with an 'identical script' error, it means the proposed change has already been successfully applied in a previous turn. Do not retry the same definition; proceed with the next action.
- **NPC Interactions:** Some interactions, like battling a trainer, can be multi-step. Ensure all initial dialogue is cleared with 'A' presses before the main event (like the battle) will trigger. Non-Battling NPCs: Not all moving NPCs are trainers. If an NPC's dialogue repeats without initiating a battle after multiple interaction attempts (direct, line-of-sight), they are likely a non-battling character. Do not get stuck in an interaction loop; update markers and move on.
- **Pathfinding Logic:** If a path is repeatedly blocked or a tool reports 'No path found,' do not assume you are soft-locked. Re-examine the map visually for alternative routes like ledges or other one-way tiles that may have been missed.
- **Dialogue & Movement:** I must ensure all dialogue boxes are closed by pressing 'A' before attempting any movement inputs. Trying to move with text on screen will fail.
- **Agent-based fixes must be verified in both simple and complex scenarios before a tool is considered fully functional. A fix for one case may not cover all failure conditions.
- **Problem-Solving Escalation:** When stuck on a puzzle after exhausting simple, self-generated hypotheses, I must escalate to a more powerful problem-solving tool, such as my custom agents. Repeating failed attempts is inefficient.
- **Exploration Before Puzzles:** Prioritize exploring all reachable areas of a new map before attempting complex puzzles to ensure all context and potential clues have been gathered.
- **Tool Input Verification:** Before concluding a tool is broken (e.g., `find_path` returning 'No path found'), I must first verify that my inputs and assumptions are correct. Pathing to an 'unseen' tile is an invalid input, as the tool correctly treats them as impassable. My strategy must adapt to the tool's logic.
- **Random Chance Strategy:** If a strategy based on random chance (like waiting for moving NPCs) fails repeatedly (3+ times), I must switch to a deterministic strategy (like proactively stunning them in favorable positions).
- **Agent Escalation:** When multiple self-generated hypotheses for a puzzle have failed, especially after getting stuck in a repetitive loop (like the stun-gun strategy), I must escalate to a more powerful problem-solving tool like an agent. Even if the agent's initial suggestions are not the final solution, they serve the critical purpose of breaking cognitive fixation and forcing a re-evaluation of the problem's root assumptions.
- **Herding Puzzles:** Interacting with an object (like the Farfetch'd) from an adjacent tile can trigger movement along a complex, pre-determined path, not just simple repulsion. The direction of approach is the key trigger.
- **Visual Path Verification:** Before executing a move, I must visually confirm the path on the ASCII map and game screen to avoid simple navigational errors like walking into walls. This supplements tool-based pathfinding.
- **Debugging Cycle Avoidance:** When a core tool repeatedly fails despite multiple fixes, the core algorithm is likely fundamentally flawed. I must avoid getting stuck in a loop of incremental, failing changes. The correct approach is to either replace the logic with a known-working version from another tool or re-implement it from first principles, rather than continuing with minor tweaks.
- **Puzzle State Changes:** Some puzzles, like the Goldenrod Dept. Store basement, may change their state based on triggers that are not immediately obvious, such as leaving and re-entering the area. If internal solutions fail, I must consider external actions as potential triggers.
- **Interaction vs. Line of Sight:** If direct interaction with a trainer-like NPC results in a dialogue loop, the battle trigger is likely entering their line of sight. If both methods fail, they may not be a battlable trainer.
- **Positional Awareness:** Always verify my own coordinates and the coordinates of relevant NPCs before using a targeted tool like `stun_npc`. Wasting a turn on an unnecessary action is a failure of observation.
- **Notepad Edit Precision:** When using `notepad_edit` with the `replace` action, the `old_text` must be an exact match. If an edit fails because the text is not found, it's possible the change was already successfully applied in a previous turn. Verify the current notepad content before retrying.
- **Blocked Movement vs. Battle Start:** A 'Movement Blocked' alert does not guarantee a wild battle has started. I must wait for the battle screen text to appear before assuming I am in a battle and pressing 'A' to advance dialogue. This prevents wasted turns from incorrect assumptions.
- **Struggle Mechanic Failure:** Repeatedly selecting a 0 PP move does not trigger Struggle in this game. If a Pokémon runs out of PP, the only viable options are to switch out or use an item. Do not get stuck in a loop trying to force Struggle.
- **Proactive Automation:** I must not wait until a manual task becomes a major bottleneck before automating it. If I identify any repetitive, complex, or error-prone manual action, creating a tool or agent to handle it becomes an immediate high-priority task, superseding non-critical gameplay actions. Deferring automation is a strategic failure.
- **Resource Management:** Avoid inefficient battles (e.g., against high-defense, low-EXP opponents) that drain PP for minimal gain. Running away is often the more strategic option to conserve resources for more important fights or exploration.
- **Warp Carpet Anomaly:** The `WARP_CARPET_DOWN` tile at Union Cave (17, 3) was confusing. A manual 'Down' press failed due to a wall, but an automated path through the same tile succeeded in warping me. The exact mechanic is unclear and needs further investigation.
- **Tool Context Awareness:** Tools like `select_battle_option` are context-specific and will fail if used when the required UI (e.g., the main battle menu) is not visible. Always verify the game state before calling a context-dependent tool.
- **Type Disadvantage Switching:** When a Pokémon is facing an opponent with a significant type advantage (e.g., Rock/Ground vs. Fighting), switching out is not just an option, it's a critical necessity to avoid taking massive damage or being knocked out. Preserving HP is key.
- **Interaction Pre-check:** Before pressing 'A' to interact with any NPC or object, I must first perform a pre-check: verify my character is standing on an adjacent tile AND is facing the target directly. Wasting a turn on a failed interaction due to poor positioning is a critical error.
- **Proactive Stunning:** To avoid wasting turns on failed interactions with moving NPCs, the default strategy must be to use `stun_npc` to freeze them in place *before* attempting to approach and talk to them.
- **Pathing Interruption:** Even short, automated paths can be interrupted by moving NPCs. Proactive stunning is the most reliable strategy to ensure path execution and successful interaction.
- **IMMEDIATE TOOL MAINTENANCE (Addendum):** Do not defer tool fixes. If a tool breaks in a specific context (like a battle menu), I must stay in that context and fix it immediately, even if it means taking damage or losing a turn. The context is critical for debugging and is lost once I leave.
- **Ilex Forest Path:** The entrance is from Azalea Town, and the exit is at (1, 5).
- **Movement Loop Breaking:** When stuck in a movement loop or repeatedly blocked, changing the immediate navigation target is an effective strategy to break the cycle and find a new, clear path.
- **Interaction Loops:** If repeated 'A' presses (2-3 times) on an NPC or object do not advance the game state (dialogue, battle start, etc.), the interaction is likely stuck. Do not continue pressing 'A'. Break the loop by performing a different action, such as moving one tile away and back, to reset the state before attempting to interact again.
- **VERIFY ALL WARPS:** Before setting a navigation goal to a warp, I MUST first confirm its existence and coordinates in the `Game State Information -> Map Events -> Warps` list. My visual assessment or memory can be wrong.
- **CONSULT YOUR KNOWLEDGE BASE:** My notepad contains critical, verified information about game mechanics (like impassable tiles). I MUST consult this knowledge base *before* attempting an action to avoid repeating solved problems and wasting turns on impossible movements, as seen with the COUNTER tile incident.
- **TRUST THE GAME STATE OVER MEMORY:** After experiencing severe hallucinations (e.g., battling a non-existent trainer, being in the wrong location), it is a critical, non-negotiable directive to always trust the raw Game State Information as the absolute source of truth. My own memory or interpretation of events is unreliable and must be discarded if it contradicts the game state.
- **One-Way Warps:** Some warps, especially holes in the floor, may be one-way exits. If simple interaction methods (stepping on, pressing 'A', pressing a direction) fail repeatedly, assume it is an exit or requires a complex external trigger. Do not get stuck testing simple interactions.

# Game Mechanics & Systems
- The Day/Night cycle is an important mechanic in this game, affecting events.
- Received 5 POKé BALLS from the scientist in Elm's Lab. I can now catch wild Pokémon.
- The PC in Pokémon Centers is used for Pokémon and item storage.
- BERRY trees grow new BERRIES every day.
- Healing at a Pokémon Center restores all HP and PP for the entire party and cures any status conditions.
- **Game State Updates:** The game's internal map data (like a `CUT_TREE` changing to a `FLOOR`) does not fully update until all on-screen text from the preceding action is cleared. Attempting to use tools like `find_path` before the overworld is fully interactive will result in the tool using stale data and failing.
- **HEADBUTT Mechanic:** The move HEADBUTT can be used outside of battle to shake certain trees (`HEADBUTT_TREE` tiles). This can cause sleeping Pokémon to fall out, providing a new method for encounters.
- **Environmental Obstacle Resets:** The CUT_TREE at (8, 25) in Ilex Forest reappeared after I left the map and returned. This suggests some environmental obstacles might reset upon re-entry.
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
- **Type Anomaly:** Normal-type moves (like CUT) are not very effective against Water/Rock-types (like CORSOLA). This is a unique mechanic to this game.

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
- **SUPER_NERD**: Impassable NPC, functions as a wall.
- **Pathing to Impassable Objects:** When using a pathfinding tool to navigate to an impassable object (like an NPC, sign, or vending machine), the target coordinates must be a valid, traversable tile *adjacent* to the object, not the object's tile itself.
- **PLANT**: A decorative object that functions as an impassable WALL tile.
- **INCENSE_BURNER**: An impassable decorative object.
- **To interact with NPCs behind counters** (like Nurses or Clerks), you must face the counter tile directly in front of them, not the NPC tile itself, and then press A.
- **FENCE (Visual):** The fence-like structure on Route 38 at (30, 11) is functionally an impassable `WALL` tile. Confirmed by attempting to move onto it.
- **BROKEN_FLOOR**: Not yet encountered. Previous note about it being in the Burned Tower was likely a hallucination.

# Current Quest: Journey to Olivine City
- **Objective:** Investigate the sick Pokémon at the Olivine Lighthouse.
- **Status:** I am in Ecruteak City and have determined that I am currently blocked from progressing in the Burned Tower. My only other lead is the rumor about a sick Pokémon in Olivine City.

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
- **GRAMPS in Route 36 Gatehouse:** Mentioned the strange tree was the reason fewer people were visiting the RUINS OF ALPH.
- **FISHER on Ecruteak City (9, 22):** Heard a rumor that the Pokémon at the Olivine Lighthouse is sick.
- **Fisher in Olivine Pokémon Center:** A sailor in the Olivine Cafe next door can teach the move STRENGTH, which can move big boulders.

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

## Olivine Lighthouse 1F Warp Puzzle
- **Summary:** The warp on 1F at (16, 13) and (17, 13) is not triggered by any simple, internal mechanic.
- **Exhausted Hypotheses:**
  - Direct interaction ('A' button).
  - Stepping on the tiles from all valid cardinal directions.
  - Continuous movement across both tiles (west-to-east and east-to-west).
  - Changing facing direction while on the tiles.
  - The wandering NPC's position (tested randomly and systematically).
  - Interacting with the NPC.
  - A full systematic sweep of every floor tile to find an invisible switch.
- **Conclusion:** Having exhausted all internal triggers, the solution must be external to this room. I must explore Olivine City for a clue, item, or NPC to progress.

# Obstacles and Solutions
- A strange tree blocks the road north of Goldenrod City (Route 35). It can be cleared using a SQUIRTBOTTLE, which is obtained from the Flower Shop after defeating Whitney. The Lass in the shop confirms this is the correct sequence of events.

# Held Items
- **QUICK CLAW:** Received from a Teacher in the National Park. When held by a Pokémon, it may allow them to attack first in battle.

# PC Inventory
- **Box 1:**
  - Hestia (MAGBY), Lv15, Female

# Tool Development Lessons
- **Case-Insensitive Parsing:** When creating tools that parse UI text (like item or move names), all string comparisons must be made case-insensitive (e.g., by converting both strings to uppercase). The game's text can have subtle capitalization differences (like 'POKé BALL' vs 'POKÉ BALL') that will cause case-sensitive logic to fail catastrophically.
- **Pathing Over Warps:** Pathfinding tools must not treat all warp tiles as non-traversable. Some warps, like multi-tile WARP_CARPETS, are part of a valid path and must be treated as regular floor tiles unless they are the final destination.
- **Warp vs. Map Edge:** I must distinguish between formal warp tiles (like doors, listed in Map Events) and map edge transitions (walking off the map). Hallucinating a warp where a transition exists can cause validation errors and flawed navigation plans. Always verify against the `Map Events -> Warps` list.
- **Pathing into the Unknown:** Pathfinding tools (`find_path`, `verify_reachability`) correctly treat 'unseen' tiles as impassable walls. This is a feature, not a bug. To explore, I must pathfind to a known, adjacent tile and then manually step into the unseen area. This prevents the tool from generating invalid paths through unexplored territory.
- **Pathing Interruption:** Automated paths can be interrupted by wild battles. After the battle, the original path is void and must be recalculated from the new current position.
- **Tool Output for Autopress:** When a custom tool has `autopress_buttons: true`, its `print()` output MUST be a valid JSON array of strings. Any other text, such as debug statements, will corrupt the output and cause a JSON parsing error.
- **Tool Debugging Logic:** When a tool fails repeatedly in a predictable way (e.g., always selecting the wrong item), the problem is likely a core logic or syntax error, not a simple timing issue. I must investigate the code itself rather than just tweaking parameters like sleep timers.
- **Tool Robustness:** Tools must be written to handle all likely edge cases. A tool failing because a target is already selected indicates a lack of robust design. Fixing such flaws immediately is critical to maintaining automation efficiency.
- **Agent UI Parsing Warning:** Agents can hallucinate the structure of a UI when parsing it from screen text. I must always verify an agent's core assumptions about the UI layout before trusting its code. Simple, robust parsing methods that rely on stable structural elements are superior to complex, brittle ones that rely on variable content.
- **Agent Code Verification:** Agent-provided code, especially for UI parsing, must be critically scrutinized. The agent may hallucinate UI elements or structure (e.g., PP counters on the same line as a move name). Always verify the agent's core assumptions against direct observation of the screen text before implementing its code. Simple, observation-based logic is often more robust and reliable.
- **Inventory-Aware Tools:** Any tool designed to interact with a player's inventory (like `select_item`) MUST parse the *current, visible* inventory from the screen text. Relying on a hardcoded, complete list of all possible items in the game is a fundamental design flaw, as it does not reflect the player's actual possessions and will lead to catastrophic pathfinding and selection errors.
- **Tool Integrity:** If a tool is broken, I must fix it immediately. Manually performing the tool's intended action is a violation of the 'Default to Automation' principle and indicates a critical failure that must be addressed before any other action.
- **Debugging Escalation:** When a tool repeatedly fails in a predictable way, the problem is likely a core logic or syntax error, not a simple timing issue. Escalate complex debugging to specialized agents (like `python_code_debugger`) promptly instead of attempting prolonged manual fixes.

# Hallucinations & Corrections
- **Olivine Lighthouse Staircase:** I hallucinated that the staircase at (8, 12) was a warp tile. The game state confirmed it is a WALL. The actual entry point is likely an adjacent traversable tile, such as (8, 11). This is a critical reminder to always trust game state data over visual interpretation.

# Tile & Object Mechanics
- **DOOR**: A traversable warp tile leading into or out of a building.
- **BUOY**: An object found in water. Appears to be impassable, functioning like a WALL tile within a WATER area.

# Strategic Principles & Lessons Learned
- **Warp Loop Anomaly:** The warp at Olivine City (19, 27) creates a confusing loop by repeatedly sending me to the Port Passage. If a warp behaves unexpectedly, I must mark it as problematic and investigate alternative routes immediately rather than getting stuck in a repetitive cycle.