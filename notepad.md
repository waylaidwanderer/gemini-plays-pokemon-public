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
- **Steps:** Allows vertical movement between `ground` and `elevated_ground` tiles.
- **Ladders (`ladder_up`, `ladder_down`):** Function as instant 1x1 warps between floors. `ladder_up` leads to a higher floor, `ladder_down` leads to a lower floor.
- **Hole:** A tile that functions as a warp, dropping the player to a lower floor. Boulders can be pushed into these to affect puzzles on the floor below.
- **Spinner (`spinner_up`, `spinner_down`, `spinner_left`, `spinner_right`):** Forces movement in the specified direction.

## B. General Rules & Heuristics
- **PC Interaction:** To use a PC, stand directly below it, face up, and press 'A'.
- **HM Usage:** HMs are used from the party menu. Fainted Pokémon can use field moves.
- **"No Will to Fight" Message (Correction):** Appears when the party menu cursor is on a fainted Pokémon.
- **Level Cap:** The level cap with 8 badges is 65.
- **Special NPC Interaction:** Certain puzzles may require walking *through* an NPC rather than interacting with them (e.g., Summer Beach House).
- **Pushing Boulders (Mechanic Corrected):** Pushing a boulder does NOT move the player. The player character remains in the tile from which the push was initiated.
- **PC Tile Anomaly:** The tile for interacting with the Pokémon Center PC is sometimes labeled as `grass` in the map data, despite being indoors.

## C. Puzzle Mechanics
- **Delayed Boulder Barrier Opening:** Some boulder barriers may not open immediately after the corresponding switch is activated. The change might only trigger after moving a certain distance away from the switch/barrier area. (Observed in Victory Road 1F)
- **Immediate Boulder Barrier Opening:** Unlike the puzzle on 1F, the barrier on Victory Road 2F opens immediately upon solving the corresponding boulder puzzle. (Observed in Victory Road 2F)

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

# III. Active Plans & Puzzles
### Victory Road 2F Puzzle
- **Objective:** Push the boulder from (5, 15) to the switch at (2, 17).
- **Plan:** `[{"action": "move", "target": [1, 10]}, {"action": "move", "target": [2, 10]}, {"action": "move", "target": [2, 11]}, {"action": "move", "target": [2, 12]}, {"action": "move", "target": [3, 12]}, {"action": "move", "target": [3, 13]}, {"action": "move", "target": [3, 14]}, {"action": "move", "target": [4, 14]}, {"action": "move", "target": [5, 14]}, {"action": "push", "direction": "Down"}, {"action": "move", "target": [5, 15]}, {"action": "move", "target": [6, 15]}, {"action": "move", "target": [6, 16]}, {"action": "push", "direction": "Left"}, {"action": "move", "target": [5, 16]}, {"action": "push", "direction": "Left"}, {"action": "move", "target": [4, 16]}, {"action": "push", "direction": "Left"}, {"action": "move", "target": [4, 15]}, {"action": "move", "target": [3, 15]}, {"action": "move", "target": [2, 15]}, {"action": "push", "direction": "Down"}]`
- **Current Step:** `{"action": "push", "direction": "Left"}`

# IV. Core Gameplay Lessons
- **Immediate Tool Refinement:** Deferring fixes for critical tools is a major strategic error. Faulty tools must be addressed immediately.
- **Verify Tool Outputs Before Trusting:** A faulty plan is worse than no plan. My tools can have bugs, and I must verify their outputs before blindly following them. This is especially true after correcting a tool's logic.
- **Archived Puzzle Solutions:** Puzzles can reset upon re-entering a map. Archived solutions may be outdated. Always observe the current state of a puzzle before acting.
- **Trust the Game State:** My own assumptions can be wrong. The Game State Information is the absolute source of truth and must be trusted over my memory or intuition.
- **Break Unproductive Loops:** If a strategy fails repeatedly, it's better to change the approach or goal than to persist in an inefficient loop.
- **Confirmation Bias:** I must be wary of trying to prove my own assumptions right. It's important to trust system warnings and evidence that contradicts my beliefs.
- **Efficient Debugging:** When a tool fails, the first step should be to add extensive logging/debugging to understand its internal state. Trial-and-error fixes are inefficient and should be avoided.
- **No Premature Documentation:** Do not document an event or status in the notepad until it has been confirmed by the game state. Recording intentions as facts is a form of hallucination.

# V. Archives

## A. Completed Puzzles
### Victory Road 1F Puzzle
- **Objective:** Push the boulder from (17, 13) to the switch at (18, 14).
- **Status:** Complete.
- **Solution Note:** Activating the switch does not immediately open the barrier at (10, 13). The barrier opens after moving away from the puzzle area.

### Victory Road 3F Puzzle
- **Objective:** Push the boulder from (23, 4) to the switch at (23, 7).
- **Status:** Complete.