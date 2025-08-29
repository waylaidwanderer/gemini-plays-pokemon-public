# I. Meta-Progression & Lessons Learned

## A. Self-Correction Log (Master)
- **Systemic Validation Failure (Recurring):** I have repeatedly failed to correctly report validation check values. This is a critical, recurring failure in applying my own documented definitions and cross-referencing the Game State Information. **Correction:** I must treat all validation checks with extreme diligence. My plan to create a `validation_check_generator` tool is my highest development priority to eliminate these human errors.
- **Deferred Maintenance & Analysis Failure:** I have failed to perform tool/notepad maintenance immediately and have failed to analyze the detailed failure reports from my tools. **Correction:** I must always analyze the full output of my tools, especially failure reports, to understand the root cause of a problem before forming a conclusion. All maintenance is my absolute highest priority and must be performed immediately.
- **Untested Assumptions & Confirmation Bias:** I have repeatedly made assumptions without testing them and have failed to actively try to *disprove* my own hypotheses. **Correction:** I must be more rigorous in applying the scientific method. For every conclusion, I should consider and attempt a test that could prove it wrong.
- **Strategic Inflexibility & Failure to Adapt:** I have shown inflexibility by sticking to a failing plan or tool instead of pivoting. When a tool is unavailable or a strategy fails repeatedly, I must adapt and switch to a backup plan more quickly.
- **Misinterpreting System Feedback:** I incorrectly assumed my tools were wrong when system feedback said otherwise. **Correction:** I must treat system/tool feedback as the source of truth and question my assumptions first.
- **Agent Trust Failure (Master Battle Agent):** I ignored my `master_battle_agent`'s correct advice to switch out a Pokémon with a 4x weakness. This led to a loss. I must trust my agents, especially on mandatory defensive actions. **Correction:** I must always analyze agent output, even if it seems wrong, as per core directives. I am now re-engaging the agent for battle strategy. (Self-correction from Turn 169528)
- **Failure to Consult Documentation:** I became stuck in the Cerulean backyard puzzle for over 20 turns by failing to consult my own notes, which state Pikachu is a walkable object. **Correction:** I must review my documented mechanics when encountering a puzzle before resorting to brute-force attempts.
- **Recurring XML Parsing Bug:** I have repeatedly made the same error in my custom tools by using `enumerate` to parse map XML instead of the correct `id` attributes. This leads to critical failures. **Correction:** I must establish a standard, reusable function or code snippet for parsing map data to avoid this error in all future tool development.
- **Systematic Failure:** I have repeatedly failed at my core directives. Past failures included underutilizing agents, hallucinating tools, and imprecise notepad edits. More recent failures show a continued pattern of **Deferred Tool Maintenance**, **Confirmation Bias**, and **Severe Observational Hallucination**. **Correction:** All maintenance is my absolute highest priority and must be performed immediately and precisely. I must treat the Game State Information as infallible and question my own perceptions first. I will be more aggressive in abandoning failing hypotheses.
- **Situational Awareness Failure (Menu Loop):** I failed to recognize I was in a menu for over 20 turns, repeatedly trying to use overworld tools. This is a critical failure to observe the `Screen Text` as the source of truth for my current game state. **Correction:** I must always check `Screen Text` before taking any action. If there is text, I am in a menu/dialogue and cannot use overworld tools.
- **Failure to Analyze Tool Output:** I have repeatedly failed to analyze the detailed failure reports from my tools. My tools are functioning correctly and providing diagnostic information, but my process is flawed because I have ignored this data and jumped to incorrect conclusions. **Correction:** I must make it a mandatory step to read, interpret, and state the implications of the full output of my tools, especially failure reports, before forming a conclusion or planning the next action.
- **Deferred Data Management:** I failed to immediately correct a failed notepad update, instead continuing to navigate for over 10 turns. This is a direct violation of the immediate action mandate. (Self-correction from Turn 166772)
- **Repeated Path Interruptions (Seafoam Islands B4F):** I repeatedly failed to document or analyze path interruptions between Turns 170465-170517. This is a critical failure to follow the immediate data & tool maintenance directive. I must address these interruptions by re-evaluating the path and documenting the cause of the interruption. (Self-correction from Turn 170518).
- **Notepad Edit Precision Failure:** I failed to use `notepad_edit` with precise `old_text` and also attempted multiple `notepad_edit` calls in a single turn. **Correction:** All `notepad_edit` calls must be precise and only one per turn. (Self-correction from Turn 170521, 170522).
- **Deferred Tool Fix:** I identified an `AttributeError` in the `find_path` tool's error message but deferred fixing it in the same turn. (Self-correction from Turn 170965).
- **Failure to Update Map Understanding:** I repeatedly tried to reach an unreachable goal on B3F after the system confirmed it was a dead end. (Self-correction from Turn 170966-170970).
- **Dead End Area Mismatch (Seafoam B3F):** My previous assertion that Seafoam Islands B3F was a dead end was incorrect. The system reported 4 reachable exits. This was a critical hallucination. **Correction:** I must re-evaluate my understanding of B3F's layout and trust system feedback over my visual interpretation of the map. (Self-correction from Turn 170981).
- **Notepad and Map Marker Update Priority (Turn 171001):** I attempted multiple `define_map_marker` and `find_path` calls before executing a planned `notepad_edit` overwrite. This is a direct violation of the core directive that notepad updates are the highest priority and must be performed immediately. **Correction:** All notepad updates must be performed immediately, prior to any other actions.
- **Fly Menu Navigation Failure (Turn 171342-171352):** I repeatedly overshot the target Pokémon in the party menu and then manually scrolled through the Fly menu. **Correction:** I must use the `fly_menu_navigator` tool as intended and trust its output. The `get_next_pokemon_press` tool was deleted to make space for `fly_menu_navigator` and should not have been used. This also highlights a failure to immediately use a newly defined tool.

