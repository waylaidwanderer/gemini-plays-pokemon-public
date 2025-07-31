# I. Game Mechanics & Traversal
## A. Core Rules
- **Level Cap:** 8 badges = Level 65.
- **PC Interaction:** Stand directly below the PC, face up, and press 'A'.
- **HM Usage:** HMs are used from the party menu. Fainted Pokémon can use field moves.
- **Surfing:** Not all `ground` tiles adjacent to `water` are valid starting points.
- **Puzzle Resets:** Leaving and re-entering a floor resets all boulders to their original positions.
- **Off-Screen State Changes:** An object's state will not update in the map data until it is visible on-screen.

## B. Tile Glossary & Movement Rules
- `ground`: Standard walkable tile.
- `grass`: Wild Pokémon encounters.
- `water`: Requires SURF.
- `impassable`: Wall.
- `ledge`: One-way traversal. Can only be jumped DOWN from the tile directly above. Acts as a wall from all other directions.
- `elevated_ground`: Walkable, different elevation. It is NOT possible to step down from an `elevated_ground` tile to an adjacent `ground` tile. All elevation changes must use 'steps' tiles.
- `steps`: Allows movement between `ground` and `elevated_ground` in both directions.
- `boulder_switch`: Floor switch for boulders.
- `boulder_barrier`: Impassable barrier linked to a boulder switch.
- `cleared_boulder_barrier`: A former barrier that acts as a one-way ramp. It is possible to move from `ground` (elevation 0) onto it, and from it onto `elevated_ground` (elevation 2), but it is NOT possible to move from it directly back down to `ground`.
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

## B. Strategic Notes
- **"No Will to Fight" Message:** A party menu cursor error on a fainted Pokémon, not a refusal to battle.
- **Victory Road Trainers:** Defeated trainers in Victory Road act as impassable obstacles.
- **Struggle Mechanic:** Struggle is only used automatically when a Pokémon is out of PP for ALL of its moves.

# III. Tool Development & Debugging
## A. Tool Status
- **`gem_pathfinder_v2` Status:** The tool is now fully functional after several iterative fixes.
- **`boulder_puzzle_solver` Status:** Timed out on Victory Road 2F puzzle. I have added logging to the BFS loop to diagnose the performance issue.

## B. Agent/Tool Ideas
- `party_health_assessor_agent`: Could analyze party status to recommend when a retreat to a Pokémon Center is strategically necessary.

## C. Debugging Principles & Lessons
- **Scientific Method:** Use a scientific approach: form a hypothesis, test it, and document the conclusion.
- **Trust System Feedback:** System feedback (like warnings or a tool's 'no path found' error) is the source of truth and MUST be trusted over personal assumptions or agent outputs.
- **Agent vs. Tool:** Complex, deterministic, computational tasks like state-space searches (BFS) are better suited for code-based Tools, not reasoning-based Agents.
- **Tool Timeouts are Bugs:** A tool timeout is a performance bug that must be diagnosed and fixed, not a reason to abandon the tool for a manual approach.

# IV. Current Plan: Survive Victory Road 2F
**Status:** Party is critically injured. I am trapped on Victory Road 2F.
**Current Step:** My `boulder_puzzle_solver` tool timed out on the western boulder puzzle. I have added logging to its code to diagnose the performance issue. My immediate next step is to run the tool again to analyze the new debug output. If it succeeds, I will execute the provided solution.

# V. Archived Plans & Disproven Hypotheses
- **(Failed) Retreat from Victory Road 1F:** My plan to retreat from Victory Road 1F via the entrance at (9, 18) failed. The `gem_pathfinder_v2` tool repeatedly found no path, which I eventually confirmed was due to defeated trainers blocking the way. This forced me to take the ladder to 2F, trapping me deeper inside.
- **(Confirmed) Victory Road Trainer Impassability:** Confirmed that defeated trainers in Victory Road act as impassable obstacles.
- **(Failed) Agent-led Retreat:** My `puzzle_strategist_agent` incorrectly concluded the puzzle was unsolvable, leading to a plan to retreat via the ladder at (2, 2). This was proven false by system feedback.
- **(Confirmed) Victory Road 2F Western Dead End:** Confirmed via system feedback and re-evaluation that this area is NOT a dead end. The path forward is via the elevated platform, accessible because the boulder puzzle was already solved.
- **(Confirmed) Victory Road 3F Western Platform Dead End:** Confirmed via system feedback that this platform is NOT a dead end. My previous conclusions were hallucinations based on a fundamental misunderstanding of the map's elevation.
- **(Confirmed) Victory Road 3F Boulder Switch Test:** Confirmed that the player cannot activate a boulder switch without a boulder.
- **(Failed) Victory Road 1F Puzzle - Blocked! (Initial Agent Failure):** My `puzzle_strategist_agent` initially determined that the boulder puzzles on this floor were unsolvable. This was proven to be a hallucination by system feedback. The root cause was a flawed `get_impassable_coords` tool that did not account for defeated trainers as obstacles. This plan to retreat was abandoned.
- **(Failed) Abandoning Tool Output:** I abandoned the `boulder_puzzle_solver`'s output after only a few steps, assuming it was wrong. This was a critical process error. My tools are built on perfect map data and should be trusted over my manual reasoning unless proven definitively incorrect through complete testing.