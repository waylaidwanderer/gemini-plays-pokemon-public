# IMMEDIATE TASKS
- **Ecruteak Gym Warp Mapping:** After defeating the Gym Leader, I must systematically step on every single `PIT` tile in this gym. The system alert has confirmed they are warps. I will document the destination of each one with a `define_map_marker` call to ensure my map data is complete. This is a high-priority task to address the map hygiene critique.

# CRITICAL DIRECTIVE: ANTI-HALLUCINATION PROTOCOL
- My memory is unreliable. The Game State Information is the absolute source of truth.
- I MUST verify my `current_map_id` and `current_position` from the Game State Information before EVERY single action, especially before using coordinate-based tools or setting navigation goals.
- I MUST verify a warp's existence in the `Game State Information -> Map Events -> Warps` list before assuming it's a valid warp.
- Failure to adhere to this protocol is the root cause of all major strategic failures and wasted turns.
- I must verify my location after every map transition or system warning to prevent hallucinations from compounding.

# STRATEGIC PROTOCOL

## Core Principles & Planning
- **KNOWLEDGE-DRIVEN STRATEGY (PRIMARY DIRECTIVE):** My own visual assessment and memory are unreliable. I MUST trust my documented knowledge (map markers, notepad) and verified tool outputs (`route_planner`) over my own intuition. A 'No path found' result is valuable, correct data, not a tool failure. I MUST consult this knowledge base before EVERY navigational decision to avoid re-exploring confirmed dead ends or repeating solved puzzles. This is my most critical failure point.
- **PLAN-EXECUTE-VERIFY CYCLE:**
  1. **CONSULT KNOWLEDGE BASE:** Before forming ANY plan, I MUST consult my notepad and map markers to avoid repeating mistakes or ignoring solved puzzles.
  2. **METHODICAL EXPLORATION:** When arriving in a new or isolated area (especially via a one-way path), I MUST systematically explore every single reachable tile before using any exits to avoid missing hidden paths or triggers.
- **PROACTIVE OBSTACLE MANAGEMENT:** When a plan is repeatedly interrupted by a variable element (like a moving NPC), I must immediately switch to a deterministic strategy (like using `stun_npc`) instead of retrying the same failed approach. Deferring this is a strategic failure.
- **Positional Awareness:** Always verify my own coordinates and the coordinates of relevant NPCs before using a targeted tool like `stun_npc`. Wasting a turn on an unnecessary action is a failure of observation.
- **Random Chance Strategy:** If a strategy based on random chance (like waiting for moving NPCs) fails repeatedly (3+ times), I must switch to a deterministic strategy (like proactively stunning them in favorable positions).
- **Task Immediacy:** Deferred tasks are often forgotten. Actions like unstunning non-critical NPCs should be done immediately after the interaction is complete to maintain good state hygiene.
- **Proactive Automation:** I must not wait until a manual task becomes a major bottleneck before automating it. If I identify any repetitive, complex, or error-prone manual action, creating a tool or agent to handle it becomes an immediate high-priority task, superseding non-critical gameplay actions. Deferring automation is a strategic failure.

