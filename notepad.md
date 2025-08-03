# I. Core Gameplay & World Rules

## A. Game Mechanics
- **Level Cap:** 8 badges = Level 65.
- **PC Interaction:** Stand directly below the PC, face up, and press 'A' to access Pokémon Storage. 'Gem's PC' is for items.
- **HM Usage:** HMs are used from the party menu. Fainted Pokémon can use field moves.
- **Surfing:** Not all `ground` tiles adjacent to `water` are valid starting points.
- **Puzzle Resets:** Leaving and re-entering a map (e.g., Victory Road 1F to Route 23) resets its boulder puzzles. Using ladders between floors (e.g., 1F to 2F) does NOT reset them.
- **Off-Screen State Changes:** An object's state (like a `boulder_barrier`) will not update in the map data until it is visible on-screen.
- **Boulder Pushing:** Activate Strength once from the party menu. Then, for each push, simply walk into the boulder. It does not need to be reactivated for every push.

## B. Tile Glossary & Movement Rules
- `ground`: Standard walkable tile (Elevation 0).
- `elevated_ground`: Walkable tile at a higher elevation (Elevation 2). It is IMPOSSIBLE to step directly between `ground` and `elevated_ground`.
- `steps`: Allows two-way movement between `ground` and `elevated_ground`.
- `cleared_boulder_barrier`: A former barrier that acts as a one-way ramp (Elevation 1). Connects to adjacent elevations but cannot be stepped up onto from `ground` or down from to `ground`.
- `ledge`: One-way traversal. Can only be jumped DOWN from the tile directly above. Acts as a wall from all other directions.
- `impassable`: Wall. Defeated trainers on Victory Road 1F & 2F are impassable obstacles.
- `boulder_switch`: Floor switch for boulders.
- `boulder_barrier`: Impassable barrier linked to a switch.
- `hole`: Drops to a lower floor. Pushing a boulder into one moves it to the floor below.

# II. Battle Intelligence

## A. Verified Type Effectiveness Chart
- **Super Effective (2x):** Psychic > Ghost, Poison; Ghost > Psychic; Electric > Rock, Water; Flying > Grass, Poison, Fighting; Ice > Ground, Grass, Flying, Dragon; Ground > Poison, Fire, Electric, Rock, Ground; Rock > Fire, Ice, Flying, Bug; Fighting > Normal, Rock, Ice; Water > Fire, Ground, Rock; Grass > Water, Ground, Rock; Bug > Grass, Poison, Psychic; Poison > Grass, Bug
- **Not Very Effective (0.5x):** Normal !> Rock; Electric !> Grass, Electric, Dragon; Rock !> Psychic; Psychic !> Psychic; Poison !> Poison, Ground, Rock, Ghost; Ice !> Water, Ice, Fire; Fighting > Poison, Flying, Psychic, Bug; Water !> Water, Grass, Dragon; Grass !> Fire, Grass, Poison, Flying, Bug, Dragon
- **Immune (0x):** Flying immune to Ground; Ground immune to Electric; Ghost immune to Normal, Fighting

## B. Strategic Notes & Mechanics
- **"No Will to Fight" Message:** A party menu cursor error on a fainted Pokémon, not a refusal to battle.
- **Struggle Mechanic:** Used automatically only when a Pokémon is out of PP for ALL moves.
- **Full Heal:** Cures status conditions only, does not restore HP.

# III. Core Principles & Methodology
- **Agent-First Approach:** Before attempting any manual solution for a complex problem (puzzles, multi-step navigation, difficult battles), I MUST consult the relevant specialist agent first (`puzzle_strategist_agent`, `battle_strategist_agent`, etc.).
- **Scientific Method:** Use a scientific approach: form a hypothesis, test it, and document the conclusion. Do not modify tools to test hypotheses; test them with in-game actions first.
- **Trust System Feedback:** System feedback (like validation warnings or tool errors) is the source of truth and MUST be trusted over personal assumptions or agent outputs.
- **IMMEDIATE ACTION:** Flaws in tools or data management (notepad, markers) must be addressed immediately, not deferred as goals.

# IV. Archived Lessons & Puzzle Solutions

## Victory Road 2F - Western Boulder
- **Hypothesis #1 (Original):** Push boulder at (5, 15) south to (5, 17), then left to switch at (2, 17).
- **Test:** Pushed boulder to (5, 17).
- **Conclusion:** FAILED. Could not access (6, 17) to push left. Boulder was trapped.
- **Hypothesis #2:** Push boulder at (6, 15) left to (5, 15), then down to (5, 17), then left to switch at (2, 17).
- **Test:** Pushed boulder to (2, 17).
- **Conclusion:** SUCCESS. Barrier at (8, 9) and (8, 10) was cleared after visual confirmation.

## Victory Road 2F - Eastern Boulder (Failed Hypotheses)
- **Hypothesis #1 (Push Up):** Push boulder at (6, 6) UP to (6, 5).
- **Test:** Pushed boulder to (6, 5).
- **Conclusion:** FAILED. Path upwards is a dead end. The only way forward is down.
- **Hypothesis #2 (Push Down):** Push boulder at (6, 6) down to (6, 8), then right through the cleared barrier at (8, 9), then down to the switch at (10, 17).
- **Conclusion:** FAILED. Boulder is on `ground` and cannot be pushed up to the `elevated_ground` where the barrier is.
- **Hypothesis #3 (Use other boulder):** Push the boulder at (5, 16) to the switch at (10, 17).
- **Conclusion:** FAILED. Path is blocked by an impassable wall at X=9.

## Victory Road 3F Puzzle
- The `gem_pathfinder_v2` tool repeatedly failed to find a path to the warp at (27, 9). This was initially mistaken for a bug in the A* algorithm. The tool was working correctly; the path was blocked by a boulder I had inadvertently moved into the main corridor. This highlights the importance of careful movement during puzzle-solving to avoid creating new obstacles.

## General Mechanics
- **Boulder Pushing:** When pushing a boulder (horizontally or vertically), the player character does NOT move into the boulder's previous tile. This was observed on Victory Road 1F.

## Victory Road 1F - Elevation Test
## B. Solved Puzzles & Verified Mechanics

### Victory Road 1F
- **Elevation Test:** Confirmed direct movement between `elevated_ground` and `ground` is impossible. An agent's initial analysis was flawed.

### Victory Road 2F
- **Western Boulder:** Solved by pushing the boulder at (5,15) to the switch at (2,17). This cleared the barrier at (8,9) and (8,10).
- **Eastern Boulder (Failed Attempts):** Documented multiple failed hypotheses, including pushing the northern boulder, which always gets trapped, and trying to push the southern boulder east, which also gets trapped against a wall. These failures confirm the puzzle is more complex than a simple push.
- **Boulder Push Mechanic:** Confirmed Strength only needs to be activated once from the party menu, not before every single push.

### Victory Road 3F
- **Path Blockage:** I learned that inadvertently moving a boulder can block main pathways, which my pathfinder correctly identified as an impassable route. This was a user error, not a tool failure.

## Victory Road 2F - Boulder Push Mechanic (Corrected)
- **Hypothesis #1:** The HM Strength must be reactivated from the party menu before each individual boulder push.
- **Test 1:** After a failed push, Strength was reactivated. The next push succeeded.
- **Conclusion 1 (Initial):** The hypothesis seemed correct.
- **Test 2:** A subsequent push was attempted *without* reactivating Strength.
- **Conclusion 2 (Final):** SUCCESS. The boulder moved. The initial hypothesis was **incorrect**. The first failure was likely a positioning error or a one-time glitch. Strength does NOT need to be reactivated for every push.