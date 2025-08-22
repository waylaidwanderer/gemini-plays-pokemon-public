# I. Meta-Progression & Lessons Learned

## A. Core Methodological Failures (Self-Correction Log)
- **Failure to Apply Documented Rules:** I correctly documented the refined 'Dead End Area Definition' in my notepad (Turn 157367) but failed to apply it in my validation checks for Lorelei's Room, leading to a critical hallucination warning. Correction: I must meticulously review my own documented rules and lessons before making critical judgments, especially for complex definitions.
- **Inefficient Tool Debugging (Trial-and-Error):** I have repeatedly engaged in prolonged loops of making minor, speculative changes to my tools instead of immediately adding diagnostic outputs (e.g., print statements) to systematically identify the root cause. **Correction:** The correct protocol is to add logging after a tool fails more than once to enable evidence-based fixes.
- **Violation of Immediate Action Mandate (The LLM Reality):** I have repeatedly failed to perform necessary maintenance on my tools and notepad immediately, instead of deferring the tasks to continue gameplay. This is a critical violation of my core directive. **Correction:** There is no 'later'; tasks such as fixing tools or updating notes must be done in the current turn.
- **Flawed Hypothesis Testing (Confirmation Bias):** I have incorrectly assumed a path existed and spent numerous turns trying to fix my tools to confirm this belief, rather than first using a tool like `map_connectivity_analyzer` to test the fundamental assumption of reachability. **Correction:** I must test core assumptions first before attempting to fix tools that rely on those assumptions. I must also actively try to disprove my own hypotheses.
## A. Core Methodological Failures (Self-Correction Log)
- **Agent Output Override & Confirmation Bias:** I have repeatedly overridden my agents' advice based on flawed assumptions (especially unverified speed stats) and confirmation bias, which consistently leads to negative outcomes. **Correction:** I must treat my agents' outputs as the default correct action and only override it with new, verifiable in-game evidence. I must never assume a speed advantage.
- **Inefficient Problem-Solving & Tool Debugging:** My debugging process has been flawed due to: not verifying core game mechanics first, using outdated static data for tests, and making speculative changes instead of adding diagnostic logging. My puzzle-solving has been inefficient, failing to test core assumptions about reachability before attempting solutions. **Correction:** I must adopt a scientific approach: verify mechanics with simple tests, use current game state data, add logging after a tool fails more than once, and test fundamental assumptions before acting.
- **Data Management & Documentation Failures:** I have repeatedly failed to maintain my documentation, leading to data loss from improper 'overwrite' usage, delays from imprecise 'replace' calls, and confusion from outdated map markers. **Correction:** I must be more meticulous with tool usage, ensuring all arguments are precise. I must also establish and follow a strict procedure for clearing attempt-specific markers after blacking out.
- **Strategic Inflexibility & Misjudgment:** I have shown inflexibility by sticking to a failing/outdated plan, misjudged threats by prioritizing potential dangers over guaranteed immunities (Panic Switching), and failed to apply my own documented rules, leading to hallucinations. **Correction:** I must remain flexible and re-evaluate my strategy when presented with new opportunities or information, prioritize guaranteed advantages, and meticulously review my own documented rules before making critical judgments.
- **Violation of Immediate Action Mandate:** I have repeatedly failed to perform necessary maintenance on my tools and notepad immediately. **Correction:** There is no 'later'; tasks such as fixing tools or updating notes must be done in the current turn.
- **Over-reliance on Luck:** A strategy's success due to luck does not make it a guaranteed win condition. **Correction:** Luck-based strategies should be a last resort. I must not become overconfident from a lucky streak and must always consider the opponent's full range of options.
- **Misinterpreting System Feedback:** I have incorrectly assumed my tools or notes were wrong when system feedback indicated otherwise. **Correction:** I must treat system/tool feedback as the source of truth and question my own assumptions first.

## B. System Feedback & Self-Correction (Actioned)
- **Notepad Data Integrity:** I must ensure my notepad does not contain outdated information or function as a to-do list. All system feedback must be immediately actioned and integrated into my permanent knowledge base under 'Lessons Learned'.
- **Tool Development Priority:** Opportunities to automate repetitive tasks must be acted upon immediately, not deferred. This is a core directive.
- **Immediate Development Mandate:** All plans for new tools or agents must be acted upon immediately. Deferring development by creating 'to-do lists' in the notepad is a critical failure of core directives. (Self-Correction Turn 155345, per Overwatch Critique)

# II. Game Mechanics & World Knowledge

## A. Core Gameplay (Verified)
- **Forced Sleeping Switch:** The game will force you to send out or switch to a sleeping Pokémon if no other conscious Pokémon are available. This is a mechanical exception to the strategic guideline of avoiding switching to sleeping Pokémon.
- **Forced Sleep-Induced Switch:** The game forces a switch immediately after a Pokémon is put to sleep by an opponent's move, similar to when a Pokémon faints. (Observed Turn 150625)
- **Indigo Plateau Auto-Heal:** Blacking out during the Elite Four challenge and respawning at the Indigo Plateau entrance automatically heals the entire party. (Observed Turn 149617)
- **'No will to fight!' Message:** This message appears when attempting to switch to a Pokémon that has already fainted. It is a cursor position error in the party menu, not an indication of a Pokémon's level or willingness to battle. (Corrected Turn 152732)