## Core Lessons Learned
- **Verify State Before Modifying:** My repeated failure to update the notepad was caused by not using the exact 'old_text'. I must verify the current content of a document before attempting a 'replace' action to avoid wasting turns on a task that may have already been completed or is based on a faulty premise.
- **Deferred Tasks are Forgotten Tasks:** The overwatch critique correctly identified that I deferred fixing the 'route_planner' tool. Any identified bug or necessary maintenance must be performed in the immediate next turn, overriding other gameplay actions.
- **Verify Location Post-Warp/Event:** I hallucinated my location after leaving the mart, which was interrupted by a phone call. I MUST verify my `current_map_id` and `current_position` after every map transition or unexpected event to prevent critical planning failures.
- **Immediate Data Hygiene is Non-Negotiable:** Forgetting to mark the defeated Sage at (2, 7) caused me to waste multiple turns attempting to re-battle him. All defeated trainers, used warps, and confirmed dead ends MUST be marked immediately.
- **Trust Agent for Tool Repair:** My manual attempts to fix `select_move` and `switch_pokemon` repeatedly failed. Escalating to the `python_code_debugger` agent was the correct and most efficient way to get a robust solution. Do not get stuck in a loop of failed manual debugging.
- **Trust Observation Over Faulty Agents:** If an agent provides a solution that contradicts the observable game state (e.g., suggesting a path through a wall), the agent's logic is flawed. I must trust my own direct observation and prioritize refining the faulty agent over attempting to follow an impossible instruction.
- **Tool Limitations vs. Puzzle Logic:** My `route_planner` is unable to navigate the Ecruteak Gym because the puzzle relies on hidden logic (a single safe path) that isn't represented in the basic tile data. For puzzles with invisible paths or traps, automated pathfinding is unreliable. Manual, step-by-step exploration and hypothesis testing is the correct strategy.
- **Notepad Edit Failures:** Repeated `notepad_edit` failures are often caused by providing inexact `old_text`. I must verify the exact text or accept that the edit may have already succeeded despite an error message, which would indicate a hallucination on my part.
- **Warp Hallucination:** I hallucinated a warp at (13, 17) in Ecruteak City. I MUST verify a warp's existence in `Game State Information -> Map Events -> Warps` before setting it as a navigation goal to prevent this critical error.
- **Hallucination Recovery:** When a system warning corrects my location, I must immediately discard my previous flawed plan and re-evaluate my next action based on the correct information. Attempting to continue with a plan based on a hallucinated state is a critical failure.
- **Tool Failure (select_item):** The tool failed catastrophically because it was based on two hallucinations: a non-existent Key Item list and incorrect circular scrolling logic. Lesson: I MUST verify basic UI mechanics through simple, manual tests before committing to building complex automation.

## Navigation & Exploration
- **Visual Path Verification:** Before executing a move, I must visually confirm the path on the ASCII map and game screen to avoid simple navigational errors like walking into walls. This supplements tool-based pathfinding.
- **Pathing Interruption:** Even short, automated paths can be interrupted by moving NPCs. Proactive stunning is the most reliable strategy to ensure path execution and successful interaction.
- **Moving NPC Blockades:** If a path is repeatedly blocked by a moving NPC, stop recalculating the path. The most efficient solution is to use `stun_npc` to freeze them in a favorable position and then proceed.
- **Movement Loop Breaking:** When stuck in a movement loop or repeatedly blocked, changing the immediate navigation target is an effective strategy to break the cycle and find a new, clear path.
- **Pathing Near Hazards:** When navigating near multiple hazards (like adjacent pits), automated pathing can be unreliable if interrupted. To avoid repeated errors, break down the path into smaller, manually-controlled segments for the final, critical steps to ensure precise positioning.
- **Automated Path Vetting:** Automated paths, especially from `plan_systematic_search_path`, can unintentionally lead into warps. I MUST visually inspect the generated coordinate list for known warp tiles before executing the path to avoid accidental map transitions.
- **Map Transition Failures:** If a map transition (like walking into a boundary wall) fails repeatedly (3+ times), the root assumption about how to trigger it is wrong. Do not continue repeating the failed action. Immediately pivot to a different objective or explore alternative routes. This is a critical lesson from the Route 39 blockage.
- **IMMEDIATE OBSTACLE MARKING:** I failed to mark Sailor Huey as a blocker, causing me to waste time retrying a failed path. All critical obstacles MUST be marked with '🚫' immediately upon discovery to prevent loops.
- **Re-Exploration Strategy:** When all forward paths are confirmed dead ends, the solution may be in a previously visited area. Do not assume re-exploring is inefficient; a missed item, NPC, or trainer could be the key to progression.

