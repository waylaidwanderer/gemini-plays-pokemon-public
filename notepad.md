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
- **Pushing Boulders (Mechanic Corrected... Again):** Pushing a boulder moves the boulder one tile AND also moves the player into the boulder's now-vacant tile.

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

# III. Current Objective: Victory Road & The Pokémon League
**Primary Goal:** Defeat the Elite Four and become the Pokémon League Champion.
**Secondary Goal:** Solve the Victory Road boulder puzzles to reach the exit.

# IV. Core Gameplay Lessons
- **Plan Boulder Routes First:** Before pushing any boulder, use the pathfinder to verify the *entire* planned route for both the player and the boulder. This will prevent soft-locking the puzzle by revealing impassable tiles or dead ends early.
- **Immediate Tool Refinement:** Deferring fixes for critical tools is a major strategic error. Faulty tools must be addressed immediately.
- **Verify Tool Outputs Before Trusting:** A faulty plan is worse than no plan. My tools can have bugs, and I must verify their outputs before blindly following them.
- **Trust the Game State:** My own assumptions can be wrong. The Game State Information is the absolute source of truth and must be trusted over my memory or intuition.
- **Confirmation Bias:** I must be wary of trying to prove my own assumptions right. It's important to trust system warnings and evidence that contradicts my beliefs.
- **Efficient Debugging:** When a tool fails, the first step should be to add extensive logging/debugging to understand its internal state. Trial-and-error fixes are inefficient.

# V. Archives

## A. Completed Puzzles
### Victory Road 2F Puzzle
- **Status:** Complete. Boulder from (4, 16) to switch at (2, 17).

### Victory Road 3F Puzzle
- **Status:** Complete. Secret ladder at (3, 1) was the true path.

# VI. Victory Road 1F Boulder Puzzle Plan
- **Objective:** Move the boulder at (17, 15) onto the switch at (18, 14).
- **Step 1:** Navigate to tile (17, 16).
- **Step 2:** Push the boulder at (17, 15) NORTH to (17, 14).
- **Step 3:** Navigate to tile (18, 13).
- **Step 4:** Push the boulder at (17, 14) EAST to (18, 14), activating the switch.