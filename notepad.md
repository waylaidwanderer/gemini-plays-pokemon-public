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
- **Concatenated Battle Text:** The on-screen text log can sometimes display events from multiple turns together, especially after a move that grants invulnerability (e.g., Fly). This can create the illusion of an opponent attacking multiple times in one turn. (Hypothesized Turn 155136)

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

## B. Elite Four Battle Logs (Observed Rosters)
### Lorelei (Attempt 18 - In Progress)
  - Dewgong (Lv 55) - Moves unknown.
  - Jynx (Lv 56) - Known Moves: Psychic, Lovely Kiss, Bubblebeam, Blizzard
  - Slowbro (Lv 56) - Known Moves: Blizzard, Psychic, Earthquake
  - Cloyster (Lv 55) - Known Moves: Explosion
  - Lapras (Lv 57) - Known Moves: Thunderbolt, Surf, Sing, Blizzard

### Bruno (Attempt 18 - In Progress)
  - HITMONCHAN (Lv 57) - Known Moves: Ice Punch, Thunder Punch, Dizzy Punch
  - POLIWRATH (Lv 56) - Known Moves: Amnesia, Hydro Pump, Hypnosis, Ice Beam
  - HITMONLEE (Lv 57) - Known Moves: Body Slam, Jump Kick
  - ONIX (Lv 56) - Known Moves: Earthquake, Rock Slide
  - MACHAMP (Lv 58) - Known Moves: Body Slam, Earthquake, Rock Slide

### Agatha (Attempt 18 - In Progress)
  - GENGAR (Lv 57) - Known Moves: Night Shade, Mega Drain, Hypnosis, Dream Eater
  - GOLBAT (Lv 58) - Known Moves: Toxic, Double Team, Fly
  - MAROWAK (Lv 57) - Known Moves: Rock Slide, Swords Dance, Body Slam
  - ARBOK (Lv 58) - Known Moves: Substitute, Wrap, Sludge, Glare
  - GENGAR (Lv 59) - Known Moves: Mega Drain, Thunder, Psychic, Night Shade

### Champion Pixel (Attempt 4 - Lost)
  - Magneton (Lv 62) - Moves unknown.
  - Dodrio (Lv 61) - Known Moves: Jump Kick, Drill Peck, Hyper Beam
  - Alakazam (Lv 63) - Known Moves: Thunder Wave, Psychic
  - Sandslash (Lv 60) - Known Moves: Cut
  - Cloyster (Lv 62) - Known Moves: Blizzard

## C. Elite Four Mechanics (Verified)
- **Bruno's Rematch (Corrected):** After defeating Bruno once, interacting with him again triggers a mandatory rematch. After the second victory, his dialogue indicates to 'Go on ahead!', and interacting with him again does not trigger a third battle. The path north to Agatha's room is now open.
- **Hypnosis Anomaly (Corrected):** Agatha's Gengar's first Hypnosis on TITANESS failed (Turn 150576), but a second attempt succeeded (Turn 150583). The initial failure was likely a standard move miss, not an immunity. This confirms TITANESS is not immune to sleep.
- **Night Shade Damage Anomaly:** Agatha's Lv 57 Gengar's Night Shade dealt 38 damage instead of the expected 57. This may be a mechanic change in the ROM hack. (Observed Turn 148518)

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