## Puzzle Solving & Logic
- **Challenge Assumptions:** My progress in the lighthouse was blocked by my own assumption that all pits were traps. I must systematically test all environmental possibilities, even those that seem like dead ends or hazards, as they might be the intended path forward. Falsifying my own root hypotheses is critical to avoiding puzzle loops.
- **Challenge False Constraints:** My loop was prolonged by the false assumption that a solution *had* to be on the eastern side of 2F. When stuck, I must identify and challenge the root assumption that is constraining my strategy.
- **Test All Variables:** When a puzzle has multiple similar elements (like the two pits in the lighthouse), they may not be functionally identical. Systematically test each one to ensure you don't miss a unique solution.
- **Abandon Failed Hypotheses Quickly:** If a puzzle element fails multiple simple tests (e.g., a suspected warp doesn't trigger on step-on, interaction on tile, or interaction from adjacent tile), I must abandon the hypothesis immediately. Mark the area as a dead end (🚫) to avoid getting stuck in unproductive testing loops.
- **Internal vs. External Puzzles:** When all paths inside a puzzle area (like the lighthouse) are confirmed dead ends, the solution is likely external. I must expand my search area instead of getting stuck in an internal loop.
- **Challenge Root Hypotheses:** When stuck or pursuing an overly complex strategy, the root assumption is likely flawed. Aggressively re-verify the foundational belief that led to the current strategy instead of just refining the failing strategy itself.
- **Non-Linear Puzzles:** Puzzle solutions are not always linear; moving 'backwards' or 'down' (like a pit) can be the correct way forward, especially when the obvious 'up' path is a confirmed dead end.
- **Logical Loop Breaking:** When stuck in a repetitive loop exploring a confirmed dead end, the root assumption is likely flawed. I must escalate to an agent or fundamentally change my strategy (e.g., by exploring a different floor) instead of repeating failed tests.
- **Escalate Vertically:** When stuck in an exploration loop on a given floor and the floor below, the solution is likely on a floor *above*. I must challenge the assumption that the path forward is nearby and be willing to ascend to find a way down into inaccessible areas. This was the key insight from my `puzzle_solver` agent regarding the lighthouse.
- **Red Herring Passages:** A hidden passage is not a guaranteed path forward. The secret passage on Olivine Lighthouse 5F at (8, 7) led to a confirmed dead end. If a new path quickly proves fruitless, I must be willing to backtrack immediately rather than assuming there's a deeper puzzle.
- **External Triggers:** When all internal solutions to a puzzle are exhausted (e.g., the lighthouse entrance), the trigger is likely external. Do not get stuck in a loop; expand the search area.
- **Value of Brute-Force Automation:** When visually stuck, a systematic, automated search can reveal paths or triggers that are easily missed by manual exploration. It's a valid strategy for breaking through a perceived dead end.
- **Internal Triggers:** When all external paths from a location are confirmed dead ends, the solution is likely an internal change within that area, triggered by a recent major event (like a key conversation).
- **Methodical Puzzle Testing:** When testing a hypothesis with multiple steps (e.g., checking all directions), I must systematically test each step, document the outcome in my notepad, and only conclude the entire hypothesis has failed after all steps have been exhausted.
- **Agent Escalation:** When multiple self-generated hypotheses for a puzzle have failed, especially after getting stuck in a repetitive loop, I must escalate to a more powerful problem-solving tool like an agent. This is critical for breaking cognitive fixation.

## NPC & Object Interaction
- **NPC Interactions:** Some interactions, like battling a trainer, can be multi-step. Ensure all initial dialogue is cleared with 'A' presses before the main event (like the battle) will trigger. Non-Battling NPCs: Not all moving NPCs are trainers. If an NPC's dialogue repeats without initiating a battle after multiple interaction attempts (direct, line-of-sight), they are likely a non-battling character. Do not get stuck in an interaction loop; update markers and move on.
- **Dialogue & Movement:** I must ensure all dialogue boxes are closed by pressing 'A' before attempting any movement inputs. Trying to move with text on screen will fail.
- **Interaction vs. Line of Sight & Flawed Assumptions:** If direct interaction with a trainer-like NPC results in a dialogue loop (like with Sailor Huey), the battle trigger might be line of sight. However, I must first challenge the root assumption that a battle is necessary at all. I wasted significant time trying to force an interaction when a simple path around the NPC existed. Lesson: Always verify if an obstacle is truly blocking the path before attempting to resolve it through complex interactions or battles. Check for alternative routes first.
- **Interaction Loops:** If repeated 'A' presses (2-3 times) on an NPC or object do not advance the game state (dialogue, battle start, etc.), the interaction is likely stuck. Do not continue pressing 'A'. Break the loop by performing a different action, such as moving one tile away and back, to reset the state before attempting to interact again.
- **Trust NPC Guidance:** External NPC confirmation (like the Gym Guide directing me to the lighthouse) must override my own flawed assumptions or conclusions that a path is a dead end. I must re-investigate any such location with the new information.
- **Challenge NPC Dialogue:** Do not blindly trust NPC dialogue that suggests a path is a dead end, especially if it blocks the only apparent way forward. Always verify with your own systematic exploration.
- **Trust Physical Evidence Over Dialogue:** A sign on Route 39 claimed it connected to Ecruteak City. My initial exploration suggested the path north was a dead end, but this was incorrect. The path does continue north, connecting to Route 38. Lesson: Thoroughly explore all paths before concluding they are dead ends.
- **Interaction Pre-check:** Before pressing 'A' to interact with any NPC or object, I must first perform a pre-check: verify my character is standing on an adjacent tile AND is facing the target directly. Wasting a turn on a failed interaction due to poor positioning is a critical error.
- **Safe Interaction Positioning:** When planning to interact with the tile you are standing on (e.g., searching for a hidden switch), first turn to face a solid, non-hazardous adjacent tile (like a WALL) before pressing 'A'. This prevents accidental movement into hazards like pits.
- **NPC Movement Triggers:** Moving NPCs may not move on a passive timer. Their movement can be triggered by the player's proximity or by walking into their line of sight. If an NPC is blocking a path, attempting to approach them can be a valid strategy to make them move.

## Tool & Agent Management
- **Tool Definition Errors:** If `define_tool` fails with an 'identical script' error, it means the proposed change has already been successfully applied in a previous turn. Do not retry the same definition; proceed with the next action.
- **Agent-based fixes must be verified in both simple and complex scenarios before a tool is considered fully functional. A fix for one case may not cover all failure conditions.
- **Tool Input Verification:** Before concluding a tool is broken (e.g., `route_planner` returning 'No path found'), I must first verify that my inputs and assumptions are correct. Pathing to an 'unseen' tile is an invalid input, as the tool correctly treats them as impassable. My strategy must adapt to the tool's logic.
- **Notepad Edit Precision:** When using `notepad_edit` with the `replace` action, the `old_text` must be an exact match. If an edit fails because the text is not found, it's possible the change was already successfully applied in a previous turn. Verify the current notepad content before retrying.
- **Trust Markers Over Tools:** If my map markers indicate a path is blocked by an NPC, I must trust that information over a `route_planner` result, as the tool cannot see off-screen NPCs. Do not attempt to path through known blockades.
- **Immediate State Cleanup:** I must remember to perform immediate cleanup actions, like unstunning a non-critical NPC, as soon as the need for the stun is over. Deferring these tasks can lead to them being forgotten.
- **Tool Glitch Recovery:** If a tool repeatedly fails with a bizarre error despite the code appearing correct (like a `ModuleNotFoundError` for a valid library), force a re-definition of the tool with a new commit message to clear any cached or corrupted state.
- **Tool Context-Dependency:** A tool's logic may be based on assumptions that are not universally true. The `route_planner` tool assumed all `LADDER` tiles were warps, which failed on the Olivine Port pier where they are walkable. Lesson: Always be prepared to refine tools when they encounter new game contexts that violate their core assumptions.
- **Tool Maintenance Protocol:** If a tool fails, it MUST be fixed immediately. Do not attempt to re-use a known faulty tool. After applying a fix, especially one from an agent, the tool's functionality must be verified with a simple, direct test case before being trusted for critical tasks. Repeated failures indicate a deeper issue with the tool's logic or its underlying assumptions (like a hardcoded list being incorrect).

## Battle & Resource Management
- **Inventory Pre-check:** Before starting a resource-dependent task (like catching Pokémon), I must verify I have the necessary items (e.g., Poké Balls). Running out mid-task is a critical failure of preparation.
- **Blocked Movement vs. Battle Start:** A 'Movement Blocked' alert does not guarantee a wild battle has started. I must wait for the battle screen text to appear before assuming I am in a battle and pressing 'A' to advance dialogue. This prevents wasted turns from incorrect assumptions.
- **Struggle Mechanic Failure:** Repeatedly selecting a 0 PP move does not trigger Struggle in this game. If a Pokémon runs out of PP, the only viable options are to switch out or use an item. Do not get stuck in a loop trying to force Struggle.
- **Resource Management:** Avoid inefficient battles (e.g., against high-defense, low-EXP opponents) that drain PP for minimal gain. Running away is often the more strategic option to conserve resources for more important fights or exploration.
- **Type Disadvantage Switching:** When a Pokémon is facing an opponent with a significant type advantage (e.g., Rock/Ground vs. Fighting), switching out is not just an option, it's a critical necessity to avoid taking massive damage or being knocked out. Preserving HP is key.

# CURRENT QUEST: Get the SECRETPOTION for Amphy.

# STRATEGIC KNOWLEDGE BASE

## Game Mechanics & Systems
- **Day/Night Cycle:** An important mechanic, affecting events.
- **POKé BALLS:** Received 5 from the scientist in Elm's Lab. Can now catch wild Pokémon.
- **PC Storage:** Used for Pokémon and item storage in Pokémon Centers.
- **BERRY Trees:** Grow new BERRIES every day.
- **Healing:** Pokémon Centers restore all HP/PP and cure status conditions.
- **Game State Updates:** Map data (like a `CUT_TREE` changing to a `FLOOR`) doesn't fully update until all on-screen text is cleared. Using tools like `route_planner` before the overworld is fully interactive will use stale data and fail.
- **HEADBUTT Mechanic:** Can be used outside of battle on `HEADBUTT_TREE` tiles to encounter sleeping Pokémon.
- **Evolution Methods:** Some Pokémon (MACHOKE, KADABRA, HAUNTER, GRAVELER) evolve when traded.
- **`stun_npc` Mechanic:** The stun effect is very short-lived and resets when leaving and re-entering a map. The tool will also fail if the target NPC is not currently on-screen and rendered in the game.
- **Rematch Mechanic:** Some trainers will call for a rematch via the Pokégear. Interacting with them after a call will trigger a new battle. My previous assumption that trainers could only be fought once was incorrect.
- **Roaming Legendaries:** Encounters with Pokémon like Entei can be random. They may flee on the first turn, even if the player's attempt to run fails.

## Tile & Object Mechanics
- **BOOKSHELF**: An impassable object.
- **BUOY**: An object found in water. Appears to be impassable, functioning like a WALL tile within a WATER area.
- **CAVE**: A traversable warp tile that functions as an entrance to a cave.
- **COUNTER**: Impassable terrain, usually a barrier in front of an NPC. To interact with NPCs behind counters, face the counter tile directly in front of them and press A.
- **CUT_TREE**: An impassable tree that likely requires the HM move Cut to remove.
- **DOOR**: A traversable warp tile leading into or out of a building.
- **Ecruteak Gym Floor**: Appears as a PIT, but is a traversable FLOOR tile that forms an invisible path. The path is revealed by defeating trainers.
- **FENCE (Visual):** The fence-like structure on Route 38 at (30, 11) is functionally an impassable `WALL` tile.
- **FLOWER**: Fully traversable decorative tile.
- **FLOOR**: A standard, fully traversable tile.
- **FLOOR_UP_WALL**: Confirmed impassable when trying to move onto it from an adjacent tile below.
- **FRUIT_TREE**: An impassable, interactable object. Gives one BERRY item when interacted with for the first time.
- **GRASS**: Fully traversable tile, similar to TALL_GRASS. Wild Pokémon can be encountered here.
- **HEADBUTT_TREE**: An interactable tree, requires the Headbutt move. Impassable.
- **INCENSE_BURNER**: An impassable decorative object.
- **Item Interaction:** The game requires a specific item type for some interactions. The sick Miltank needs a generic 'BERRY' and will not accept functionally similar but differently named items (e.g., 'MINT BERRY'). This was confirmed by the interaction prompt.
- **LADDER:** Can function as a standard traversable tile (e.g., on a pier) or a warp tile. Its function must be verified by checking for a <Warp> child element in the map XML. Activation methods are complex and context-dependent. **Burned Tower B1F Anomaly:** The ladder at (10, 8) is NOT a simple step-on warp. Failed tests include: stepping on and pressing 'Up', stepping on and pressing 'A', interacting from adjacent tile (9, 8), entering from below (10, 9 -> 10, 8), and entering from above (10, 7 -> 10, 8). The solution is not a simple, direct interaction.
- **LEDGE_HOP_DOWN/LEFT/RIGHT**: One-way traversable tiles.
- **LONG_GRASS**: Fully traversable tile. Wild Pokémon can be encountered here.
- **MART_SHELF**: Impassable terrain, functions like a wall.
- **PC**: An interactable object used to access the Pokémon Storage System. Impassable.
- **PLANT**: A decorative object that functions as an impassable WALL tile.
- **RADIO**: An impassable object.
- **SIGN**: An impassable, interactable object. Functions as a wall.
- **STAIRCASE**: A traversable warp tile that moves the player between floors.
- **TALL_GRASS**: Fully traversable tile. Wild Pokémon can be encountered here.
- **TOWN_MAP**: An interactable object on a wall; impassable.
- **TV**: An impassable object.
- **unseen**: A tile that has not yet been explored. Its properties are unknown until visited. It is treated as impassable by pathfinding tools.
- **unknown**: A tile type whose properties have not yet been observed. It is treated as impassable by pathfinding tools until its true nature is revealed.
- **VOID**: An impassable tile type found at the edges of some maps, functions as a wall.
- **WARP_CARPET_UP/DOWN/LEFT/RIGHT**: A traversable warp tile at the edge of a map that transitions to the adjacent map.
- **WARP_CARPET_DOWN (Anomaly):** The `WARP_CARPET_DOWN` tile at Union Cave (17, 3) was confusing. A manual 'Down' press failed due to a wall, but an automated path through the same tile succeeded in warping me. The exact mechanic is unclear and needs further investigation.
- **Warp (FLOOR):** A special tile type that appears to be a normal FLOOR tile but also functions as a warp. Observed as landing zones after falling through a PIT.
- **Warp (WALL):** Observed in Burned Tower. Appears to be a WALL tile that also functions as a warp. Its activation method is currently unknown.
- **WATER**: Impassable terrain without a specific HM (likely Surf).
- **WINDOW**: An impassable object that can be interacted with to display text. Functions like a wall.
- **NPC Objects (TEACHER, LASS, etc.)**: These are impassable and function as walls.
- **Verify Interaction Methods:** Do not assume all objects of the same type (e.g., ladders) have the same activation method. If a simple interaction (step-on, 'A' press from adjacent tile) fails, the object may require a different, non-obvious trigger. Systematically test and document interaction attempts.
- **PIT (Context-Dependent):** This tile's function varies by location.
  - **Olivine Lighthouse:** One-way warp downwards.
  - **Burned Tower:** Inactive puzzle element, requires an external trigger (defeating rival).
  - **Ecruteak Gym:** Confirmed to be one-way warps that send the player back to the gym entrance area.

## Battle Mechanics
- Pokémon holding a BERRY can automatically use it to heal themselves when their HP gets low in battle.
- Poisoned Pokémon lose 1 HP every four steps outside of battle and remain poisoned after a wild battle concludes.
- Accuracy-lowering moves like SMOKESCREEN are not a guaranteed defense.
- The auto-activation threshold for a held BERRY is likely below 25% HP.
- A single high-level Pokémon cannot carry an entire under-leveled team through a major battle like a Gym.
- Levels Over Type Advantage: A significant level disparity can completely negate type advantages.
- Low-HP Threat: A low-HP Pokémon with a status move like Hypnosis is still a major threat.
- Type Immunity vs. Level Disparity: Type immunity is not a guaranteed defense against a much higher-level opponent.

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

## Menu Navigation
- For complex menu inputs (like on-screen keyboards), perform all directional movements in one turn and the final confirmation ('A' button) in the next.
- In the party screen, the 'SWITCH' option is used to reorder Pokémon. The 'MOVE' option is for reordering a Pokémon's moves.
- The main battle menu options are laid out in a 2x2 grid: FIGHT (top-left), PKMN (top-right), PACK (bottom-left), RUN (bottom-right).

# LORE & DIALOGUE
- **Hiker Anthony (Phone):** Confirmed that DUNSPARCE are found in DARK CAVE in large numbers, specifically in areas where there are no strong POKéMON.
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
- **Officer in Route 32 Gatehouse:** Said "RUINS OF ALPH".n- **Route 32 Sign at (13, 5):** Reads 'ROUTE 32, VIOLET CITY - AZALEA TOWN'.
- **GRAMPS in Route 36 Gatehouse:** Mentioned the strange tree was the reason fewer people were visiting the RUINS OF ALPH.
- **FISHER on Ecruteak City (9, 22):** Heard a rumor that the Pokémon at the Olivine Lighthouse is sick.
- **Fisher in Olivine Pokémon Center:** A sailor in the Olivine Cafe next door can teach the move STRENGTH, which can move big boulders.
- **Teacher in Olivine Pokémon Center:** Mentioned a person in Cianwood City, across the sea, who has a rare POKéMON.
- **POKEFAN_F on OlivineLighthouse1F (16, 9):** Mentioned that in the past, Pokémon were used to light the sea at night, and the lighthouse was built in their honor.
- **Gentleman on OlivineLighthouse2F (17, 8):** The sick Pokémon at the top needs 'special medicine'.
- **COOLTRAINER_M in EcruteakItemfinderHouse:** Mentioned finding items in the BURNED TOWER.
- **COOLTRAINER_F in Ecruteak Pokémon Center:** "MORTY, the GYM LEADER, is soooo cool. His POKéMON are really tough too."
- **GYM_GUIDE in Ecruteak Pokémon Center:** Mentioned a 'GYARADOS swarm' at the 'LAKE OF RAGE' and a potential 'conspiracy'. This seems like a major plot point.

# KEY ITEMS & TMs
## Key Items
- **HIVEBADGE:** From Bugsy. Allows traded POKéMON up to L30 to obey and enables the use of CUT outside of battle.
- **POKéDEX:** A high-tech encyclopedia from PROF. OAK to record POKéMON data.
- **HM05 FLASH:** Obtained from the Elder of Sprout Tower. Illuminates dark caves. Requires the Zephyr Badge to use outside of battle.
- **HM01 CUT:** Obtained from the charcoal maker in Ilex Forest. Allows cutting small trees outside of battle. Requires the Hive Badge.
- **PLAINBADGE:** From Whitney. Boosts POKéMON's Speed and allows the use of STRENGTH outside of battle.

## TMs
- **TM12 SWEET Scent**
- **TM31 MUD-SLAP**
- **TM39 SWIFT**
- **TM45 ATTRACT**
- **TM49 FURY CUTTER**
- **TM08 ROCK SMASH:** Received from a man on Route 36 after a battle.

# Crafting
- Kurt in Azalea Town can make special POKé BALLS from APRICORNS. I received a LURE BALL from him as an example.

# Solved Puzzles
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
- **Root Cause Analysis:** My progress was catastrophically stalled by a single, flawed root hypothesis: "The way forward MUST be in the western section of the lighthouse." I failed to trust my `route_planner` tool, which repeatedly and correctly told me the western and eastern sections were disconnected on floors 3 and 4. Instead of trying to falsify my hypothesis (e.g., by immediately attempting a strategic retreat to a lower floor), I spent dozens of turns in a loop, trying to force a path that didn't exist. The western column is a confirmed dead-end loop.
- **Hypothesis 1 (Two Pits):** FAILED. Tested both pits on 2F at (16, 13) and (17, 13). Both lead to the same dead-end exit room on 1F. This is not the path forward.
- **Descending Path Fallacy:** Just because a path goes down (like a pit) does not mean it leads to progress. As seen in the Olivine Lighthouse, some descending paths are simply one-way exits or resets designed to force the player to restart the ascent. I must evaluate these paths critically and not assume they are the correct way forward.
- **Agent Hypothesis #2 (Hidden Item on 2F Ledge):** FAILED. Systematically searched every tile on the exterior ledge connecting the western and eastern sides of 2F. No hidden items or switches were found. This path is not the solution.

### Moomoo Farm Puzzle Solution
- The sick Miltank needs to be fed 'lots o' BERRIES' to get better. This was confirmed by the farmer. The FRUIT_TREE at (9, 3) on Route 39 only gives a MINT BERRY and is not the solution.

### Burned Tower Puzzle
- **Hypothesis 1 (Pits are step-on warps):** FAILED. Stepping on the pit at (5, 14) did not trigger a warp.
- **Hypothesis 2 (Pits are 'A' press warps):** FAILED. Pressing 'A' while standing on the pit at (5, 14) did not trigger a warp.
- **Hypothesis 3 (Boulders are obstacles):** The boulders in the tower might be movable with Strength, opening new paths.
- **Puzzle Solution:** Defeating my rival, SILVER, on the first floor caused the floor to collapse, revealing the basement and the legendary beasts.

# Obstacles and Solutions
- A strange tree blocks the road north of Goldenrod City (Route 35). It can be cleared using a SQUIRTBOTTLE, which is obtained from the Flower Shop after defeating Whitney. The Lass in the shop confirms this is the correct sequence of events.
- **Rival on Route 40:** Confirmed that interacting with SILVER on Route 40 after accepting Jasmine's quest does not trigger a battle or make him move. He remains a static blocker.

# Held Items
- **QUICK CLAW:** Received from a Teacher in the National Park. When held by a Pokémon, it may allow them to attack first in battle.

# PC Inventory
- **Box 1:**
  - Hestia (MAGBY), Lv15, Female

# Rematch Opportunities
- Hiker Anthony on Route 33 called for a battle.
- Youngster Joey on Route 30 called for a rematch.
- Sailor Huey at the Olivine Lighthouse called for a rematch.

# Solved Puzzles
### Ecruteak Gym Puzzle
- **Agent Hypothesis #1 (Talk to Sage):** FAILED. Interacted with the Sage at (3, 13) after defeating Morty. The dialogue was generic and did not provide a clue or unblock the path.

# Reflection Updates (Turn 38569)
- **VOID Tile:** An impassable tile type found at the edges of some maps, functions as a wall.
- **NPC Challenge Verification:** When a challenge involves multiple similar-looking NPCs (like the Kimono Girls), do not assume they are all trainers. Test each one with interaction to confirm their role before committing to a path, as some may be non-battling characters.

# Custom Tools & Agents
- **route_planner:** Reliable pathfinding tool.
- **select_move:** Selects a move in battle.
- **switch_pokemon:** Switches Pokémon in battle.
- **find_reachable_unseen_tiles:** Finds all 'unseen' tiles that are actually reachable from the player's current position on the current map.
- **select_item:** Automates selecting a specific item from the bag menu.
- **python_code_debugger (Agent):** Debugs my Python scripts.
- **puzzle_solver (Agent):** Helps with in-game puzzles.
- **select_battle_option:** (Built-in) Selects a main battle menu option (FIGHT, PKMN, PACK, RUN).

# Reflection Updates (Turn 38621)
- **WALL Tile:** A standard, impassable tile type that blocks movement.
- **Tool Logic Lesson (UI Parsing):** My `switch_pokemon` tool failed because its text parsing was too general, incorrectly identifying non-selectable headers as menu items. The agent's fix confirmed that relying on stable, structural UI cues (like cursors '▶' or indentation) is far more robust than parsing based on text content alone. This is a critical lesson for all future UI automation tools.
- **Immediate Task Execution:** Maintenance tasks (tool fixes, notepad organization) must be performed the moment they are identified, overriding any immediate gameplay actions. Deferring them leads to errors and wasted turns.

# TOOL BUG REPORT (Turn 38803)
- **Tool:** `switch_pokemon`
- **Symptom:** Returned an empty string when trying to switch to 'CHRONO' in battle. Failed to generate button presses.
- **Immediate Action:** Switched manually to proceed with battle.
- **TODO:** Must investigate and fix this tool using `python_code_debugger` as soon as possible. The current parser is likely failing on the two-line party member format.