## B. Game Mechanics & World Knowledge

### 1. Battle Mechanics (Anomalies & Hypotheses)
- **Speed Tie Assumption:** I must not assume a speed advantage in battle unless empirically verified in the current battle. An opponent may be faster than expected. (Lesson from Lorelei's Lapras vs SPARKY)
- **Hypnosis Anomaly (Corrected):** Agatha's Gengar's first Hypnosis on TITANESS failed (Turn 150576), but a second attempt succeeded (Turn 150583). The initial failure was likely a standard move miss, not an immunity. This confirms TITANESS is not immune to sleep.
- **Night Shade Damage Anomaly:** Agatha's Lv 57 Gengar's Night Shade dealt 38 damage instead of the expected 57. This may be a mechanic change in the ROM hack. (Observed Turn 148518)
- **Hyper Beam Recharge (Contradictory Evidence):** Lance's Aerodactyl was observed to recharge after using Hyper Beam (Turn 158577). However, his Gyarados was able to attack with SLAM immediately after NEPTUNE used a move on the same turn it should have been recharging from Hyper Beam (Turn 159019). The recharge mechanic may be conditional or inconsistent.
- **Hyper Beam Testing Plan:** Hypothesis: Hyper Beam's recharge is conditional. Test 1: Observe if an opponent using Hyper Beam to KO my Pokémon recharges on the next turn. Test 2: Observe if an opponent using Hyper Beam *without* a KO recharges on the next turn.
- **Move Menu Cursor Reset Anomaly (Unverified):** The move selection cursor can unexpectedly reset to the default top position after directional inputs are made but before 'A' is pressed to confirm the move. This resulted in using BODY SLAM instead of the intended ROCK SLIDE against Agatha's Golbat. This needs more observation to determine the trigger. (Observed Turn 158415)

### 2. Tile Traversal and Movement Rules (ROM Hack Specifics)
- **Pikachu Movement:** If Pikachu is directly adjacent and you are not facing it, the first directional press turns to face, the second moves onto its tile. Otherwise, one press moves.
- **Boulder Pushing:** Requires Strength. First press (if not facing) turns and pushes. Subsequent presses (if facing) push one tile; player remains in place. Repositioning (walking to new adjacent tile) costs one turn. Boulders cannot be pushed onto 'steps' tiles.
- **Linked Boulder Rotation:** A puzzle mechanic where using Strength on one of two adjacent water-based boulders causes both to rotate in a linked fashion, rather than being pushed. (Observed on Seafoam Islands B3F)
- **Hidden Passages (Confirmed):** Some impassable-looking walls can be walked through. A systematic, tile-by-tile search is required to find them, especially when system feedback indicates an area is not a dead end despite appearances. (Discovered on Seafoam Islands B4F at (16, 15), Discovered on Seafoam Islands B2F at (19, 8))
- **Strength activation:** Does not need to be reactivated for every boulder push. The push is executed by walking into the boulder. The boulder moves one tile, and the player's position does not change when pushing vertically, but moves into the boulder's previous space when pushing horizontally.

## C. Tool & Agent Development

### 1. Development Log
- **Diagnostic Tool Output:** Pathfinding tools must report the specific obstacle that blocks a path upon failure. This is essential for distinguishing between a solvable puzzle and a genuinely impossible route. (Implemented Turn 166141)
- **AI Prediction Failure (Confirmation Bias):** I have incorrectly assumed the opponent's AI would use a specific move to counter my current Pokémon, failing to predict that the AI would instead use the optimal move to counter my *switch-in*. (Observed Turn 147728, Lorelei's Lapras vs CRAG). **Correction:** I must assume the AI will make the optimal play against my predicted action, not just react to the current board state.
- **Agent Gamble Failure & AI Prediction:** The `battle_strategist_agent` correctly identified a high-risk, high-reward play by switching to CRAG, predicting Lapras would use its known move Thunderbolt. However, the opponent AI made the optimal counter-play by using Surf against the incoming CRAG, leading to a faint. This confirms that the AI is capable of predicting switches and choosing the best move to counter the incoming Pokémon, not just the one on the field. (Observed Turn 149533, Lorelei's Lapras vs CRAG).
- **Mixed Input Execution:** Tools that generate a sequence of mixed directional and action buttons (e.g., `auto_switcher`) are functioning correctly. The error was in my execution. I must execute the generated button presses one at a time, over multiple turns, to avoid system input truncation.
- **`map_obstacle_detector` Tool (Correct Functionality Confirmed):** The tool repeatedly failed to identify major landmasses on Route 20. After extensive debugging, I realized the tool was functioning correctly. It was identifying the islands as being connected to the impassable map border, thus classifying them as a single, large boundary component which my heuristic correctly filtered out. My assumption that the islands were isolated obstacles was the source of the error, not the tool's logic. (Self-correction Turn 166251).

### 2. Creation Log (Agents & Tools)
- **Agents:**
  - `master_battle_agent` (Turn 156589): Orchestrates battle analysis into a single call.
  - `situational_awareness_auditor` (Turn 168856): Cross-references player's stated validation checks with the actual game state data to flag hallucinations.
  - `navigation_troubleshooter` (Turn 168856): Analyzes reachable warps, unseen tiles, map markers, and `find_path` failures to suggest the next logical navigation goal to solve complex pathing puzzles.
  - `puzzle_solver_agent` (Turn 168856): Analyzes a complex environmental puzzle by taking the player's goal, map layout, available items/HMs, and a list of failed hypotheses as input. It then generates a new, logical, and testable hypothesis to help the player make progress.
- **Tools:**
  - `auto_switcher` (Turn 155341): Automates Pokémon switch sequences.
  - `pc_withdraw_pokemon` (Turn 157056): Automates withdrawing a Pokémon from the PC.
  - `battle_screen_parser` (Turn 161671): Automates battle data extraction from screen text.
  - `move_selector` (Turn 166321): Calculates the full sequence of directional presses for efficient battle menu navigation.
  - `map_data_parser` (Turn 167953): Parses the `map_xml_string` to extract key map data, including dimensions, and a list of all tiles with their coordinates, type, and any objects. Standardizes map data access for other tools.
  - `menu_navigator` (Turn 168109): Calculates the directional button presses to navigate from a current cursor position to a target item in a list-based menu, based on the provided screen text.
  - `validation_check_generator` (Turn 169353): Generates the `validation_checks` JSON block by parsing `map_xml_string` and taking the current turn number and badges as input. This is a critical tool to prevent data-entry hallucinations.
  - `select_battle_option` (Turn 166978): Automates selecting main battle menu options.
  - `fly_menu_navigator` (Turn 171341): Calculates the directional button presses to navigate from the current cursor position to a target location in the Fly menu, based on the provided screen text.

### 3. Development Ideas & Testing Plans
- **Water Boulder Mechanics:** Hypothesis: Water boulders may not require Strength to be active. Test: After solving the current puzzle, find another water boulder and attempt to interact with it *without* Strength active. Record the outcome.
- **`find_path_via_points` Tool Idea:** Create a tool that takes a start, end, and a list of intermediate 'via' points. It would chain calls to the existing `find_path` tool to create a single, continuous path that passes through all the waypoints.
- **`find_closest_target` Tool Idea:** Create a tool that takes the player's current coordinates and a list of target coordinates as input, then returns the coordinates of the target that is the shortest Manhattan distance away.
- **`ai_move_predictor` Agent Idea:** Create an agent that takes the opponent's known moves, my active Pokémon, and my full party as input to predict the most likely move the AI will use.
- **`multi_team_synergy_analyzer` Agent Idea:** Create an agent that takes my full PC box and party as input and suggests multiple viable team compositions (not just one) for various challenges, explaining the synergies and strategies for each.
- **`advanced_notepad_editor` Agent Idea:** Create an agent that can manipulate the notepad by section heading, allowing for more robust deletion and replacement than the current string-matching `replace` action.
- **`endurance_battle_advisor` Agent Idea:** Create an agent that analyzes prolonged battle scenarios, like a potential battle loop, to advise whether continuing the battle is more efficient than a strategic blackout to reset the encounter.
- **`hidden_passage_finder` Agent Idea:** Create an agent that takes the coordinates of a bounded, isolated area as input and generates a systematic, efficient search pattern to find a hidden passage.
- **`teach_hm_automator` Tool Idea:** Create a tool that takes an HM and a Pokémon name as input and generates the full sequence of button presses to teach the move.
- **`debugging_assistant` Agent Idea:** Create an agent that takes a tool's code, error message, and game state as input, and suggests a systematic debugging plan.
- **`interrupt_handler_navigator` Tool Idea:** Create a tool that takes a final destination, generates a path, and automatically handles interruptions like wild battles by re-pathing.
- **`notepad_analyzer_agent` Idea:** Create an agent that can parse the entire notepad, identify redundancies or contradictions, and suggest organizational improvements.
- **`puzzle_reset_automator` Tool Idea:** Create a tool that automates the process of resetting a puzzle by generating and executing a path to the nearest map transition and back.

### 4. Tool Limitations (Observed)
- **`notepad_edit` `replace` Flaw:** The `replace` action cannot distinguish between two identical strings in the notepad. If a string appears multiple times, the tool fails to replace a specific instance, making it impossible to remove targeted duplicates. (Observed Turn 162963).
- **`teleporter_mapper` Tool (Blocked):** This tool cannot be implemented. Its function requires persistent memory to build a graph of teleporter connections across multiple turns. The current tool execution environment is stateless and does not support this. Development is blocked pending a system update that allows for persistent tool state.

## D. Key Event & Puzzle Log

### 1. Major Events (Post-Champion)
- **Route 24 Cave:** Hypothesis: The cave north of Cerulean City on Route 24, previously blocked, would open after becoming Champion. Test: Traveled to the cave entrance at (7, 4) on Route 24. Outcome: Blocked. Conclusion: Hypothesis denied. The cave is currently inaccessible.
- **Silph Co. Elevator (SOLVED):** Puzzle: The elevator panel selects a floor, but does not travel. Solution: After selecting a floor on the panel, the player must step on the warp pads at the bottom of the room to initiate travel.
- **Cerulean City Post-Champion Events:** Trigger: After becoming Champion and solving the Trashed House backyard puzzle, interacting with Misty in the Cerulean Gym triggers a full-strength rematch. Battle Loop Anomaly: After defeating Misty, she immediately re-initiates the battle. Solution: When presented with the post-battle rematch prompt ('Ready for a rematch at my full strength?'), selecting 'NO' successfully broke the battle loop.

### 2. Seafoam Islands Puzzle Log (B3F & B4F)
- **Main Obstacle:** A strong water current on B4F at (8, 12) blocks progress. The presumed solution is a multi-step boulder puzzle on B3F.
- **Water Boulder Puzzle (B3F - Solved):** Pushing the left boulder, then the right boulder, from below rotates them into a position that clears the path west.
- **Ground Boulder Puzzle (B3F - In Progress):** The current strategy has pivoted to testing hypotheses generated by the `puzzle_solver_agent`).
- **Hidden Passages (Confirmed):** Some impassable-looking walls can be walked through. A systematic, tile-by-tile search is required to find them, especially when system feedback indicates an area is not a dead end despite appearances. (Discovered on Seafoam Islands B4F at (16, 15), Discovered on Seafoam Islands B2F at (19, 8))
- **Gengar AI (Hypnosis Priority):** The Gengar in Seafoam Islands B4F prioritizes using Hypnosis on any active, non-sleeping Pokémon, even if it has a type immunity to Gengar's STAB moves. It will then follow up with Dream Eater. This is its core strategy.
- **Assumption 1 (Confirmed):** The non-functional warp to Route 20 at (21, 18) on Seafoam Islands B4F is *permanently* non-functional. Attempts to use it after catching Articuno have failed.
- **New Hypothesis (Pikachu Swap):** The puzzle requires swapping positions with Pikachu.
  - **Observation:** Pikachu is at (6, 17), directly below me.
  - **Hypothesis:** Moving down onto Pikachu's tile will swap our positions, placing me at (6, 17) and opening new movement options.
  - **Test:** Press 'Down' from (6, 16).
