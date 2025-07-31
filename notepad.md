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

## B. Strategic Notes
- **"No Will to Fight" Message:** A party menu cursor error on a fainted Pokémon, not a refusal to battle.
- **Victory Road Trainers:** Defeated trainers in Victory Road act as impassable obstacles.

# III. Tool Development & Debugging
## A. Tool Status
- **`gem_pathfinder_v2` Status:** The tool is now fully functional after several iterative fixes. It correctly identifies the player, impassable objects (including NPCs and boulders), and handles elevation changes via 'steps' tiles.

## B. Debugging Principles & Lessons
- **Scientific Method:** Use a scientific approach: form a hypothesis, create a minimal test case, and incrementally build up complexity.
- **Trust System Feedback:** System feedback, even when contradictory to personal observation, must be prioritized as it may reveal hallucinations or fundamental misunderstandings of game mechanics. Direct in-game evidence should be used to test hypotheses that could explain the discrepancy.
- **Avoid Confirmation Bias:** Actively try to disprove my own assumptions. My recent hallucinations on Victory Road 2F and 3F are critical lessons in trusting system feedback and re-evaluating my own perception when faced with a contradiction.

# IV. Current Plans & Tasks
## A. Current Plan: Navigate to Indigo Plateau
My immediate goal is to reach the eastern side of Victory Road 2F and ascend the ladder at (24, 8) to reach the main area of Victory Road 3F.

## B. Archived Plans
- **Victory Road 2F Western Dead End:** Confirmed via system feedback and re-evaluation that this area is NOT a dead end. The path forward is via the elevated platform, accessible because the boulder puzzle was already solved.
- **Victory Road 3F Western Platform Dead End:** Confirmed via system feedback that this platform is NOT a dead end. My previous conclusions were hallucinations based on a fundamental misunderstanding of the map's elevation.
- **Victory Road 3F Boulder Switch Test:** Confirmed that the player cannot activate a boulder switch without a boulder.
- **Victory Road Trainer Test:** Confirmed that defeated trainers in Victory Road act as impassable obstacles. Attempt to walk through the defeated Pokemaniac at (5, 3) on Victory Road 2F failed.
- **Victory Road Trainer Test 2:** The system insists the eastern part of Victory Road 2F is reachable, but my path is blocked by the defeated Pokemaniac at (5, 3). This contradicts my previous test. Hypothesis: My previous test was flawed, and defeated trainers are NOT impassable. Test: Navigate to (4, 3) and attempt to walk right onto (5, 3).
- **Conclusion:** Attempt to walk through the defeated Pokemaniac at (5, 3) failed. Defeated trainers in Victory Road are confirmed to be impassable obstacles. The system's feedback implies an alternate route must exist.
- **Puzzle Resets:** Leaving and re-entering a floor resets all boulders to their original positions.