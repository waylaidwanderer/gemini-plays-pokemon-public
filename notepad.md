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
- **Dead End Area Definition:** An area is NOT a 'dead end' if there are reachable unvisited warps, Reachable Undiscovered Map Connections, OR the `Reachable Unseen Tiles` list for the current map contains entries. A room with multiple reachable exits (warps/connections) is also NOT a dead end, even if all tiles have been seen. (Corrected Turn 151866)

# II. Battle Information

## A. Type Effectiveness Chart (Verified)
- **Objective:** Systematically test and verify all type matchups in this ROM hack, as the standard chart is unreliable.
- **Method:** During battles, especially against the Elite Four, prioritize using moves with uncertain effectiveness to gather data. Record all super-effective, not-very-effective, and immune interactions observed.
- **Findings:**
  - Flying is not very effective against Rock (Observed: ECHO's Fly vs Bruno's Onix).
  - Ground is super-effective against Rock/Ground dual-types (Observed: Bruno's Onix vs CRAG's Golem).
  - Ground is super-effective against Ground-types (Verified via agent prompt).
  - Ground is super-effective against Poison-types (Observed: REVENANT vs Agatha's Gengar).
  - Ground is super-effective against Electric-types (Observed: Bruno's Machamp vs SPARKY).
  - Fighting is super-effective against Normal-types (Observed: Bruno's Machamp vs TITANESS).
  - Fighting is super-effective against Ice-types (Observed: Bruno's Hitmonchan vs NEPTUNE).
  - Fighting is super-effective against Rock-types (Observed: Bruno's Machamp vs CRAG).
  - Flying is immune to Ground-type moves (Observed: Pixel's Dodrio vs REVENANT's Marowak).
  - Ground is super-effective against Psychic-types (Observed: CRAG's Golem vs Lorelei's Slowbro).
  - Psychic is super-effective against Poison-types (Observed: Lorelei's Slowbro vs ECHO's Golbat).
  - Grass is super-effective against Ground-types (Observed: Agatha's Gengar vs REVENANT's Marowak).
  - Ice is super-effective against Ground-types (Observed: Bruno's Poliwrath vs REVENANT's Marowak).
  - Ice is not very effective against Psychic-types (Observed: NEPTUNE's Ice Beam vs Lorelei's Slowbro).
  - Water is not very effective against Water/Psychic dual-types (Observed: NEPTUNE's Surf vs Lorelei's Slowbro).
  - Rock is super-effective against Flying (Observed: Bruno's Machamp vs ECHO's Golbat).

## B. Elite Four Battle Logs (Observed Rosters)
### Lorelei
  - Slowbro (Lv 56) - Known Moves: Blizzard, Psychic
  - Cloyster (Lv 55) - Moves unknown.
  - Dewgong (Lv 55) - Moves unknown.
  - Jynx (Lv 56) - Known Moves: Psychic, Lovely Kiss
  - Lapras (Lv 57) - Known Moves: Thunderbolt, Surf, Sing

### Bruno (Attempt 10 - Won)
  - HITMONCHAN (Lv 57) - Known Moves: Ice Punch, Thunder Punch
  - ONIX (Lv 56) - Known Moves: Earthquake, Explosion
  - MACHAMP (Lv 58) - Known Moves: Earthquake, Karate Chop, Rock Slide, Body Slam
  - HITMONCHAN (Lv 57) - Known Moves: Ice Punch, Thunder Punch
  - POLIWRATH (Lv 56) - Known Moves: Amnesia, Hydro Pump, Hypnosis, Ice Beam

### Agatha (Attempt 11 - Lost)
  - GENGAR (Lv 57) - Known Moves: Night Shade, Mega Drain, Hypnosis, Dream Eater
  - GOLBAT (Lv 58) - Known Moves: Toxic, Double Team, Fly
  - MAROWAK (Lv 57) - Known Moves: Rock Slide, Swords Dance, Body Slam
  - ARBOK (Lv 58) - Known Moves: Substitute, Wrap, Sludge
  - GENGAR (Lv 59) - Known Moves: Mega Drain, Thunder, Psychic, Night Shade

### Lance (Attempt 4 - Lost)
  - Dragonite (Lv 61) - Moves unknown.
  - Gyarados (Lv 60) - Known Moves: Fly

### Champion Pixel (Attempt 1 - Lost)
  - Magneton (Lv 62) - Moves unknown.
  - Dodrio (Lv 61) - Known Moves: Jump Kick, Drill Peck, Hyper Beam
  - Alakazam (Lv 63) - Known Moves: Thunder Wave, Psychic

## C. Elite Four Mechanics (Verified)
- **Bruno's Rematch:** After defeating Bruno once, the exit to Agatha's room is blocked. Interacting with him again triggers a mandatory rematch. This second victory is required to proceed. (Observed Turn 150529)
- **Hypnosis Anomaly (Corrected):** Agatha's Gengar's first Hypnosis on TITANESS failed (Turn 150576), but a second attempt succeeded (Turn 150583). The initial failure was likely a standard move miss, not an immunity. This confirms TITANESS is not immune to sleep.
- **Night Shade Damage Anomaly:** Agatha's Lv 57 Gengar's Night Shade dealt 38 damage instead of the expected 57. This may be a mechanic change in the ROM hack. (Observed Turn 148518)

# III. Meta-Progression & Lessons Learned

## A. Core Methodological Failures (Self-Correction Log)
- **Inefficient Tool Debugging (Trial-and-Error):** I have repeatedly engaged in prolonged loops of making minor, speculative changes to my tools instead of immediately adding diagnostic outputs (e.g., print statements) to systematically identify the root cause. **Correction:** The correct protocol is to add logging after a tool fails more than once to enable evidence-based fixes.
- **Violation of Immediate Action Mandate (The LLM Reality):** I have repeatedly failed to perform necessary maintenance on my tools and notepad immediately, instead of deferring the tasks to continue gameplay. This is a critical violation of my core directive. **Correction:** There is no 'later'; tasks such as fixing tools or updating notes must be done in the current turn.
- **Flawed Hypothesis Testing (Confirmation Bias):** I have incorrectly assumed a path existed and spent numerous turns trying to fix my tools to confirm this belief, rather than first using a tool like `map_connectivity_analyzer` to test the fundamental assumption of reachability. **Correction:** I must test core assumptions first before attempting to fix tools that rely on those assumptions. I must also actively try to disprove my own hypotheses.
- **Misinterpreting System Feedback:** I have incorrectly assumed my tools or notes were wrong when system feedback indicated otherwise. This led to wasted time trying to 'fix' things that were already correct or pathing to unreachable locations. **Correction:** I must treat system/tool feedback as the source of truth and question my own assumptions first.
- **Over-reliance on Luck (Confirmation Bias):** The FLASH strategy against Bruno's Machamp was successful multiple times due to luck, reinforcing the belief it was a guaranteed win condition. However, it failed when the opponent used a different move (Rock Slide), which may have had higher base accuracy. **Correction:** Luck-based strategies should be a last resort. I must not become overconfident from a lucky streak and must always consider the opponent's full range of options.
- **Agent Output Override Failure (Confirmation Bias):** I incorrectly overrode the `battle_strategist_agent`'s advice to switch to TITANESS against Jynx, instead switching to ECHO. This was a critical error based on my own flawed assumption, which created a dangerous situation and was flagged by the Overwatch system. **Correction:** I must treat the agent's output as the default correct action and only override it if I can definitively prove its underlying assumptions are wrong based on new in-game evidence. (Observed Turn 151161, Corrected Turn 151190)
- **Failure to Trust Agent (Confirmation Bias):** I incorrectly assumed my agent's recommendation to switch to TITANESS against Jynx was suboptimal, leading to a disastrous switch to ECHO instead. This was a critical error rooted in a failure to trust my own tools and was flagged by the Overwatch system. **Correction:** I must adhere to the agent's recommendations unless I have definitive, in-game evidence to prove its reasoning is flawed. (Observed Turn 151161, Corrected Turn 151190)
- **Notepad Overwrite Error (Data Loss):** I incorrectly used the 'overwrite' action in turn 151346 with outdated content, erasing several new development goals. **Correction:** When using 'overwrite', I must ensure I am providing the full, most current version of the notepad to prevent data loss. This is a critical data management failure.
- **Speed Assumption:** I must not assume my Pokémon is faster than an opponent's of the same species, even with a level advantage. Agatha's Lv58 Golbat proved to be faster than my Lv65 ECHO. This is a critical lesson in not making unverified assumptions about stats.

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

# V. Untested Hypotheses (Active)
- **PC Box Selection Anomaly:** The game may select the box one position *below* the highlighted cursor. This has only been observed once and requires further testing to confirm if it's a consistent bug. (Next Test: Next time 'CHANGE BOX' is used).
- **Tool Maintenance Error (Corrected):** I incorrectly logged that I deferred a tool fix in turn 151892. My action log confirms I implemented the fix for `generate_path_plan` in turn 151891. This was a data entry error, not a procedural one. Maintaining accurate logs is critical.
- **Forced Switch Anomaly:** In turn 151914, I intended to switch to TITANESS, but the game sent out REVENANT instead. This may have been a game bug, an input error on my part, or an unknown game mechanic. This requires careful observation of future switch commands to determine if it's a recurring issue.

### Lance (Attempt 5 - Lost)
  - Charizard (Lv 60) - Known Moves: Hyper Beam, Earthquake

### Type Effectiveness Update
- Ground is super-effective against Electric-types (Observed: Lance's Charizard vs SPARKY).