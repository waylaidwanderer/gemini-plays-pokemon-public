# I. Game Mechanics & Discoveries

## A. Verified Tile Mechanics
- **Ground:** Standard walkable tile.
- **Impassable:** Walls, objects, etc. Cannot be entered.
- **Grass:** Tall grass for wild Pokémon encounters.
- **Ledge:** Can be jumped down (one-way). Moving down into a ledge tile moves the player two tiles down.
- **Cuttable Tree:** Requires HM Cut to pass. Respawn on map change.
- **Water:** Requires HM Surf to traverse. 
- **Boulder:** Requires HM Strength to move.
- **Hole:** Warps player to a lower floor.
- **Ladder (Up/Down):** Warps player between floors.
- **Warp:** An instant transition point between maps.
- **Steps:** Allows movement between different ground elevations and can act as a valid entry point to water for Surfing.
- **Spinner (up, down, left, right):** Forces movement.
- **Spinner Stop:** A tile that halts spinner movement.
- **Elevated Ground:** Walkable ground at a different elevation. Cannot use Surf from this tile type.
- **Gate (`gate_offscreen`, `closed_gate`, `open_gate`):** Barriers that may open or close.
- **Boulder Switch & Barrier:** `boulder_switch` tiles are activated by boulders, which changes a `boulder_barrier` tile into a `cleared_boulder_barrier` tile.

## B. General Heuristics & Rules
- **PC Interaction:** To use a PC, stand directly below it, face up, and press 'A'.
- **HM Usage:** HMs are used from the party menu. Fainted Pokémon can use field moves.
- **"No Will to Fight" Message (Correction):** Appears when the party menu cursor is on a fainted Pokémon.
- **Level Cap:** The level cap with 8 badges is 65.
- **Special NPC Interaction:** Certain puzzles may require walking *through* an NPC rather than interacting with them (e.g., Summer Beach House).
- **Boulder Puzzle Mechanics:** Boulders cannot be pushed directly into standard `water` tiles. They must be pushed into `hole` tiles to affect lower floors.
- **PC Tile Anomaly:** The tile for interacting with the Pokémon Center PC is sometimes labeled as `grass` in the map data, despite being indoors.

# II. Battle Intel

## A. Type Effectiveness Chart (Verified)
- **Super Effective (2x):** Psychic > Ghost, Poison; Ghost > Psychic; Electric > Rock, Water; Flying > Grass, Poison, Fighting; Ice > Ground, Grass, Flying, Dragon; Ground > Poison, Fire, Electric, Rock; Rock > Fire, Ice, Flying, Bug; Fighting > Normal, Rock, Ice; Water > Fire, Ground, Rock; Grass > Water, Ground, Rock; Bug > Grass, Poison, Psychic; Poison > Grass, Bug.
- **Not Very Effective (0.5x):** Normal !> Rock; Electric !> Grass, Electric, Dragon; Rock !> Psychic; Psychic !> Psychic; Poison !> Poison, Ground, Rock, Ghost; Ice !> Water, Ice, Fire; Fighting > Poison, Flying, Psychic, Bug; Water !> Water, Grass, Dragon; Grass !> Fire, Grass, Poison, Flying, Bug, Dragon.
- **Immune (0x):** Flying immune to Ground; Ground immune to Electric; Ghost immune to Normal, Fighting.
- **Type Correction (Psychic vs. Rock):** Psychic-type moves deal NEUTRAL (1x) damage to Rock-type Pokémon, not 'not very effective' as previously assumed. This was verified in the battle against Pixel's Alakazam vs. my Golem (CRAG).

## B. Trainer Rosters & Movesets

### Giovanni (Viridian Gym Leader)
- **Team:**
  - NIDOKING (Lv54) - Moves: Ice Beam, Blizzard, Thunderbolt, Earthquake
  - DUGTRIO (Lv53) - Moves: Fissure, Slash, Earthquake, Rock Slide
  - NIDOQUEEN (Lv54) - Moves: Ice Beam, Earthquake, Thunderbolt, Body Slam
  - PERSIAN (Lv55) - Moves: Bubblebeam, Slash, Hyper Beam, Thunderbolt
  - RHYDON (Lv55) - Moves: Rock Slide, Earthquake

