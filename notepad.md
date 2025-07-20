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

## B. General Heuristics & Rules
- **PC Interaction:** To use a PC, stand on the tile directly below it, face up, and press 'A'.
- **HM Usage:** HMs are used from the party menu outside of battle. Fainted Pokémon can use field moves.
- **"No Will to Fight" Message (Correction):** This message appears only when the cursor in the party menu is on an already fainted Pokémon. It is a UI error, not a gameplay mechanic.
- **Confirmation Bias Warning:** The game's feedback (e.g., being unable to move) is the ultimate source of truth. If a tool's output (like a path plan) contradicts the game's behavior, the tool is flawed and must be debugged. Do not repeatedly attempt an action that the game has shown to be invalid.

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
- **Seafoam Islands B4F Western Water Current:** The current at (8, 12) is too strong to SURF against. The solution is likely on an upper floor (B1F or B2F).
- **NPC Kris (B4F):** The NPC Kris at (8, 3) on B4F has information relevant to progressing. (Currently inaccessible due to water current).

## C. Confirmed Unsolvable / Dead Ends
- **Seafoam Islands B3F Main Boulder Puzzle:** The `boulder_puzzle_solver` tool confirmed this is unsolvable from the western platform (turn #88200). The purpose of this puzzle remains unknown. It does not appear to affect the water currents.

# IV. Tool Development & Strategy

## A. Development Log
- **Pathfinder Tool (Invalid Path):** The tool generated multiple invalid paths that attempted to move through 'impassable' tiles. The root cause was flawed traversal logic in the `is_traversable` function that did not correctly account for all tile transition rules. The tool has been rewritten with more robust logic.
- **Boulder Puzzle Solver (SURF Inability):** The tool was unable to account for SURF when pathfinding to boulders, leading to incorrect 'No solution found' results. The tool has been upgraded to include SURF logic in its internal pathfinder.
- **Pathfinder Tool (Invalid Path - Elevated Ground):** The tool generated a path from `ground` to `elevated_ground`, which is an invalid move. The `is_traversable` function was updated to correctly restrict movement between `ground` and `elevated_ground` unless `steps` are used.

## B. Brainstorming: New Agents
- **Hypothesis Generator Agent:** An agent that takes a failed action and the current game state as input, and outputs a list of new, testable hypotheses to investigate. This could help structure problem-solving and avoid repetitive loops.