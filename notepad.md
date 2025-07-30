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
- `elevated_ground`: Walkable, different elevation. It is possible to step DOWN from an `elevated_ground` tile to an adjacent `ground` tile.
- `steps`: Allows movement between `ground` and `elevated_ground` in both directions.
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
- **Reasoning:** The party is critically injured. The only path to the exit is through the eastern boulder puzzle on 1F.
- **Plan:**
  1. Navigate to the eastern side of Victory Road 1F.
  2. Solve the boulder puzzle to clear the barrier at (10, 13).
  3. Navigate to the exit at (9, 18).
  4. Heal at the Indigo Plateau.
  5. Return to Victory Road to solve remaining puzzles.
- **Key Discoveries:**
  - Boulders cannot be pushed onto `steps` tiles.
  - It is NOT possible to step down from an `elevated_ground` tile to an adjacent `ground` tile unless using a `steps` tile.
  - Defeated trainers are impassable obstacles.

# IV. Tool Development & Debugging
- **`gem_pathfinder_v2` Status:** The tool's traversal logic for `elevated_ground` tiles has been corrected. The tool's assessment of path availability must be trusted.
- **`puzzle_strategist_agent` Status:** The agent has a known logical flaw, incorrectly identifying solvable puzzles as impossible. It needs to be refined to perform a more exhaustive search of all possible moves before declaring a puzzle unsolvable.
- **Debugging Principle:** Trust tool outputs once they are confirmed to be working correctly. When a tool fails, re-evaluate the map data and my own assumptions to find the true obstacle and form a new plan.
- **Lesson on Confirmation Bias:** I must be wary of confirmation bias. I previously wasted time assuming a path was blocked because my tools were flawed and my understanding of game mechanics was incorrect. I must actively try to disprove my own assumptions and be more willing to change my strategy when my tools contradict my beliefs.