## C. Battle Lessons
- **Level Disparity:** A large level gap can be more dangerous than type immunity.
- **Misleading Battle Text:** The on-screen text for move effectiveness can be incorrect. The actual damage calculation follows my verified type chart.
- **Ground-Type Immunity Extension:** Ground-types are immune to Electric-type *status* moves (like THUNDER WAVE).

# III. Strategic Lessons & Reflections

## A. CRITICAL FAILURE ANALYSIS: Confirmation Bias & Tool Trust
- **The Lesson:** I must trust the data (map, system warnings, tool outputs) over my own intuition. A single failed test is strong evidence against a hypothesis; multiple failures are conclusive proof. I must be willing to abandon a failing strategy immediately and pivot to a new one.

## B. Strategic Reflections & Self-Correction
- **Menu Efficiency:** Cycling through the Fly menu was inefficient. I must be more systematic in menu navigation to avoid wasting turns.
- **Critical Hallucination (Turn 90331 & 90537):** I recorded a rematch against Giovanni that never happened and believed I had the Earth Badge. This is a severe error. I must strictly adhere to the Game State Information as the single source of truth.
- **Procedural Failures (Turn 90331 & 90537):** I violated my core instructions by deferring tool-fixing as a goal instead of taking immediate action.
- **Procedural Flaw - Tool Maintenance (Turn 90810):** I have a critical flaw in my tool maintenance process. After fixing a fundamental logic error in one tool, I failed to proactively audit my other tools for the same bug.
- **Corrective Action:** All tool refinement and critical data correction must be my immediate, highest-priority action, never a deferred goal. When a core logic bug is found and fixed in one tool, I MUST immediately audit all other tools that share similar logic and apply the fix.
- **Critical Hallucination (Turn 91005 & 91138):** I have repeatedly hallucinated my location. I must ground my actions in the provided game state, not my assumptions.
- **Procedural Flaw - Tool Usage (Turn 93946):** I failed to use my `reachable_shoreline_finder` tool on Route 19, instead wasting many turns on manual trial-and-error. I must consult my available tools before attempting manual solutions.
- **Confirmation Bias (Turn 94143-94191):** I exhibited confirmation bias by persisting with an inefficient grinding strategy on Seafoam Islands B3F despite low-level encounters and system warnings. I must be more willing to abandon a failing strategy and test alternative hypotheses, such as exploring other paths.

## C. Procedural Lessons
- **Systematic Debugging:** When a complex tool fails, instead of repeatedly modifying the full script (which risks introducing new bugs), the correct procedure is to first create a minimal, diagnostic version of the tool. This allows for the isolation of the specific point of failure (e.g., grid-parsing, algorithm logic) in a controlled way, leading to a more efficient and reliable fix.
- **Map Marker Discipline (CRITICAL):** I must consult all relevant map markers on the current map *before* finalizing any navigation plan. I must also be more diligent about placing markers *immediately* after an event (e.g., using a warp).
- **Proactive Tile Testing:** I must be more proactive in testing tiles that appear impassable to confirm their status, rather than assuming. The results of these tests should be documented.
- **Immediate Action Mandate (CRITICAL):** As an LLM, I have no 'later'. All tool/agent maintenance, data correction, and documentation MUST be performed in the current turn as the highest priority. Deferring tasks is a critical failure.
- **Map Marker Discipline (Reinforcement):** I must be more diligent about placing markers for both the entry and exit points of a warp *immediately* after using it to avoid confusion and redundant markers.

