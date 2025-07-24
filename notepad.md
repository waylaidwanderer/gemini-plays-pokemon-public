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

## B. Current Trainer Rosters & Movesets

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

## A. Current Strategy: Victory Road 1F Puzzle
- **Conclusion:** The southern boulder puzzle is confirmed unsolvable by standard mechanics (`boulder_puzzle_solver` and `gem_pathfinder` fail). The area is a dead end.
- **Current Hypothesis:** A hidden, non-standard mechanic exists to resolve the puzzle.
- **Test Plan:** Systematic brute-force exploration. Visit every reachable tile in the southern area and interact with all four adjacent walls/objects.
- **Search Grid:** (2,13)-(4,13), (1,14)-(3,14), (1,15)-(2,15), (4,16)-(6,16), (3,17)-(8,17), (7,18)-(10,18).
- **Progress:** All walls around (2,13) and (3,11) have been checked with no results.

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

## B. Archived Trainer Rosters
### Giovanni (Viridian Gym Leader)
- **Team:** NIDOKING (Lv54), DUGTRIO (Lv53), NIDOQUEEN (Lv54), PERSIAN (Lv55), RHYDON (Lv55)

## C. Agent & Tool Refinement Log
- **Battle Strategist Agent (Turn 91179):** Updated to prioritize survival by assuming worst-case scenarios and weighing level disparity.
- **Battle Strategist Agent (Turn 94114):** Updated to correctly interpret the 'training' goal.
- **`delete_map_marker` Tool (Turn 95077):** Standardized gate markers.
- **`retreat_planner_agent` (Turn 96236):** Refined to check inventory before suggesting item-based solutions.

## D. Tool Development Log
- **Pathfinder & Boulder Puzzle Solver:** Fixed SURF transitions, ledge logic, and consolidated tools.
- **`spinner_maze_solver`:** Rewrote path reconstruction logic.
- **`reachable_shoreline_finder`:** Created to find valid SURF starting points.
- **`connectivity_checker`:** Deleted due to redundancy.
- **`find_closest_unseen_tile`:** Deleted due to flawed logic.
- **`boulder_puzzle_solver` (Turn 95239-95310):** Created and refined to solve boulder puzzles.
- **Hole:** A tile that likely serves as a target for boulder puzzles, causing the boulder to drop to a lower floor.

**New Strategy: Brute-Force Exploration**
**Conclusion:** All tool-assisted and hypothesis-driven attempts to solve the southern boulder puzzle have failed. The current state is confirmed to be a dead end by all standard mechanics.
**New Hypothesis:** A hidden, non-standard mechanic exists to resolve the puzzle from its current state.
**Test Plan:** Systematically visit every reachable tile in the southern area and interact with all four adjacent walls/objects. I will track my progress here to ensure complete coverage.
- **Search Grid:** (2,13)-(4,13), (1,14)-(3,14), (1,15)-(2,15), (4,16)-(6,16), (3,17)-(8,17), (7,18)-(10,18).