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
- **Boulder Switch & Barrier:** `boulder_switch` tiles are activated when a boulder is pushed onto them, which typically changes a `boulder_barrier` tile into a `cleared_boulder_barrier` tile (effectively `ground`).

## B. General Heuristics & Rules
- **PC Interaction:** To use a PC, stand on the tile directly below it, face up, and press 'A'.
- **HM Usage:** HMs are used from the party menu outside of battle. Fainted Pokémon can use field moves.
- **"No Will to Fight" Message (Correction):** This message appears only when the cursor in the party menu is on an already fainted Pokémon. It is a UI error, not a gameplay mechanic.
- **Surf Mechanic:** You cannot initiate Surf from an `elevated_ground` tile. You must be on a `ground`, `steps`, or `grass` tile adjacent to water.

# II. Battle Intel

## A. Type Effectiveness Chart (Verified)
- **Super Effective (2x):** Psychic > Ghost, Poison; Ghost > Psychic; Electric > Rock, Water; Flying > Grass, Poison, Fighting; Ice > Ground, Grass, Flying, Dragon; Ground > Poison, Fire, Electric, Rock; Rock > Fire, Ice, Flying, Bug; Fighting > Normal, Rock, Ice; Water > Fire, Ground, Rock; Grass > Water, Ground, Rock; Bug > Grass, Poison, Psychic; Poison > Grass, Bug.
- **Not Very Effective (0.5x):** Normal !> Rock; Electric !> Grass, Electric, Dragon; Rock !> Psychic; Psychic !> Psychic; Poison !> Poison, Ground, Rock, Ghost; Ice !> Water, Ice, Fire; Fighting !> Poison, Flying, Psychic, Bug; Water !> Water, Grass, Dragon; Grass !> Fire, Grass, Poison, Flying, Bug, Dragon.
- **Immune (0x):** Flying immune to Ground; Ground immune to Electric; Ghost immune to Normal, Fighting.

## B. Trainer Rosters & Movesets
*This section is for recording the teams and moves of significant trainers (Gym Leaders, Rivals) after a battle is concluded.*

# III. Puzzles & Exploration

## A. Seafoam Islands Puzzle Mechanics
- **Core Concept:** The primary puzzle involves pushing boulders on upper floors (1F, B1F, B2F) into specific holes. These boulders then fall to lower floors (B3F, B4F), where they act as barriers to redirect or block strong water currents, allowing access to new areas.
- **Current Status:** An initial attempt to stop the western current by dropping boulders from the eastern side of 1F failed. The eastern caves proved to be a dead end. The solution must involve the boulders on the western side of the caves.

# IV. Strategic Lessons & Reflections

## A. CRITICAL FAILURE ANALYSIS: Confirmation Bias in Seafoam Islands (Turns ~89480-89516)
- **The Failure:** I wasted significant time exploring the eastern side of the Seafoam Islands based on a flawed hypothesis. I repeatedly descended into isolated, dead-end rooms, ignoring system warnings, my own tool's output, and map data that indicated these paths were not viable for crossing the cave system.
- **Root Cause - Confirmation Bias:** I became fixated on the idea that the eastern descent was the solution and failed to abandon the hypothesis after the first few failed tests. Instead of accepting the dead ends and repeated `pathfinder` failures as proof my hypothesis was wrong, I treated them as minor setbacks or tool bugs and kept looking for another eastern path. This is a classic case of confirmation bias.
- **The Lesson:** A single failed test is strong evidence against a hypothesis. Multiple failures are conclusive proof. I must be more willing to abandon a failing strategy immediately and pivot to a new one. I must trust the data (map, system warnings, tool outputs) over my own intuition. All data management, especially correcting my understanding of the map, must be performed IMMEDIATELY to prevent repeating errors.

## B. Tool Development Log
- **Pathfinder & Boulder Puzzle Solver:** Both tools initially had a bug where their internal pathfinding logic couldn't handle land-to-water SURF transitions. This has been fixed.
- **Boulder Puzzle Solver Failures (1F):** The solver repeatedly timed out or failed on the 1F puzzle. This was not a tool bug, but a signal that my hypothesis was wrong. I assumed the puzzle was solvable immediately. **The lesson is to treat repeated tool failures not as a sign to keep trying, but as evidence that my fundamental understanding of the puzzle's state is incorrect. I must be more willing to abandon a failing hypothesis and pivot to exploration.**

# V. Puzzle Hypotheses Log

## A. Seafoam Islands
- **B3F Puzzle (West Platform):**
  - **Hypothesis 1:** Push boulder at (6, 15) into hole at (7, 17).
    - **Result:** FAILED. `boulder_puzzle_solver` reported 'No solution found'. Player cannot reach the required push position.
  - **Hypothesis 2:** Push boulders at (9, 15) & (10, 15) into holes at (4, 17) & (7, 17).
    - **Result:** FAILED. `boulder_puzzle_solver` reported 'No solution found'.
  - **Conclusion:** The puzzle on the western B3F platform is unsolvable from that platform alone. The solution must lie elsewhere.

## C. Pathfinder Bug Fix (Turn 89499)
- **The Bug:** The `pathfinder` tool was unable to find a path to a 'hole' tile because the `is_traversable` function did not recognize 'hole' as a valid land tile to move onto from 'ground'.
- **The Fix:** I updated the `is_traversable` function to include 'hole' in the set of `valid_land_types` and added a condition to allow movement between 'ground' and 'hole' tiles.
- **The Lesson:** My custom tools need to be robust enough to handle all known tile types. When a tool fails on a seemingly simple task, it's a strong indicator of a logic bug that needs immediate attention.