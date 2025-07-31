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
- **Trust In-Game Evidence:** Direct, in-game evidence must always be trusted over personal assumptions or even system feedback if the feedback contradicts observable game physics.
- **Avoid Confirmation Bias:** Actively try to disprove my own assumptions. My recent hallucination on Victory Road 3F (thinking I was at a dead end when I wasn't) is a key lesson. I concluded I was stuck based on my pathfinder's failure without fully investigating *why* it failed, which was due to my misunderstanding of the platform's elevation.

# IV. Current Plans & Tasks
## A. Current Plan: Navigate Victory Road 3F
My immediate goal is to get off this isolated western platform and explore the main area of the floor.
**Hypothesis:** The 'steps' tile at (2, 10) is the only way down to the lower level of this platform.
**Execution Plan:**
1.  Navigate to the steps at (2, 10).
2.  Descend the steps to the lower ground level.
3.  Explore the newly accessible area and find a path to the eastern side of the map, targeting the unvisited warp at (27, 9).

## B. Archived Plans
- **Victory Road 2F Western Boulder Puzzle:** Completed.
- **Victory Road 2F Boulder at (6, 6):** Confirmed impossible to solve from the eastern side.
- **Victory Road 2F Eastern Path:** Invalidated as a dead end.
- **Victory Road 3F Western Platform Dead End:** Confirmed via system feedback that this platform is NOT a dead end. My previous conclusions were hallucinations based on a misunderstanding of elevation and my pathfinder's limitations.

## C. Victory Road 3F Puzzle Hypothesis (DEBUNKED)
**Hypothesis:** The player can activate `boulder_switch` tiles without a boulder.
**Test Result:** Stepping on the switch at (4, 6) and pressing 'A' had no effect. The barrier at (8, 11) remained closed.
**Conclusion:** Hypothesis is FALSE. The player cannot activate switches.