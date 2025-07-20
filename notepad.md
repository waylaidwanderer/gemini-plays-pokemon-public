# I. Game Mechanics & Discoveries

## A. Verified Tile Mechanics
- **Ground:** Standard walkable tile.
- **Impassable:** Walls, objects, etc. Cannot be entered.
- **Grass:** Tall grass for wild Pokémon encounters.
- **Ledge:** Can be jumped down (one-way). Moving down into a ledge tile moves the player two tiles down.
- **Cuttable Tree:** Requires HM Cut to pass. Becomes `ground` after cutting, but respawns on map change.
- **Water:** Requires HM Surf to traverse. To use Surf, you must be standing on a 'ground', 'water', or 'steps' tile adjacent to water, face the water, and use the HM from the party menu.
- **Boulder:** Requires HM Strength to move.
- **Hole:** Warps player to a lower floor or a specific spot.
- **Ladder (Up/Down):** Warps player between floors.
- **Warp:** An instant transition point between maps or areas.
- **Steps:** Allows vertical and horizontal movement between 'steps' and adjacent 'ground' or 'elevated_ground' tiles.
- **Spinner (up, down, left, right):** Forces movement in a specific direction.
- **Spinner Stop:** A tile that halts movement from a spinner.
- **Elevated Ground:** Walkable ground at a different elevation. Movement between `ground` and `elevated_ground` is only possible via `steps`.
- **Gate (`gate_offscreen`, `closed_gate`, `open_gate`):** Barriers that may open or close based on game events. `gate_offscreen` is treated as open for pathfinding.
- **Boulder Switch & Barrier:** `boulder_switch` tiles are activated when a boulder is pushed onto them, which typically changes a `boulder_barrier` tile into a `cleared_boulder_barrier` tile (effectively `ground`). Will test further upon next encounter.

## B. General Heuristics & Rules
- **PC Interaction:** To use a PC, stand on the tile directly below it, face up, and press 'A'.
- **HM Usage:** HMs are used from the party menu outside of battle. Fainted Pokémon can use field moves.
- **"No Will to Fight" Message (Correction):** This message appears only when the cursor in the party menu is on an already fainted Pokémon. It is a UI error, not a gameplay mechanic.
- **Confirmation Bias Warning:** The game's feedback (e.g., being unable to move, system warnings) is the ultimate source of truth. If a tool's output (like a path plan) contradicts the game's behavior, the tool is flawed and must be debugged. Do not repeatedly attempt an action that the game has shown to be invalid.
- **Surf Mechanic:** You cannot initiate Surf from an `elevated_ground` tile. You must be on a `ground`, `steps`, or `grass` tile adjacent to water.

# II. Battle Intel

## A. Type Effectiveness Chart (Verified)
- **Super Effective (2x):** Psychic > Ghost, Poison; Ghost > Psychic; Electric > Rock, Water; Flying > Grass, Poison, Fighting; Ice > Ground, Grass, Flying, Dragon; Ground > Poison, Fire, Electric, Rock; Rock > Fire, Ice, Flying, Bug; Fighting > Normal, Rock, Ice; Water > Fire, Ground, Rock; Grass > Water, Ground, Rock; Bug > Grass, Poison, Psychic; Poison > Grass, Bug.
- **Not Very Effective (0.5x):** Normal !> Rock; Electric !> Grass, Electric, Dragon; Rock !> Psychic; Psychic !> Psychic; Poison !> Poison, Ground, Rock, Ghost; Ice !> Water, Ice, Fire; Fighting !> Poison, Flying, Psychic, Bug; Water !> Water, Grass, Dragon; Grass !> Fire, Grass, Poison, Flying, Bug, Dragon.
- **Immune (0x):** Flying immune to Ground; Ground immune to Electric; Ghost immune to Normal, Fighting.

## B. Trainer Rosters & Movesets
*This section is for recording the teams and moves of significant trainers (Gym Leaders, Rivals) after a battle is concluded.*

# III. Puzzles & Exploration

## A. Solved Puzzles
- **Seafoam Islands B3F Water Current (East):** The strong water current on B4F is disabled by pushing a single, isolated boulder at (20, 7) on B3F into a hole at (20, 6).

## B. Ongoing Puzzles & Investigations
- **Seafoam Islands B4F Western Water Current:** The current at (8, 12) is too strong to SURF against. The solution is the main boulder puzzle on B3F.
- **NPC Kris (B4F):** The NPC Kris at (8, 3) on B4F has information relevant to progressing. (Currently inaccessible due to water current).
- **Seafoam Islands B3F Main Boulder Puzzle:** The `boulder_puzzle_solver` tool initially failed, but has since been fixed. The puzzle is now the primary objective to test the tool's new logic.

# IV. Tool Development & Strategy

## A. Development Log
- **Pathfinder Tool (Invalid Path - Elevated Ground):** The tool generated a path from `ground` to `elevated_ground`, which is an invalid move. The `is_traversable` function was updated to correctly restrict movement between `ground` and `elevated_ground` unless `steps` are used.
- **Pathfinder Tool (Invalid Path - Water):** The tool generated a path from a `ground` tile directly into a `water` tile. This is an invalid move as it requires using Surf from the menu. **Limitation:** The tool cannot currently plan multi-stage paths that involve starting on land, using an HM like Surf, and then navigating on water.
- **Boulder Puzzle Solver (Failure & Fix):** The `boulder_puzzle_solver` returned 'No solution found' for the western B3F puzzle. This was due to two bugs: an incorrect initial check in the `player_a_star` function and improper handling of movement between `ground` and `elevated_ground`. The tool has been updated with a corrected script and now requires testing on the original puzzle.

## B. Future Tool/Agent Ideas
- **Advanced Pathfinder Tool:** Enhance the `pathfinder` to handle multi-stage navigation, including the use of HMs like Surf or Cut from the menu to transition between terrain types (e.g., land -> water).
- **Cave Navigator Agent:** Could generate high-level, multi-floor navigation plans for complex dungeons.
- **Puzzle Element Finder Tool:** Could parse map XML to automatically identify coordinates of puzzle elements like boulders and switches.

## C. Self-Correction & Lessons Learned
- **User Error vs. Tool Error:** When a tool appears to fail, first consider if the failure was due to user error (e.g., using an outdated path after an interruption) before assuming the tool itself is bugged. Verify the context before debugging.
- **Overwatch Critique (Tool Refinement):** Received a critical critique for not immediately fixing the `boulder_puzzle_solver` tool after it failed. Core directive is to prioritize tool maintenance. This mistake has been corrected, and the tool was fixed at the next safe opportunity.
- **Dead End Misidentification:** Incorrectly concluded that Seafoam Islands B2F was a dead end after one path failed, ignoring other reachable warps. I must be more thorough and trust system data over hasty assumptions.
- **Pathfinder Tool (Impassable Target):** The tool failed to find a path to an impassable target because the logic for finding an adjacent, reachable goal was flawed. It incorrectly used `is_traversable` from the impassable tile itself. The logic has been updated to check if the adjacent tile is a valid standing tile, then lets A* find the path.
- **Wild Encounter:** Encountered a wild SLOWPOKE (Lv35) at (5, 13) on Seafoam Islands 1F.
- **Wild Encounter:** Encountered a wild KRABBY (Lv32) at (7, 7) on Seafoam Islands 1F.