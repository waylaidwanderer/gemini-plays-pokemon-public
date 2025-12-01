# CRITICAL DIRECTIVE: ANTI-HALLUCINATION PROTOCOL
- My memory is unreliable. The Game State Information is the absolute source of truth.
- I MUST verify my `current_map_id` and `current_position` from the Game State Information before EVERY single action, especially before using coordinate-based tools or setting navigation goals.
- I MUST verify a warp's existence in the `Game State Information -> Map Events -> Warps` list before assuming it's a valid warp.
- Failure to adhere to this protocol is the root cause of all major strategic failures and wasted turns.

# Strategic Protocol
- **PLAN-EXECUTE-VERIFY CYCLE:**
  1. **CONSULT KNOWLEDGE BASE:** Before forming ANY plan, I MUST consult my notepad and map markers to avoid repeating mistakes or ignoring solved puzzles.
  2. **METHODICAL EXPLORATION:** When arriving in a new or isolated area (especially via a one-way path), I MUST systematically explore every single reachable tile before using any exits to avoid missing hidden paths or triggers.

- **Tool Definition Errors:** If `define_tool` fails with an 'identical script' error, it means the proposed change has already been successfully applied in a previous turn. Do not retry the same definition; proceed with the next action.
- **NPC Interactions:** Some interactions, like battling a trainer, can be multi-step. Ensure all initial dialogue is cleared with 'A' presses before the main event (like the battle) will trigger. Non-Battling NPCs: Not all moving NPCs are trainers. If an NPC's dialogue repeats without initiating a battle after multiple interaction attempts (direct, line-of-sight), they are likely a non-battling character. Do not get stuck in an interaction loop; update markers and move on.
- **Pathfinding Logic:** If a path is repeatedly blocked or a tool reports 'No path found,' do not assume you are soft-locked. Re-examine the map visually for alternative routes like ledges or other one-way tiles that may have been missed.
- **Dialogue & Movement:** I must ensure all dialogue boxes are closed by pressing 'A' before attempting any movement inputs. Trying to move with text on screen will fail.
- **Agent-based fixes must be verified in both simple and complex scenarios before a tool is considered fully functional. A fix for one case may not cover all failure conditions.
- **Exploration Before Puzzles:** Prioritize exploring all reachable areas of a new map before attempting complex puzzles to ensure all context and potential clues have been gathered.
- **Tool Input Verification:** Before concluding a tool is broken (e.g., `find_path` returning 'No path found'), I must first verify that my inputs and assumptions are correct. Pathing to an 'unseen' tile is an invalid input, as the tool correctly treats them as impassable. My strategy must adapt to the tool's logic.
- **Random Chance Strategy:** If a strategy based on random chance (like waiting for moving NPCs) fails repeatedly (3+ times), I must switch to a deterministic strategy (like proactively stunning them in favorable positions).
- **Herding Puzzles:** Interacting with an object (like the Farfetch'd) from an adjacent tile can trigger movement along a complex, pre-determined path, not just simple repulsion. The direction of approach is the key trigger.
- **Visual Path Verification:** Before executing a move, I must visually confirm the path on the ASCII map and game screen to avoid simple navigational errors like walking into walls. This supplements tool-based pathfinding.
- **Debugging Cycle Avoidance:** When a core tool repeatedly fails despite multiple fixes, the core algorithm is likely fundamentally flawed. I must avoid getting stuck in a loop of incremental, failing changes. The correct approach is to either replace the logic with a known-working version from another tool, re-implement it from first principles, or delete the tool to prevent reliance on faulty logic.
- **Puzzle State Changes:** Some puzzles, like the Goldenrod Dept. Store basement, may change their state based on triggers that are not immediately obvious, such as leaving and re-entering the area. If internal solutions fail, I must consider external actions as potential triggers.
- **Interaction vs. Line of Sight & Flawed Assumptions:** If direct interaction with a trainer-like NPC results in a dialogue loop (like with Sailor Huey), the battle trigger might be line of sight. However, I must first challenge the root assumption that a battle is necessary at all. I wasted significant time trying to force an interaction when a simple path around the NPC existed. Lesson: Always verify if an obstacle is truly blocking the path before attempting to resolve it through complex interactions or battles. Check for alternative routes first.
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
- **Ilex Forest Path:** The entrance is from Azalea Town, and the exit is at (1, 5).
- **Movement Loop Breaking:** When stuck in a movement loop or repeatedly blocked, changing the immediate navigation target is an effective strategy to break the cycle and find a new, clear path.
- **Interaction Loops:** If repeated 'A' presses (2-3 times) on an NPC or object do not advance the game state (dialogue, battle start, etc.), the interaction is likely stuck. Do not continue pressing 'A'. Break the loop by performing a different action, such as moving one tile away and back, to reset the state before attempting to interact again.
- **CONSULT YOUR KNOWLEDGE BASE:** My notepad contains critical, verified information about game mechanics (like impassable tiles). I MUST consult this knowledge base *before* attempting an action to avoid repeating solved problems and wasting turns on impossible movements, as seen with the COUNTER tile incident.
- **One-Way Warps:** Some warps, especially holes in the floor, may be one-way exits. If simple interaction methods (stepping on, pressing 'A', pressing a direction) fail repeatedly, assume it is an exit or requires a complex external trigger. Do not get stuck testing simple interactions.
- **Warp Loop Anomaly:** The warp at Olivine City (19, 27) creates a confusing loop by repeatedly sending me to the Port Passage. If a warp behaves unexpectedly, I must mark it as problematic and investigate alternative routes immediately rather than getting stuck in a repetitive cycle.
- **Warp Activation Diversity:** Warps can be activated in multiple ways: step-on (ladders), interaction ('A' press), one-way drops (likely PITs), or by external triggers. I must test multiple methods before concluding a warp is inactive.
- **Trust Your Tools:** My `find_path` tool correctly identified a path on Olivine Lighthouse 1F that I had completely missed through manual exploration. This proves that I should trust the output of my verified tools over my own flawed visual assessment, especially in complex layouts. A tool's 'No path found' is equally valuable information.
- **TOOL FAILURE INVESTIGATION:** If a tool produces an unexpected result (e.g., pathing into a wall), I must investigate the root cause immediately. Continuing without understanding the failure risks repeating the error. This may involve examining the tool's code, verifying input data, or checking for stale game state information.
- **Observe Before Assuming:** When seemingly stuck (e.g., trapped in a room), the first action must be to re-examine the entire known map for obvious, overlooked exits before assuming a complex, hidden solution is required. Trust the map data over my own narrative of the situation.
- **IMMEDIATE OBSTACLE MARKING:** I failed to mark Sailor Huey as a blocker, causing me to waste time retrying a failed path. All critical obstacles MUST be marked with '🚫' immediately upon discovery to prevent loops.
- **Notepad Edit Loops:** If a `notepad_edit` 'replace' action fails with a 'text not found' error multiple times, it is highly likely the edit was already successful in a previous turn. I must verify the current notepad content before retrying the same edit to avoid getting stuck in an unproductive loop.
- **`find_path` Tool Limitation:** The tool cannot see off-screen objects. This means it can generate paths that appear valid but are blocked by NPCs that are not currently rendered. I must rely on my own map markers to navigate around known off-screen obstacles.
- **Trust NPC Guidance:** External NPC confirmation (like the Gym Guide directing me to the lighthouse) must override my own flawed assumptions or conclusions that a path is a dead end. I must re-investigate any such location with the new information.
- **Value of Brute-Force Automation:** When visually stuck, a systematic, automated search can reveal paths or triggers that are easily missed by manual exploration. It's a valid strategy for breaking through a perceived dead end.
- **Non-Linear Puzzles:** Puzzle solutions are not always linear; moving 'backwards' or 'down' (like falling through a pit) can be the correct way forward, especially when the obvious 'up' path is a confirmed dead end.
- **External Triggers:** If all internal solutions to a puzzle are exhausted (e.g., the lighthouse entrance), the trigger is likely external. Do not get stuck in a loop; expand the search area.
- **Task Immediacy:** Deferred tasks are often forgotten. Actions like unstunning non-critical NPCs should be done immediately after the interaction is complete to maintain good state hygiene.
- **TOOL USAGE DISCIPLINE:** When using a custom tool that outputs button presses, I MUST remember to set `autopress_buttons: true` if I want the actions to be executed. Forgetting this parameter causes the tool to do nothing, wasting a turn.

# Game Mechanics & Systems
- The Day/Night cycle is an important mechanic in this game, affecting events.
- Received 5 POKé BALLS from the scientist in Elm's Lab. I can now catch wild Pokémon.
- The PC in Pokémon Centers is used for Pokémon and item storage.
- BERRY trees grow new BERRIES every day.
- Healing at a Pokémon Center restores all HP and PP for the entire party and cures any status conditions.
- **Game State Updates:** The game's internal map data (like a `CUT_TREE` changing to a `FLOOR`) does not fully update until all on-screen text from the preceding action is cleared. Attempting to use tools like `find_path` before the overworld is fully interactive will result in the tool using stale data and failing.
- **HEADBUTT Mechanic:** The move HEADBUTT can be used outside of battle to shake certain trees (`HEADBUTT_TREE` tiles). This can cause sleeping Pokémon to fall out, providing a new method for encounters.
- **Environmental Obstacle Resets:** The CUT_TREE at (8, 25) in Ilex Forest reappeared after I left the map and returned. This suggests some environmental obstacles might reset upon re-entry.
- **Battle Anomaly:** A recurring battle anomaly has been observed. Interacting with some trainers (e.g., Sailor Huey, Gentleman Alfred) sometimes displays the battle-starting dialogue but then returns to the overworld without initiating combat. However, this is inconsistent; a later attempt to battle Sailor Huey triggered a proper battle. The exact cause or trigger condition is unknown.
- **Evolution Methods:** Some POKéMON, like MACHOKE, KADABRA, HAUNTER, and GRAVELer, evolve when traded.
- **Intermediate Warp Pathing:** My `find_path` tool was causing loops by treating intermediate warp tiles (like ladders) as normal floor tiles. Lesson: Pathfinding tools must treat all warps as impassable unless they are the explicit final destination of the path.

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
| Water | Fire | Super Effective |
| Water | Rock | Super Effective |
| Water | Ground | Super Effective |

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
- **WINDOW**: An impassable object that can be interacted with to display text. Functions like a wall.
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
- **unseen**: A tile that has not yet been explored. Its properties are unknown until visited.
- **BUOY**: An object found in water. Appears to be impassable, functioning like a WALL tile within a WATER area.
- **WARP_CARPET_LEFT**: A traversable warp tile at the edge of a a map that transitions to the adjacent map on the left. To activate, you must attempt to move left from the carpet tile, effectively trying to walk 'off' the map.
- **TEACHER / LASS / BIRD / OFFICER / YOUNGSTER / POKEFAN_M**: These NPC objects are impassable and function as walls.
- **FRUIT_TREE**: An impassable, interactable object. Gives one BERRY item (like PRZCUREBERRY) when interacted with for the first time. Subsequent interactions yield nothing.
- **CAVE**: A traversable warp tile that functions as an entrance to a cave.
- **VOID**: An impassable tile type found at the edges of some maps, functions as a wall.
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
- **BROKEN_FLOOR**: Not yet encountered. Previous note about it being in the Burned Tower was likely a hallucination.
- **PIT**: Confirmed one-way warp tile in Olivine Lighthouse. Stepping on it causes the player to fall to the floor below.
- **LADDER**: A traversable warp tile. Activated by stepping *onto* the tile, which immediately triggers the warp. No additional button presses are needed.

# Current Quest: Olivine Lighthouse
- **Objective:** Investigate the sick Pokémon at the Olivine Lighthouse.
- **Status:** I am on the 2nd floor of the Olivine Lighthouse, in the eastern section.
- **Olivine Lighthouse Puzzle:**
  - **Objective:** Reach the top floor to find Jasmine and the sick Pokémon.
  - **Key Insight:** Progress is made by falling through pits on 2F to access a sealed-off eastern section of 1F. The path upwards is from this eastern section.
  - **Summary of Findings:**
    - **2F:** The western path has a ladder at (5, 3) leading up to a confirmed dead end on 3F. The eastern path is where I am currently exploring.
    - **3F:** The western side, accessed from 2F, is a confirmed dead end. The eastern side is currently inaccessible.
  - **Current Hypothesis:** The correct path to the upper floors must be on this eastern side of 2F. I am systematically searching the area.

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
- **Methodical Puzzle Testing:** When testing a hypothesis with multiple steps (e.g., checking all directions), I must systematically test each step, document the outcome in my notepad, and only conclude the entire hypothesis has failed after all steps have been exhausted.
- **Agent Escalation:** When multiple self-generated hypotheses for a puzzle have failed, especially after getting stuck in a repetitive loop, I must escalate to a more powerful problem-solving tool like an agent. This is critical for breaking cognitive fixation.
- **Warp Data Conflict Resolution:** If the Mental Map XML or a system warning indicates a warp exists, but it's not on the official `Game State Information -> Warps` list and initial interaction tests fail, do not immediately dismiss it as a hallucination. Treat it as a potentially real warp with a non-obvious or event-based trigger. Mark it and continue to investigate other paths, but keep it in mind as a possible solution if all other avenues are exhausted.
- **Challenge Assumptions:** My progress in the lighthouse was blocked by my own assumption that all pits were traps. I must systematically test all environmental possibilities, even those that seem like dead ends or hazards, as they might be the intended path forward. Falsifying my own root hypotheses is critical to avoiding puzzle loops.
- **Safe Interaction Positioning:** When planning to interact with the tile you are standing on (e.g., searching for a hidden switch), first turn to face a solid, non-hazardous adjacent tile (like a WALL) before pressing 'A'. This prevents accidental movement into hazards like pits.
- **TRUST YOUR KNOWLEDGE BASE:** I wasted significant time in a loop because I ignored my own verified map marker and notepad entry. I MUST consult my own data before forming a new plan to avoid repeating solved puzzles.
- **Challenge False Constraints:** My loop was prolonged by the false assumption that a solution *had* to be on the eastern side of 2F. When stuck, I must identify and challenge the root assumption that is constraining my strategy.
- **Test All Variables:** When a puzzle has multiple similar elements (like the two pits in the lighthouse), they may not be functionally identical. Systematically test each one to ensure you don't miss a unique solution path.
- **Abandon Failed Hypotheses Quickly:** If a puzzle element fails multiple simple tests (e.g., a suspected warp doesn't trigger on step-on, interaction while on tile, or interaction from adjacent tile), I must abandon the hypothesis immediately. Mark the area as a dead end (🚫) to avoid getting stuck in unproductive testing loops.
- **Internal vs. External Pzzles:** When all paths inside a puzzle area (like the lighthouse) are confirmed dead ends, the solution is likely external. I must expand my search area instead of getting stuck in an internal loop.
- **Challenge Root Hypotheses:** When stuck or pursuing an overly complex strategy, the root assumption is likely flawed. Aggressively re-verify the foundational belief that led to the current strategy instead of just refining the failing strategy itself.

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

# Obstacles and Solutions
- A strange tree blocks the road north of Goldenrod City (Route 35). It can be cleared using a SQUIRTBOTTLE, which is obtained from the Flower Shop after defeating Whitney. The Lass in the shop confirms this is the correct sequence of events.

# Held Items
- **QUICK CLAW:** Received from a Teacher in the National Park. When held by a Pokémon, it may allow them to attack first in battle.

# PC Inventory
- **Box 1:**
  - Hestia (MAGBY), Lv15, Female

# Tools & Agents

## Built-in Tools
- `notepad_edit`, `run_code`, `define_agent`, `delete_agent`, `define_map_marker`, `delete_map_marker`, `stun_npc`, `define_tool`, `delete_tool`, `select_battle_option`

## Custom Tools
- `select_item`
- `select_move`
- `switch_pokemon`
- `find_path`

## Custom Agents
- `python_code_debugger`
- `puzzle_solver`

# Reminders & To-Do

## General
- **Tool Glitch Recovery:** If a tool repeatedly fails with a bizarre error despite the code appearing correct (like a `ModuleNotFoundError` for a valid library), force a re-definition of the tool with a new commit message to clear any cached or corrupted state.

## Olivine City

# Rematch Opportunities
- Hiker Anthony on Route 33 called for a battle.
- Youngster Joey on Route 30 called for a rematch.
- Sailor Huey at the Olivine Lighthouse called for a rematch.

# Item Interaction Mechanics
- To give an item to an overworld sprite (like the sick Miltank), I must interact with the sprite directly. Using the item from the PACK menu only works on my own POKéMON.
- The game may require a specific item type (e.g., a generic 'BERRY') and will not accept functionally similar but differently named items (e.g., 'BITTER BERRY').
- **Tool Design Philosophy:** My `find_path` tool failed repeatedly because its logic was too specific (relying on a list of NPC names). The fix was to generalize the rule: any tile with any object is impassable. **Lesson:** When designing tools, prefer simple, general rules over complex, specific ones that are brittle and likely to fail when encountering new or unexpected game elements. Similarly, my `plan_systematic_search_path` tool failed because it used a naive nearest-neighbor algorithm instead of true pathfinding. **Lesson:** Build new tools on the proven, robust logic of existing tools whenever possible to avoid re-introducing fundamental flaws.
- **Battle Start Anomaly:** Interacting with some trainers (Sailor Huey, Gentleman Alfred) displays the battle-starting dialogue, but then the game returns to the overworld without initiating combat. This has happened multiple times and seems to be a recurring issue.

### Olivine Lighthouse Puzzle - Agent Hypotheses
- **Hypothesis 1 (FAILED):** There is a hidden pit on the 3rd floor (western side) that drops the player onto the suspicious tiles on the 2nd floor.
  - **Test Result:** Systematically walked over every floor tile on the western side of 3F. No hidden pit was found. Hypothesis is disproven.
- **Hypothesis 2 (FAILED):** Exhausting the Gentleman NPC's dialogue on the eastern 2nd floor will activate the suspicious tiles.
  - **Test Result:** Spoke to the NPC twice. Dialogue repeated with no effect. Hypothesis is disproven.

# To-Do List

# Battle Anomaly
- A recurring issue has been observed where interacting with some trainers (e.g., Sailor Huey, Gentleman Alfred, Youngster on Route 39) displays their pre-battle dialogue, but the game then returns to the overworld without initiating combat. This is inconsistent, as some of these trainers have been successfully battled on later attempts. If a battle fails to start after 1-2 attempts, mark the trainer as bugged and move on to avoid getting stuck in an interaction loop.

# Reflection Lessons (Turn 29624)
- **Path Interruption Strategy:** When a long, automated path (like from `plan_systematic_search_path`) is interrupted by a new or moving obstacle, the entire path is invalid. The correct procedure is to immediately regenerate the path from the new current position, not attempt to resume the old one.
- **Dynamic NPC Presence:** Some NPCs that appear static may despawn and respawn based on player position or other triggers. Their sudden absence can open previously blocked paths, and their reappearance can re-block them. The map state is not always persistent even within a single visit.

# Reflection Lessons (Turn 29676)
- **Reactive Loop Breaking:** When a plan is repeatedly interrupted by a variable element (like a moving NPC), I must immediately switch to a deterministic strategy (like using `stun_npc`) instead of retrying the same failed approach. Recognizing and breaking these reactive loops is critical to avoid wasting time.

# Reflection Lessons (Turn 29728)
- **External Puzzle Solutions:** When a complete, systematic exploration of a self-contained area (like the Olivine Lighthouse) yields no path forward, the solution is likely external. I must trust key NPC dialogue that points toward an external requirement (like needing 'special medicine') and shift my objective accordingly, rather than getting stuck re-testing failed internal hypotheses.

# Reflection Lessons (Turn 29782)
- **Tool Robustness:** My `plan_systematic_search_path` tool failed catastrophically because its XML parser used a brittle `find('Object')` method that failed to detect nested objects, causing paths to lead directly into NPCs. The fix was to use a robust `find('.//Object')` search. **Lesson:** Tool logic must be generalized to handle all variations of game data structures. Prefer simple, robust rules over complex, specific ones that are prone to failure.

# To-Do List (New)

# Reflection Lessons (Turn 29831)
- **Tool Failure Protocol:** If a core tool demonstrates a fundamental logic failure (e.g., `plan_systematic_search_path` generating a non-contiguous path), I must stop all attempts to use it immediately. The only valid next action is to debug and fix the tool. Attempting to re-run the tool or work around its output is an inefficient loop and a strategic failure.

# Reflection Lessons (Turn 29884)
- **External Puzzle Solutions:** When a complete, systematic exploration of a self-contained area yields no path forward, the solution is likely external. I must trust key NPC dialogue that points toward an external requirement (like needing 'special medicine') and shift my objective accordingly, rather than getting stuck re-testing failed internal hypotheses.

# Reflection Lessons (Turn 29932)
- **TRUST YOUR TOOLS:** If `find_path` returns 'No path found', it is a definitive statement that the destination is unreachable from the current position based on known traversable tiles. I must trust this output and immediately form a new hypothesis about the path forward, rather than questioning the tool.
- **`find_path` Tool Limitation:** The tool cannot see off-screen objects. This means it can generate paths that appear valid but are blocked by NPCs that are not currently rendered. I must rely on my own map markers to navigate around known off-screen obstacles or move to bring objects on-screen before pathing.

# Reflection Lessons (Turn 30144)
- **Path Interruption:** My long, automated path was interrupted because I tried to move onto a one-way ledge tile in the wrong direction. Lesson: For long paths, either break them into smaller, verifiable chunks or use a robust tool like `exploration_manager` to handle interruptions gracefully. Blindly executing a long path is risky and prone to failure.

# Pathing Strategy Update
- My long paths are constantly being interrupted. The system critique correctly pointed out that I should be using the `exploration_manager` agent to handle this. Once `find_path` is confirmed to be working correctly, I MUST use `exploration_manager` to break long paths into smaller, manageable chunks to avoid these repeated failures.

# Reflection Lessons (Turn 30196)
- **Tool Logic Robustness:** My `find_path` tool failed because its one-way ledge logic was incomplete. It only checked the a current tile, not the destination tile, allowing it to generate illegal paths *onto* ledges. **Lesson:** When developing tools, logic must be tested against all edge cases. Prefer simple, general rules that cover all possibilities over complex, specific ones.
- **Tool Input Validity:** Attempting to use `find_path` to navigate to an 'unseen' tile is an invalid use of the tool, as it correctly treats them as impassable. My strategy must adapt to the tool's known logic and limitations.
- **`find_path` Off-Screen Limitation:** The tool cannot see off-screen objects. This means it can generate paths that appear valid but are blocked by NPCs that are not currently rendered. I must rely on my own map markers or shorter paths to navigate around known off-screen obstacles.

# Reflection Lessons (Turn 30248)
- **Proactive Stunning:** When a planned path goes near a moving NPC, even if it doesn't directly interact with them, proactively stunning them is the most reliable strategy to prevent random path interruptions. Relying on path recalculation after an interruption is less efficient.
- **Stun Mechanic:** The 'stun' effect from `stun_npc` is temporary. The POKEFAN_F in the lighthouse started moving again after a few turns. The effect likely wears off after a set number of steps or turns.

# New Exploration Strategy
- The `plan_systematic_search_path` tool has been deleted due to being fundamentally buggy and unreliable.
- The `exploration_manager` agent has been deleted as it is now obsolete.
- **New Method:** For exploring complex, unknown areas, I will visually divide the map into quadrants. I will then use the reliable `find_path` tool to navigate to a central, traversable point within each quadrant to ensure full coverage without relying on a single, fragile, all-encompassing path.
- If a core tool requires more than 2-3 debug cycles to fix, its fundamental logic is likely flawed. It is more efficient to delete the tool and adopt a simpler, more reliable strategy than to get stuck in an unproductive debugging loop.

# Item Interaction Mechanics
- To give an item to an overworld sprite (like the sick Miltank), I must interact with the sprite directly. Using the item from the PACK menu only works on my own POKéMON.
- The game may require a specific item type (e.g., a generic 'BERRY') and will not accept functionally similar but differently named items (e.g., 'BITTER BERRY').

# Lessons Learned
- **Tool Definition Errors:** If `define_tool` fails with an 'identical script' error, the change has already been applied. Do not retry.
- **NPC Interactions:** Some interactions are multi-step. Clear all dialogue. If dialogue repeats without a battle, the NPC is non-battling.
- **Pathfinding Logic:** If a path is blocked, visually re-examine the map for alternatives like ledges.
- **Dialogue & Movement:** Always close dialogue boxes with 'A' before moving.
- **Exploration Before Puzzles:** Explore all reachable areas before attempting complex puzzles.
- **Tool Input Verification:** Pathing to an 'unseen' tile is an invalid input for `find_path`.
- **Random Chance Strategy:** If a random strategy (waiting for NPCs) fails 3+ times, switch to a deterministic one (stunning them).
- **Herding Puzzles:** The direction of approach can be the key trigger for object movement.
- **Visual Path Verification:** Visually confirm paths on the ASCII map to supplement tools.
- **Debugging Cycle Avoidance:** If a core tool repeatedly fails, its algorithm is likely flawed. Replace or delete it, don't get stuck in a fix loop.
- **Puzzle State Changes:** Puzzle states can change based on external triggers like leaving and re-entering an area.
- **Interaction vs. Line of Sight:** If direct interaction fails, consider line of sight. But first, challenge the root assumption that interaction is necessary at all. Always look for a path *around* an obstacle first.
- **Positional Awareness:** Always verify your own and your target's coordinates before using a targeted tool like `stun_npc`.
- **Blocked Movement vs. Battle Start:** A 'Movement Blocked' alert is not a guarantee of a wild battle.
- **Struggle Mechanic Failure:** Repeatedly selecting a 0 PP move does not trigger Struggle in this game.
- **Proactive Automation:** Automate repetitive, complex, or error-prone manual actions immediately.
- **Resource Management:** Run from inefficient battles to conserve PP.
- **Warp Carpet Anomaly:** A manual 'Down' press on a `WARP_CARPET_DOWN` can fail due to a wall, but an automated path may succeed. The mechanic needs more investigation.
- **Tool Context Awareness:** Context-specific tools will fail if used when the required UI is not visible.
- **Type Disadvantage Switching:** Switching out is critical when facing a significant type disadvantage.
- **Interaction Pre-check:** Verify you are adjacent and facing your target before pressing 'A'.
- **Proactive Stunning:** Stun moving NPCs *before* attempting to approach and interact.
- **Pathing Interruption:** Short, automated paths can be interrupted by moving NPCs. Proactive stunning is the most reliable strategy.
- **Movement Loop Breaking:** Change your immediate navigation target to break a movement loop.
- **Interaction Loops:** If 'A' presses (2-3 times) don't advance the game state, the interaction is stuck. Move away and back to reset it.
- **CONSULT YOUR KNOWLEDGE BASE:** Always check the notepad and map markers before acting to avoid repeating solved problems.
- **One-Way Warps:** Some warps (like pits) may be one-way exits. Test multiple interaction methods before giving up.
- **Warp Loop Anomaly:** If a warp behaves unexpectedly (like the Olivine Port Passage loop), mark it as problematic and find an alternative route.
- **Warp Activation Diversity:** Warps can be activated by step-on, 'A' press, one-way drops, or external triggers.
- **Trust Your Tools:** A verified tool's output (like `find_path`) should be trusted over flawed visual assessment.
- **TOOL FAILURE INVESTIGATION:** Investigate the root cause of any tool failure immediately.
- **Observe Before Assuming:** When stuck, re-examine the map for obvious exits before assuming a complex solution.
- **IMMEDIATE OBSTACLE MARKING:** Mark all critical obstacles with '🚫' immediately.
- **`find_path` Tool Limitation:** The tool cannot see off-screen objects. Rely on map markers to navigate around known off-screen obstacles.
- **Trust NPC Guidance:** Key NPC dialogue should override your own flawed assumptions.
- **Value of Brute-Force Automation:** A systematic, automated search can reveal paths missed by manual exploration.
- **Non-Linear Puzzles:** The correct path forward can sometimes be 'backwards' or 'down'.
- **External Triggers:** If all internal solutions to a puzzle are exhausted, the trigger is likely external.
- **Task Immediacy:** Perform tasks like unstunning NPCs immediately after the interaction is complete.
- **TOOL USAGE DISCIPLINE:** Remember to set `autopress_buttons: true` for custom tools that output button presses.
- **Item Interaction Mechanics:** To give an item to an overworld sprite, interact with it directly. The game may require a specific item type (e.g., 'BERRY') and not accept similar items.
- **Tool Design Philosophy:** Design tools with simple, general rules over complex, specific ones to make them more robust.
- **Path Interruption Strategy:** If an automated path is interrupted, regenerate it from the new current position.
- **Dynamic NPC Presence:** Some NPCs may despawn and respawn based on player position, opening or closing paths.
- **Reactive Loop Breaking:** If a plan is repeatedly interrupted, switch to a deterministic strategy (like stunning).
- **External Puzzle Solutions:** When a self-contained area is fully explored with no path forward, the solution is likely external. Trust NPC dialogue pointing to an external requirement.
- **Tool Robustness:** Tool logic must be generalized to handle all variations of game data structures.
- **Tool Failure Protocol:** If a core tool has a fundamental logic failure, stop using it and fix it immediately.
- **TRUST YOUR TOOLS (Revisited):** 'No path found' is a definitive statement that the destination is unreachable with current knowledge.
- **Path Interruption (Revisited):** For long paths, break them into smaller chunks.
- **Tool Logic Robustness (Revisited):