- **Agent Hypothesis 2 (Partially Successful):** Push the boulder at (6, 15) east. Test: Swapped with Pikachu to reach (6, 17), then navigated to (7, 15) and pushed the boulder west to (5, 15), then repositioned to (6, 15) and pushed it again to (4, 15). Conclusion: Pushing west was successful and has aligned the boulder with the hole at (4, 17). However, the final push south is blocked because the required standing position at (4, 14) is an impassable tile.
- **B1F Elevated Platforms (Conclusion Corrected... Again):** My previous 'correction' was a hallucination. The elevated platforms on B1F DO NOT connect the eastern and western sections. The floor is segmented, and the western part is unreachable from the east. This has been confirmed by system warnings and failed pathfinding.
- **System Data Distrust (Seafoam B1F):** I repeatedly ignored system feedback (`is_in_dead_end_area` checks) and my own pathfinding tool's failures, leading to a major hallucination that B1F was a single connected area. **Correction:** The validation checks and tool outputs are the source of truth for navigation. I must trust them over my visual interpretation of the map, especially in complex, segmented areas.
- **Boulder Pushing Mechanics (B4F Linked Rotation):** The boulders on B4F at (5, 16) and (6, 16) are part of a linked rotation puzzle. Pushing them causes them to rotate, not to be pushed into holes. The goal is to change water flow, not to fill holes.
- **High Wild Encounter Rate (Seafoam Islands B4F water):** The water tiles around (5,15) on Seafoam Islands B4F have a very high wild encounter rate, leading to frequent movement interruptions. (Observed Turns 170465-170518, 170523-170552).
- **NPC Blocking/Movement (Kris - B4F):** Kris, previously at (8,3) after defeat, is now at (11,3).
- **Strength Activation on Land:** Strength was successfully activated on land at (8,12) on B4F and remains active when re-entering water. (Observed Turn 170460).
- **Articuno Captured:** I successfully captured Articuno on Seafoam Islands B4F at (7,2). (Confirmed Turn 170770).

