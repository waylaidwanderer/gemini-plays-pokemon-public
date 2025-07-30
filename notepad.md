# I. Game Mechanics & Traversal
## A. Core Rules
- **Level Cap:** 8 badges = Level 65.
- **"No Will to Fight" Message:** A party menu cursor error on a fainted Pokémon, not a refusal to battle.
- **HM Usage:** HMs are used from the party menu. Fainted Pokémon can use field moves.
- **PC Interaction:** Stand directly below the PC, face up, and press 'A'.
- **Surfing:** Not all `ground` tiles adjacent to `water` are valid starting points.
- **Puzzle Resets:** Leaving and re-entering a floor resets all boulders to their original positions.
- **Data Trust:** The map XML data is the ultimate source of truth for traversal.
## B. Tile Glossary & Movement Rules
- `ground`: Standard walkable tile.
- `grass`: Wild Pokémon encounters.
- `water`: Requires SURF.
- `impassable`: Wall.
- `ledge`: One-way traversal. Can only be jumped DOWN from the tile directly above. Acts as a wall from all other directions.
- `elevated_ground`: Walkable, different elevation. Movement between elevations is *only* possible via `steps` tiles.
- `steps`: Allows movement between `ground` and `elevated_ground`.
- `boulder_switch`: Floor switch for boulders.
- `boulder_barrier`: Impassable barrier linked to a boulder switch.
- `cleared_boulder_barrier`: A former barrier, now acts as `ground`.
- `hole`: Drops to a lower floor. Pushing a boulder into one causes it to appear on the floor below.
- `spinner`: Forces movement.
- `ladder_up` / `ladder_down`: Warps between floors.
- `cuttable`: A tree that can be removed with the HM Cut.

# II. Battle Intel
## A. Type Effectiveness Chart (Verified)
- **Super Effective (2x):** Psychic > Ghost, Poison; Ghost > Psychic; Electric > Rock, Water; Flying > Grass, Poison, Fighting; Ice > Ground, Grass, Flying, Dragon; Ground > Poison, Fire, Electric, Rock, Ground; Rock > Fire, Ice, Flying, Bug; Fighting > Normal, Rock, Ice; Water > Fire, Ground, Rock; Grass > Water, Ground, Rock; Bug > Grass, Poison, Psychic; Poison > Grass, Bug
- **Not Very Effective (0.5x):** Normal !> Rock; Electric !> Grass, Electric, Dragon; Rock !> Psychic; Psychic !> Psychic; Poison !> Poison, Ground, Rock, Ghost; Ice !> Water, Ice, Fire; Fighting > Poison, Flying, Psychic, Bug; Water !> Water, Grass, Dragon; Grass !> Fire, Grass, Poison, Flying, Bug, Dragon
- **Immune (0x):** Flying immune to Ground; Ground immune to Electric; Ghost immune to Normal, Fighting
- **Correction:** Psychic-type moves deal NEUTRAL (1x) damage to Rock-type Pokémon.

# III. Puzzle Mechanics & Problem Solving
## A. Current Puzzle Plan
- *[Plan for current puzzle will go here]*

## B. Key Discoveries
- **Victory Road 1F - Boulder/Steps Interaction (Confirmed):** Boulders cannot be pushed onto `steps` tiles.
- **Victory Road 1F - Elevation Rule (Confirmed):** Movement between `ground` and `elevated_ground` is ONLY possible by traversing a `steps` tile.

# IV. Agent & Tool Development
## A. Development Ideas
- **Agent Idea:** `boulder_puzzle_strategist`. Takes the map state (boulder/switch/player positions) and devises an optimal push sequence.
- **Tool Idea:** `get_boulder_moves`. A helper tool that identifies all possible moves for all boulders on the current map.

## B. Tool Status & Lessons
- `gem_pathfinder_v2` (Bug Confirmed): The tool is generating invalid paths that attempt to move through `impassable` tiles. My previous conclusion that the tool was working was incorrect. The tool cannot be trusted for navigation until this is fixed. Manual navigation is required.

# V. Debugging Methodology
- **Principle:** Avoid confirmation bias. When a tool fails, do not assume it's a bug.
- **Process:**
  1. If a tool fails (e.g., `gem_pathfinder_v2` returns 'No path found'), do not immediately try to fix it.
  2. Call `tool_diagnostics_agent` with the tool's output and a summary of the map layout.
  3. **If Assessment is 'Correct Assessment':** My understanding of the map is wrong. I must re-evaluate the map data to find the true obstacle and form a new navigation plan.
  4. **If Assessment is 'Likely Tool Bug':** The tool is likely flawed. Add extensive logging, re-run the tool to capture debug data, analyze the logs to form a hypothesis about the bug, and then implement a fix.