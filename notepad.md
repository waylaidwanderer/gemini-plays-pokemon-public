# CRITICAL DIRECTIVE: ANTI-HALLUCINATION PROTOCOL
- My memory is unreliable. The Game State Information is the absolute source of truth.
- I MUST verify my `current_map_id` and `current_position` from the Game State Information before EVERY single action, especially before using coordinate-based tools or setting navigation goals.
- I MUST verify a warp's existence in the `Game State Information -> Map Events -> Warps` list before assuming it's a valid warp.
- Failure to adhere to this protocol is the root cause of all major strategic failures and wasted turns.

# Strategic Protocol
- **KNOWLEDGE-DRIVEN STRATEGY (PRIMARY DIRECTIVE):** My own visual assessment and memory are unreliable. I MUST trust my documented knowledge (map markers, notepad) and verified tool outputs (`find_path`) over my own intuition. A 'No path found' result is valuable, correct data, not a tool failure. I MUST consult this knowledge base before EVERY navigational decision to avoid re-exploring confirmed dead ends or repeating solved puzzles. This is my most critical failure point.
- **PLAN-EXECUTE-VERIFY CYCLE:**
  1. **CONSULT KNOWLEDGE BASE:** Before forming ANY plan, I MUST consult my notepad and map markers to avoid repeating mistakes or ignoring solved puzzles.
  2. **METHODICAL EXPLORATION:** When arriving in a new or isolated area (especially via a one-way path), I MUST systematically explore every single reachable tile before using any exits to avoid missing hidden paths or triggers.
