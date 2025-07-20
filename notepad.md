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
- **Seafoam Islands B4F Western Water Current:** The current at (8, 12) is too strong to SURF against. The solution is likely on an upper floor (B1F or B2F). **Hypothesis Failed:** Exploration of B1F and B2F revealed no solution. New hypothesis: The main boulder puzzle on B3F is the key.
- **NPC Kris (B4F):** The NPC Kris at (8, 3) on B4F has information relevant to progressing. (Currently inaccessible due to water current).
- **Seafoam Islands B3F Main Boulder Puzzle:** The `boulder_puzzle_solver` tool confirmed this is unsolvable from the western platform (turn #88200). **Re-evaluating this conclusion.** It's possible the tool was flawed or the input was incorrect.

# IV. Tool Development & Strategy

## A. Development Log
- **Pathfinder Tool (Invalid Path - Elevated Ground):** The tool generated a path from `ground` to `elevated_ground`, which is an invalid move. The `is_traversable` function was updated to correctly restrict movement between `ground` and `elevated_ground` unless `steps` are used.
- **Seafoam Islands B4F Western Water Current (Hypothesis #2 Failed):** Pushing the isolated boulder at (20, 7) on B3F into the hole at (20, 6) did NOT stop the western water current. New hypothesis: The NPC Kris at (8, 3) has the solution.
- **Pathfinder Tool (Invalid Path - Water):** The tool generated a path from a `ground` tile directly into a `water` tile. This is an invalid move as it requires using Surf from the menu.
  - **Fix:** Modified the logic to prevent any pathing from a land tile (`ground`, `grass`, etc.) directly to a `water` tile. The tool should only path between adjacent water tiles or from a water tile to an adjacent land tile. Land-to-water transitions must be handled as a separate, multi-step action.

## B. Future Tool/Agent Ideas
- **Cave Navigator Agent:** Could generate high-level, multi-floor navigation plans for complex dungeons.
- **Puzzle Element Finder Tool:** Could parse map XML to automatically identify coordinates of puzzle elements like boulders and switches.

## C. Self-Correction & Lessons Learned
- **User Error vs. Tool Error:** When a tool appears to fail, first consider if the failure was due to user error (e.g., using an outdated path after an interruption) before assuming the tool itself is bugged. Verify the context before debugging.

## D. Navigational Insights
- **Route 22 & 15 Layout:** These routes are split by one-way ledges. The southern sections do not provide access to the northern sections containing the main patches of tall grass. The northern sections are likely only accessible after obtaining all 8 badges and passing through the Pokémon League Reception Gate.
- **Surf Mechanic:** You cannot initiate Surf from an `elevated_ground` tile. You must be on a `ground`, `steps`, or `grass` tile adjacent to water.
- **Seafoam Islands Eastern Path (Hypothesis Failed):** The eastern entrances on Route 20 lead to an isolated, dead-end section of the cave. The path down from 1F -> B1F -> B2F -> B3F does not connect to the main western puzzle area. The true path forward must be through the western entrance on Route 20.
- **Seafoam Islands Eastern Path (Hypothesis Failed):** The eastern entrances on Route 20 lead to an isolated, dead-end section of the cave. The path down from 1F -> B1F -> B2F -> B3F does not connect to the main western puzzle area. The true path forward must be through the western entrance on Route 20.
- **Seafoam Islands Eastern Path (Hypothesis Failed):** The eastern entrances on Route 20 lead to an isolated, dead-end section of the cave. The path down from 1F -> B1F -> B2F -> B3F does not connect to the main western puzzle area. The true path forward must be through the western entrance on Route 20.
- **Seafoam Islands Eastern Path (Hypothesis Failed):** The eastern entrances on Route 20 lead to an isolated, dead-end section of the cave. The path down from 1F -> B1F -> B2F -> B3F does not connect to the main western puzzle area. The true path forward must be through the western entrance on Route 20.