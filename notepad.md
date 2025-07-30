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
## A. Current Puzzle Plan: Victory Road 3F
- **Objective:** Clear the boulder barrier at (8, 11) to access the western part of the floor.
- **Hypothesis (Disproven):** A boulder must be dropped from 3F to 2F to solve the 2F puzzle. (This was based on a misunderstanding of the 2F puzzle's unsolvable state).
- **New Hypothesis:** The boulder at (25, 11) must be pushed onto the switch at (4, 6) to clear the barrier at (8, 11). This will likely grant access to the western section of 3F, which contains another puzzle.

## B. Key Discoveries
- **Victory Road 1F - Boulder/Steps Interaction (Confirmed):** Boulders cannot be pushed onto `steps` tiles.
- **Victory Road 1F - Elevation Rule (Confirmed):** Movement between `ground` and `elevated_ground` is ONLY possible by traversing a `steps` tile.
- **Victory Road 1F - Eastern Puzzle (Confirmed Unsolvable):** The eastern boulder puzzle is unsolvable in its current state, making the eastern section a dead end for progress.
- **Victory Road 2F - Defeated Trainers (Confirmed):** Defeated trainers are impassable obstacles.

# IV. Agent & Tool Development
## A. Tool Status & Lessons
- `gem_pathfinder_v2` (Confirmed): The tool is working correctly. My manual pathing has been repeatedly flawed, leading me to incorrectly assume the tool was bugged. The tool's assessment of path availability is based on the ground-truth map XML and MUST be trusted over manual pathing attempts.

# V. Debugging Methodology
- **Principle:** Trust the tool. When `gem_pathfinder_v2` fails, do not immediately assume it's a bug.
- **Process:**
  1. If `gem_pathfinder_v2` returns 'No path found', trust its assessment.
  2. My understanding of the map is likely wrong. I must re-evaluate the map data (especially tile types like `steps` and `elevated_ground`) to find the true obstacle and form a new navigation plan.
  3. Only if a path is manually verified to be 100% valid according to established traversal rules should a tool bug be considered. In that case, add logging to diagnose the issue.
- **Lesson on Confirmation Bias:** I must be wary of confirmation bias. I previously wasted time on the Victory Road 1F eastern puzzle because I *assumed* it was the correct path, ignoring evidence from my tools that it was blocked. I must actively try to disprove my own assumptions and be more willing to change my strategy when my tools contradict my beliefs.