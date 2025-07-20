# I. Game Mechanics & Discoveries

## A. Verified Tile Mechanics
- **Ground:** Standard walkable tile.
- **Impassable:** Walls, objects, etc. Cannot be entered.
- **Grass:** Tall grass for wild Pokémon encounters.
- **Ledge:** Can be jumped down (one-way). Moving down into a ledge tile moves the player two tiles down.
- **Cuttable Tree:** Requires HM Cut to pass. Becomes `ground` after cutting, but respawns on map change.
- **Water:** Requires HM Surf to traverse. To use Surf from a land tile, you must be standing on a 'ground', 'water', or 'steps' tile adjacent to water, face the water, and use the HM from the party menu. Strength can be used while surfing.
- **Boulder:** Requires HM Strength to move.
- **Hole:** Warps player to a lower floor or a specific spot on the same/different floor.
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
- **Trust the Data:** I incorrectly concluded the western 1F platform was a dead end. The system critique revealed other reachable warps were available. I must always trust the `navigable_warps` data over my visual assessment of the map.

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
- **Seafoam Islands B3F Layout:** Discovered that the eastern and western sections of B3F are not connected. The main boulder puzzle area is only accessible from a specific ladder on B4F (the eastern one), not the ladder connected to the western side.

## B. Failed Puzzle Attempts
- **Seafoam Islands B3F Boulder Puzzle (West):** The `boulder_puzzle_solver` tool confirmed that the puzzle in the isolated western section is unsolvable with the current configuration of boulders and holes. It is a red herring.

## C. Solved Development Issues
- **Boulder Puzzle Solver Refinement:** The `boulder_puzzle_solver` tool has been updated to incorporate A* pathfinding for player reachability checks. This prevents it from failing when the player is in an isolated area, which was confirmed on B3F.
- **Pathfinder Tool (Invalid Path):** The pathfinder generated multiple invalid paths that attempted to move through 'impassable' tiles. This was caused by a logical flaw in the `is_traversable` function, which did not correctly prioritize the 'impassable' check and had incomplete logic for movement between special tile types like 'steps' and 'ladders'. The function was rewritten with a clear hierarchy of checks to resolve the issue.
- **Boulder Puzzle Solver (Invalid/Hanging):** The solver had multiple issues. First, it produced an invalid solution by failing to verify that the player could reach the exact push position. This was fixed by removing the 'find adjacent goal' logic from the inner `player_a_star`. Second, it would hang indefinitely due to a `NameError` and then due to the inner `player_a_star` lacking a timeout. Both issues were resolved, and the tool is now functional.

## D. Future Development Ideas
- **Puzzle Identifier Tool:** Create a tool that parses the `map_xml_string` to automatically identify puzzles (like boulder/switch combos or spinner mazes) and output their key coordinates. This would streamline using solver tools. (Correction: This must be a tool, not an agent, because it involves parsing raw XML data, which is a computational task.)

## E. Unverified Hypotheses
- **Normal-type effectiveness:** Normal (observed from CUT) might be super-effective against Grass and/or Psychic types (vs. LEGION the EXEGGCUTE).

## F. Ongoing Development Issues
*This section is for puzzles that remain unsolved.*
- **Pathfinder Tool (Repeated Failures):** The pathfinder tool is consistently failing to find simple paths on Seafoam Islands B4F, despite manual movement being possible. This is causing system warnings about hallucinated unseen tiles. Multiple attempts to patch the `is_traversable` function and A* logic have failed. Current plan is to add extensive debug prints to trace the execution and pinpoint the logical error, as advised by the `code_debugger_agent`.