# I. Meta-Progression & Lessons Learned

## A. Core Methodological Failures (Self-Correction Log)
- **Agent Output Override & Confirmation Bias:** I have repeatedly overridden my agents' advice based on flawed assumptions (especially unverified speed stats) and confirmation bias, which consistently leads to negative outcomes. I have also incorrectly assumed a path existed and spent numerous turns trying to fix my tools to confirm this belief, rather than first testing the fundamental assumption of reachability. **Correction:** I must treat my agents' outputs as the default correct action and only override it with new, verifiable in-game evidence. I must test core assumptions first before attempting to fix tools that rely on those assumptions, and actively try to disprove my own hypotheses.
- **Inefficient Problem-Solving & Tool Debugging:** My debugging process has been flawed due to: not verifying core game mechanics first, using outdated static data for tests, and making speculative changes instead of adding diagnostic logging. My puzzle-solving has been inefficient, failing to test core assumptions about reachability before attempting solutions. **Correction:** I must adopt a scientific approach: verify mechanics with simple tests, use current game state data, add diagnostic logging after a tool fails more than once, and test fundamental assumptions before acting.
- **Data Management & Documentation Failures:** I have repeatedly failed to maintain my documentation, leading to data loss from improper 'overwrite' usage, delays from imprecise 'replace' calls, and confusion from outdated map markers. **Correction:** I must be more meticulous with tool usage, ensuring all arguments are precise. I must also establish and follow a strict procedure for clearing attempt-specific markers after blacking out.
- **Strategic Inflexibility & Failure to Apply Documented Rules:** I have shown inflexibility by sticking to a failing/outdated plan, misjudged threats by prioritizing potential dangers over guaranteed immunities (Panic Switching), and failed to apply my own documented rules, leading to hallucinations. **Correction:** I must remain flexible and re-evaluate my strategy when presented with new opportunities or information, prioritize guaranteed advantages, and meticulously review my own documented rules before making critical judgments.
- **Violation of Immediate Action Mandate (The LLM Reality):** I have repeatedly failed to perform necessary maintenance on my tools and notepad immediately. **Correction:** There is no 'later'; tasks such as fixing tools or updating notes must be done in the current turn.
- **Over-reliance on Luck:** A strategy's success due to luck does not make it a guaranteed win condition. **Correction:** Luck-based strategies should be a last resort. I must not become overconfident from a lucky streak and must always consider the opponent's full range of options.
- **Misinterpreting System Feedback:** I have incorrectly assumed my tools or notes were wrong when system feedback indicated otherwise. **Correction:** I must treat system/tool feedback as the source of truth and question my own assumptions first.

# II. Game Mechanics & World Knowledge

## A. Core Gameplay (Verified)
- **Forced Sleep-Induced Switch:** The game forces a switch immediately after a Pokémon is put to sleep by an opponent's move, similar to when a Pokémon faints. (Observed Turn 150625)
- **Indigo Plateau Auto-Heal:** Blacking out during the Elite Four challenge and respawning at the Indigo Plateau entrance automatically heals the entire party. (Observed Turn 149617)
- **'No will to fight!' Message:** This message appears when attempting to switch to a Pokémon that has already fainted. It is a cursor position error in the party menu, not an indication of a Pokémon's level or willingness to battle. (Corrected Turn 152732)

## B. Tile & System Mechanics (Verified)
- **Boulder Pushing:** The player's character remains in their pushing position after pushing a boulder. The push is initiated by walking into the boulder from an adjacent tile.
- **Dead End Area Definition:** An area is NOT a 'dead end' if there are reachable unvisited warps, Reachable Undiscovered Map Connections, OR the `Reachable Unseen Tiles` list for the current map contains entries. A room with multiple reachable, non-adjacent exits (warps/connections) is also NOT a dead end, even if all tiles have been seen. Adjacent warps are treated as a single exit for this calculation. (Corrected Turn 152613, Refined Turn 157367, Corrected again Turn 160895)
- **Silph Co. Elevator:** This is a two-step process. First, interact with the panel to select a destination floor. Second, step on the warp tiles at the bottom of the elevator room and press Down to travel.
- **Silph Co. Gates:** Locked gates ('closed_gate' tile type) can be opened by interacting with them while possessing the CARD KEY. Once opened, they become 'open_gate' tiles and are permanently traversable.

