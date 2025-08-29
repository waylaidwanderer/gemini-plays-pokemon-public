# I. Meta-Progression & Lessons Learned

## A. Self-Correction Log (Master)

- **Core Principles (Internalized):** Lessons on strategic flexibility, agent trust, documentation use, and situational awareness have been internalized and are now core operating principles.
- **Repeated Path Interruptions (Seafoam Islands B4F):** I repeatedly failed to document or analyze path interruptions between Turns 170465-170517. This is a critical failure to follow the immediate data & tool maintenance directive. I must address these interruptions by re-evaluating the path and documenting the cause of the interruption. (Self-correction from Turn 170518).
- **Notepad Edit Precision Failure:** I failed to use `notepad_edit` with precise `old_text` and also attempted multiple `notepad_edit` calls in a single turn. **Correction:** All `notepad_edit` calls must be precise and only one per turn. (Self-correction from Turn 170521, 170522).
- **Failure to Update Map Understanding:** I repeatedly tried to reach an unreachable goal on B3F after the system confirmed it was a dead end. (Self-correction from Turn 170966-170970).
- **Dead End Area Mismatch (Lavender Cubone House):** My previous assertion that Lavender Cubone House was not a dead end was incorrect. The system reported it as a dead end. **Correction:** I must re-evaluate my understanding of map layouts and trust system feedback over my visual interpretation. (Self-correction from Turn 172659)
- **Dead End Area Mismatch (Seafoam B3F):** My previous assertion that Seafoam Islands B3F was a dead end was incorrect. The system reported 4 reachable exits. This was a critical hallucination. **Correction:** I must re-evaluate my understanding of B3F's layout and trust system feedback over my visual interpretation of the map. (Self-correction from Turn 170981).
- **Notepad and Map Marker Update Priority (Turn 171001):** I attempted multiple `define_map_marker` and `find_path` calls before executing a planned `notepad_edit` overwrite. This is a direct violation of the core directive that notepad updates are the highest priority and must be performed immediately. **Correction:** All notepad updates must be performed immediately, prior to any other actions.
- **Fly Menu Navigation Failure (Turn 171342-171352):** I repeatedly overshot the target Pokémon in the party menu and then manually scrolled through the Fly menu. **Correction:** I must use the `fly_menu_navigator` tool as intended and trust its output. The `get_next_pokemon_press` tool was deleted to make space for `fly_menu_navigator` and should not have been used. This also highlights a failure to immediately use a newly defined tool.
- **Deferred Map Marker Creation (Turns 172822, 172872, 172881):** I cut trees but deferred defining map markers for them until a later turn (172829, 172877, 172882). **Correction:** Map markers must be defined immediately on the same turn the event occurs.
- **Repeated `find_path` Calls without Re-evaluation (Turns 172922-172929):** I repeatedly called `find_path` to the same target after it failed without adapting my strategy or re-evaluating the cause of failure. **Correction:** When a tool's output is unexpected, I must immediately adapt my strategy and re-evaluate the underlying cause of the failure.
- **Recurring Deferred Notepad and Map Marker Updates (Critique from Turn 172930, 173597 - Critical Failure):** The overwatch critique highlighted a recurring lapse in performing notepad and map marker updates *immediately*, citing specific turns where updates were deferred. This is a critical failure to adhere to the core directive that all maintenance must be performed in the *current turn* without deferral. **Correction:** I must ensure all notepad updates and map marker definitions are performed in the *current turn* without deferral, and this issue will be prioritized in all future actions.
- **Tool Refinement (Critique from Turn 173623 - Critical Failure):** I have repeatedly failed to refine my `find_path` tool to provide diagnostic information about *why* a path is blocked. My `menu_navigator` and `select_battle_option` tools exhibit execution issues. I have deferred fixing these, prioritizing the ongoing battle. **Correction:** Tool refinement is a higher priority than any short-term gameplay objective. I must immediately refine faulty tools using `define_tool`.
- **Notepad Redundancy (Critique from Turn 173623 - Critical Failure):** My notepad contains significant outdated and redundant information. **Correction:** I must break down large-scale reorganization into smaller, focused `replace` or `append` actions to avoid destructive changes.
- **Map Marker Usage (Critique from Turn 173623 - Critical Failure):** My map markers section is currently empty, which is a critical failure. **Correction:** I must immediately begin diligently marking every discovered NPC, defeated trainer, used warp, dead end, and key discovery with Map Markers.

# III. Game & World Knowledge

## A. Battle Mechanics & Type Effectiveness
- **Verified Type Chart:**
  - Electric is super-effective against Poison/Flying, Water, Water/Ice, and Water/Psychic.
  - Fighting is super-effective against Ice, Normal, and Rock.
  - Flying is immune to Ground.
  - Ghost is immune to Ground.
  - Grass is super-effective against Ground, Ground/Rock, and Water/Ice.
  - Ground is super-effective against Electric, Ghost, Ground, Psychic, and Rock/Ground.
  - Normal is immune to Ghost.
  - Psychic is super-effective against Poison.
  - Rock is super-effective against Flying.