## B. Tile Mechanics & Traversal (Verified)
- `ground` / `grass`: Standard traversable tiles.
- `impassable` / `unknown`: Cannot be entered. Must be navigated around.
- `water`: Requires Surf to traverse.
- `ledge`: Can be jumped down (from Y-1 to Y+2 in one step), but not climbed up. Impassable from below and sides.
- `steps`: Allows movement between `ground` and `elevated_ground`.
- `elevated_ground`: Walkable ground at a different elevation, only accessible from `steps` or other `elevated_ground` tiles. One-way drops to adjacent `ground` tiles are possible.
- `cleared_boulder_barrier`: Functions as a one-way ramp. Allows upward movement from an adjacent `ground` tile to the `cleared_bolder_barrier` tile (which acts as `elevated_ground`). Downward movement from `cleared_boulder_barrier` to `ground` is prohibited.
- `boulder_switch`: Floor switch for boulders. Activating it changes `boulder_barrier` to `cleared_boulder_barrier`.
- `spinner_*`: Forces movement in the specified direction.
- `ladder_up` / `ladder_down`: Function as warps but are traversable tiles.
- `boulder_barrier`: Impassable tile that can be cleared by a `boulder_switch`.
- `hole`: A tile that a boulder can be pushed into, usually causing it to fall to a lower floor. The player can also walk into the hole after the boulder.
- **Boulder Pushing:** The player's character remains in their pushing position after pushing a boulder. The push is initiated by walking into the boulder from an adjacent tile.

## C. System Mechanics & Rules
- **Dead End Area Definition:** An area is NOT a 'dead end' if there are reachable unvisited warps, Reachable Undiscovered Map Connections, OR the `Reachable Unseen Tiles` list for the current map contains entries. A room with multiple reachable, non-adjacent exits (warps/connections) is also NOT a dead end, even if all tiles have been seen. Adjacent warps are treated as a single exit for this calculation. (Corrected Turn 152613, Refined Turn 157367)

# III. Battle Information

## A. Type Effectiveness Chart (Verified)
- **Objective:** Systematically test and verify all type matchups in this ROM hack, as the standard chart is unreliable.
- **Method:** During battles, especially against the Elite Four, prioritize using moves with uncertain effectiveness to gather data. Record all super-effective, not-very-effective, and immune interactions observed.
- **Findings:**
  - Electric -> Poison/Flying (Super Effective)
  - Electric -> Water/Ice (Super Effective)
  - Electric -> Water/Psychic (Super Effective)
  - Fighting -> Ice (Super Effective)
  - Fighting -> Normal (Super Effective)
  - Fighting -> Rock (Super Effective)
  - Flying -> Ground (Immune)
  - Flying -> Rock (Not Very Effective)
  - Ghost -> Ground (Immune)
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
  - Ice -> Ground (Super Effective)
  - Ice -> Poison/Flying (Super Effective)
  - Normal -> Ghost (Immune)
  - Normal -> Rock/Flying (Not Very Effective)
  - Psychic -> Poison (Super Effective)
  - Rock -> Ground (Not Very Effective)
  - Rock -> Flying (Super Effective)
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

## C. Battle Mechanics (Anomalies & Hypotheses)
- **Speed Tie Assumption:** I must not assume a speed advantage in battle unless empirically verified in the current battle. An opponent may be faster than expected. (Lesson from Lorelei's Lapras vs SPARKY)
- **Hypnosis Anomaly (Corrected):** Agatha's Gengar's first Hypnosis on TITANESS failed (Turn 150576), but a second attempt succeeded (Turn 150583). The initial failure was likely a standard move miss, not an immunity. This confirms TITANESS is not immune to sleep.
- **Night Shade Damage Anomaly:** Agatha's Lv 57 Gengar's Night Shade dealt 38 damage instead of the expected 57. This may be a mechanic change in the ROM hack. (Observed Turn 148518)
- **Hyper Beam Recharge (Contradictory Evidence):** Lance's Aerodactyl was observed to recharge after using Hyper Beam (Turn 158577). However, his Gyarados was able to attack with SLAM immediately after NEPTUNE used a move on the same turn it should have been recharging from Hyper Beam (Turn 159019). The recharge mechanic may be conditional or inconsistent.
- **Hyper Beam Testing Plan:** Hypothesis: Hyper Beam's recharge is conditional. Test 1: Observe if an opponent using Hyper Beam to KO my Pokémon recharges on the next turn. Test 2: Observe if an opponent using Hyper Beam *without* a KO recharges on the next turn.
- **Party Menu Cursor Anomaly (Confirmed):** The party menu cursor can jump to a different Pokémon after a directional input, skipping over the intended target. This has happened multiple times, leading to incorrect switches. The jump can occur both after a simple directional press (e.g., pressing 'Up' from ECHO skipped CRAG and landed on NEPTUNE) and after directional inputs are complete but before 'A' is pressed to open the sub-menu. (Observed Turn 157449 vs Lorelei, Observed Turn 158300 & 158363 vs Bruno, Observed Turn 158837 vs Bruno, Observed Turn 159956 vs Bruno where 'Down' from CRAG skipped ECHO and landed on TITANESS). I must now visually confirm the cursor's final position *every single turn* within the party menu before making another input.
- **Move Menu Cursor Position Anomaly (Unverified):** The cursor in the move selection menu may default to the last move used, rather than the top-most move. This needs further observation to confirm if it's a consistent mechanic. (Observed Turn 158281 vs Bruno's Poliwrath, Observed Turn 158403 vs Agatha).
- **Move Menu Cursor Reset Anomaly (Unverified):** The move selection cursor can unexpectedly reset to the default top position after directional inputs are made but before 'A' is pressed to confirm the move. This resulted in using BODY SLAM instead of the intended ROCK SLIDE against Agatha's Golbat. This needs more observation to determine the trigger. (Observed Turn 158415)
- **Hypnosis Switch Anomaly:** Unlike other sleep-inducing moves, Poliwrath's Hypnosis did not force an immediate switch after putting ECHO to sleep. (Observed Turn 159225)
- **Switch Override Anomaly (Confirmed):** The game can override a player's intended switch, sending out a different Pokémon. The outcome appears unpredictable and is not always the party lead. (Observed 1: Switching from a sleeping Pokémon, NEPTUNE -> TITANESS resulted in REVENANT being sent out, Turn 157150. Observed 2: Switching from the lead Pokémon, REVENANT -> SPARKY resulted in NEPTUNE being sent out, Turn 159506. Observed 3: Attempting to switch from NEPTUNE to REVENANT resulted in TITANESS being sent out, Turn 159685).

