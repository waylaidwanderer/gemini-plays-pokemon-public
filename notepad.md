# I. Game Mechanics & Discoveries

## A. Verified Tile Mechanics
- **Ground:** Standard walkable tile.
- **Impassable:** Walls, objects, etc. Cannot be entered.
- **Grass:** Tall grass for wild Pokémon encounters.
- **Ledge:** Can be jumped down (one-way). Moving down into a ledge tile moves the player two tiles down.
- **Cuttable Tree:** Requires HM Cut to pass. Becomes `ground` after cutting, but respawns on map change.
- **Water:** Requires HM Surf to traverse. To use Surf, you must be standing on a 'ground', 'water', or 'steps' tile adjacent to water, face the water, and use the HM from the party menu. It is not a standard walking move from land.
- **Boulder:** Requires HM Strength to move.
- **Hole:** Warps player to a lower floor or a specific spot.
- **Ladder (Up/Down):** Warps player between floors.
- **Warp:** An instant transition point between maps or areas.
- **Steps:** Allows vertical and horizontal movement between 'steps' and adjacent 'ground' or 'elevated_ground' tiles.
- **Spinner (up, down, left, right):** Forces movement in a specific direction.
- **Spinner Stop:** A tile that halts movement from a spinner.
- **Elevated Ground:** Walkable ground at a different elevation. Movement between `elevated_ground` and `ground` is only possible via `steps`.
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
- **Seafoam Islands B3F Layout:** Discovered that the eastern and western sections of B3F are not connected. The main boulder puzzle area is only accessible from a specific ladder on B4F (the eastern one).

## B. Failed Puzzle Attempts
- **Seafoam Islands B3F Boulder Puzzle (West):** The `boulder_puzzle_solver` tool confirmed that the puzzle in the isolated western section is unsolvable with the current configuration of boulders and holes. It is a red herring.

## C. Solved Development Issues
- **Pathfinder Tool (Invalid Path):** The pathfinder generated multiple invalid paths that attempted to move through 'impassable' tiles or from land to water. The root cause was a flawed sorting key in the A* algorithm's logic for finding an adjacent tile when the primary target was blocked. This caused it to fail repeatedly and was the source of my map hallucinations. The tool has been rewritten with corrected logic.

## D. Future Development Ideas
- **Puzzle Identifier Tool:** Create a tool that parses the `map_xml_string` to automatically identify puzzles (like boulder/switch combos or spinner mazes) and output their key coordinates. This would streamline using solver tools.
- **Agent-Assisted Tool Definition:** An agent that takes a high-level description of a bug and debugging suggestions to help formulate the `define_tool` call, reducing manual effort.

## E. Unverified Hypotheses
- **Normal-type effectiveness:** Normal (observed from CUT) might be super-effective against Grass and/or Psychic types (vs. LEGION the EXEGGCUTE).

## F. Ongoing Development Issues
*This section is for puzzles that remain unsolved.*
- **Strong Current:** Acts as an event-based impassable tile. Cannot be entered with SURF even from an adjacent tile.

## F. Future Development Ideas
- **Puzzle Identifier Tool:** Create a tool that parses the `map_xml_string` to automatically identify puzzles (like boulder/switch combos or spinner mazes) and output their key coordinates. This would streamline using solver tools.
- **Tool Debug Assistant Agent:** An agent that takes a traceback and failing code to suggest specific, granular debugging steps, like where to insert print statements.