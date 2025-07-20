# I. Game Mechanics & Discoveries

## A. Verified Tile Mechanics
- **Ground:** Standard walkable tile.
- **Impassable:** Walls, objects, etc. Cannot be entered.
- **Grass:** Tall grass for wild Pokémon encounters.
- **Ledge:** Can be jumped down (one-way). Moving down into a ledge tile moves the player two tiles down.
- **Cuttable Tree:** Requires HM Cut to pass. Becomes `ground` after cutting, but respawns on map change.
- **Water:** Requires HM Surf to traverse. To use Surf from a land tile, you must be standing on a 'ground', 'water', or 'steps' tile adjacent to water, face the water, and use the HM from the party menu.
- **Boulder:** Requires HM Strength to move.
- **Hole:** Warps player to a lower floor.
- **Ladder (Up/Down):** Warps player between floors.
- **Warp:** An instant transition point between maps or areas within a map.
- **Steps:** Allows vertical and horizontal movement between 'steps' and adjacent 'ground' or 'elevated_ground' tiles.
- **Spinner (up, down, left, right):** Forces movement in a specific direction.
- **Spinner Stop:** A tile that halts movement from a spinner.
- **Elevated Ground:** Walkable ground at a different elevation. Movement between `elevated_ground` and `ground` is only possible via `steps`.
- **Gate (`gate_offscreen`, `closed_gate`, `open_gate`):** Barriers that may open or close based on game events. `gate_offscreen` is treated as open for pathfinding.

## B. General Heuristics & Rules
- **PC Interaction:** To use a PC, stand on the tile directly below it, face up, and press 'A'.
- **HM Usage:** HMs are used from the party menu outside of battle. Fainted Pokémon can use field moves.
- **"No Will to Fight" Message (Correction):** This message appears only when the cursor in the party menu is on an already fainted Pokémon. It is a UI error, not a gameplay mechanic.

# II. Game Mechanics & Discoveries

## A. Verified Tile Mechanics
- **Ground:** Standard walkable tile.
- **Impassable:** Walls, objects, etc. Cannot be entered.
- **Grass:** Tall grass for wild Pokémon encounters.
- **Ledge:** Can be jumped down (one-way). Moving down into a ledge tile moves the player two tiles down.
- **Cuttable Tree:** Requires HM Cut to pass. Becomes `ground` after cutting, but respawns on map change.
- **Water:** Requires HM Surf to traverse. To use Surf from a land tile, you must be standing on a 'ground', 'water', or 'steps' tile adjacent to water, face the water, and use the HM from the party menu.
- **Boulder:** Requires HM Strength to move.
- **Hole:** Warps player to a lower floor.
- **Ladder (Up/Down):** Warps player between floors.
- **Warp:** An instant transition point between maps or areas within a map.
- **Steps:** Allows vertical and horizontal movement between 'steps' and adjacent 'ground' or 'elevated_ground' tiles.
- **Spinner (up, down, left, right):** Forces movement in a specific direction.
- **Spinner Stop:** A tile that halts movement from a spinner.
- **Elevated Ground:** Walkable ground at a different elevation. Movement between `elevated_ground` and `ground` is only possible via `steps`.
- **Gate (`gate_offscreen`, `closed_gate`, `open_gate`):** Barriers that may open or close based on game events. `gate_offscreen` is treated as open for pathfinding.

## B. General Heuristics & Rules
- **PC Interaction:** To use a PC, stand on the tile directly below it, face up, and press 'A'.
- **HM Usage:** HMs are used from the party menu outside of battle. Fainted Pokémon can use field moves.
- **"No Will to Fight" Message (Correction):** This message appears only when the cursor in the party menu is on an already fainted Pokémon. It is a UI error, not a gameplay mechanic.

# III. Tool Development & Usage

## A. Custom Tools & Agents
- My agents (`battle_strategist_agent`, etc.) are for high-level reasoning.
- My tools (`pathfinder`, etc.) are for complex computational tasks.
- **Tool Development:** My `pathfinder` tool has been updated to correctly handle impassable targets. It still cannot account for scripted barriers like the strong current, so manual exploration is sometimes needed.
- **Agent Usage Reminder:** I must use my `menu_navigator_agent` for all complex menu tasks to avoid manual errors.

# IV. Puzzles & Lessons Learned

## A. Seafoam Islands Puzzle

- **Hypothesis 7 (Confirmed):** The correct path to the western boulder puzzle on B3F is to take the ladder from B4F at (12, 8) up to the western elevated platform on B3F. From there, a long, winding path around the room's perimeter leads down to the ground level where the boulders are.
- **Untested Hypothesis:** The ladder at (26, 5) on B4F is the exit.

## C. Strategic Lessons
- **Confirmation Bias:** I exhibited confirmation bias by assuming my initial pathing ideas were the only solution, instead of trusting game state data when it contradicted my tools. I must actively try to disprove my own hypotheses.
- **Strategic Flexibility:** If a strategy is failing repeatedly, I must pivot to a different approach.
- **Trust the Game State:** I must trust the game state information (e.g., 'navigable warps') over my own interpretations or tool outputs, as it is the absolute source of truth.
- **LLM Reality:** Data management tasks (notepad, agents, tools) must be performed immediately and not deferred.

# V. Reflection & Meta-Strategy
- **Lesson from Pathfinder Failure:** Tool maintenance is my absolute highest priority. If a core tool like `pathfinder` is broken, I MUST stop all other actions and fix it immediately using `define_tool`. Deferring fixes is a critical failure.
- **Untested Link:** I am currently assuming that solving the second boulder puzzle on the upper floors will stop the western current on B4F. This link is not yet proven and must be tested after the puzzle is solved.
- **Hypothesis 8 (Untested):** The warps at (21, 18) and (22, 18) on B3F are one-way exits. The correct path requires backtracking to B2F to find an alternate route down.