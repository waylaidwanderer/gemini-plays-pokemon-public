# I. Core Game Mechanics

## A. Tile Mechanics
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
- **Cleared Boulder Barrier (Corrected):** Functions as a one-way ramp. It can only be entered from a `steps` tile when moving from `ground` to `elevated_ground`. It is impassable from adjacent `ground` tiles and cannot be used to move down from `elevated_ground` to `ground`.

## B. General Rules & Heuristics
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
- **Type Correction (Psychic vs. Rock):** Psychic-type moves deal NEUTRAL (1x) damage to Rock-type Pokémon, not 'not very effective' as previously assumed.

## B. Trainer Rosters & Movesets

### Giovanni (Viridian Gym Leader)
- **Team:** NIDOKING (Lv54), DUGTRIO (Lv53), NIDOQUEEN (Lv54), PERSIAN (Lv55), RHYDON (Lv55)

### Cool Trainer M (Victory Road 1F)
- **Team:** ELECTABUZZ (Lv53), SNORLAX (Lv53), SLOWBRO (Lv53), PORYGON (Lv53)
- **Notes:** Spams Hyper Potions.

### Cool Trainer M (Victory Road 3F)
- **Location:** (29, 6)
- **Team:** CHARIZARD (Lv52), MAGNETON (Lv52)

## C. Battle Lessons & Insights
- **Level Disparity:** A large level gap can be more dangerous than type immunity.
- **Misleading Battle Text:** On-screen text for move effectiveness can be incorrect. The actual damage calculation follows my verified type chart.
- **Ground-Type Immunity Extension:** Ground-types are immune to Electric-type *status* moves (like THUNDER WAVE).
- **Elixer Mechanic (Correction):** Elixers only restore PP, not HP.

# III. World Navigation & Puzzles

## A. Victory Road 1F Navigation Log
**Objective:** Solve the main boulder puzzle (boulder at (15,3), switch at (18,14)).

**Attempt 1:** Used `boulder_puzzle_solver` from (7,12). **Outcome:** Failed. Player cannot reach boulder.
**Attempt 2:** Used `gem_pathfinder` from (6,14) to (14,3). **Outcome:** Failed. Path not found.
**Attempt 3:** Used `gem_pathfinder` from (9,18) to (14,3) after fixing 'boulder_switch' bug. **Outcome:** Failed. Target unreachable.
**Attempt 4:** Re-entered from (9,18), used `gem_pathfinder` to (14,3). **Outcome:** Failed. Path not found.
**Conclusion:** The southern entrance area is completely isolated from the northern puzzle area.

**New Hypothesis:** The isolated southern area has its own puzzle involving the boulders at (3,11) and (6,16). Solving this puzzle will likely open the path to the ladder at (2,2), which leads to Victory Road 2F.

# IV. Agent & Tool Development

## A. Future Development Ideas
- **Puzzle Orchestrator Agent:** Create an agent to manage multi-step puzzles in Victory Road, using existing `boulder_puzzle_solver` and `gem_pathfinder` tools.
- **Pokedex Analysis (Review):** Review `team_composition_advisor_agent` capabilities before creating a new Pokedex agent to avoid redundancy.

## B. Development Backlog
*No outstanding bugs. All tools are currently functional.*

# V. Archive

## A. Strategic Lessons & Reflections
- **Core Lesson:** Trust data (game state, tool outputs) over intuition. Adhere to the scientific method for all puzzles (Observe, Hypothesize, Test, Conclude, Experiment).
- **Procedural Mandates:** All tool/agent maintenance and data correction are the immediate, highest-priority action. When a core logic bug is found, audit all other tools for the same flaw. Consult map markers and available tools before acting. Use systematic, minimal tests for debugging complex tools.
- **Past Hallucinations:** I must strictly ground all actions and reasoning in the provided Game State Information as the single source of truth.
- **Confirmation Bias on Route 23 (Turn 95544):** I repeatedly failed to find a land-only path to Victory Road but persisted with workarounds instead of accepting the tool's output, which indicated a water crossing was mandatory. Lesson: Trust the data from my tools over my own assumptions, and if a hypothesis is repeatedly falsified, abandon it immediately.

## B. Agent & Tool Refinement Log
- **Battle Strategist Agent (Turn 91179):** Updated to prioritize survival by assuming worst-case scenarios and weighing level disparity.
- **Battle Strategist Agent (Turn 94114):** Updated to correctly interpret the 'training' goal.
- **`delete_map_marker` Tool (Turn 95077):** Standardized gate markers.
- **`retreat_planner_agent` (Turn 96236):** Refined to check inventory before suggesting item-based solutions.

## C. Tool Development Log
- **Pathfinder & Boulder Puzzle Solver:** Fixed SURF transitions, ledge logic, and consolidated tools.
- **`spinner_maze_solver`:** Rewrote path reconstruction logic.
- **`reachable_shoreline_finder`:** Created to find valid SURF starting points.
- **`connectivity_checker`:** Deleted due to redundancy.
- **`find_closest_unseen_tile`:** Deleted due to flawed logic.
- **`boulder_puzzle_solver` (Turn 95239-95310):** Created and refined to solve boulder puzzles.