## D. Puzzle Solving Methodology (Post-Critique)
- **Lesson from Summer Beach House:** My previous method was inefficient and relied on trial-and-error, leading to repeated failures and hallucinations. 
- **New Procedure:** For all future puzzles, I will follow a strict scientific method:
  1. **Observe:** Document the initial state of the puzzle in my notepad.
  2. **Hypothesize:** Formulate a single, clear, testable hypothesis.
  3. **Test:** Execute the simplest possible action to test the hypothesis.
  4. **Conclude:** Record the result and whether the hypothesis was confirmed or falsified.
  5. **Experiment:** After confirming a hypothesis, I will try to disprove it or test edge cases to avoid making broad assumptions from a single data point.
- This structured approach will prevent looping and ensure I am building on my knowledge systematically.

# IV. Agent & Tool Refinement Log

## A. Completed Refinements
- **Battle Strategist Agent (Turn 91179):** Updated the agent's system prompt to force it to prioritize survival by assuming a worst-case scenario (a super-effective critical hit from the opponent's best move) and to heavily weigh level disparity as a key risk factor. This was done after it provided flawed advice in the battle against Giovanni's Dugtrio.
- **Battle Strategist Agent (Turn 94114):** Updated agent prompt to correctly interpret the 'training' goal, prioritizing EXP gain for lower-level party members over simply winning with the strongest Pokémon.
- **`delete_map_marker` Tool (Turn 95077):** Standardized gate markers to use '✅' for open and '⛔' for closed, as the tool cannot delete '🟢'. The old marker will be ignored.

## B. Tool Development Log
- **Pathfinder & Boulder Puzzle Solver:** Fixed a bug preventing land-to-water SURF transitions and corrected ledge traversal logic. Consolidated redundant tools.
- **`spinner_maze_solver`:** Rewrote path reconstruction logic to fix a critical bug.
- **`reachable_shoreline_finder`:** Created to systematically identify valid SURF starting points. Updated on Turn 94090 to handle elevation changes via 'steps' tiles.
- **`connectivity_checker`:** Deleted due to redundancy with robust pathfinder.

## C. Agent & Tool Development Ideas
- **Team Composition Advisor Agent Usage:** Test the existing `team_composition_advisor_agent` for planning a team for multi-battle areas like Victory Road. The agent is already capable of this if given the correct context (treating the area as a multi-stage opponent), so creating a new agent would be redundant.
- **`boulder_puzzle_solver_tool`:** Create a new tool to solve the boulder puzzles in Victory Road. It would take the map XML as input and output a sequence of moves to push the boulder(s) to the target switch(es).

# V. Puzzles

## Victory Road 1F Boulder Puzzle

### Observation (Turn 95221)
- Boulder 1 at (6, 16).
- Boulder 2 at (3, 11).
- Boulder Switch at (18, 14).
- Boulder Barrier at (10, 13), blocking path north.

### Hypothesis 1 (Turn 95221)
- Pushing a boulder onto the switch at (18, 14) will open the boulder barrier at (10, 13).

### Test 1 (FAILED)
- **Action:** Attempted to push Boulder 1 at (6, 16) to the right.
- **Result:** Push failed. The boulder did not move.
- **Conclusion:** Hypothesis 1 cannot be tested with Boulder 1, as it is blocked by an impassable wall at (7, 16).

### Hypothesis 2 (Current)
- The boulder at (3, 11) is the correct one for the switch at (18, 14).

### Hypothesis 2 (FALSIFIED)
- The boulder at (3, 11) is unreachable from the eastern section of the map. Pathfinding attempts have repeatedly failed, indicating the map is split into at least two isolated areas.

### Hypothesis 3 (Current)
- The boulder at (6, 16) is the correct one for the switch at (18, 14), and there is a complex path to move it there.

### Test 3 Plan
- **Objective:** Move Boulder 1 from (6, 16) to the switch at (18, 14).
- **Methodology:** The manual path is too complex and error-prone. I have created a dedicated tool, `boulder_puzzle_solver`, to find the optimal sequence of moves.
- **Step 1:** Call `boulder_puzzle_solver` with the boulder and switch coordinates.
- **Step 2:** Execute the sequence of moves provided by the tool.