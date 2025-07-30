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
## B. Trainer Battle Rules
- **Defeated Trainers:** Are **IMPASSABLE** obstacles. They do not respawn and block movement.

# III. Puzzle Mechanics & Problem Solving
## A. Methodology
- **Systematic Approach:** When stuck, do not repeat failed actions. Re-evaluate the entire map, look for in-game clues (like empty switches), and form a new, testable hypothesis. Avoid confirmation bias by actively trying to disprove initial assumptions.
## B. Key Discoveries
- **Victory Road 1F - Boulder/Steps Interaction (Confirmed):** Boulders cannot be pushed onto `steps` tiles.
- **Victory Road 1F - Elevation Rule (Confirmed):** Movement between `ground` and `elevated_ground` is ONLY possible by traversing a `steps` tile.

# IV. Archived Lessons & Tool Development
- **Systematic Problem-Solving:** Trust game data over intuition. Add debug logging to tools as a first step, not a last resort.
- **Immediate Action:** Log all data and fix all tools in the turn of discovery. This includes disproven hypotheses to avoid repeating mistakes.
- **Tool Development Status (Functional):** `gem_pathfinder_v2`: The pathfinder's core logic is now considered reliable. Past failures were primarily due to user error, specifically not using the `ignorable_coords` parameter to tell the tool to path around movable obstacles during puzzle-solving.

# V. Future Development Ideas

- **Flee Agent:** An agent to automatically run from non-essential wild battles to improve navigation efficiency.
- **Pathfinder Error Messages:** Refine `gem_pathfinder_v2` to provide more specific error messages on failure (e.g., 'Path failed due to illegal move between elevations'). This would make it a valuable diagnostic tool.
- **Puzzle Strategist Agent:** An agent to analyze the current state of a puzzle (e.g., boulder and switch locations) and devise a high-level strategic solution. This would separate the 'what to do' (agent's job) from the 'how to do it' (tool's job).