- **PROACTIVE OBSTACLE MANAGEMENT:** When a plan is repeatedly interrupted by a variable element (like a moving NPC), I must immediately switch to a deterministic strategy (like using `stun_npc`) instead of retrying the same failed approach. Deferring this is a strategic failure.
- **Tool Definition Errors:** If `define_tool` fails with an 'identical script' error, it means the proposed change has already been successfully applied in a previous turn. Do not retry the same definition; proceed with the next action.
- **NPC Interactions:** Some interactions, like battling a trainer, can be multi-step. Ensure all initial dialogue is cleared with 'A' presses before the main event (like the battle) will trigger. Non-Battling NPCs: Not all moving NPCs are trainers. If an NPC's dialogue repeats without initiating a battle after multiple interaction attempts (direct, line-of-sight), they are likely a non-battling character. Do not get stuck in an interaction loop; update markers and move on.
- **Pathfinding Logic:** If a path is repeatedly blocked or a tool reports 'No path found,' do not assume you are soft-locked. Re-examine the map visually for alternative routes like ledges or other one-way tiles that may have been missed. Long automated paths are unreliable due to off-screen and moving NPCs; break them into smaller, visually confirmed segments.
- **Dialogue & Movement:** I must ensure all dialogue boxes are closed by pressing 'A' before attempting any movement inputs. Trying to move with text on screen will fail.
- **Agent-based fixes must be verified in both simple and complex scenarios before a tool is considered fully functional. A fix for one case may not cover all failure conditions.
- **Exploration Before Puzzles:** Prioritize exploring all reachable areas of a new map before attempting complex puzzles to ensure all context and potential clues have been gathered.
- **Tool Input Verification:** Before concluding a tool is broken (e.g., `find_path` returning 'No path found'), I must first verify that my inputs and assumptions are correct. Pathing to an 'unseen' tile is an invalid input, as the tool correctly treats them as impassable. My strategy must adapt to the tool's logic.
- **Random Chance Strategy:** If a strategy based on random chance (like waiting for moving NPCs) fails repeatedly (3+ times), I must switch to a deterministic strategy (like proactively stunning them in favorable positions).
- **Herding Puzzles:** Interacting with an object (like the Farfetch'd) from an adjacent tile can trigger movement along a complex, pre-determined path, not just simple repulsion. The direction of approach is the key trigger.
- **Visual Path Verification:** Before executing a move, I must visually confirm the path on the ASCII map and game screen to avoid simple navigational errors like walking into walls. This supplements tool-based pathfinding.
- **Puzzle State Changes:** Some puzzles, like the Goldenrod Dept. Store basement, may change their state based on triggers that are not immediately obvious, such as leaving and re-entering the area. If internal solutions fail, I must consider external actions as potential triggers.
- **Interaction vs. Line of Sight & Flawed Assumptions:** If direct interaction with a trainer-like NPC results in a dialogue loop (like with Sailor Huey), the battle trigger might be line of sight. However, I must first challenge the root assumption that a battle is necessary at all. I wasted significant time trying to force an interaction when a simple path around the NPC existed. Lesson: Always verify if an obstacle is truly blocking the path before attempting to resolve it through complex interactions or battles. Check for alternative routes first.
- **Positional Awareness:** Always verify my own coordinates and the coordinates of relevant NPCs before using a targeted tool like `stun_npc`. Wasting a turn on an unnecessary action is a failure of observation.
- **Notepad Edit Precision:** When using `notepad_edit` with the `replace` action, the `old_text` must be an exact match. If an edit fails because the text is not found, it's possible the change was already successfully applied in a previous turn. Verify the current notepad content before retrying.
- **Blocked Movement vs. Battle Start:** A 'Movement Blocked' alert does not guarantee a wild battle has started. I must wait for the battle screen text to appear before assuming I am in a battle and pressing 'A' to advance dialogue. This prevents wasted turns from incorrect assumptions.
- **Struggle Mechanic Failure:** Repeatedly selecting a 0 PP move does not trigger Struggle in this game. If a Pokémon runs out of PP, the only viable options are to switch out or use an item. Do not get stuck in a loop trying to force Struggle.
- **Proactive Automation:** I must not wait until a manual task becomes a major bottleneck before automating it. If I identify any repetitive, complex, or error-prone manual action, creating a tool or agent to handle it becomes an immediate high-priority task, superseding non-critical gameplay actions. Deferring automation is a strategic failure.
- **Resource Management:** Avoid inefficient battles (e.g., against high-defense, low-EXP opponents) that drain PP for minimal gain. Running away is often the more strategic option to conserve resources for more important fights or exploration.
- **Warp Carpet Anomaly:** The `WARP_CARPET_DOWN` tile at Union Cave (17, 3) was confusing. A manual 'Down' press failed due to a wall, but an automated path through the same tile succeeded in warping me. The exact mechanic is unclear and needs further investigation.
- **Type Disadvantage Switching:** When a Pokémon is facing an opponent with a significant type advantage (e.g., Rock/Ground vs. Fighting), switching out is not just an option, it's a critical necessity to avoid taking massive damage or being knocked out. Preserving HP is key.
- **Interaction Pre-check:** Before pressing 'A' to interact with any NPC or object, I must first perform a pre-check: verify my character is standing on an adjacent tile AND is facing the target directly. Wasting a turn on a failed interaction due to poor positioning is a critical error.
- **Pathing Interruption:** Even short, automated paths can be interrupted by moving NPCs. Proactive stunning is the most reliable strategy to ensure path execution and successful interaction.
- **Ilex Forest Path:** The entrance is from Azalea Town, and the exit is at (1, 5).
- **Movement Loop Breaking:** When stuck in a movement loop or repeatedly blocked, changing the immediate navigation target is an effective strategy to break the cycle and find a new, clear path.
- **Interaction Loops:** If repeated 'A' presses (2-3 times) on an NPC or object do not advance the game state (dialogue, battle start, etc.), the interaction is likely stuck. Do not continue pressing 'A'. Break the loop by performing a different action, such as moving one tile away and back, to reset the state before attempting to interact again.
- **One-Way Warps:** Some warps, especially holes in the floor, may be one-way exits. If simple interaction methods (stepping on, pressing 'A', pressing a direction) fail repeatedly, assume it is an exit or requires a complex external trigger. Do not get stuck testing simple interactions.
- **Warp Loop Anomaly:** The warp at Olivine City (19, 27) creates a confusing loop by repeatedly sending me to the Port Passage. If a warp behaves unexpectedly, I must mark it as problematic and investigate alternative routes immediately rather than getting stuck in a repetitive cycle.
- **Warp Activation Diversity:** Warps can be activated in multiple ways: step-on (ladders), interaction ('A' press), one-way drops (likely PITs), or by external triggers. I must test multiple methods before concluding a warp is inactive.
- **IMMEDIATE OBSTACLE MARKING:** I failed to mark Sailor Huey as a blocker, causing me to waste time retrying a failed path. All critical obstacles MUST be marked with '🚫' immediately upon discovery to prevent loops.
- **Trust NPC Guidance:** External NPC confirmation (like the Gym Guide directing me to the lighthouse) must override my own flawed assumptions or conclusions that a path is a dead end. I must re-investigate any such location with the new information.
- **Value of Brute-Force Automation:** When visually stuck, a systematic, automated search can reveal paths or triggers that are easily missed by manual exploration. It's a valid strategy for breaking through a perceived dead end.
- **External Triggers:** If all internal solutions to a puzzle are exhausted (e.g., the lighthouse entrance), the trigger is likely external. Do not get stuck in a loop; expand the search area.
- **Task Immediacy:** Deferred tasks are often forgotten. Actions like unstunning non-critical NPCs should be done immediately after the interaction is complete to maintain good state hygiene.
- **Trust Markers Over Tools:** If my map markers indicate a path is blocked by an NPC, I must trust that information over a `find_path` result, as the tool cannot see off-screen NPCs. Do not attempt to path through known blockades.
- **Immediate State Cleanup:** I must remember to perform immediate cleanup actions, like unstunning a non-critical NPC, as soon as the need for the stun is over. Deferring these tasks can lead to them being forgotten.
- **Tool Glitch Recovery:** If a tool repeatedly fails with a bizarre error despite the code appearing correct (like a `ModuleNotFoundError` for a valid library), force a re-definition of the tool with a new commit message to clear any cached or corrupted state.
- **Re-Exploration Strategy:** When all forward paths are confirmed dead ends, the solution may be in a previously visited area. Do not assume re-exploring is inefficient; a missed item, NPC, or trainer could be the key to progression.
- **Empty Gyms:** If a Gym Leader is absent, the gym itself might be empty and serve as a clue or trigger rather than a battle challenge. Full exploration is still necessary.
- **Internal Triggers:** When all external paths from a location are confirmed dead ends, the solution is likely an internal change within that area, triggered by a recent major event (like a key conversation).

# High Priority Task
- Fix the `find_path` tool. The `simple_path` tool is too unreliable as it doesn't account for objects. The main tool needs to be updated to correctly handle on-screen objects and complex warp tiles to prevent future pathing failures.

# Game Mechanics & Systems
- The Day/Night cycle is an important mechanic in this game, affecting events.
- Received 5 POKé BALLS from the scientist in Elm's Lab. I can now catch wild Pokémon.
- The PC in Pokémon Centers is used for Pokémon and item storage.
- BERRY trees grow new BERRIES every day.
- Healing at a Pokémon Center restores all HP and PP for the entire party and cures any status conditions.
- **Game State Updates:** The game's internal map data (like a `CUT_TREE` changing to a `FLOOR`) does not fully update until all on-screen text from the preceding action is cleared. Attempting to use tools like `find_path` before the overworld is fully interactive will result in the tool using stale data and failing.
- **HEADBUTT Mechanic:** The move HEADBUTT can be used outside of battle to shake certain trees (`HEADBUTT_TREE` tiles). This can cause sleeping Pokémon to fall out, providing a new method for encounters.
- **Environmental Obstacle Resets:** The CUT_TREE at (8, 25) in Ilex Forest reappeared after I left the map and returned. This suggests some environmental obstacles might reset upon re-entry.
- **Evolution Methods:** Some POKéMON, like MACHOKE, KADABRA, HAUNTER, and GRAVELer, evolve when traded.
- **Stun Reset & Off-Screen Failure:** The `stun_npc` effect resets when leaving and re-entering a map. The tool will fail if the target NPC is not currently on-screen and rendered in the game. The stun effect is also very short-lived, making long automated paths after stunning an NPC unreliable.
- **Battle Anomaly:** A recurring issue has been observed where interacting with some trainers (e.g., Sailor Huey, Gentleman Alfred, Youngster on Route 39) displays their pre-battle dialogue, but the game then returns to the overworld without initiating combat. This is inconsistent, as some of these trainers have been successfully battled on later attempts. If a battle fails to start after 1-2 attempts, mark the trainer as bugged and move on to avoid getting stuck in an interaction loop.
- **Item Interaction Mechanics:** To give an item to an overworld sprite (like the sick Miltank), I must interact with the sprite directly. Using the item from the PACK menu only works on my own POKéMON. The game may require a specific item type (e.g., a generic 'BERRY') and will not accept functionally similar but differently named items (e.g., 'BITTER BERRY').

# Tile & Object Mechanics
- **WALL**: Impassable terrain.
- **FLOOR**: A standard, fully traversable tile.
- **STAIRCASE**: A traversable warp tile that moves the player between floors.
- **TOWN_MAP**: An interactable object on a wall; impassable.
- **TV**: An impassable object.
- **BOOKSHELF**: An impassable object.
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
- **FLOOR_UP_WALL**: Confirmed impassable when trying to move onto it from an adjacent tile above. My previous hypothesis that it was a one-way ledge was a hallucination.
- **WARP_CARPET_RIGHT**: A traversable warp tile at the edge of a map that transitions to the adjacent map on the right. To activate, you must attempt to move right from the carpet tile, effectively trying to walk 'off' the map.
- **WARP_CARPET_UP**: A traversable warp tile at the edge of a map that transitions to the adjacent map above. Must move up to activate. Confirmed that moving from this tile to a FLOOR tile below it is possible, so it is not a one-way ledge.
- **WARP_CARPET_DOWN**: A traversable warp tile at the edge of a map that transitions to the adjacent map below. Must move down to activate.
- **unseen**: A tile that has not yet been explored. Its properties are unknown until visited. It is treated as impassable by pathfinding tools.
- **VOID**: An impassable tile type found at the edges of some maps, functions as a wall.
- **BUOY**: An object found in water. Appears to be impassable, functioning like a WALL tile within a WATER area.
- **WARP_CARPET_LEFT**: A traversable warp tile at the edge of a a map that transitions to the adjacent map on the left. To activate, you must attempt to move left from the carpet tile, effectively trying to walk 'off' the map.
- **TEACHER / LASS / BIRD / OFFICER / YOUNGSTER / POKEFAN_M**: These NPC objects are impassable and function as walls.
- **FRUIT_TREE**: An impassable, interactable object. Gives one BERRY item (like PRZCUREBERRY) when interacted with for the first time. Subsequent interactions yield nothing.
- **CAVE**: A traversable warp tile that functions as an entrance to a cave.
- **GRASS**: Fully traversable tile, similar to TALL_GRASS. Wild POKéMON can be encountered here.
- **FLOWER**: Fully traversable decorative tile.
- **SIGN**: An impassable, interactable object. Functions as a wall.
- **To interact with objects** like ladders, signs, or switches, you must be on an adjacent tile and facing the object. Attempting to interact while standing *on* the object itself will fail.
- **Route 30's one-way ledges** (`LEDGE_HOP_DOWN`) make northbound travel from Cherrygrove City impossible. The route is effectively a one-way path when traveling south from Route 31. This is a critical piece of information for future navigation planning.
- **SUPER_NERD**: Impassable NPC, functions as a wall.
- **Pathing to Impassable Objects:** When using a pathfinding tool to navigate to an impassable object (like an NPC, sign, or vending machine), the target coordinates must be a valid, traversable tile *adjacent* to the object, not the object's tile itself.
- **PLANT**: A decorative object that functions as an impassable WALL tile.
- **INCENSE_BURNER**: An impassable decorative object.
- **To interact with NPCs behind counters** (like Nurses or Clerks), you must face the counter tile directly in front of them, not the NPC tile itself, and then press A.
- **FENCE (Visual):** The fence-like structure on Route 38 at (30, 11) is functionally an impassable `WALL` tile. Confirmed by attempting to move onto it.
- **PIT**: Confirmed one-way warp tile in Olivine Lighthouse. Stepping on it causes the player to fall to the floor below. This is an environmental warp and will NOT appear in the official `Game State Information -> Warps` list.
- **LADDER**: Can function as a standard traversable tile (e.g., on a pier) or a warp tile. If it has a `<Warp>` child element in the map XML, it's a warp activated by stepping *onto* the tile. If not, it is simply a walkable surface. Context is key.
- **WINDOW**: An impassable object that can be interacted with to display text. Functions like a wall.

# Battle Mechanics
- Pokémon holding a BERRY can automatically use it to heal themselves when their HP gets low in battle.
- Poisoned Pokémon lose 1 HP every four steps outside of battle and remain poisoned after a wild battle concludes.
- Accuracy-lowering moves like SMOKESCREEN are not a guaranteed defense.
- The auto-activation threshold for a held BERRY is likely below 25% HP.
- A single high-level Pokémon cannot carry an entire under-leveled team through a major battle like a Gym.
- Levels Over Type Advantage: A significant level disparity can completely negate type advantages. My Lv8 ROCKY was one-shot by a move it should have resisted, proving that raw power from a higher level is a critical factor.
- Low-HP Threat: A low-HP Pokémon with a status move like Hypnosis is still a major threat. Prioritize eliminating it quickly, even if it means using a stronger Pokémon and not spreading EXP optimally, to avoid having the whole team disabled.
- Type Immunity vs. Level Disparity: Type immunity (e.g., Flying vs. Ground) is not a guaranteed defense against a much higher-level opponent. A significant level gap means the opponent can still knock out the immune Pokémon with its other, non-resisted moves.

## Type Effectiveness Chart (Verified)
| Attacking Type | Defending Type | Effectiveness |
| :--- | :--- | :--- |
| Grass | Fire | Not Very Effective |
| Normal | Ghost | No Effect |
| Normal | Rock | Not Very Effective |
| Flying | Rock | Not Very Effective |
| Fire | Rock | Not Very Effective |
| Ground | Flying | No Effect |
| Normal | Water/Rock | Not Very Effective |
| Rock | Flying | Super Effective |
| Rock | Bug | Super Effective |
| Water | Fire | Super Effective |
| Water | Rock | Super Effective |
| Water | Ground | Super Effective |

# Menu Navigation
- For complex menu inputs (like on-screen keyboards), perform all directional movements in one turn and the final confirmation ('A' button) in the next. Do not mix directional and action buttons in the same input sequence to avoid errors.
- In the party screen, the 'SWITCH' option is used to reorder Pokémon. The 'MOVE' option is for reordering a Pokémon's moves. Confusing these leads to menu loops.
- The main battle menu options are laid out in a 2x2 grid: FIGHT (top-left), PKMN (top-right), PACK (bottom-left), RUN (bottom-right). Navigating from FIGHT requires 'Right' for PKMN and 'Down' for PACK.

# Current Quest: Get SECRETPOTION for Amphy
- **Objective:** Travel to Cianwood City to get the SECRETPOTION for Amphy.
- **Location:** Cianwood City is across the sea.
- **Source:** A pharmacy in Cianwood City.

# Key Items
- **HIVEBADGE:** From Bugsy. Allows traded POKéMON up to L30 to obey and enables the use of CUT outside of battle.
- **POKéDEX:** A high-tech encyclopedia from PROF. OAK to record POKéMON data.
- **HM05 FLASH:** Obtained from the Elder of Sprout Tower. Illuminates dark caves. Requires the Zephyr Badge to use outside of battle.
- **HM01 CUT:** Obtained from the charcoal maker in Ilex Forest. Allows cutting small trees outside of battle. Requires the Hive Badge.
- **PLAINBADGE:** From Whitney. Boosts POKéMON's Speed and allows the use of STRENGTH outside of battle.

# TMs
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
- **Teacher in Olivine Pokémon Center:** Mentioned a person in Cianwood City, across the sea, who has a rare POKéMON.
- **POKEFAN_F on OlivineLighthouse1F (16, 9):** Mentioned that in the past, Pokémon were used to light the sea at night, and the lighthouse was built in their honor.
- **Gentleman on OlivineLighthouse2F (17, 8):** The sick Pokémon at the top needs 'special medicine'.

# Crafting
- Kurt in Azalea Town can make special POKé BALLS from APRICORNS. I received a LURE BALL from him as an example.

# Puzzle Solutions & Lessons
- **IMMEDIATE TOOL MAINTENANCE:** If a core tool (like `find_path`) fails, fixing it becomes the absolute highest priority, superseding all other gameplay actions. Deferring fixes leads to repeated, catastrophic failures.
- **TOOL FAILURE INVESTIGATION:** If a tool produces an unexpected result (e.g., pathing into a wall), I must investigate the root cause immediately. Continuing without understanding the failure risks repeating the error. This may involve examining the tool's code, verifying input data, or checking for stale game state information.
- **Tool Design Philosophy:** My `find_path` tool failed repeatedly because its logic was too specific (relying on a list of NPC names). The fix was to generalize the rule: any tile with any object is impassable. **Lesson:** When designing tools, prefer simple, general rules over complex, specific ones that are brittle and likely to fail when encountering new or unexpected game elements. Similarly, my `plan_systematic_search_path` tool failed because it used a naive nearest-neighbor algorithm instead of true pathfinding. **Lesson:** Build new tools on the proven, robust logic of existing tools whenever possible to avoid re-introducing fundamental flaws.
- **Agent Output Verification:** When a custom agent provides a fix for a tool, especially one that parses game data like the map XML, I must manually verify the agent's core assumptions against the actual data structure. Blindly implementing a fix without this verification step can lead to repeated, frustrating tool failures.
- **Tool Context Awareness:** Tools like `select_battle_option` are context-specific and will fail if used when the required UI (e.g., the main battle menu) is not visible. Always verify the game state before calling a context-dependent tool.
- **`find_path` Tool Limitation:** The tool cannot see off-screen objects. This means it can generate paths that appear valid but are blocked by NPCs that are not currently rendered. I must rely on my own map markers to navigate around known off-screen obstacles.
- **Intermediate Warp Pathing:** My `find_path` tool was causing loops by treating intermediate warp tiles (like ladders) as normal floor tiles. Lesson: Pathfinding tools must treat all warps as impassable unless they are the explicit final destination of the path.
- **TOOL USAGE DISCIPLINE:** When using a custom tool that outputs button presses, I MUST remember to set `autopress_buttons: true` if I want the actions to be executed. Forgetting this parameter causes the tool to do nothing, wasting a turn.
- **BATTLE TOOL DISCIPLINE:** In battle, I must use my `select_battle_option` tool to choose FIGHT/PKMN/PACK/RUN instead of manual presses to avoid errors. Similarly, I must use `select_move` and `switch_pokemon` for their respective sub-menus.
- **Data Source Hierarchy:** When there is a conflict between my internal map data (XML) and the official `Game State Information` (e.g., the warp list), the Game State is the absolute source of truth. Relying on unverified data from the XML can lead to unproductive testing loops.
- **Defeated Trainers as Obstacles:** Defeated trainers are still physical obstacles. Pathfinding must account for their current coordinates, even if they are static and non-hostile.
- **Stun Reset:** The `stun_npc` effect appears to reset when leaving and re-entering a map. Do not rely on it for multi-map pathing.
- **Challenge NPC Dialogue:** Do not blindly trust NPC dialogue that suggests a path is a dead end, especially if it blocks the only apparent way forward. Always verify with your own systematic exploration.
- **Pathing Near Hazards:** When navigating near multiple hazards (like adjacent pits), automated pathing can be unreliable if interrupted. To avoid repeated errors, break down the path into smaller, manually-controlled segments for the final, critical steps to ensure precise positioning.
- **Automated Path Vetting:** Automated paths, especially from `plan_systematic_search_path`, can unintentionally lead into warps. I MUST visually inspect the generated coordinate list for known warp tiles before executing the path to avoid accidental map transitions.
- **Tool Context-Dependency:** A tool's logic may be based on assumptions that are not universally true. The `find_path` tool assumed all `LADDER` tiles were warps, which failed on the Olivine Port pier where they are walkable. Lesson: Always be prepared to refine tools when they encounter new game contexts that violate their core assumptions.
- **Methodical Puzzle Testing:** When testing a hypothesis with multiple steps (e.g., checking all directions), I must systematically test each step, document the outcome in my notepad, and only conclude the entire hypothesis has failed after all steps have been exhausted.
- **Agent Escalation:** When multiple self-generated hypotheses for a puzzle have failed, especially after getting stuck in a repetitive loop, I must escalate to a more powerful problem-solving tool like an agent. This is critical for breaking cognitive fixation.
- **Warp Data Conflict Resolution:** The official `Game State Information -> Warps` list is the single source of truth for all active warps. Data from other sources (like the Mental Map XML) that suggests a warp exists where one is not officially listed should be treated as a potential data artifact or an inactive warp that requires an external, non-obvious trigger. Do not get stuck in loops testing these.
- **Challenge Assumptions:** My progress in the lighthouse was blocked by my own assumption that all pits were traps. I must systematically test all environmental possibilities, even those that seem like dead ends or hazards, as they might be the intended path forward. Falsifying my own root hypotheses is critical to avoiding puzzle loops.
- **Safe Interaction Positioning:** When planning to interact with the tile you are standing on (e.g., searching for a hidden switch), first turn to face a solid, non-hazardous adjacent tile (like a WALL) before pressing 'A'. This prevents accidental movement into hazards like pits.
- **Challenge False Constraints:** My loop was prolonged by the false assumption that a solution *had* to be on the eastern side of 2F. When stuck, I must identify and challenge the root assumption that is constraining my strategy.
- **Test All Variables:** When a puzzle has multiple similar elements (like the two pits in the lighthouse), they may not be functionally identical. Systematically test each one to ensure you don't miss a unique solution path.
- **Abandon Failed Hypotheses Quickly:** If a puzzle element fails multiple simple tests (e.g., a suspected warp doesn't trigger on step-on, interaction while on tile, or interaction from adjacent tile), I must abandon the hypothesis immediately. Mark the area as a dead end (🚫) to avoid getting stuck in unproductive testing loops.
- **Internal vs. External Puzzles:** When all paths inside a puzzle area (like the lighthouse) are confirmed dead ends, the solution is likely external. I must expand my search area instead of getting stuck in an internal loop.
- **Challenge Root Hypotheses:** When stuck or pursuing an overly complex strategy, the root assumption is likely flawed. Aggressively re-verify the foundational belief that led to the current strategy instead of just refining the failing strategy itself.
- **Non-Linear Puzzles:** Puzzle solutions are not always linear; moving 'backwards' or 'down' (like falling through a pit) can be the correct way forward, especially when the obvious 'up' path is a confirmed dead end.
- **Test All Puzzle Variables:** When a puzzle has multiple similar elements (e.g., two pits on the same floor), I must not assume they are functionally identical. Each variable must be tested independently to avoid missing a unique solution.
- **Logical Loop Breaking:** When stuck in a repetitive loop exploring a confirmed dead end, the root assumption is likely flawed. I must escalate to an agent or fundamentally change my strategy (e.g., by exploring a different floor) instead of repeating failed tests.
- **Escalate Vertically:** When stuck in an exploration loop on a given floor and the floor below, the solution is likely on a floor *above*. I must challenge the assumption that the path forward is nearby and be willing to ascend to find a way down into inaccessible areas. This was the key insight from my `puzzle_solver` agent regarding the lighthouse.
- **Red Herring Passages:** A hidden passage is not a guaranteed path forward. The secret passage on Olivine Lighthouse 5F at (8, 7) led to a confirmed dead end. If a new path quickly proves fruitless, I must be willing to backtrack immediately rather than assuming there's a deeper puzzle.
- **Challenge Root Hypothesis in Loops:** When physically stuck in a repetitive loop (e.g., walled off in a section with only one entrance/exit), the root hypothesis about how to progress is likely flawed. I assumed the central column was the only path up, which was wrong. I must backtrack to an earlier point and find an entirely different route instead of trying to force a solution within the loop.
- **Deterministic vs. Random Chance:** If a strategy based on random chance (like waiting for a moving NPC) fails even once, immediately switch to a deterministic strategy (like using `stun_npc`). Relying on luck is inefficient and leads to wasted turns.
- **Detour Identification:** Do not assume every new path or area is part of the main quest progression. The Battle Tower, for example, was a side area. I must evaluate new paths critically and be willing to backtrack quickly if they don't align with my primary goal.
- **Local Solutions:** When a quest is presented in a specific location (e.g., a sick Miltank at Moomoo Farm), the solution is very likely found within that same immediate area. Do not assume a long journey to another location is required unless explicitly directed.
- **Olivine City Navigation:** Olivine City is physically divided into western and eastern sections by impassable walls and buildings. The only way to cross between them is via the main southern road that runs east-west near the Pokémon Center and port. If `find_path` returns 'No path found', it's likely due to this segmentation. The solution is to backtrack and find a different street to navigate around the central building block.

## Solved Puzzles
### Azalea Gym
- Gym Guide: The Gym Leader is BUGSY. His Bug POKéMON are weak to Fire and Flying-type moves.
- **Solution:** The gym puzzle involves finding two hidden floor switches. The first, located on the path to the right-side trainer, makes a new trainer appear on the left side. The second, on the path to the left-side trainer, makes another new trainer appear. The path to these trainers is not blocked by the Twins in the middle; it is possible to walk around the bottom of the gym. Defeating all trainers is not required to reach Bugsy.

### Goldenrod Department Store
- **Elevator:** The elevator is controlled by the panel at (3, 0). Interacting with the panel brings up a floor selection menu. After selecting a floor, you must walk onto the corresponding warp carpet to travel. The warp to B1F is at (1, 3) and the warp to 1F is at (2, 3).
- **B1F Box Puzzle:** My own movement is causing changes in the a map layout. A WALL at (5, 10) changed to a FLOOR after I moved. The Machop at (7, 7) is likely the key to solving the puzzle. The previous solution of leaving and returning the room seems to be only a partial trigger.

### Goldenrod Gym
- Gym Guide: This is a Normal-type gym. Fighting-type POKéMON are recommended.
- **Puzzle Mechanic:** The gym puzzle is solved by walking along the outer perimeter of the entrance room. The direction and sequence of these walks cause different trainers to appear and disappear, opening and closing paths. The correct sequence of perimeter walks and trainer battles is required to open the path to the main gym area.

### Goldenrod Underground Switch Room Puzzle
- **Failed Hypothesis:** The puzzle is solved by repeatedly entering and exiting the 'GoldenrodUndergroundSwitchRoomEntrances' area to cycle through different room configurations. (Failed after 5+ attempts, triggered a loop warning).
- **New Hypothesis:** The puzzle requires accessing the switch rooms from a different path. The main underground connects the north and south city entrances. I will re-enter the underground from the southern entrance in Goldenrod City and explore the lower level again, as my path was previously blocked and new events (Granny NPC) may have occurred.
- **Agent Hypothesis #1 (Full Traversal):** FAILED. Attempted to walk from the north entrance to the south entrance. Path was blocked by a SUPER_NERD at (3, 27) that appears only in the 'north entrance' configuration. This confirms a simple traversal is impossible.
- **Agent Hypothesis #2 (Defeat All Trainers):** FAILED. The SUPER_NERD at (3, 27) that blocks the path does not initiate a battle, only dialogue. This makes defeating all trainers impossible in this configuration.
- **Agent Hypothesis #3 (In-and-Out Ladders):** FAILED for northern ladder (3, 2). The blocking SUPER_NERD at (3, 27) did not move. Will proceed to test other accessible ladders.

### Ruins of Alph - Kabuto Chamber Puzzle
- **Clue:** "A POKéMON that hid on the sea floor. Eyes on its back scanned the area."
- **Solution:** The image is KABUTO.

### Olivine Lighthouse Puzzle
- **Root Cause Analysis:** My progress was catastrophically stalled by a single, flawed root hypothesis: "The way forward MUST be in the western section of the lighthouse." I failed to trust my `find_path` tool, which repeatedly and correctly told me the western and eastern sections were disconnected on floors 3 and 4. Instead of trying to falsify my hypothesis (e.g., by immediately attempting a strategic retreat to a lower floor), I spent dozens of turns in a loop, trying to force a path that didn't exist. The western column is a confirmed dead-end loop.

# Obstacles and Solutions
- A strange tree blocks the road north of Goldenrod City (Route 35). It can be cleared using a SQUIRTBOTTLE, which is obtained from the Flower Shop after defeating Whitney. The Lass in the shop confirms this is the correct sequence of events.

# Held Items
- **QUICK CLAW:** Received from a Teacher in the National Park. When held by a Pokémon, it may allow them to attack first in battle.

# PC Inventory
- **Box 1:**
  - Hestia (MAGBY), Lv15, Female

# Rematch Opportunities
- Hiker Anthony on Route 33 called for a battle.
- Youngster Joey on Route 30 called for a rematch.
- Sailor Huey at the Olivine Lighthouse called for a rematch.

# Moomoo Farm Puzzle - Agent Hypotheses
- **Hypothesis 1 (High Priority):** The 'BERRY' is from a special, interactable tree on the Moomoo Farm grounds.
- **Hypothesis 2:** An NPC inside the farm buildings will give me the 'BERRY'.
- **Hypothesis 3:** The 'BERRY' is a hidden item on the ground somewhere on Route 39 or within the farm.

# Agent Escalation Protocol
- When an exploration path is confirmed as a dead end (e.g., blocked by an unmovable NPC), I MUST immediately mark it with '🚫' to prevent getting stuck in a wasteful exploration loop. Furthermore, if I find myself repeatedly testing failed hypotheses for a puzzle, I MUST escalate to my `puzzle_solver` agent instead of continuing the loop. This is a non-negotiable protocol to prevent strategic stagnation.

# find_path Failure Analysis (Olivine Lighthouse)
- The tool repeatedly failed by treating all intermediate warp tiles (even walkable `FLOOR` tiles with a warp property) as impassable walls. This created false negatives where clear paths were reported as 'No path found'.
- The proposed fix is to introduce a `TRANSITION_WARP_TYPES` set (`DOOR`, `STAIRCASE`, `CAVE`, `PIT`, `LADDER`) to differentiate warps that force a map transition from those that are just walkable entry points. The logic should only mark intermediate `TRANSITION_WARP_TYPES` as walls, allowing the pathfinder to correctly navigate over walkable warp tiles.