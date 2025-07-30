# I. Game Mechanics & Traversal
## A. Core Rules
- **Level Cap:** 8 badges = Level 65.
- **"No Will to Fight" Message:** A party menu cursor error on a fainted Pokémon, not a refusal to battle.
- **HM Usage:** HMs are used from the party menu. Fainted Pokémon can use field moves.
- **PC Interaction:** Stand directly below the PC, face up, and press 'A'.
- **Surfing:** Not all `ground` tiles adjacent to `water` are valid starting points.
- **Puzzle Resets:** Leaving and re-entering a floor resets all boulders to their original positions.
- **Data Trust:** The map XML data is the ultimate source of truth for traversal.
- **Off-Screen State Changes:** An object's state (e.g., a `boulder_barrier` changing to `cleared_boulder_barrier`) will not update in the map data until the object is visible on-screen.
## B. Tile Glossary & Movement Rules
- `ground`: Standard walkable tile.
- `grass`: Wild Pokémon encounters.
- `water`: Requires SURF.
- `impassable`: Wall.
- `ledge`: One-way traversal. Can only be jumped DOWN from the tile directly above. Acts as a wall from all other directions.
- `elevated_ground`: Walkable, different elevation. It is NOT possible to step down from an `elevated_ground` tile to an adjacent `ground` tile unless using a `steps` tile.
- `steps`: Allows movement between `ground` and `elevated_ground` in both directions.
- `boulder_switch`: Floor switch for boulders.
- `boulder_barrier`: Impassable barrier linked to a boulder switch.
- `cleared_boulder_barrier`: A former barrier, now acts as `ground`.
- `hole`: Drops to a lower floor. Pushing a boulder into one causes it to appear on the floor below.
- `spinner`: Forces movement.
- `ladder_up` / `ladder_down`: Warps between floors.
- `cuttable`: A tree that can be removed with the HM Cut.
- **Defeated Trainers (Hypothesis):** Some defeated trainers may be impassable obstacles. The Juggler at (22, 14) on Victory Road 2F was confirmed to be impassable. However, this may not apply to all defeated trainers. Further testing is required.

# II. Battle Intel
## A. Type Effectiveness Chart (Verified)
- **Super Effective (2x):** Psychic > Ghost, Poison; Ghost > Psychic; Electric > Rock, Water; Flying > Grass, Poison, Fighting; Ice > Ground, Grass, Flying, Dragon; Ground > Poison, Fire, Electric, Rock, Ground; Rock > Fire, Ice, Flying, Bug; Fighting > Normal, Rock, Ice; Water > Fire, Ground, Rock; Grass > Water, Ground, Rock; Bug > Grass, Poison, Psychic; Poison > Grass, Bug
- **Not Very Effective (0.5x):** Normal !> Rock; Electric !> Grass, Electric, Dragon; Rock !> Psychic; Psychic !> Psychic; Poison !> Poison, Ground, Rock, Ghost; Ice !> Water, Ice, Fire; Fighting > Poison, Flying, Psychic, Bug; Water !> Water, Grass, Dragon; Grass !> Fire, Grass, Poison, Flying, Bug, Dragon
- **Immune (0x):** Flying immune to Ground; Ground immune to Electric; Ghost immune to Normal, Fighting
- **Correction:** Psychic-type moves deal NEUTRAL (1x) damage to Rock-type Pokémon.

# III. Tool Development & Debugging
- **`gem_pathfinder_v2` Status:** The tool's `is_obstacle` logic was flawed, incorrectly treating all objects as impassable. This has been corrected by removing the object check. The tool now correctly paths around impassable trainers and through passable ones.
- **`puzzle_strategist_agent` Status:** The agent has proven reliable, correctly identifying an unsolvable puzzle on Victory Road 1F and providing a step-by-step solution for the solvable puzzle on Victory Road 2F.
- **Debugging Principle:** Trust direct, in-game evidence over personal assumptions. When a tool fails after being corrected, re-evaluate the map data and my own understanding to find the true obstacle and form a new plan.
- **Lesson on Confirmation Bias:** I must be wary of confirmation bias. I previously wasted time assuming a path was blocked because my tools were flawed and my understanding of game mechanics was incorrect. I must actively try to disprove my own assumptions and be more willing to change my strategy when my tools contradict my beliefs.

# IV. Current Plans
## A. Victory Road 2F Eastern Boulder Puzzle
My `puzzle_strategist_agent` has provided a 19-step solution to move the boulder at (6, 6) to the switch at (10, 17), which will clear the barrier at (24, 15).
1. **Push boulder at (6, 6) DOWN**
2. **Push boulder at (6, 7) DOWN**
3. **Push boulder at (6, 8) RIGHT**
4. **Push boulder at (7, 8) RIGHT**
5. **Push boulder at (8, 8) DOWN**
6. **Push boulder at (8, 9) RIGHT**
7. **Push boulder at (9, 9) DOWN**
8. **Push boulder at (9, 10) RIGHT**
9. **Push boulder at (10, 10) RIGHT**
10. **Push boulder at (11, 10) RIGHT**
11. **Push boulder at (12, 10) DOWN**
12. **Push boulder at (12, 11) DOWN**
13. **Push boulder at (12, 12) DOWN**
14. **Push boulder at (12, 13) DOWN**
15. **Push boulder at (12, 14) DOWN**
16. **Push boulder at (12, 15) DOWN**
17. **Push boulder at (12, 16) DOWN**
18. **Push boulder at (12, 17) LEFT**
19. **Push boulder at (11, 17) LEFT**