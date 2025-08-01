# I. Game Mechanics & Traversal
## A. Core Rules
- **Level Cap:** 8 badges = Level 65.
- **PC Interaction:** Stand directly below the PC, face up, and press 'A'.
- **HM Usage:** HMs are used from the party menu. Fainted Pokémon can use field moves.
- **Surfing:** Not all `ground` tiles adjacent to `water` are valid starting points.
- **Puzzle Resets:** Leaving and re-entering a floor resets all boulders to their original positions.
- **Off-Screen State Changes:** An object's state will not update in the map data until it is visible on-screen.
- **Boulder Pushing:** It is possible to push a boulder by standing adjacent to it, facing it, and moving towards it (e.g., standing below at Y+1, facing up, and pressing Up to push it to Y-1). You do not need to be on the opposite side. Boulders cannot be pushed into `impassable` tiles.

## B. Tile Glossary & Movement Rules
- `ground`: Standard walkable tile.
- `grass`: Wild Pokémon encounters.
- `water`: Requires SURF.
- `impassable`: Wall.
- `ledge`: One-way traversal. Can only be jumped DOWN from the tile directly above. Acts as a wall from all other directions.
- `elevated_ground`: Walkable, different elevation. It is NOT possible to step down from an `elevated_ground` tile to an adjacent `ground` tile.
- `steps`: Allows movement between `ground` and `elevated_ground` in both directions.
- `boulder_switch`: Floor switch for boulders.
- `boulder_barrier`: Impassable barrier linked to a boulder switch.
- `cleared_boulder_barrier`: A former barrier that acts as a one-way ramp. It is possible to move from it onto `elevated_ground` (elevation 2), but it is NOT possible to move from it directly back down to `ground` or to enter it from ANY adjacent `ground` tile.
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
- **Struggle Mechanic:** Struggle is only used automatically when a Pokémon is out of PP for ALL of its moves.
- **Full Heal Mechanic:** This item ONLY cures status conditions. It does NOT restore HP. This was verified by attempting to use it on multiple injured Pokémon with no status effects, which resulted in the message 'It won't have any effect.'

# III. Current Strategy: Victory Road 1F
- **Objective:** Reach the ladder to 2F at (2, 2).
- **Primary Strategy:** The puzzle must be solved in stages. The eastern boulder puzzle is the key to the final solution, but it is currently unreachable. Therefore, the immediate goal is to solve the western boulder puzzle to create a path to the eastern section.
- **Immediate Plan:** Maneuver the boulder at (6, 16) to a position that allows access to the elevated platform via the steps at (6, 14).

# IV. Archived Plans & Disproven Hypotheses
- **Hypothesis (Disproven):** The true path requires walking through defeated trainers. **Test:** Modified `gem_pathfinder_v2` to ignore trainer collision. **Result:** The tool returned 'No path found.' **Conclusion:** The map geometry itself makes the eastern section unreachable from the entrance, regardless of trainer passability.
- **Hypothesis (Disproven):** The path to the ladder on Victory Road 1F is through the western boulder puzzle. **Test:** Used `gem_pathfinder_v2` to find a path to (2, 2) while hypothetically ignoring the boulder at (6, 15) and defeated trainers. **Result:** The tool returned 'No path found.' **Conclusion:** The geometry of the western section makes reaching the ladder from that side impossible. The path must be through the eastern section.
- **Hypothesis (Disproven):** It might be possible to step down from an `elevated_ground` tile to a `ground` tile on Victory Road 1F. **Test:** Attempted to move from (6, 10) [`elevated_ground`] to (6, 9) [`ground`]. **Result:** Movement was blocked. **Conclusion:** The rule that you cannot step down from `elevated_ground` is confirmed to be true for this map.
- **Hypothesis (Disproven):** The boulder at (3, 10) is the key to the puzzle. **Test:** Attempted to push the boulder up from (3, 11). **Result:** Movement was blocked by an impassable tile at (3, 9). **Conclusion:** The boulder at (3, 10) is a red herring.
- **Hypothesis (Disproven):** The boulder at (6, 15) can be pushed up the steps at (6, 14). **Test:** Attempted to push the boulder up from (6, 16) on turn 114437. **Result:** Movement was blocked. **Conclusion:** The rule that boulders cannot be pushed onto `steps` tiles is definitively confirmed. The western path is not viable through this method.

# V. Tool & Agent Development
## A. Ideas & Future Plans
- A `pathfinder_debugger_agent` could be useful. It could analyze a failed pathfinding attempt and suggest potential causes (e.g., 'Hypothesis: An NPC at (X,Y) is blocking the path, try ignoring it.')
- A `puzzle_reset_strategist` could be useful. It could analyze the map state and determine if resetting the puzzle (by leaving the map) is the most efficient path forward, rather than trying to solve it from a bad state.
- Refine `puzzle_strategist_agent` to output `ignorable_coords` directly, streamlining the puzzle-solving workflow.

## B. Debugging Principles & Lessons
- **Scientific Method:** Use a scientific approach: form a hypothesis, test it, and document the conclusion. Do not modify tools to test hypotheses; test them with in-game actions first.
- **Trust System Feedback:** System feedback (like validation warnings or tool errors) is the source of truth and MUST be trusted over personal assumptions or agent outputs.
- **IMMEDIATE ACTION:** Flaws in tools or data management (notepad, markers) must be addressed immediately, not deferred as goals.
- **Hypothesis (Disproven):** The boulder at (3, 10) is the key to the puzzle. **Test:** Attempted to push the boulder up from (3, 11). **Result:** Movement was blocked by an impassable tile at (3, 9). **Conclusion:** The boulder at (3, 10) is a red herring.