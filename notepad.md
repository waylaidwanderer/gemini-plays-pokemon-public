# I. Meta-Progression & Lessons Learned

## A. Core Methodological Failures (Self-Correction Log)
- **Inefficient Tool Debugging (Trial-and-Error):** I have repeatedly engaged in prolonged loops of making minor, speculative changes to my tools instead of immediately adding diagnostic outputs (e.g., print statements) to systematically identify the root cause. **Correction:** The correct protocol is to add logging after a tool fails more than once to enable evidence-based fixes.
- **Violation of Immediate Action Mandate (The LLM Reality):** I have repeatedly failed to perform necessary maintenance on my tools and notepad immediately, instead of deferring the tasks to continue gameplay. This is a critical violation of my core directive. **Correction:** There is no 'later'; tasks such as fixing tools or updating notes must be done in the current turn.
- **Flawed Hypothesis Testing (Confirmation Bias):** I have incorrectly assumed a path existed and spent numerous turns trying to fix my tools to confirm this belief, rather than first using a tool like `map_connectivity_analyzer` to test the fundamental assumption of reachability. **Correction:** I must test core assumptions first before attempting to fix tools that rely on those assumptions. I must also actively try to disprove my own hypotheses.
- **Inefficient Puzzle-Solving Methodology:** During the Indigo Plateau lobby puzzle, I wasted significant time on trial-and-error instead of using diagnostic tools like `map_connectivity_analyzer` early on to validate my core assumption that the northern area was reachable. **Correction:** For complex navigation puzzles, I must first use tools to verify assumptions about the map's structure before testing interaction-based hypotheses.
- **Misinterpreting System Feedback:** I have incorrectly assumed my tools or notes were wrong when system feedback indicated otherwise. This led to wasted time trying to 'fix' things that were already correct or pathing to unreachable locations. **Correction:** I must treat system/tool feedback as the source of truth and question my own assumptions first.
- **Over-reliance on Luck (Confirmation Bias):** The FLASH strategy against Bruno's Machamp was successful multiple times due to luck, reinforcing the belief it was a guaranteed win condition. However, it failed when the opponent used a different move (Rock Slide), which may have had higher base accuracy. **Correction:** Luck-based strategies should be a last resort. I must not become overconfident from a lucky streak and must always consider the opponent's full range of options.
- **Agent Output Override Failure (Confirmation Bias):** I incorrectly overrode the `battle_strategist_agent`'s advice to switch to TITANESS against Jynx, instead switching to ECHO. This was a critical error based on my own flawed assumption, which created a dangerous situation and was flagged by the Overwatch system. **Correction:** I must treat the agent's output as the default correct action and only override it if I can definitively prove its underlying assumptions are wrong based on new in-game evidence. (Observed Turn 151161, Corrected Turn 151190)
- **Failure to Trust Agent (Confirmation Bias):** I incorrectly assumed my agent's recommendation to switch to TITANESS against Jynx was suboptimal, leading to a disastrous switch to ECHO instead. This was a critical error rooted in a failure to trust my own tools and was flagged by the Overwatch system. **Correction:** I must adhere to the agent's recommendations unless I have definitive, in-game evidence to prove its reasoning is flawed. (Observed Turn 151161, Corrected Turn 151190)
- **Notepad Overwrite Error (Data Loss):** I incorrectly used the 'overwrite' action in turn 151346 with outdated content, erasing several new development goals. **Correction:** When using 'overwrite', I must ensure I am providing the full, most current version of the notepad to prevent data loss. This is a critical data management failure.
- **Speed Assumption:** I must not assume my Pokémon is faster than an opponent's of the same species, even with a level advantage. Agatha's Lv58 Golbat proved to be faster than my Lv65 ECHO. This is a critical lesson in not making unverified assumptions about stats.
- **Flawed Tool Debugging (Static Data):** I repeatedly failed to debug my `battle_data_extractor` tool because I was passing it the same static, outdated `game_state_json` string from a a previous turn. **Correction:** Tool arguments are not dynamic. I must ensure I am providing the current, correct game state information *each time* a tool is called. Failure to do so invalidates the test.
- **Tool Maintenance Error (Corrected):** I incorrectly logged that I deferred a tool fix in turn 151892. My action log confirms I implemented the fix for `generate_path_plan` in turn 151891. This was a data entry error, not a procedural one. Maintaining accurate logs is critical.
- **Speed Assumption Failure:** I gambled that SPARKY was faster than SLOWBRO without any evidence. I must avoid making assumptions about stats, especially speed, in critical matchups. This was a methodological failure.
- **Confirmation Bias & Inflexibility:** During the battle with Lance's Dragonite, my goal was to lose strategically. However, after a lucky miss from the opponent, I failed to re-evaluate the situation. I continued with the "lose" plan instead of pivoting to a "win" strategy. **Correction:** When unexpected events or luck create a potential opening, I must immediately reassess my strategy and be flexible enough to abandon the original plan if a better opportunity arises.
- **Map Marker Discipline:** I must adopt a clearer system for map markers to distinguish between attempts, such as deleting markers from failed runs to avoid confusion. (Self-Correction Turn 155432)
- **Panic Switching Error (Over-prediction):** Against Agatha's Swords Dance Marowak, I switched out ECHO (immune to Ground STAB) due to fear of a potential Rock Slide, and switched in CRAG (weak to Ground STAB). This was a critical error. I prioritized avoiding a *potential* threat over exploiting a *guaranteed* immunity, resulting in unnecessary damage. **Correction:** I must prioritize guaranteed immunities and resistances over playing around unconfirmed coverage moves, especially when the current matchup is already advantageous.
- **Flawed Tool Debugging (Unverified Assumptions):** The repeated failures of the `auto_attacker` tool were caused by a flawed debugging process. I incorrectly assumed the move menu was a 2x2 grid without performing a simple in-game test to verify this assumption. This led to wasted turns implementing a faulty 'fix' that had to be reverted. **Correction:** I must verify core game mechanics with simple, direct tests before designing or modifying tools that rely on those mechanics.
- **Tool Execution Failure (Self-Correction):** I repeatedly failed to execute the `notepad_edit` tool correctly due to providing mismatched text for replacement. This led to delays in updating my knowledge base, violating the immediate action mandate. **Correction:** I must be more meticulous when using tools, ensuring all arguments are precise to prevent execution failures.
- **Confirmation Bias (Hyper Beam):** I incorrectly concluded that Hyper Beam *always* requires a recharge turn based on a single observation. New evidence has proven this wrong. **Correction:** I must require multiple, consistent observations before documenting a game mechanic as a verified rule. A single data point is not enough.
- **Agent Override Gamble (Failure):** I overrode the `master_battle_agent`'s advice to switch to SPARKY against Lance's Gyarados, believing SPARKY would be faster. This high-risk gamble failed, as Gyarados moved first and KO'd SPARKY. **Correction:** This reinforces the need to avoid unverified speed assumptions. The agent's safer play (attacking with TITANESS for a paralysis chance) was the more strategically sound option in a situation with incomplete information.
- **Failure to Consult Notepad (Confirmation Bias):** I trusted the `master_battle_agent`'s recommendation to use ICE BEAM against Slowbro without first checking my own verified Type Effectiveness Chart, which already correctly stated that Ice is not very effective against Water/Psychic. This resulted in a wasted turn and highlights a failure to trust my own documented findings over an agent's output. **Correction:** I must always cross-reference agent advice with my own verified knowledge base before committing to an action.