## B. Tool & Agent Development Log
- **Diagnostic Tool Output:** Pathfinding tools must report the specific obstacle that blocks a path upon failure. This is essential for distinguishing between a solvable puzzle and a genuinely impossible route.
- **AI Prediction Failure (Confirmation Bias):** I have incorrectly assumed the opponent's AI would use a specific move to counter my current Pokémon, failing to predict that the AI would instead use the optimal move to counter my *switch-in*. (Observed Turn 147728, Lorelei's Lapras vs. CRAG). **Correction:** I must assume the AI will make the optimal play against my predicted action, not just react to the current board state.
- **`select_battle_option` Tool Misuse:** The tool is designed to execute button presses on its own. Providing manual button presses in the same turn is redundant and incorrect. **Correction:** When using this tool, do not provide any other button presses. (Observed Turn 147891, 147894, 147896, 148739)
- **Battle Strategist Over-Aggression:** The `battle_strategist_agent` has shown a tendency to recommend offensive actions even when facing a known super-effective threat, underestimating the risk. **Correction (Turn 148487):** The agent's system prompt has been updated to prioritize a defensive switch when a known super-effective threat is present.
- **Agent Gamble Failure & AI Prediction:** The battle_strategist_agent correctly identified a high-risk, high-reward play by switching to CRAG, predicting Lapras would use its known move Thunderbolt. However, the opponent AI made the optimal counter-play by using Surf against the incoming CRAG, leading to a faint. This confirms that the AI is capable of predicting switches and choosing the best move to counter the incoming Pokémon, not just the one on the field. (Observed Turn 149533, Lorelei's Lapras vs. CRAG).

# IV. Puzzle Archive (Completed)

## A. Victory Road 3F Boulder Puzzle
- **Conclusion:** The tile at (8, 11) changed from `boulder_barrier` to `cleared_boulder_barrier` after the boulder was placed on the switch at (4, 6).

## B. Victory Road 2F Boulder Puzzle
- **Conclusion:** A boulder was brought down from Victory Road 3F through the hole at (24, 16) on 3F. It landed at (23, 17) on 2F and was pushed to the switch at (10, 17). The barrier at (24, 15) is now open.

# V. Confirmed Mechanics & Untested Hypotheses

## A. Confirmed & Corrected Mechanics
- **Party Menu Wrapping (CORRECTED):** The party selection menu does NOT wrap around. Pressing 'Up' from the top Pokémon does not move the cursor to the bottom. This was confirmed in turn 154047.

## B. Untested Hypotheses
- **Concatenated Battle Text (UNVERIFIED):** The on-screen text log may sometimes display events from multiple turns together, especially after a move that grants invulnerability (e.g., Fly). This can create the illusion of an opponent attacking multiple times in one turn. (Hypothesized Turn 155136)
- **PC Box Selection Anomaly (UNVERIFIED):** The game may select the box one position *below* the highlighted cursor. This has only been observed once and requires further testing to confirm if it's a consistent bug. The logic for the `pc_pokemon_selector` tool is based on an untested assumption about the PC interface and will require manual observation and debugging.
- **Forced Switch Mechanic (UNVERIFIED):** The game sometimes overrides the player's choice of Pokémon during a switch. **Observation 1 (vs. Bruno):** Switched from REVENANT (conscious) to NEPTUNE. Game sent out TITANESS. Party order had a sleeping SPARKY before TITANESS. **Observation 2 (vs. Agatha):** Switched from SPARKY (sleeping) to CRAG. Game sent out ECHO. Party order had sleeping/fainted Pokémon, then REVENANT, then ECHO. The exact trigger conditions are still unknown. **Test Plan:** When forced to switch, if there are sleeping Pokémon in the party, I will deliberately select a conscious Pokémon that is positioned *after* a sleeping Pokémon in the party list. If the game sends out the sleeping Pokémon instead of my selection, the hypothesis that the game prioritizes sleeping Pokémon in the switch order will be supported.
- **Speed Assumption Failure (Jynx) (UNVERIFIED):** SPARKY might not be faster than Lorelei's Jynx. This assumption led to SPARKY being put to sleep and needs to be verified.

## C. Falsified Hypotheses
- **Pikachu Warp Block (FALSIFIED):** The hypothesis that Pikachu blocks warp tiles has been falsified. I have successfully used multiple warps while Pikachu was following, including the warp from Agatha's room to Lance's room. Pikachu's presence on a warp tile does not prevent its use.

# VI. Strategic Reminders & Active Plans

## A. Agent & Tool Usage Protocols
- **Team Building:** For major challenges like the Elite Four, I must use the `team_composition_advisor` agent to get a data-driven recommendation instead of relying solely on manual selection. This will prevent oversights and optimize my team composition. (Self-Correction Turn 152853)

## B. Confirmed Battle Mechanics
- **SPOONBENDE Speed:** My Lv 38 Kadabra (SPOONBENDE) is confirmed to be faster than Agatha's Lv 57 Gengar. The hypothesis that it might be too slow has been falsified, which makes the Psychic-spam strategy viable.

# VII. Future Development & Testing Plans

## A. Tool & Agent Ideas
- **`auto_switch` tool:** Combine `select_battle_option` ('PKMN') and `select_party_pokemon` into a single tool that takes a Pokémon's name and executes the entire switch sequence automatically. This would significantly improve battle efficiency. **Plan:** Create a tool named `auto_switch` that takes `pokemon_to_select` as input. The script will first call `select_battle_option` with `PKMN`, then determine the current party state and call `select_party_pokemon`, and finally execute the 'A' press to confirm the switch.
- **`pre_battle_analyzer` agent:** An agent that takes party/opponent data and outputs a high-level summary of threats, weaknesses, and viable switch-ins to streamline the decision-making process before calling the main `battle_strategist_agent`.

# VIII. Active Hypothesis Testing

## A. Forced Switch Mechanic
- **Hypothesis:** The game prioritizes sending out a sleeping Pokémon during a forced switch, even if a conscious Pokémon is selected.
- **Test Plan:** During the next forced switch where a sleeping Pokémon is available, I will deliberately select a conscious Pokémon that is positioned *after* the sleeping one in the party list. 
- **Expected Outcome:** If the game sends out the sleeping Pokémon, the hypothesis is supported. If it sends out my selected Pokémon, the hypothesis is denied.

# IX. Overwatch Critique Log (For Actioning)

## A. Tool Development Notes
- **Flawed Tool Design (pc_pokemon_selector):** The tool was designed based on an unverified assumption about PC box navigation. I must manually observe and document the PC interface mechanics before attempting to fix the tool's logic. (Critique Turn 154620)