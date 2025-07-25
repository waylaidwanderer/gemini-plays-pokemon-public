# I. Game Mechanics & World Rules

## A. Tile Mechanics & Traversal
- **Ground:** Standard walkable tile.
- **Grass:** Walkable tile where wild Pokémon can be encountered.
- **Water:** Can be crossed using the SURF HM.
- **Impassable:** Walls, trees, and other objects that block movement.
- **Elevated Ground:** Walkable ground at a different elevation. Cannot use Surf from this tile type.
- **Gate (`gate_offscreen`, `closed_gate`, `open_gate`):** Barriers that may open or close.
- **Boulder Switch:** A floor switch activated by a boulder. Is a traversable tile.
- **Boulder Barrier:** An impassable barrier that becomes a `cleared_boulder_barrier` tile when the corresponding switch is activated.
- **Cleared Boulder Barrier:** A traversable ground tile that appears after a boulder puzzle is solved. It allows movement between different elevations, acting like a ramp.
- **Steps:** Allows vertical movement between `ground` and `elevated_ground` tiles. Pushing boulders onto them is not possible.
- **Ladders (`ladder_up`, `ladder_down`):** Function as instant 1x1 warps between floors.
- **Hole:** A tile that functions as a warp, dropping the player to a lower floor. Boulders can be pushed into these to affect puzzles on the floor below.
- **Spinner (`spinner_up`, `spinner_down`, `spinner_left`, `spinner_right`):** Forces movement in the specified direction.
- **Pushing Boulders (Mechanic Corrected):** Pushing a boulder moves the boulder one tile but does NOT move the player. The player remains on the tile from which the push was initiated.

## B. General Rules & Heuristics
- **PC Interaction:** To use a PC, stand directly below it, face up, and press 'A'.
- **HM Usage:** HMs are used from the party menu. Fainted Pokémon can use field moves.
- **"No Will to Fight" Message (Correction):** Appears when the party menu cursor is on a fainted Pokémon.
- **Level Cap:** The level cap with 8 badges is 65.
- **Special NPC Interaction:** Certain puzzles may require walking *through* an NPC rather than interacting with them (e.g., Summer Beach House).
- **PC Tile Anomaly:** The tile for interacting with the Pokémon Center PC is sometimes labeled as `grass` in the map data, despite being indoors.

# II. Battle Intel

## A. Type Effectiveness Chart (Verified)
- **Super Effective (2x):** Psychic > Ghost, Poison; Ghost > Psychic; Electric > Rock, Water; Flying > Grass, Poison, Fighting; Ice > Ground, Grass, Flying, Dragon; Ground > Poison, Fire, Electric, Rock; Rock > Fire, Ice, Flying, Bug; Fighting > Normal, Rock, Ice; Water > Fire, Ground, Rock; Grass > Water, Ground, Rock; Bug > Grass, Poison, Psychic; Poison > Grass, Bug.
- **Not Very Effective (0.5x):** Normal !> Rock; Electric !> Grass, Electric, Dragon; Rock !> Psychic; Psychic !> Psychic; Poison !> Poison, Ground, Rock, Ghost; Ice !> Water, Ice, Fire; Fighting > Poison, Flying, Psychic, Bug; Water !> Water, Grass, Dragon; Grass !> Fire, Grass, Poison, Flying, Bug, Dragon.
- **Immune (0x):** Flying immune to Ground; Ground immune to Electric; Ghost immune to Normal, Fighting.
- **Type Correction (Psychic vs. Rock):** Psychic-type moves deal NEUTRAL (1x) damage to Rock-type Pokémon, not 'not very effective' as previously assumed.

## B. Known Trainer Rosters & Movesets

### Cool Trainer M (Victory Road 3F) - DEFEATED
- **Location:** (29, 6)
- **Team:** CHARIZARD (Lv52), MAGNETON (Lv52), TENTACRUEL (Lv52)

### Cool Trainer F (Victory Road 3F) - DEFEATED
- **Location:** (14, 4)
- **Team:** WIGGLYTUFF (Lv54), CLEFABLE (Lv54), CHANSEY (Lv54), EEVEE (Lv57)
- **Observed Moves:**
  - WIGGLYTUFF: Lovely Kiss, Body Slam, Double-Edge
  - CLEFABLE: Body Slam, Light Screen, Metronome, Sing
  - CHANSEY: Double-Edge, Mega Punch
  - EEVEE: Jump Kick

# III. Current Objective: Victory Road
**Primary Goal:** Navigate through Victory Road to reach the Pokémon League.

## A. Victory Road 1F Puzzle Plan 2.0
**Current State:** The boulder barrier at (10, 13) is closed. My pathfinder tool is bugged, and my previous plan was based on a flawed assumption.
**Puzzle Components (from `puzzle_solver_tool`):
- Boulders: (15, 3), (3, 11), (17, 14)
- Switch: (18, 14)
- Barrier: (10, 13)
**New Hypothesis:** One of the three boulders must be pushed onto the switch. The previous attempt with the boulder at (17, 14) failed because the path is blocked by an impassable wall at (16, 14).
**Current Step:** First, I must fix my `gem_pathfinder` tool. Once the tool is reliable, I will use it to test the reachability of the other two boulders at (15, 3) and (3, 11). This will determine the correct starting point for the puzzle.

## B. Archived/Failed Plans
### Victory Road 1F Puzzle - Attempt 2 (FAILED)
- **Hypothesis:** The boulder starting at (6, 17) could be pushed to the switch at (18, 14).
- **Conclusion:** This was incorrect. The path is blocked by an impassable wall at (16, 14), which I failed to notice due to a hallucination and a faulty pathfinder. This highlights the danger of confirmation bias and the need to trust the map data over intuition.

### Victory Road 1F Puzzle - Attempt 3 (FAILED)
- **Hypothesis:** The boulder at (3, 11) was the correct starting point.
- **Conclusion:** This was incorrect. The boulder at (3, 10) is blocked from being pushed north by an impassable wall at (3, 9). This path is impossible.

### Victory Road 1F Puzzle - Attempt 1 (FAILED)
- **Hypothesis:** The boulder at (3, 11) was the first step.
- **Conclusion:** This was incorrect. The area with this boulder is inaccessible until the barrier at (10, 13) is opened.

# IV. Core Gameplay Lessons
- **Immediate Tool Refinement:** Deferring fixes for critical tools is a major strategic error. Faulty tools must be addressed immediately.
- **Verify Tool Outputs Before Trusting:** A faulty plan is worse than no plan. My tools can have bugs, and I must verify their outputs before blindly following them.
- **Trust the Game State:** My own assumptions can be wrong. The Game State Information is the absolute source of truth and must be trusted over my memory or intuition.
- **Confirmation Bias:** I must be wary of trying to prove my own assumptions right. It's important to trust system warnings and evidence that contradicts my beliefs.
- **Efficient Debugging:** When a tool fails, the first step should be to add extensive logging/debugging to understand its internal state. Trial-and-error fixes are inefficient.

# V. Archives

## A. Completed Puzzles
### Victory Road 2F Puzzle
- **Status:** Complete. Boulder from (4, 17) to switch at (2, 17).

### Victory Road 3F Puzzle
- **Status:** Complete. Secret ladder at (3, 1) was the true path.

# VI. Tool & Agent Ideas
- **Puzzle Strategist Agent:** An agent that takes the output of the `puzzle_solver_tool` (a list of puzzle components) and suggests a logical, sequential plan to solve the puzzle. This would be the next step after getting a reliable component list.