- **Anomalies & Hypotheses:**
  - **Night Shade Damage:** May be altered in this ROM hack.
  - **Hyper Beam Recharge:** May be conditional or inconsistent.
  - **Move Menu Cursor Reset:** May randomly reset to the top position.

## B. Tile & Field Mechanics
- **Linked Boulder Rotation:** Some water-based boulders rotate in a linked fashion.
- **Hidden Passages:** Impassable-looking walls can sometimes be walked through.
- **Strength Mechanics:** Does not need to be reactivated per push. Player position can change depending on push direction.
- **HM Field Move Usage:** Requires two 'A' presses (prompt + confirmation).

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
- **`interrupt_handler_navigator` Tool Idea:** Create a tool that takes a final destination, generates a path, and automatically handles interruptions like wild battles by re-pathing.
- **`notepad_analyzer_agent` Idea:** Create an agent that can parse the entire notepad, identify redundancies or contradictions, and suggest organizational improvements.
- **`puzzle_reset_automator` Tool Idea:** Create a tool that automates the process of resetting a puzzle by generating and executing a path to the nearest map transition and back.
- **Agent Refinement: `master_battle_agent` `recommended_lead`:** The `master_battle_agent`'s reasoning for `recommended_lead` could be more robust, especially when the opponent's full team is not known. This is an area for potential future refinement.

### 4. Tool Limitations (Observed)
- **`notepad_edit` `replace` Flaw:** The `replace` action cannot distinguish between two identical strings in the notepad. If a string appears multiple times, the tool fails to replace a specific instance, making it impossible to remove targeted duplicates. (Observed Turn 162963).
- **`teleporter_mapper` Tool (Blocked):** This tool cannot be implemented. Its function requires persistent memory to build a graph of teleporter connections across multiple turns. The current tool execution environment is stateless and does not support this. Development is blocked pending a system update that allows for persistent tool state.

## D. Key Event & Puzzle Log

### 1. Major Events (Post-Champion)
- **Route 24 Cave:** Remains blocked after becoming Champion.
- **Silph Co. Elevator (SOLVED):** After selecting a floor, must step on the warp pads to travel.
- **Cerulean City Post-Champion Events:** Misty rematch is triggered after solving the Trashed House backyard puzzle. Battle loop is broken by selecting 'NO' to the rematch prompt.

### 2. Seafoam Islands Puzzle Log
- **Main Obstacle:** Strong water current on B4F blocked progress, solved by a boulder puzzle on B3F.
- **B4F Linked Boulder Rotation:** Boulders at (5, 16) and (6, 16) are part of a linked rotation puzzle to change water flow.
- **Articuno Captured:** Successfully captured Articuno on B4F at (7,2).

## E. Opponent Information
- **Lorelei (E4):** Slowbro (Earthquake), Jynx (Bubblebeam), Gengar (Lv 59), Cloyster (Lv 55, Explosion).
- **Bruno (E4):** Hitmonchan (Ice Punch, Thunder Punch), Onix (Explosion), Machamp (Earthquake).
- **Agatha (E4):** Gengar (Hypnosis, Dream Eater).
- **Lance (E4):** Dragonite (Lv 61, Slam, Thunder Wave, Wrap, Hyper Beam), Gyarados (Slam), Aerodactyl (Earthquake), Charizard (Earthquake, Flamethrower).
- **Misty (Rematch):** Seadra (Lv 64), Golduck (Lv 65, Psychic, Blizzard), Lapras (Lv 64, Hydro Pump, Thunder, Psychic, Blizzard), Vaporeon (Acid Armor), Starmie (Thunderbolt).
- **Kris (Snorlax):** Snorlax (Earthquake, Body Slam, REST).
- **Craig (Power Plant):** JOLTEON (Lv 55, DIG, THUNDERBOLT, PIN MISSILE, THUNDER WAVE), AERODACTYL (Lv 55, ROCK SLIDE), EXEGGUTOR (Lv 55, MEGA DRAIN, PSYCHIC), SNORLAX (Lv 55, AMNESIA, EARTHQUAKE, BODY SLAM, REST).

## F. General Game Tips (ROM Hack Specifics)
- **Normal vs Electric Neutrality (Hypothesis):** Need to verify if Normal-type moves are neutral against Electric-types by observing battle text in a future encounter.

# IV. Area & Navigation Insights

## A. Power Plant (ID: 83)
- **Objective:** Find and defeat trainer CRAIG, then find and capture Zapdos.
- **Status:** Currently navigating Rock Tunnel to reach it.