# III. Battle Information

## A. Type Effectiveness Chart (Verified)
- **Objective:** Systematically test and verify all type matchups in this ROM hack, as the standard chart is unreliable.
- **Method:** During battles, especially against the Elite Four, prioritize using moves with uncertain effectiveness to gather data. Record all super-effective, not-very-effective, and immune interactions observed.
- **Findings:**
  - Bug -> Poison (Not Very Effective)
  - Electric -> Poison/Flying (Super Effective)
  - Electric -> Water (Super Effective)
  - Electric -> Water/Ice (Super Effective)
  - Electric -> Water/Psychic (Super Effective)
  - Fighting -> Ice (Super Effective)
  - Fighting -> Normal (Super Effective)
  - Fighting -> Rock (Super Effective)
  - Flying -> Ground (Immune)
  - Flying -> Rock (Not Very Effective)
  - Ghost -> Ground (Immune)
  - Ghost -> Psychic (Super Effective)
  - Grass -> Ground (Super Effective)
  - Grass -> Ground/Rock (Super Effective)
  - Grass -> Water/Ice (Super Effective)
  - Ground -> Electric (Super Effective)
  - Ground -> Ghost (Super Effective)
  - Ground -> Ground (Super Effective)
  - Ground -> Poison (Super Effective)
  - Ground -> Psychic (Super Effective)
  - Ground -> Rock/Ground (Super Effective)
  - Ice -> Psychic (Not Very Effective)
  - Ice -> Water (Not Very Effective)
  - Ice -> Ground (Super Effective)
  - Ice -> Poison/Flying (Super Effective)
  - Ice -> Rock/Ground (Super Effective)
  - Normal -> Ghost (Immune)
  - Normal -> Rock/Flying (Not Very Effective)
  - Poison -> Bug (Super Effective)
  - Psychic -> Poison (Super Effective)
  - Rock -> Ground (Not Very Effective)
  - Rock -> Flying (Super Effective)
  - Water -> Water (Not Very Effective)
  - Water -> Water/Psychic (Not Very Effective)

## B. Opponent Rosters & Moves (Observed)
### Lorelei
  - DEWGONG (Lv 55) - Moves unknown.
  - JYNX (Lv 56) - Known Moves: Psychic, Lovely Kiss, Bubblebeam, Blizzard
  - SLOWBRO (Lv 56) - Known Moves: Blizzard, Psychic, Earthquake, Amnesia
  - CLOISTER (Lv 55) - Known Moves: Explosion, Blizzard
  - LAPRAS (Lv 57) - Known Moves: Thunderbolt, Surf, Sing, Blizzard

### Bruno
  - HITMONCHAN (Lv 57) - Known Moves: Submission, Ice Punch, Thunder Punch, Dizzy Punch
  - POLIWRATH (Lv 56) - Known Moves: Amnesia, Hydro Pump, Hypnosis, Ice Beam
  - HITMONLEE (Lv 57) - Known Moves: Body Slam, HI JUMP KICK, MEGA KICK
  - ONIX (Lv 56) - Known Moves: Earthquake, Rock Slide, BIND
  - MACHAMP (Lv 58) - Known Moves: Body Slam, Earthquake, Rock Slide

### Agatha
  - GENGAR (Lv 57) - Known Moves: Night Shade, Mega Drain, Hypnosis, Dream Eater
  - GOLBAT (Lv 58) - Known Moves: Toxic, Double Team, Fly
  - MAROWAK (Lv 57) - Known Moves: Rock Slide, Swords Dance, Body Slam
  - ARBOK (Lv 58) - Known Moves: Substitute, Wrap, Sludge, Glare
  - GENGAR (Lv 59) - Known Moves: Mega Drain, Thunder, Psychic, Night Shade