## B. System Feedback & Self-Correction (Actioned)
- **Notepad Data Integrity:** I must ensure my notepad does not contain outdated information or function as a to-do list. All system feedback must be immediately actioned and integrated into my permanent knowledge base under 'Lessons Learned'.
- **Tool Development Priority:** Opportunities to automate repetitive tasks must be acted upon immediately, not deferred. This is a core directive.
- **Immediate Development Mandate:** All plans for new tools or agents must be acted upon immediately. Deferring development by creating 'to-do lists' in the notepad is a critical failure of core directives. (Self-Correction Turn 155345, per Overwatch Critique)
- **Party Menu Wrapping (ANOMALY):** The party selection menu appears to wrap, but its behavior is highly unpredictable and buggy. Pressing 'Up' from the top Pokémon can jump the cursor to an unexpected position in the list, not necessarily the bottom. This was confirmed in turn 158745.
- **Team Composition Strategy (Verified):** Used the `team_composition_advisor` agent to confirm that my current team of six level 65 Pokémon is the optimal lineup against the Elite Four and Champion. The agent provided a detailed strategic breakdown for each battle. (Verified Turn 157088)

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
  - Electric is super-effective against Water/Ice dual-types (Observed: Lorelei's Cloyster/Dewgong vs SPARKY; Agatha's Gengar's Thunder vs NEPTUNE's Lapras).
  - Electric is super-effective against Water/Psychic dual-types (Observed: Lorelei's Slowbro vs SPARKY).
  - Fighting is super-effective against Ice-types (Observed: Bruno's Hitmonchan vs NEPTUNE; Bruno's Hitmonlee vs NEPTUNE).
  - Fighting is super-effective against Normal-types (Observed: Bruno's Machamp vs TITANESS).
  - Fighting is super-effective against Rock-types (Observed: Bruno's Machamp vs CRAG).
  - Flying is immune to Ground-type moves (Observed: Pixel's Dodrio vs REVENANT's Marowak).
  - Flying is not very effective against Rock (Observed: ECHO's Fly vs Bruno's Onix).
  - Ghost is immune to Ground-type moves (Observed: battle_strategist_agent reasoning vs Agatha's Gengar).
  - Grass is super-effective against Ground-types (Observed: Agatha's Gengar vs REVENANT's Marowak).
  - Grass is super-effective against Ground/Rock dual-types (Observed: Agatha's Gengar's Mega Drain vs CRAG's Golem).
  - Grass is super-effective against Water/Ice dual-types (Observed: Agatha's Gengar's Mega Drain vs NEPTUNE's Lapras).
  - Ground is super-effective against Electric-types (Observed: Bruno's Machamp vs SPARKY; Lorelei's Slowbro's Earthquake vs SPARKY).
  - Ground is super-effective against Ghost-types (Observed: REVENANT's Earthquake vs Agatha's Gengar).
  - Ground is super-effective against Ground-types (Observed: Lance's Aerodactyl's Earthquake vs CRAG's Golem).
  - Ground is super-effective against Poison-types (Observed: REVENANT vs Agatha's Gengar).
  - Ground is super-effective against Psychic-types (Observed: CRAG's Golem vs Lorelei's Slowbro).
  - Ground is super-effective against Rock/Ground dual-types (Observed: Bruno's Onix vs CRAG's Golem).
  - Ice is not very effective against Psychic-types (Observed: NEPTUNE's Ice Beam vs Lorelei's Slowbro).
  - Ice is super-effective against Ground-types (Observed: Bruno's Poliwrath vs REVENANT's Marowak).
  - Normal is immune to Ghost-type moves (Observed: CRAG's Body Slam vs Agatha's Gengar).
  - Normal is not very effective against Rock/Flying (Observed: REVENANT's Headbutt vs Lance's Aerodactyl).
  - Psychic is super-effective against Poison-types (Observed: Lorelei's Slowbro vs ECHO's Golbat).
  - Rock is not very effective against Ground (Observed: CRAG's Rock Slide vs Agatha's Marowak).
  - Rock is super-effective against Flying (Observed: Bruno's Machamp vs ECHO's Golbat).
  - Water is not very effective against Water/Psychic dual-types (Observed: NEPTUNE's Surf vs Lorelei's Slowbro).

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

## C. Battle Mechanics (Anomalies & Unverified)
- **Hypnosis Anomaly (Corrected):** Agatha's Gengar's first Hypnosis on TITANESS failed (Turn 150576), but a second attempt succeeded (Turn 150583). The initial failure was likely a standard move miss, not an immunity. This confirms TITANESS is not immune to sleep.
- **Night Shade Damage Anomaly:** Agatha's Lv 57 Gengar's Night Shade dealt 38 damage instead of the expected 57. This may be a mechanic change in the ROM hack. (Observed Turn 148518)
- **Hyper Beam Recharge (Contradictory Evidence):** Lance's Aerodactyl was observed to recharge after using Hyper Beam (Turn 158577). However, his Gyarados was able to attack with SLAM immediately after NEPTUNE used a move on the same turn it should have been recharging from Hyper Beam (Turn 159019). The recharge mechanic may be conditional or inconsistent.
- **Hyper Beam Testing Plan:** Hypothesis: Hyper Beam's recharge is conditional. Test 1: Observe if an opponent using Hyper Beam to KO my Pokémon recharges on the next turn. Test 2: Observe if an opponent using Hyper Beam *without* a KO recharges on the next turn.
- **Switch Override Anomaly:** The game has demonstrated unusual behavior when switching out a sleeping Pokémon during the Elite Four battle against Lorelei. When attempting to switch from a sleeping NEPTUNE to TITANESS, the game instead sent out REVENANT (the party lead). This may be a specific, undocumented mechanic related to sleep or the Set battle style. (Observed Turn 157150)
- **Party Menu Cursor Anomaly (Confirmed):** The party menu cursor can jump to a different Pokémon after a directional input, skipping over the intended target. This has happened multiple times, leading to incorrect switches. The jump can occur both after a simple directional press (e.g., pressing 'Up' from ECHO skipped CRAG and landed on NEPTUNE) and after directional inputs are complete but before 'A' is pressed to open the sub-menu. (Observed Turn 157449 vs Lorelei, Observed Turn 158300 & 158363 vs Bruno, Observed Turn 158837 vs Bruno). I must now visually confirm the cursor's final position *every single turn* within the party menu before making another input.
- **Move Menu Cursor Position Anomaly (Unverified):** The cursor in the move selection menu may default to the last move used, rather than the top-most move. This needs further observation to confirm if it's a consistent mechanic. (Observed Turn 158281 vs Bruno's Poliwrath, Observed Turn 158403 vs Agatha).
- **Move Menu Cursor Reset Anomaly (Unverified):** The move selection cursor can unexpectedly reset to the default top position after directional inputs are made but before 'A' is pressed to confirm the move. This resulted in using BODY SLAM instead of the intended ROCK SLIDE against Agatha's Golbat. This needs more observation to determine the trigger. (Observed Turn 158415)

# IV. Tool & Agent Development

## A. Tool & Agent Development Log
- **Agent Idea:** A 'meta-strategy' agent that takes the `master_battle_agent`'s output and my own assessment to reconcile a final action, especially in cases with unique threats like OHKO moves.
- **Diagnostic Tool Output:** Pathfinding tools must report the specific obstacle that blocks a path upon failure. This is essential for distinguishing between a solvable puzzle and a genuinely impossible route.
- **AI Prediction Failure (Confirmation Bias):** I have incorrectly assumed the opponent's AI would use a specific move to counter my current Pokémon, failing to predict that the AI would instead use the optimal move to counter my *switch-in*. (Observed Turn 147728, Lorelei's Lapras vs. CRAG). **Correction:** I must assume the AI will make the optimal play against my predicted action, not just react to the current board state.
- **Agent Gamble Failure & AI Prediction:** The battle_strategist_agent correctly identified a high-risk, high-reward play by switching to CRAG, predicting Lapras would use its known move Thunderbolt. However, the opponent AI made the optimal counter-play by using Surf against the incoming CRAG, leading to a faint. This confirms that the AI is capable of predicting switches and choosing the best move to counter the incoming Pokémon, not just the one on the field. (Observed Turn 149533, Lorelei's Lapras vs. CRAG).
- **Mixed Input Execution:** Tools that generate a sequence of mixed directional and action buttons (e.g., `auto_switcher`) are functioning correctly. The error was in my execution. I must execute the generated button presses one at a time, over multiple turns, to avoid system input truncation.
- **`auto_switcher` Tool Created:** Developed in Turn 155341 to fully automate the Pokémon switch sequence, improving battle efficiency.
- **`auto_attacker` Tool Created:** Developed in Turn 155553 to streamline battle actions by combining move selection and execution into a single command.
- **Master Battle Agent (Implemented Turn 156589):** Created a new orchestrator agent (`master_battle_agent`) that takes raw party/enemy JSON and internally calls `type_map_generator`, `battle_data_extractor`, and `battle_strategist_agent` to return a single, final action. This streamlines the 3-step battle analysis process into a single tool call, improving turn efficiency.
- **`pc_withdraw_pokemon` Tool Created (Turn 157056):** Developed to automate the process of selecting and withdrawing a specific Pokémon from the PC, improving team management efficiency.

# V. Future Exploration & Testing Goals
- **Team Composition Re-evaluation:** If this Elite Four run fails, I must re-evaluate my team composition using the `team_composition_advisor` agent.
- **Lance's Chamber Mystery Room:** If I black out, my next priority is to thoroughly investigate the secret room in Lance's chamber (accessible via warp at 25, 17). I will interact with all tiles and scenery to check for hidden items or events.
- **Party Menu Cursor Anomaly (Testing Plan):** On future switches, I will test input timing (fast vs. slow presses, pauses) to identify patterns in the cursor jump anomaly and determine if it can be controlled or predicted.

  - Ice is super-effective against Poison/Flying dual-types (Observed: Bruno's Hitmonchan vs ECHO's Golbat).