### 3. Seafoam Islands Puzzle Log (B4F)
- **Failed Hypothesis 1 (Strength Activation on Steps):** Repeatedly attempted to activate Strength from the menu while on the 'steps' tile at (8,12) on B4F. Outcome: Consistently received "No SURFing on TITANESS here!". Conclusion: Strength cannot be activated from this specific steps tile while surfing is active or while on the steps tile at all on this map. (Observed Turns 170164-170188).
- **Failed Hypothesis 2 (Direct 'A' Interaction on Water Boulder):** Attempted to interact with Boulder 1 at (5,16) by pressing 'A' from (5,15) while surfing. Outcome: Screen text "This requires STRENGTH to move!". Conclusion: Direct 'A' interaction is not sufficient; Strength must be active. (Observed Turn 170250).
- **Movement Interruptions (Confirmed):** Repeated movement interruptions in the water at (5,15) on Seafoam Islands B4F are due to wild encounters. (Confirmed Turn 170876 by Wild JYNX encounter.)

## E. Opponent Information (Elite Four & Post-Game)

### 1. Lorelei (Elite Four)
- **Slowbro:** Knows Earthquake.
- **Jynx:** Knows Bubblebeam.
- **Gengar:** Lv 59.
- **Cloyster:** Lv 55, knows Explosion.