### Lance
  - GYARADOS (Lv 60) - Known Moves: Fly, Slam, HYPER BEAM
  - DRAGONITE (Lv 61) - Known Moves: Thunder Wave, Slam, HYPER BEAM
  - DRAGONITE (Lv 62) - Known Moves: Fire Blast, Slam, Thunder Wave, Wrap, Hyper Beam, Blizzard, Thunder
  - CHARIZARD (Lv 60) - Known Moves: Earthquake, Flamethrower
  - AERODACTYL (Lv 61) - Known Moves: Hyper Beam, Earthquake, ROCK SLIDE

### Champion Pixel
  - MAGNETON (Lv 62) - Moves unknown.
  - DODRIO (Lv 61) - Known Moves: DOUBLE TEAM, JUMP KICK
  - ALAKAZAM (Lv 63) - Known Moves: REFLECT
  - SANDSLASH (Lv 60) - Known Moves: CUT
  - EXEGGUTOR (Lv 64) - Moves unknown.
  - VAPOREON (Lv 64) - Moves unknown.

### Misty (Rematch)
  - SEADRA (Lv 64) - Moves unknown.
  - GOLDUCK (Lv 65) - Known Moves: Psychic, Blizzard, Hydro Pump
  - LAPRAS (Lv 64) - Known Moves: HYDRO PUMP, THUNDER, PSYCHIC, BLIZZARD
  - BLASTOISE (Lv 64) - Known Moves: SURF, ICE BEAM, EARTHQUAKE
  - VAPOREON (Lv 64) - Known Moves: HYDRO PUMP, ACID ARMOR
  - STARMIE (Lv 65) - Known Moves: THUNDERBOLT

