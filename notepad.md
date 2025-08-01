# I. Game Mechanics & Traversal
## A. Core Rules
- **Level Cap:** 8 badges = Level 65.
- **PC Interaction:** Stand directly below the PC, face up, and press 'A'.
- **HM Usage:** HMs are used from the party menu. Fainted Pokémon can use field moves.
- **Surfing:** Not all `ground` tiles adjacent to `water` are valid starting points.
- **Puzzle Resets:** Leaving and re-entering a floor resets all boulders to their original positions.
- **Off-Screen State Changes:** An object's state will not update in the map data until it is visible on-screen.
- **Boulder Pushing:** A boulder can be pushed from an adjacent tile by facing it and pressing the corresponding direction. The player only moves into the boulder's vacated space if they are positioned directly opposite the direction of the push (e.g., standing at (11,15) to push a boulder at (12,15) to (13,15)). If pushing from a perpendicular angle (e.g., standing at (12,16) to push a boulder at (12,15) north), the player's position does not change. Boulders cannot be pushed into `impassable` tiles.

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

# III. Current Strategy: Victory Road 2F Puzzle
- **Objective:** Solve the Victory Road 2F eastern boulder puzzle to reach the ladder to 3F.
- **Puzzle Elements:**
    - Western Boulder: (5, 15) -> Switch: (2, 17) -> Barrier: (8, 9), (8, 10) (SOLVED)
    - Eastern Boulder: (6, 6) -> Switch: (10, 17) -> Barrier: (24, 15)
- **New Plan (Loop Break):** The long-distance navigation strategy is failing due to constant wild encounters. My new, focused plan is to solve the eastern boulder puzzle directly. Immediate Goal: Get into position at (6, 7) to push the boulder at (6, 6).
- **Red Herring Boulders:** Both the western boulder at (3, 11) and the eastern boulder at (15, 3) are confirmed red herrings. Tests showed the western boulder is blocked by an impassable wall at (3, 9), and the eastern side of the map is physically inaccessible from the entrance.
- **Boulder Movement Rules (Confirmed):**
    - Boulders cannot be pushed onto `steps` tiles (tested at (6, 14)).
    - Pushing a boulder into a corner or against an impassable tile can make it permanently stuck, requiring a map reset to solve.
- **Victory Road 1F Traversal Rules (Confirmed):**
    - It is impossible to step down from an `elevated_ground` tile to an adjacent `ground` tile (tested at (6, 10) -> (6, 9)).
    - Defeated trainers are impassable objects and must be navigated around.

# V. Tool & Agent Principles
- **Scientific Method:** Use a scientific approach: form a hypothesis, test it, and document the conclusion. Do not modify tools to test hypotheses; test them with in-game actions first.
- **Trust System Feedback:** System feedback (like validation warnings or tool errors) is the source of truth and MUST be trusted over personal assumptions or agent outputs.
- **IMMEDIATE ACTION:** Flaws in tools or data management (notepad, markers) must be addressed immediately, not deferred as goals.

# VI. Archived Puzzle Lessons
- **Victory Road 1F:** Solved. Key takeaway was to verify all path tiles and avoid pushing boulders into corners.
- **Victory Road 2F (West):** Solved. Straightforward push to the switch.
- **Victory Road 2F (East):** Pushing the boulder north from (6,6) is a trap. My solver tool requires further refinement to handle this puzzle's complexity.

# VIII. Unverified Assumptions & Test Plans
- **Assumption:** The eastern boulder puzzle on Victory Road 2F is solvable from its starting position at (6, 6).
  - **Test Plan:** Before pushing the boulder, I will manually trace a viable path for both the boulder and myself to the switch at (10, 17) to ensure it is not a trap.
- **Assumption:** The ladder at (24, 8) is the correct path to progress on Victory Road 3F.
  - **Test Plan:** After solving the eastern puzzle, I will take the ladder at (24, 8) and explore the resulting area on 3F. If it leads to a dead end or back to a previous area, I will conclude that the ladder at (2, 2) is the main path.
## E. Victory Road 2F - Eastern Puzzle Attempt 1
- **Hypothesis:** Push the eastern boulder at (6, 6) north to (6, 5) to begin the puzzle.
- **Test:** Pushed the boulder from (6, 6) to (6, 5).
- **Result:** The boulder is now at (6, 5). The tiles to its left (5, 5) and right (7, 5) are impassable, and the tile above it (6, 4) leads to a known dead-end. It is impossible to move the boulder from this position.
- **Conclusion:** Pushing the boulder north from (6, 6) is a trap that makes the puzzle unsolvable. I must reset the map by leaving and re-entering to try a different approach.