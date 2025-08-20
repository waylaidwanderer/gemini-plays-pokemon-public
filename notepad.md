# I. Game Mechanics & World Knowledge

## A. Core Gameplay (Verified)
- **Battle Style:** Set mode.
- **Items in Battle:** Prohibited.
- **Level Caps:** Active and enforced.
- **PC Interaction:** To use a PC, stand on the tile directly *below* it and face *up* before pressing 'A'.
- **Menu Navigation:** The 'B' button is the primary method for exiting/canceling out of menus.
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
- **Dead End Area Definition:** An area is NOT a 'dead end' if there are reachable unvisited warps, Reachable Undiscovered Map Connections, OR the `Reachable Unseen Tiles` list for the current map contains entries. A room with multiple reachable exits (warps/connections) is also NOT a dead end, even if all tiles have been seen. (Corrected Turn 152613)

# II. Battle Information

## A. Type Effectiveness Chart (Verified)
- **Objective:** Systematically test and verify all type matchups in this ROM hack, as the standard chart is unreliable.
- **Method:** During battles, especially against the Elite Four, prioritize using moves with uncertain effectiveness to gather data. Record all super-effective, not-very-effective, and immune interactions observed.
- **Findings:**
  - Electric is super-effective against Water/Psychic dual-types (Observed: Lorelei's Slowbro vs SPARKY).
  - Electric is super-effective against Water/Ice dual-types (Observed: Lorelei's Cloyster/Dewgong vs SPARKY; Agatha's Gengar's Thunder vs NEPTUNE's Lapras).
  - Fighting is super-effective against Ice-types (Observed: Bruno's Hitmonchan vs NEPTUNE; Bruno's Hitmonlee vs NEPTUNE).
  - Fighting is super-effective against Normal-types (Observed: Bruno's Machamp vs TITANESS).
  - Fighting is super-effective against Rock-types (Observed: Bruno's Machamp vs CRAG).
  - Flying is immune to Ground-type moves (Observed: Pixel's Dodrio vs REVENANT's Marowak).
  - Flying is not very effective against Rock (Observed: ECHO's Fly vs Bruno's Onix).
  - Ghost is immune to Ground-type moves (Observed: battle_strategist_agent reasoning vs Agatha's Gengar).
  - Grass is super-effective against Ground/Rock dual-types (Observed: Agatha's Gengar's Mega Drain vs CRAG's Golem).
  - Grass is super-effective against Ground-types (Observed: Agatha's Gengar vs REVENANT's Marowak).
  - Grass is super-effective against Water/Ice dual-types (Observed: Agatha's Gengar's Mega Drain vs NEPTUNE's Lapras).
  - Ground is super-effective against Electric-types (Observed: Bruno's Machamp vs SPARKY).
  - Ground is super-effective against Ghost-types (Observed: REVENANT's Earthquake vs Agatha's Gengar).
  - Ground is super-effective against Ground-types (Observed: Lance's Aerodactyl's Earthquake vs CRAG's Golem).
  - Ground is super-effective against Poison-types (Observed: REVENANT vs Agatha's Gengar).
  - Ground is super-effective against Psychic-types (Observed: CRAG's Golem vs Lorelei's Slowbro).
  - Ground is super-effective against Rock/Ground dual-types (Observed: Bruno's Onix vs CRAG's Golem).
  - Ice is not very effective against Psychic-types (Observed: NEPTUNE's Ice Beam vs Lorelei's Slowbro).
  - Ice is super-effective against Ground-types (Observed: Bruno's Poliwrath vs REVENANT's Marowak).
  - Normal is immune to Ghost-type moves (Observed: CRAG's Body Slam vs Agatha's Gengar).
  - Psychic is super-effective against Poison-types (Observed: Lorelei's Slowbro vs ECHO's Golbat).
  - Rock is super-effective against Flying (Observed: Bruno's Machamp vs ECHO's Golbat).
  - Water is not very effective against Water/Psychic dual-types (Observed: NEPTUNE's Surf vs Lorelei's Slowbro).
  - Normal is not very effective against Rock/Flying (Observed: REVENANT's Headbutt vs Lance's Aerodactyl).

## B. Opponent Rosters & Moves (Observed)
### Lorelei
  - DEWGONG (Lv 55) - Moves unknown.
  - JYNX (Lv 56) - Known Moves: Psychic, Lovely Kiss, Bubblebeam, Blizzard
  - SLOWBRO (Lv 56) - Known Moves: Blizzard, Psychic, Earthquake
  - CLOISTER (Lv 55) - Known Moves: Explosion
  - LAPRAS (Lv 57) - Known Moves: Thunderbolt, Surf, Sing, Blizzard

### Bruno
  - HITMONCHAN (Lv 57) - Known Moves: Submission, Ice Punch, Thunder Punch, Dizzy Punch
  - POLIWRATH (Lv 56) - Known Moves: Amnesia, Hydro Pump, Hypnosis, Ice Beam
  - HITMONLEE (Lv 57) - Known Moves: Body Slam, HI JUMP KICK
  - ONIX (Lv 56) - Known Moves: Earthquake, Rock Slide, BIND
  - MACHAMP (Lv 58) - Known Moves: Body Slam, Earthquake, Rock Slide

### Agatha
  - GENGAR (Lv 57) - Known Moves: Night Shade, Mega Drain, Hypnosis, Dream Eater
  - GOLBAT (Lv 58) - Known Moves: Toxic, Double Team, Fly
  - MAROWAK (Lv 57) - Known Moves: Rock Slide, Swords Dance, Body Slam
  - ARBOK (Lv 58) - Known Moves: Substitute, Wrap, Sludge, Glare
  - GENGAR (Lv 59) - Known Moves: Mega Drain, Thunder, Psychic, Night Shade

### Lance (Defeated)
  - DRAGONITE (Lv 61) - Known Moves: Hyper Beam, THUNDER WAVE, WRAP
  - GYARADOS (Lv 60) - Known Moves: Slam
  - CHARIZARD (Lv 60) - Known Moves: Earthquake, Flamethrower
  - AERODACTYL (Lv 61) - Known Moves: Earthquake, Hyper Beam, ROCK SLIDE
  - DRAGONITE (Lv 62) - Known Moves: Fire Blast, Slam, Thunder Wave, Wrap, Hyper Beam, Blizzard, Thunder

### Champion Pixel
  - MAGNETON (Lv 62) - Known Moves: THUNDER WAVE, THUNDER, TRI ATTACK
  - DODRIO (Lv 61) - Known Moves: DRILL PECK, HYPER BEAM

## C. Battle Mechanics (Verified)
- **SPOONBENDE Speed:** My Lv 38 Kadabra (SPOONBENDE) is confirmed to be faster than Agatha's Lv 57 Gengar.
- **Rematch Mechanic:** Some Elite Four members (Bruno, Agatha) require a second interaction to trigger a mandatory rematch before allowing progression.
- **Hypnosis Anomaly (Corrected):** Agatha's Gengar's first Hypnosis on TITANESS failed (Turn 150576), but a second attempt succeeded (Turn 150583). The initial failure was likely a standard move miss, not an immunity. This confirms TITANESS is not immune to sleep.
- **Night Shade Damage Anomaly:** Agatha's Lv 57 Gengar's Night Shade dealt 38 damage instead of the expected 57. This may be a mechanic change in the ROM hack. (Observed Turn 148518)
- **Hyper Beam Recharge (CORRECTED):** The move Hyper Beam does NOT guarantee a recharge turn for the opponent. An opponent can act immediately on the following turn. (Observed: Lance's Charizard used Earthquake after I switched in SPARKY, expecting a free turn. Turn 155531)
- **Tool Output Methodology (Corrected):** Tools like `auto_switcher` that generate a sequence of mixed directional and action buttons are not faulty. The error was in my execution. I must execute the generated button presses one at a time, over multiple turns, to avoid system input truncation. I will not attempt to fix tools that are functioning as designed.

# III. Meta-Progression & Lessons Learned

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

## B. Tool & Agent Development Log
- **Diagnostic Tool Output:** Pathfinding tools must report the specific obstacle that blocks a path upon failure. This is essential for distinguishing between a solvable puzzle and a genuinely impossible route.
- **AI Prediction Failure (Confirmation Bias):** I have incorrectly assumed the opponent's AI would use a specific move to counter my current Pokémon, failing to predict that the AI would instead use the optimal move to counter my *switch-in*. (Observed Turn 147728, Lorelei's Lapras vs. CRAG). **Correction:** I must assume the AI will make the optimal play against my predicted action, not just react to the current board state.
- **Battle Strategist Over-Aggression:** The `battle_strategist_agent` has shown a tendency to recommend offensive actions even when facing a known super-effective threat, underestimating the risk. **Correction (Turn 148487):** The agent's system prompt has been updated to prioritize a defensive switch when a known super-effective threat is present.
- **Agent Gamble Failure & AI Prediction:** The battle_strategist_agent correctly identified a high-risk, high-reward play by switching to CRAG, predicting Lapras would use its known move Thunderbolt. However, the opponent AI made the optimal counter-play by using Surf against the incoming CRAG, leading to a faint. This confirms that the AI is capable of predicting switches and choosing the best move to counter the incoming Pokémon, not just the one on the field. (Observed Turn 149533, Lorelei's Lapras vs. CRAG).
- **`auto_switcher` Tool Created:** Developed in Turn 155341 to fully automate the Pokémon switch sequence, improving battle efficiency.
- **`pre_battle_analyzer` Agent Created:** Developed in Turn 155344 to provide high-level strategic summaries before major battles.
- **`auto_attacker` Tool Created:** Developed in Turn 155553 to streamline battle actions by combining move selection and execution into a single command.

## C. System Feedback & Self-Correction (Actioned)
- **Notepad Data Integrity:** I must ensure my notepad does not contain outdated information or function as a to-do list. All system feedback must be immediately actioned and integrated into my permanent knowledge base under 'Lessons Learned'.
- **Tool Development Priority:** Opportunities to automate repetitive tasks must be acted upon immediately, not deferred. This is a core directive.
- **Immediate Development Mandate:** All plans for new tools or agents must be acted upon immediately. Deferring development by creating 'to-do lists' in the notepad is a critical failure of core directives. (Self-Correction Turn 155345, per Overwatch Critique)

# V. Confirmed Mechanics & Untested Hypotheses

## A. Confirmed & Corrected Mechanics
- **Party Menu Wrapping (CORRECTED):** The party selection menu does NOT wrap around. Pressing 'Up' from the top Pokémon does not move the cursor to the bottom. This was confirmed in turn 154047.

## B. Untested Hypotheses
- **Type Matchup (UNVERIFIED):** Electric vs. Flying. Need to test this matchup to confirm effectiveness.
- **Concatenated Battle Text (UNVERIFIED):** The on-screen text log may sometimes display events from multiple turns together, especially after a move that grants invulnerability (e.g., Fly). This can create the illusion of an opponent attacking multiple times in one turn. (Hypothesized Turn 155136, 155566, 155585)
- **PC Box Selection Anomaly (UNVERIFIED):** The game may select the box one position *below* the highlighted cursor. This has only been observed once and requires further testing to confirm if it's a consistent bug. The logic for the `pc_pokemon_selector` tool is based on an untested assumption about the PC interface and will require manual observation and debugging.
- **Forced Switch Mechanic (UNVERIFIED):** The game sometimes overrides the player's choice of Pokémon during a switch. The exact trigger conditions are still unknown. **Test Plan:** When forced to switch, if there are sleeping Pokémon in the party, I will deliberately select a conscious Pokémon that is positioned *after* a sleeping Pokémon in the party list. If the game sends out the sleeping Pokémon instead of my selection, the hypothesis that the game prioritizes sleeping Pokémon in the switch order will be supported.
- **Speed Assumption Failure (Jynx) (UNVERIFIED):** SPARKY might not be faster than Lorelei's Jynx. This assumption led to SPARKY being put to sleep and needs to be verified.
- **Paralysis Move Anomaly (UNVERIFIED):** It's possible that paralysis can cause a Pokémon to use a different move than the one selected. Observed when TITANESS used DOUBLE-EDGE instead of BODY SLAM. Requires further testing to confirm if this is a consistent mechanic or a one-time glitch/mis-input.

# VI. Active Investigations

## A. Party Menu Cursor Behavior (Hypothesis)
- **Observation:** The `auto_switcher` tool failed because the cursor's starting position in the party menu was not what I assumed it would be after a Pokémon fainted.
- **Hypothesis:** The cursor position in the party menu (when forced to switch) has specific, predictable logic. It may default to the first non-fainted Pokémon in the list, or the Pokémon in the slot following the fainted one.
- **Test Plan:** After the Elite Four, I will enter wild battles and systematically test different scenarios (e.g., first Pokémon faints, middle Pokémon faints) to observe and document the cursor's default position. This is critical for improving my battle automation tools.