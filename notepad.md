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
- **Ladders (`ladder_up`, `ladder_down`):** Function as instant 1x1 warps between floors. `ladder_up` leads to a higher floor, `ladder_down` leads to a lower floor.
- **Hole:** A tile that functions as a warp, dropping the player to a lower floor. Boulders can be pushed into these to affect puzzles on the floor below.
- **Spinner (`spinner_up`, `spinner_down`, `spinner_left`, `spinner_right`):** Forces movement in the specified direction.

## B. General Rules & Heuristics
- **PC Interaction:** To use a PC, stand directly below it, face up, and press 'A'.
- **HM Usage:** HMs are used from the party menu. Fainted Pokémon can use field moves.
- **"No Will to Fight" Message (Correction):** Appears when the party menu cursor is on a fainted Pokémon.
- **Level Cap:** The level cap with 8 badges is 65.
- **Special NPC Interaction:** Certain puzzles may require walking *through* an NPC rather than interacting with them (e.g., Summer Beach House).
- **Pushing Boulders (Mechanic Corrected):** Pushing a boulder does NOT move the player. The player remains on the tile from which the push was initiated.
- **PC Tile Anomaly:** The tile for interacting with the Pokémon Center PC is sometimes labeled as `grass` in the map data, despite being indoors.

## C. Puzzle Mechanics
- **Delayed Boulder Barrier Opening:** The barriers on Victory Road 1F, 2F, and 3F do not open immediately after the corresponding switch is activated. The change triggers after moving a certain distance away from the puzzle area.

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

# III. Active Plans
- **Current Objective:** Navigate through Victory Road to reach the Pokémon League.

### Victory Road 1F Puzzle Plan (Corrected)
**Objective:** Open the boulder barrier at (10, 13).
**Hypothesis (Attempt 1 - FAILED):** The boulder at (3, 11) was stuck, and a 'hard reset' of the map by flying far away would fix it.
**Conclusion:** The hypothesis was flawed. The boulder at (3, 11) is in an area that is currently inaccessible *because* the barrier at (10, 13) is closed. The 'hard reset' was unnecessary as I was trying to solve the puzzle out of order.

**New Hypothesis (Attempt 2):** The correct sequence is to first solve a different puzzle to open the barrier. The boulder at (6, 16) in the southern part of the map must be pushed onto the switch at (18, 14). This will open the barrier at (10, 13), granting access to the western section of the map and the boulder at (3, 11).
**Next Step:** Navigate to the southern area and push the boulder from (6, 16) to (18, 14).

# IV. Core Gameplay Lessons
- **Immediate Tool Refinement:** Deferring fixes for critical tools is a major strategic error. Faulty tools must be addressed immediately.
- **Verify Tool Outputs Before Trusting:** A faulty plan is worse than no plan. My tools can have bugs, and I must verify their outputs before blindly following them. This is especially true after correcting a tool's logic.
- **Archived Puzzle Solutions:** Puzzles can reset upon re-entering a map. Archived solutions may be outdated. Always observe the current state of a puzzle before acting.
- **Trust the Game State:** My own assumptions can be wrong. The Game State Information is the absolute source of truth and must be trusted over my memory or intuition.
- **Break Unproductive Loops:** If a strategy fails repeatedly, it's better to change the approach or goal than to persist in an inefficient loop.
- **Confirmation Bias:** I must be wary of trying to prove my own assumptions right. It's important to trust system warnings and evidence that contradicts my beliefs. My attempt to 'hard reset' the Victory Road boulder was a prime example of confirmation bias; I pursued a flawed solution for dozens of turns without first verifying that my initial premise (that the northern boulder was the correct first step) was even correct.
- **Efficient Debugging:** When a tool fails, the first step should be to add extensive logging/debugging to understand its internal state. Trial-and-error fixes are inefficient and should be avoided.
- **No Premature Documentation:** Do not document an event or status in the notepad until it has been confirmed by the game state. Recording intentions as facts is a form of hallucination.

# V. Archives

## A. Completed Puzzles
### Victory Road 2F Puzzle
- **Objective:** Push the boulder from (4, 17) to the switch at (2, 17).
- **Status:** Complete. Barrier at (8, 9) opens with delay.

### Victory Road 3F Puzzle
- **Objective:** Solve the floor's puzzle to proceed.
- **Solution:** The puzzles on this floor were a red herring. The true path forward was a secret, unmarked ladder at (3, 1) discovered by exploring an unseen tile. This ladder leads to a new area of Victory Road 2F.
- **Trust System Data Over Intuition:** The system's 'is_in_dead_end_area' flag and 'reachable_unseen_tiles' count are sources of truth. If they indicate a path exists, trust them over personal assumptions about being trapped. The system may see connections (like through elevated terrain) that are not immediately obvious.

# VI. Tool & Agent Ideas
- **Puzzle Diagnostics Agent:** An agent that takes a description of a failed puzzle and suggests troubleshooting hypotheses (e.g., map reset, hard reset, hidden switch).
- **Puzzle Strategist Agent:** An agent that takes the output of the `puzzle_solver_tool` (a list of puzzle components) and suggests a logical, sequential plan to solve the puzzle, prioritizing accessible components first.