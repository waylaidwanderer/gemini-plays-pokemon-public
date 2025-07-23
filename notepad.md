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
- **Level Cap:** The level cap with 7 badges is 55.
- **Special NPC Interaction:** Certain puzzles may require walking *through* an NPC rather than interacting with them (e.g., Summer Beach House).

## C. Area-Specific Discoveries
- **Route 23 Earth Badge Check:** A guard at (5, 36) blocks the main path. Furthermore, an invisible trigger line along Y=36 prevents any northward movement in the western maze area, effectively blocking exploration until the Earth Badge is obtained.

# II. Battle Intel

## A. Type Effectiveness Chart (Verified)
- **Super Effective (2x):** Psychic > Ghost, Poison; Ghost > Psychic; Electric > Rock, Water; Flying > Grass, Poison, Fighting; Ice > Ground, Grass, Flying, Dragon; Ground > Poison, Fire, Electric, Rock; Rock > Fire, Ice, Flying, Bug; Fighting > Normal, Rock, Ice; Water > Fire, Ground, Rock; Grass > Water, Ground, Rock; Bug > Grass, Poison, Psychic; Poison > Grass, Bug.
- **Not Very Effective (0.5x):** Normal !> Rock; Electric !> Grass, Electric, Dragon; Rock !> Psychic; Psychic !> Psychic; Poison !> Poison, Ground, Rock, Ghost; Ice !> Water, Ice, Fire; Fighting > Poison, Flying, Psychic, Bug; Water !> Water, Grass, Dragon; Grass !> Fire, Grass, Poison, Flying, Bug, Dragon.
- **Immune (0x):** Flying immune to Ground; Ground immune to Electric; Ghost immune to Normal, Fighting.

## B. Trainer Rosters & Movesets

### Giovanni (Viridian Gym Leader)
- **Team:**
  - NIDOKING (Lv54) - Moves: Ice Beam, Blizzard, Thunderbolt, Earthquake
  - DUGTRIO (Lv53) - Moves: Fissure, Slash, Earthquake, Rock Slide
  - NIDOQUEEN (Lv54) - Moves: Ice Beam, Earthquake, Thunderbolt, Body Slam
  - PERSIAN (Lv55) - Moves: Bubblebeam, Slash, Hyper Beam, Thunderbolt

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

## D. Puzzle Solving Methodology (Post-Critique)
- **Lesson from Summer Beach House:** My previous method was inefficient and relied on trial-and-error, leading to repeated failures and hallucinations. 
- **New Procedure:** For all future puzzles, I will follow a strict scientific method:
  1. **Observe:** Document the initial state of the puzzle in my notepad.
  2. **Hypothesize:** Formulate a single, clear, testable hypothesis.
  3. **Test:** Execute the simplest possible action to test the hypothesis.
  4. **Conclude:** Record the result and whether the hypothesis was confirmed or falsified.
- This structured approach will prevent looping and ensure I am building on my knowledge systematically.

# IV. Agent & Tool Refinement Log

## A. Battle Strategist Agent - Completed Refinements
- **Refinement (Turn 91179):** Updated the agent's system prompt to force it to prioritize survival by assuming a worst-case scenario (a super-effective critical hit from the opponent's best move) and to heavily weigh level disparity as a key risk factor. This was done after it provided flawed advice in the battle against Giovanni's Dugtrio.
- **Refinement (Turn 94114):** Updated agent prompt to correctly interpret the 'training' goal, prioritizing EXP gain for lower-level party members over simply winning with the strongest Pokémon.

## B. Tool Development Log
- **Pathfinder & Boulder Puzzle Solver:** Fixed a bug preventing land-to-water SURF transitions and corrected ledge traversal logic. Consolidated redundant tools.
- **`spinner_maze_solver`:** Rewrote path reconstruction logic to fix a critical bug.
- **`reachable_shoreline_finder`:** Created to systematically identify valid SURF starting points. Updated on Turn 94090 to handle elevation changes via 'steps' tiles.
- **`connectivity_checker`:** Deleted due to redundancy with robust pathfinder.

# V. Known Issues & Tool Limitations
- The `delete_map_marker` tool is unable to recognize and delete the '🟢' emoji.
- **Resolution:** I will standardize all future gate markers to use '✅' for open and '⛔' for closed. The existing '🟢' markers will be treated as legacy data and ignored.

## E. New Procedural Notes (Post-Reflection)
- **Boulder Puzzle Mechanics:** Boulders cannot be pushed directly into standard `water` tiles. They must be pushed into `hole` tiles to affect lower floors.
- **Map Marker Discipline (Reinforcement):** I must be more diligent about placing markers for both the entry and exit points of a warp *immediately* after using it to avoid confusion and redundant markers.