## C. Battle Mechanics (Anomalies & Hypotheses)
- **Speed Tie Assumption:** I must not assume a speed advantage in battle unless empirically verified in the current battle. An opponent may be faster than expected. (Lesson from Lorelei's Lapras vs SPARKY)
- **Hypnosis Anomaly (Corrected):** Agatha's Gengar's first Hypnosis on TITANESS failed (Turn 150576), but a second attempt succeeded (Turn 150583). The initial failure was likely a standard move miss, not an immunity. This confirms TITANESS is not immune to sleep.
- **Night Shade Damage Anomaly:** Agatha's Lv 57 Gengar's Night Shade dealt 38 damage instead of the expected 57. This may be a mechanic change in the ROM hack. (Observed Turn 148518)
- **Hyper Beam Recharge (Contradictory Evidence):** Lance's Aerodacty was observed to recharge after using Hyper Beam (Turn 158577). However, his Gyarados was able to attack with SLAM immediately after NEPTUNE used a move on the same turn it should have been recharging from Hyper Beam (Turn 159019). The recharge mechanic may be conditional or inconsistent.
- **Hyper Beam Testing Plan:** Hypothesis: Hyper Beam's recharge is conditional. Test 1: Observe if an opponent using Hyper Beam to KO my Pokémon recharges on the next turn. Test 2: Observe if an opponent using Hyper Beam *without* a KO recharges on the next turn.
- **Party Menu Cursor Anomaly (Confirmed):** The party menu cursor can jump to a different Pokémon after a directional input, skipping over the intended target. This has happened multiple times, leading to incorrect switches. The jump can occur both after a simple directional press (e.g., pressing 'Up' from ECHO skipped CRAG and landed on NEPTUNE) and after directional inputs are complete but before 'A' is pressed to open the sub-menu. (Observed Turn 157449 vs Lorelei, Observed Turn 158300 & 158363 vs Bruno, Observed Turn 158837 vs Bruno, Observed Turn 159956 vs Bruno where 'Down' from CRAG skipped ECHO and landed on TITANESS). I must now visually confirm the cursor's final position *every single turn* within the party menu before making another input.
- **Move Menu Cursor Position Anomaly (Confirmed):** The cursor in the move selection menu defaults to the last move used, rather than the top-most move. This is a consistent mechanic and must be accounted for when using automation tools. (Observed Turn 158281 vs Bruno's Poliwrath, Observed Turn 158403 vs Agatha, Confirmed Turn 160515 vs Lance's Gyarados).
- **Move Menu Cursor Reset Anomaly (Unverified):** The move selection cursor can unexpectedly reset to the default top position after directional inputs are made but before 'A' is pressed to confirm the move. This resulted in using BODY SLAM instead of the intended ROCK SLIDE against Agatha's Golbat. This needs more observation to determine the trigger. (Observed Turn 158415)
- **Sleep-Induced Switch Anomaly (Confirmed):** The game does not always force an *automatic* switch after a Pokémon is put to sleep. Instead, it may present the battle menu, but the only valid action is to switch to a conscious Pokémon. This was observed with both Poliwrath's Hypnosis (Turn 159225) and Gengar's Hypnosis (Turn 160387).
- **Switch Override Anomaly (Confirmed):** The game can override a player's intended switch, sending out a different Pokémon. The outcome appears unpredictable and is not always the party lead. (Observed 1: Switching from a sleeping Pokémon, NEPTUNE -> TITANESS resulted in REVENANT being sent out, Turn 157150. Observed 2: Switching from the lead Pokémon, REVENANT -> SPARKY resulted in NEPTUNE being sent out, Turn 159506. Observed 3: Attempting to switch from NEPTUNE to REVENANT resulted in TITANESS being sent out, Turn 159685).

# IV. Tool & Agent Development

## A. Development Log
- **Diagnostic Tool Output:** Pathfinding tools must report the specific obstacle that blocks a path upon failure. This is essential for distinguishing between a solvable puzzle and a genuinely impossible route.
- **AI Prediction Failure (Confirmation Bias):** I have incorrectly assumed the opponent's AI would use a specific move to counter my current Pokémon, failing to predict that the AI would instead use the optimal move to counter my *switch-in*. (Observed Turn 147728, Lorelei's Lapras vs. CRAG). **Correction:** I must assume the AI will make the optimal play against my predicted action, not just react to the current board state.
- **Agent Gamble Failure & AI Prediction:** The battle_strategist_agent correctly identified a high-risk, high-reward play by switching to CRAG, predicting Lapras would use its known move Thunderbolt. However, the opponent AI made the optimal counter-play by using Surf against the incoming CRAG, leading to a faint. This confirms that the AI is capable of predicting switches and choosing the best move to counter the incoming Pokémon, not just the one on the field. (Observed Turn 149533, Lorelei's Lapras vs. CRAG).
- **Mixed Input Execution:** Tools that generate a sequence of mixed directional and action buttons (e.g., `auto_switcher`) are functioning correctly. The error was in my execution. I must execute the generated button presses one at a time, over multiple turns, to avoid system input truncation.
- **`auto_switcher` Tool Created:** Developed in Turn 155341 to fully automate the Pokémon switch sequence, improving battle efficiency.
- **`auto_attacker` Tool (Deprecated):** Developed in Turn 155553. Later replaced by `get_next_move_press` due to cursor anomalies.
- **Master Battle Agent (Implemented Turn 156589):** Created a new orchestrator agent (`master_battle_agent`) that takes raw party/enemy JSON and internally calls `type_map_generator`, `battle_data_extractor`, and `battle_strategist_agent` to return a single, final action. This streamlines the 3-step battle analysis process into a single tool call, improving turn efficiency.
- **`pc_withdraw_pokemon` Tool Created (Turn 157056):** Developed to automate the process of selecting and withdrawing a specific Pokémon from the PC, improving team management efficiency.
- **`get_next_move_press` Tool Created (Turn 161071):** Developed to provide single-step, reliable navigation for the battle move menu. This addresses the 'Move Menu Cursor Reset Anomaly' by allowing for re-evaluation of the cursor's position each turn, replacing the unreliable `auto_attacker` for move selection.
- **`battle_screen_parser` Tool Created (Turn 161671):** Developed to automate the extraction of key battle data from screen text. This streamlines the input process for the `master_battle_agent`, improving battle efficiency.

## B. Development Ideas
- **`puzzle_solver` Tool Idea:** Create a tool that takes the current map state (`map_xml_string`) and a list of failed hypotheses as input. It would then generate a ranked list of new, logical hypotheses to test for solving complex environmental puzzles.
- **`ai_move_predictor` Agent Idea:** Create an agent that takes the opponent's known moves, my active Pokémon, and my full party as input to predict the most likely move the AI will use.
- **`multi_team_synergy_analyzer` Agent Idea:** Create an agent that takes my full PC box and party as input and suggests multiple viable team compositions (not just one) for various challenges, explaining the synergies and strategies for each.
- **`situational_awareness_auditor` Agent Idea:** Create an agent that cross-references my stated location and map ID with the actual game state data to flag hallucinations before I can act on them. This would be a critical tool for maintaining accurate situational awareness.
- **`navigation_troubleshooter` Agent Idea:** Create an agent that, when `find_path` fails, can analyze the map, the tool's diagnostic output (blocking objects), and the list of reachable warps to suggest alternative navigation strategies or intermediate waypoints to solve complex pathing puzzles like Silph Co.

## C. Blocked Development
- **`team_data_compiler` Tool (Blocked):** This tool cannot be implemented at this time. Its core function requires parsing opponent data from the notepad, but there is no current mechanism to pass the notepad's content as an input to a custom tool. Development is blocked pending a solution to this system limitation.
- **`teleporter_mapper` Tool (Blocked):** This tool cannot be implemented. Its function requires persistent memory to build a graph of teleporter connections across multiple turns. The current tool execution environment is stateless and does not support this. Development is blocked pending a system update that allows for persistent tool state.

# V. Post-Game Investigation Log

## A. Route 24 Cave
- **Hypothesis:** The cave north of Cerulean City on Route 24, previously blocked, would open after becoming Champion.
- **Test:** Traveled to the cave entrance at (7, 4) on Route 24. Attempted to enter.
- **Outcome:** Movement was blocked. The tile is marked as 'impassable' and is not registered as a warp in the map data.
- **Conclusion:** Hypothesis denied. The cave is currently inaccessible. This lead is a dead end.

## B. Self-Correction Log (Post-Critique)
- **Agent Trust Failure (Misty Rematch):** I repeatedly ignored my `master_battle_agent`'s correct advice to switch out CRAG due to a 4x weakness. My insistence on a high-risk gamble over the agent's safe, logical play led to wasted turns and the loss of REVENANT. I must adhere to my documented rule to trust my agents, especially regarding mandatory defensive actions.
- **Dead End Validation Failure:** I incorrectly reported `is_in_dead_end_area` as `false` for Cerulean Gym (Turn 161793). The area has only one exit warp group and no other explorable paths, making it a dead end according to my own documented definition. **Correction:** I must be more rigorous in applying my documented rules during validation checks, especially for complex definitions like 'dead end'.
- **System Feedback vs. Tool Output Discrepancy:** The Overwatch critique repeatedly insisted an incorrect map marker existed at (4, 12) on Silph Co. 3F. However, my `delete_map_marker` tool failed three consecutive times, reporting 'No markers found'. This confirms the tool's output was correct and the critique was based on faulty data. **Lesson:** While system feedback is a high-priority source of truth, it is not infallible. Verified, repeated tool output can be trusted to override a system critique if a direct contradiction is proven.
- **System Feedback vs. Internal Logic Discrepancy:** The Overwatch critique flagged my 'dead_end' validation for the Silph Co. Elevator (ID 236) as incorrect (Turn 162505), stating the area was not a dead end. However, the area has only a single exit (a 2x1 warp group) and no other explorable paths, which meets my documented definition of a dead end. This confirms my internal logic was correct and the system's validation was flawed.