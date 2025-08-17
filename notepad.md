# I. Game Mechanics & World Knowledge

## A. Core Gameplay (Verified)
- **Battle Style:** Set mode.
- **Items in Battle:** Prohibited.
- **Level Caps:** Active and enforced.
- **PC Interaction:** To use a PC, stand on the tile directly *below* it and face *up* before pressing 'A'.
- **Menu Navigation:** The 'B' button is the primary method for exiting/canceling out of menus.
- **Forced Sleeping Switch:** The game will force you to send out or switch to a sleeping Pokémon if no other conscious Pokémon are available. This is a mechanical exception to the strategic guideline of avoiding switching to sleeping Pokémon.
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
- **Dead End Area Definition:** An area is NOT a 'dead end' if there are reachable unvisited warps, Reachable Undiscovered Map Connections, OR the `Reachable Unseen Tiles` list for the current map contains entries. This is a correction from a previous misunderstanding.

## D. In-Battle Menu Navigation
- **Move Selection (Verified):** The move list is a single vertical column. Navigation is with Up/Down only; Left/Right do nothing.
  - **Move 1 (Top):** Press 'A'.
  - **Move 2:** From Move 1, press 'Down', then 'A'.
  - **Move 3:** From Move 1, press 'Down' twice, then 'A'.
  - **Move 4 (Bottom):** From Move 1, press 'Down' three times, then 'A'.

