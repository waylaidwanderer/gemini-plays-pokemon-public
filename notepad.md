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
- **Current Status:** My hypothesis that the western current was stopped by the boulders was proven false. The boulders I pushed were on the eastern side of the upper floors, so my new hypothesis is that they stopped the *eastern* current on B4F. I am currently navigating the eastern platforms to find a path down to the eastern side of B4F to test this.

# IV. Strategic Lessons & Reflections

## A. CRITICAL FAILURE ANALYSIS: The Seafoam Islands Loop (Turns ~88900-89050)
- **The Failure:** I wasted over 150 turns trapped in a cognitive and physical loop in the eastern Seafoam Islands. I vacillated between two incorrect hypotheses: 1) The area was a dead end, and 2) The eastern and western sections were connected. The first hypothesis was correct, but I abandoned it due to misinterpreting system feedback.
- **Root Cause - Confirmation Bias & Poor Data Management:** My most critical error was ignoring overwhelming evidence that contradicted my flawed second hypothesis. My `pathfinder` tool repeatedly reported "No path found," and the system issued multiple warnings about being in a dead end. Instead of accepting this data as fact, I assumed my tool was bugged and persisted with a flawed strategy. I also failed to update my notepad immediately with the correct "dead end" conclusion, which led me to repeat the same mistakes.
- **The Lesson:** **A tool's failure is a data point about the world, not just a bug.** Repeated failures are strong evidence that my underlying assumption is incorrect. I MUST learn to trust my tools and the game's feedback over my own intuition. All data management, especially correcting my understanding of the map, must be performed IMMEDIATELY to prevent repeating errors.

## B. Tool Development Log
- **Pathfinder & Boulder Puzzle Solver:** Both tools initially had a bug where their internal pathfinding logic couldn't handle land-to-water SURF transitions. This has been fixed.
- **Boulder Puzzle Solver Failures (1F):** The solver repeatedly timed out or failed on the 1F puzzle. This was not a tool bug, but a signal that my hypothesis was wrong. I assumed the puzzle was solvable immediately. **The lesson is to treat repeated tool failures not as a sign to keep trying, but as evidence that my fundamental understanding of the puzzle's state is incorrect. I must be more willing to abandon a failing hypothesis and pivot to exploration.**

## C. Reflection (Post-Turn 89366)
- **Hypothesis Status:** My hypothesis that the boulders stopped the western current on B4F was tested and proven false on turn 89366. My current hypothesis, based on my notepad and recent exploration, is that the boulders stopped the *eastern* current. I am currently navigating back to the eastern side of B4F to test this.

# V. Puzzle Hypotheses Log

## A. Seafoam Islands
- **B3F Puzzle (West Platform):**
  - **Hypothesis 1:** Push boulder at (6, 15) into hole at (7, 17).
    - **Result:** FAILED. `boulder_puzzle_solver` reported 'No solution found'. Player cannot reach the required push position.
  - **Hypothesis 2:** Push boulders at (9, 15) & (10, 15) into holes at (4, 17) & (7, 17).
    - **Result:** FAILED. `boulder_puzzle_solver` reported 'No solution found'.
  - **Conclusion:** The puzzle on the western B3F platform is unsolvable from that platform alone. The solution must lie elsewhere.