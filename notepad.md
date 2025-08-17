# I. Game Mechanics & World Knowledge

## A. Core Gameplay (Verified)
- **Battle Style:** Set mode.
- **Items in Battle:** Prohibited.
- **Level Caps:** Active and enforced.
- **PC Interaction:** To use a PC, stand on the tile directly *below* it and face *up* before pressing 'A'.
- **Menu Navigation:** The 'B' button is the primary method for exiting/canceling out of menus.
- **Forced Sleeping Switch:** The game will force you to send out or switch to a sleeping Pokémon if no other conscious Pokémon are available. This is a mechanical exception to the strategic guideline of avoiding switching to sleeping Pokémon.

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

# II. Battle Information

## A. Type Effectiveness Chart (Verified In-Game)
- **Super Effective (2x):** Water > Rock, Ground, Fire; Electric > Water, Flying; Rock > Flying; Ground > Fire, Electric, Rock, Poison, Psychic (Hypothesized), Ground; Ice > Ground, Grass, Flying, Dragon; Flying > Fighting, Grass, Bug; Fighting > Normal, Rock, Ice; Grass > Ground, Rock, Water; Psychic > Ghost.
- **Not Very Effective (0.5x):** Normal !> Rock; Flying !> Rock; Ice !> Fighting (Ice-type moves are NOT super-effective against Fighting-types); Psychic !> Psychic.
- **Immune (0x):** Normal immune to Ghost; Ground immune to Electric; Flying immune to Ground; Ghost immune to Ground.

## B. Elite Four Battle Logs (Observed Rosters)
### Lorelei (Attempt 2 - Defeated)
  - Slowbro (Lv 56) - Known Moves: Psychic
  - Cloyster (Lv 55) - Moves unknown.
  - Dewgong (Lv 55) - Moves unknown.
  - Jynx (Lv 56) - Moves unknown.
  - Lapras (Lv 57) - Known Moves: Blizzard

### Bruno (Attempt 2 - In Progress)
  - Hitmonchan (Lv 57) - Known Moves: Dizzy Punch, Thunderpunch, Ice Punch
  - Poliwrath (Lv 56) - Known Moves: Hydro Pump, Ice Beam
  - Hitmonlee (Lv 57) - Moves unknown.
  - Onix (Lv 56) - Known Moves: Rock Slide

### Agatha (Attempt 1 - Defeated)
  - Gengar (Lv 57) - Known Moves: Night Shade, Mega Drain, Hypnosis, Dream Eater
  - Golbat (Lv 58) - Known Moves: Toxic, Double Team, Fly
  - Marowak (Lv 57) - Known Moves: Rock Slide, Earthquake
  - Arbok (Lv 58) - Known Moves: Glare, Substitute, Wrap
  - Gengar (Lv 59) - Known Moves: Psychic, Mega Drain

### Lance (Attempt 1 - Lost)
  - Dragonite (Lv 61) - Known Moves: Slam, Thunder Wave

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
- **`select_battle_option` Tool Misuse:** The tool is designed to execute button presses on its own. Providing manual button presses in the same turn is redundant and incorrect. **Correction:** When using this tool, do not provide any other button presses. (Observed Turn 147891, 147894, 147896)

# IV. Puzzle Archive (Completed)

## A. Victory Road 3F Boulder Puzzle
- **Conclusion:** The tile at (8, 11) changed from `boulder_barrier` to `cleared_boulder_barrier` after the boulder was placed on the switch at (4, 6).

## B. Victory Road 2F Boulder Puzzle
- **Conclusion:** A boulder was brought down from Victory Road 3F through the hole at (24, 16) on 3F. It landed at (23, 17) on 2F and was pushed to the switch at (10, 17). The barrier at (24, 15) is now open.

# V. Tool & Agent Development Ideas
- **In-Battle Move Selection Tool:** Create a tool that can take a move name as input and automatically perform the necessary button presses to select it from the move menu. This would automate a tedious manual process, especially when the desired move is at the bottom of the list.
- **Agent Maintenance Tool:** Create a tool that takes a new piece of verified information (like a type effectiveness) and automatically updates both the notepad and the system prompt of a specified agent. This would reduce manual effort and prevent errors from forgetting to update one or the other.
- **TM Advisor Agent:** Create an agent that analyzes my full roster of Pokémon and available TMs to recommend optimal move assignments based on stats, typing, and strategic needs. This would automate a complex reasoning task.
- **Semi-Automated Data Extractor Tool:** A tool to guide manual PC navigation to extract Pokémon data as a workaround for the broken `pokemon_data_extractor`.
- **`pokemon_data_extractor` Failure:** The tool fails to execute even with a simple print statement and no arguments. Hypothesis that the large `game_state_string` input was the cause has been disproven. The root cause is likely an issue with the tool execution environment itself, making the tool unusable. Must proceed with manual workarounds.
- **Confirmation Bias in Navigation:** I repeatedly attempted to move north in Agatha's room, assuming the path was simply blocked by my follower, rather than questioning the core assumption that the door was open. This led to wasted turns. **Correction:** If a path is blocked more than once, I must immediately question the premise of the path's validity and test for alternate triggers or mechanics.