## F. Type Effectiveness Chart (Verified)
- **Objective:** Systematically test and verify all type matchups in this ROM hack, as the standard chart is unreliable.
- **Method:** During battles, especially against the Elite Four, prioritize using moves with uncertain effectiveness to gather data. Record all super-effective, not-very-effective, and immune interactions observed.
- **Findings:**
  - Ground is super-effective against Rock/Ground dual-types (Observed: Bruno's Onix vs CRAG's Golem).
  - Ground is super-effective against Ground-types (Verified via agent prompt).
  - Fighting is super-effective against Normal-types (Observed: Bruno's Machamp vs TITANESS).
  - Fighting is super-effective against Ice-types (Observed: Bruno's Hitmonchan vs NEPTUNE).
  - Fighting is super-effective against Rock-types (Verified via agent prompt).
  - Flying is immune to Ground-type moves (Observed: Pixel's Dodrio vs REVENANT's Marowak).

## G. In-Game Discoveries
- **Night Shade Damage Anomaly:** Agatha's Lv 57 Gengar's Night Shade dealt 38 damage instead of the expected 57. This may be a mechanic change in the ROM hack. (Observed Turn 148518)

# II. Battle Information

## A. Elite Four Battle Logs (Observed Rosters)
### Lorelei (Attempt 3 - Defeated)
  - Slowbro (Lv 56) - Known Moves: Psychic, Earthquake
  - Cloyster (Lv 55) - Moves unknown.
  - Dewgong (Lv 55) - Moves unknown.
  - Jynx (Lv 56) - Known Moves: Psychic
  - Lapras (Lv 57) - Known Moves: Thunderbolt

### Agatha (Attempt 1 - Defeated)
  - Gengar (Lv 57) - Known Moves: Night Shade, Mega Drain, Hypnosis, Dream Eater
  - Golbat (Lv 58) - Known Moves: Toxic, Double Team, Fly
  - Marowak (Lv 57) - Known Moves: Rock Slide, Earthquake
  - Arbok (Lv 58) - Known Moves: Glare, Substitute, Wrap
  - Gengar (Lv 59) - Known Moves: Psychic, Mega Drain

### Lance (Attempt 1 - Lost)
  - Dragonite (Lv 61) - Known Moves: Slam, Thunder Wave, Wrap
  - Gyarados (Lv 60) - Known Moves: Hyper Beam
  - Charizard (Lv 60) - Known Moves: Hyper Beam

### Champion Pixel (Attempt 1 - Lost)
  - Magneton (Lv 62) - Moves unknown.
  - Dodrio (Lv 61) - Known Moves: Jump Kick, Drill Peck, Hyper Beam
  - Alakazam (Lv 63) - Known Moves: Thunder Wave, Psychic

# III. Meta-Progression & Lessons Learned

## A. Core Methodological Failures (Self-Correction Log)
- **Inefficient Tool Debugging (Trial-and-Error):** I have repeatedly engaged in prolonged loops of making minor, speculative changes to my tools instead of immediately adding diagnostic outputs (e.g., print statements) to systematically identify the root cause. **Correction:** The correct protocol is to add logging after a tool fails more than once to enable evidence-based fixes.
- **Violation of Immediate Action Mandate (The LLM Reality):** I have repeatedly failed to perform necessary maintenance on my tools and notepad immediately, instead of deferring the tasks to continue gameplay. This is a critical violation of my core directive. **Correction:** There is no 'later'; tasks such as fixing tools or updating notes must be done in the current turn.
- **Flawed Hypothesis Testing (Confirmation Bias):** I have incorrectly assumed a path existed and spent numerous turns trying to fix my tools to confirm this belief, rather than first using a tool like `map_connectivity_analyzer` to test the fundamental assumption of reachability. **Correction:** I must test core assumptions first before attempting to fix tools that rely on those assumptions. I must also actively try to disprove my own hypotheses.
- **Misinterpreting System Feedback:** I have incorrectly assumed my tools or notes were wrong when system feedback indicated otherwise. This led to wasted time trying to 'fix' things that were already correct or pathing to unreachable locations. **Correction:** I must treat system/tool feedback as the source of truth and question my own assumptions first.

## B. Tool & Agent Development Log
- **Diagnostic Tool Output:** Pathfinding tools must report the specific obstacle that blocks a path upon failure. This is essential for distinguishing between a solvable puzzle and a genuinely impossible route.
- **Invulnerability-Piercing Move Failure (Hypothesis):** Moves that normally hit invulnerable opponents (e.g., Earthquake vs. Dig) have failed to connect. This may be an intentional mechanic change in the ROM hack. (Observed Turn 145570, 145588)
- **AI Prediction Failure (Confirmation Bias):** I have incorrectly assumed the opponent's AI would use a specific move to counter my current Pokémon, failing to predict that the AI would instead use the optimal move to counter my *switch-in*. (Observed Turn 147728, Lorelei's Lapras vs. CRAG). **Correction:** I must assume the AI will make the optimal play against my predicted action, not just react to the current board state.
- **`select_battle_option` Tool Misuse:** The tool is designed to execute button presses on its own. Providing manual button presses in the same turn is redundant and incorrect. **Correction:** When using this tool, do not provide any other button presses. (Observed Turn 147891, 147894, 147896, 148739)
- **Battle Agent Over-Aggression:** The `battle_strategist_agent` has shown a tendency to recommend offensive actions even when facing a known super-effective threat, underestimating the risk. **Correction (Turn 148487):** The agent's system prompt has been updated to prioritize a defensive switch when a known super-effective threat is present.
- **`pokemon_stat_formatter` (Placeholder):** Created to automate Pokémon cataloging. Realized during creation that the tool execution environment only injects `map_xml_string`, not the full game state JSON. The tool requires party data to function, so the current version is a non-functional placeholder. This is a key lesson: tools must be designed around available data inputs. Future work will involve finding a way to pass the necessary party data to a tool or agent.
- **`battle_flow_predictor` Usage Mandate:** Per Overwatch feedback (Turn 149340), I must use this agent before my next Elite Four attempt to test its effectiveness.
- **Agent Gamble Failure & AI Prediction:** The battle_strategist_agent correctly identified a high-risk, high-reward play by switching to CRAG, predicting Lapras would use its known move Thunderbolt. However, the opponent AI made the optimal counter-play by using Surf against the incoming CRAG, leading to a faint. This confirms that the AI is capable of predicting switches and choosing the best move to counter the incoming Pokémon, not just the one on the field. (Observed Turn 149533, Lorelei's Lapras vs. CRAG).
- **`last_stand_strategist_agent` (Created Turn 150111):** Created in response to a forced, no-win switch scenario against Agatha's Gengar. This agent is designed for desperate situations where standard strategic rules must be broken. It successfully identified the least detrimental option by recommending a switch to a higher-HP sleeping Pokémon (SPARKY) over a critically low-HP one (TITANESS), correctly prioritizing the chance to prolong the battle.

# IV. Puzzle Archive (Completed)

## A. Victory Road 3F Boulder Puzzle
- **Conclusion:** The tile at (8, 11) changed from `boulder_barrier` to `cleared_boulder_barrier` after the boulder was placed on the switch at (4, 6).

## B. Victory Road 2F Boulder Puzzle
- **Conclusion:** A boulder was brought down from Victory Road 3F through the hole at (24, 16) on 3F. It landed at (23, 17) on 2F and was pushed to the switch at (10, 17). The barrier at (24, 15) is now open.
- **Agent Output Override Failure (Confirmation Bias):** I incorrectly overrode the `battle_strategist_agent`'s advice to switch, believing I could secure a knockout. The agent had correctly identified a high-risk situation that I underestimated, leading to a cascade of negative outcomes and the eventual loss of the battle. **Correction:** I must treat the agent's output as the default correct action and only override it if I can definitively prove its underlying assumptions are wrong based on new in-game evidence.

## H. Untested Hypotheses
- **PC Box Selection Anomaly:** The game may select the box one position *below* the highlighted cursor. This has only been observed once and requires further testing to confirm if it's a consistent bug. (Next Test: Next time 'CHANGE BOX' is used).
- **Agent Data Staleness (Critical Failure):** The battle_strategist_agent received outdated party information (Turn 149807), causing it to recommend switching to a fainted Pokémon. This highlights a critical vulnerability in the data pipeline. Since the agent cannot be fixed to account for this, its recommendations must be treated with extreme caution and manually verified against the current party status on-screen before execution.

# V. Development & Testing Pipeline

## A. Future Development Goals
- **Pokémon Data Pipeline:** Investigate methods to pass party/PC data to custom tools to make `pokemon_stat_formatter` functional. This is a high-priority task for improving team-building efficiency.
- **Agent Usage:** Make it a priority to use the `team_composition_advisor` agent for the next major team overhaul to test its effectiveness.

## B. Untested Hypotheses (Active)
- **SPOONBENDE vs. Gengar:** Test the effectiveness of a low-level Psychic-type (SPOONBENDE, Lv 37) against Agatha's high-level Gengar. The type matchup should be favorable, but the level difference is a major risk factor.
  - Psychic is super-effective against Poison-types (Observed: Lorelei's Slowbro vs ECHO's Golbat).