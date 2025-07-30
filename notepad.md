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

# III. Current Strategy: Victory Road
- **Objective:** Exit Victory Road to heal at the Indigo Plateau.
- **Reasoning:** The party is critically injured, and the high encounter rate makes puzzle-solving inefficient and risky. A strategic retreat is necessary.
- **Plan:**
  1. Navigate to the exit on Victory Road 1F at (9, 18).
  2. Navigate to the Indigo Plateau and heal the party.
  3. Return to Victory Road to solve the remaining puzzles.
- **Key Discoveries:**
  - Boulders cannot be pushed onto `steps` tiles.
  - Movement between `ground` and `elevated_ground` is ONLY possible by traversing a `steps` tile.
  - The eastern boulder puzzle on 1F is unsolvable in its initial state, making it a dead end for progress.
  - Defeated trainers are impassable obstacles.

# IV. Tool Development & Debugging
- **`gem_pathfinder_v2` Status:** The tool is working correctly. My manual pathing has been repeatedly flawed, leading me to incorrectly assume the tool was bugged. The tool's assessment of path availability is based on the ground-truth map XML and MUST be trusted over manual pathing attempts.
- **Debugging Principle:** Trust the tool. When `gem_pathfinder_v2` fails, do not immediately assume it's a bug. My understanding of the map is likely wrong. I must re-evaluate the map data (especially tile types like `steps` and `elevated_ground`) to find the true obstacle and form a new navigation plan.
- **Lesson on Confirmation Bias:** I must be wary of confirmation bias. I previously wasted time on the Victory Road 1F eastern puzzle because I *assumed* it was the correct path, ignoring evidence from my tools that it was blocked. I must actively try to disprove my own assumptions and be more willing to change my strategy when my tools contradict my beliefs.