# IV. Tool & Agent Development

## A. Tool & Agent Development Log
- **Diagnostic Tool Output:** Pathfinding tools must report the specific obstacle that blocks a path upon failure. This is essential for distinguishing between a solvable puzzle and a genuinely impossible route.
- **AI Prediction Failure (Confirmation Bias):** I have incorrectly assumed the opponent's AI would use a specific move to counter my current Pokémon, failing to predict that the AI would instead use the optimal move to counter my *switch-in*. (Observed Turn 147728, Lorelei's Lapras vs. CRAG). **Correction:** I must assume the AI will make the optimal play against my predicted action, not just react to the current board state.
- **Agent Gamble Failure & AI Prediction:** The battle_strategist_agent correctly identified a high-risk, high-reward play by switching to CRAG, predicting Lapras would use its known move Thunderbolt. However, the opponent AI made the optimal counter-play by using Surf against the incoming CRAG, leading to a faint. This confirms that the AI is capable of predicting switches and choosing the best move to counter the incoming Pokémon, not just the one on the field. (Observed Turn 149533, Lorelei's Lapras vs. CRAG).
- **Mixed Input Execution:** Tools that generate a sequence of mixed directional and action buttons (e.g., `auto_switcher`) are functioning correctly. The error was in my execution. I must execute the generated button presses one at a time, over multiple turns, to avoid system input truncation.
- **`auto_switcher` Tool Created:** Developed in Turn 155341 to fully automate the Pokémon switch sequence, improving battle efficiency.
- **`auto_attacker` Tool Created:** Developed in Turn 155553 to streamline battle actions by combining move selection and execution into a single command.
- **Master Battle Agent (Implemented Turn 156589):** Created a new orchestrator agent (`master_battle_agent`) that takes raw party/enemy JSON and internally calls `type_map_generator`, `battle_data_extractor`, and `battle_strategist_agent` to return a single, final action. This streamlines the 3-step battle analysis process into a single tool call, improving turn efficiency.
- **`pc_withdraw_pokemon` Tool Created (Turn 157056):** Developed to automate the process of selecting and withdrawing a specific Pokémon from the PC, improving team management efficiency.

# V. Battle Logs

## A. Elite Four - Attempt 1 (Defeat)
- **Agatha:** Lost to Agatha. Her team was GENGAR (Lv 57), GOLBAT (Lv 58), MAROWAK (Lv 57), ARBOK (Lv 58), GENGAR (Lv 59). Observed her ace Gengar use Night Shade and Mega Drain.

## B. Elite Four - Attempt 2 (Defeat)
- **Lorelei:** Defeated.
- **Bruno:** Defeated.
- **Agatha:** Lost to Agatha's ace Gengar (Lv 59). The battle was lost after a critical hit Mega Drain fainted my last Pokémon, TITANESS. No new moves were observed.

## C. Elite Four - Attempt 3 (Defeat)
- **Lorelei:** Defeated.
- **Bruno:** Defeated.
- **Agatha:** Defeated.
- **Lance:** Lost to Lance. His lead Pokémon was DRAGONITE (Lv 61), which used Thunder Wave and Wrap.
- **Failure to Apply Documented Rules:** I correctly documented the refined 'Dead End Area Definition' in my notepad (Turn 157367) but failed to apply it in my validation checks for Agatha's Room, leading to a critical hallucination warning. Correction: I must meticulously review my own documented rules and lessons before making critical judgments, especially for complex definitions.