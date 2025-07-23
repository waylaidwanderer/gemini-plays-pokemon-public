# I. Game Mechanics & Discoveries

## A. Verified Tile Mechanics
- **Ground:** Standard walkable tile.
- **Impassable:** Walls, objects, etc. Cannot be entered.
- **Grass:** Tall grass for wild Pokémon encounters.
- **Ledge:** Can be jumped down (one-way). Moving down into a ledge tile moves the player two tiles down.
- **Cuttable Tree:** Requires HM Cut to pass. Respawn on map change.
- **Water:** Requires HM Surf to traverse. Surf is initiated from the party menu while adjacent to water.
- **Boulder:** Requires HM Strength to move.
- **Hole:** Warps player to a lower floor.
- **Ladder (Up/Down):** Warps player between floors.
- **Warp:** An instant transition point between maps.
- **Steps:** Allows movement between different ground elevations.
- **Spinner (up, down, left, right):** Forces movement.
- **Spinner Stop:** A tile that halts spinner movement.
- **Elevated Ground:** Walkable ground at a different elevation.
- **Gate (`gate_offscreen`, `closed_gate`, `open_gate`):** Barriers that may open or close.
- **Boulder Switch & Barrier:** `boulder_switch` tiles are activated by boulders, which changes a `boulder_barrier` tile into a `cleared_boulder_barrier` tile.

## B. General Heuristics & Rules
- **PC Interaction:** To use a PC, stand directly below it, face up, and press 'A'.
- **HM Usage:** HMs are used from the party menu. Fainted Pokémon can use field moves.
- **"No Will to Fight" Message (Correction):** Appears when the party menu cursor is on a fainted Pokémon.
- **Level Cap:** The level cap with 7 badges is 55.

## C. Area-Specific Discoveries
- **Route 23 Earth Badge Check:** A guard at (5, 36) blocks the main path. Furthermore, an invisible trigger line along Y=36 prevents any northward movement in the western maze area, effectively blocking exploration until the Earth Badge is obtained.

# II. Battle Intel

## A. Type Effectiveness Chart (Verified)
- **Super Effective (2x):** Psychic > Ghost, Poison; Ghost > Psychic; Electric > Rock, Water; Flying > Grass, Poison, Fighting; Ice > Ground, Grass, Flying, Dragon; Ground > Poison, Fire, Electric, Rock; Rock > Fire, Ice, Flying, Bug; Fighting > Normal, Rock, Ice; Water > Fire, Ground, Rock; Grass > Water, Ground, Rock; Bug > Grass, Poison, Psychic; Poison > Grass, Bug.
- **Not Very Effective (0.5x):** Normal !> Rock; Electric !> Grass, Electric, Dragon; Rock !> Psychic; Psychic !> Psychic; Poison !> Poison, Ground, Rock, Ghost; Ice !> Water, Ice, Fire; Fighting !> Poison, Flying, Psychic, Bug; Water !> Water, Grass, Dragon; Grass !> Fire, Grass, Poison, Flying, Bug, Dragon.
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

## C. Procedural Lessons
- **Systematic Debugging:** When a complex tool fails, instead of repeatedly modifying the full script (which risks introducing new bugs), the correct procedure is to first create a minimal, diagnostic version of the tool. This allows for the isolation of the specific point of failure (e.g., grid-parsing, algorithm logic) in a controlled way, leading to a more efficient and reliable fix.
- **Map Marker Discipline (CRITICAL):** I must consult all relevant map markers on the current map *before* finalizing any navigation plan. Ignoring my own data leads to wasted turns and strategic failure, as seen with the Route 23 guard.
- **Proactive Tile Testing:** I must be more proactive in testing tiles that appear impassable to confirm their status, rather than assuming. The results of these tests should be documented.

# IV. Agent & Tool Refinement Log

## A. Battle Strategist Agent - Completed Refinements
- **Refinement (Turn 91179):** Updated the agent's system prompt to force it to prioritize survival by assuming a worst-case scenario (a super-effective critical hit from the opponent's best move) and to heavily weigh level disparity as a key risk factor. This was done after it provided flawed advice in the battle against Giovanni's Dugtrio.

## B. Tool Development Log
- **Pathfinder & Boulder Puzzle Solver:** Fixed a bug preventing land-to-water SURF transitions and corrected ledge traversal logic.
- **`spinner_maze_solver`:** Rewrote path reconstruction logic to fix a critical bug.
- **`reachable_shoreline_finder`:** Created to systematically identify valid SURF starting points.
- **`connectivity_checker`:** Created to validate if a path is possible before calling a pathfinder.

# V. Known Issues & Tool Limitations
- The `delete_map_marker` tool is unable to recognize and delete the '🟢' emoji.
- **Resolution:** I will standardize all future gate markers to use '✅' for open and '⛔' for closed. The existing '🟢' markers will be treated as legacy data and ignored.

# VI. Future Strategy
- **Giovanni Prep:** Use `team_composition_advisor_agent` before the next attempt.
- **Training Location:** Seafoam Islands is the current target for grinding after finding Route 21 unsuitable.

# VII. Future Agent & Tool Ideas
- **Pokedex Completion Advisor Agent:** An agent that could analyze my current Pokedex and suggest which Pokémon to target next and where they might be found.