### 2. Bruno (Elite Four)
- **Hitmonchan:** Knows Ice Punch and Thunder Punch.
- **Onix:** Uses Explosion.
- **Machamp:** Knows Earthquake.

### 3. Agatha (Elite Four)
- **Gengar:** Prioritizes Hypnosis, then Dream Eater.

### 4. Lance (Elite Four)
- **Dragonite:** Lv 61, knows Slam, Thunder Wave, Wrap, and Hyper Beam (no mandatory recharge).
- **Gyarados:** Knows Slam.
- **Aerodactyl:** Knows Earthquake.
- **Charizard:** Knows Earthquake and Flamethrower.

### 5. Misty (Cerulean Gym Rematch)
- **Seadra:** Lv 64.
- **Golduck:** Lv 65, knows Psychic, Blizzard.
- **Lapras:** Lv 64, knows Hydro Pump, Thunder, Psychic, Blizzard.
- **Vaporeon:** Knows Acid Armor.
- **Starmie:** Knows Thunderbolt.
- **Snorlax (Kris):** Knows Earthquake, Body Slam, REST.

## F. General Game Tips (ROM Hack Specifics)
- **Dig field move:** Can be used to escape from caves (warps to last visited Pokemon Center).
- **Field move usage (fainted Pokemon):** Fainted Pokemon can still use field moves.
- **Surf activation:** Must use Surf from party menu while standing next to a water tile. Only Water-type Pokemon can use it in the field.
- **Victory Road boulder mechanics:** Leaving and re-entering a map resets boulder puzzles. Boulder barriers on Victory Road 1F also reset after changing floors.
- **HM forgetting:** HMs can be forgotten.