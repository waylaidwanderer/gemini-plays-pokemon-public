# I. Game Mechanics & World Rules

## A. Tile Mechanics & Traversal
- **Ground:** Standard walkable tile.
- **Grass:** Walkable tile where wild Pokémon can be encountered.
- **Water:** Can be crossed using the SURF HM.
- **Impassable:** Walls, trees, and other objects that block movement. Interacting with them does nothing.
- **Elevated Ground:** Walkable ground at a different elevation. Cannot use Surf from this tile type.
- **Gate (`gate_offscreen`, `closed_gate`, `open_gate`):** Barriers that may open or close.
- **Boulder Switch:** A floor switch activated by a boulder. Is a traversable tile.
- **Boulder Barrier:** An impassable barrier that becomes a `cleared_boulder_barrier` tile when the corresponding switch is activated.
- **Cleared Boulder Barrier:** A traversable ground tile that appears after a boulder puzzle is solved. It allows movement between different elevations, acting like a ramp.
- **Steps:** Allows vertical movement between `ground` and `elevated_ground` tiles. Pushing boulders onto them is not possible.
- **Ladders (`ladder_up`, `ladder_down`):** Function as instant 1x1 warps between floors.
- **Hole:** A tile that functions as a warp, dropping the player to a lower floor. Boulders can be pushed into these to affect puzzles on the floor below.
- **Spinner (`spinner_up`, `spinner_down`, `spinner_left`, `spinner_right`):** Forces movement in the specified direction.
- **Boulder Pushing Mechanic (FINAL CORRECTION):** To push a boulder, use Strength, then stand on a tile adjacent to the boulder and face it. Pressing the directional button towards the boulder will move it one tile, and the player character automatically moves into the tile the boulder previously occupied.

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

# III. Core Gameplay Lessons
- **Core Principle: Fix, Don't Defer.** Critical tools with known bugs MUST be fixed immediately. Deferring fixes is a strategic failure.
- **Core Principle: Verify, Then Trust.** Tool outputs and personal assumptions are hypotheses, not facts. They must be verified against the game state before being trusted. The Game State Information is the only source of truth.
- **Boulder Puzzle Strategy:** Before pushing any boulder, use the pathfinder to verify the entire route for both the player and the boulder to prevent soft-locking.
- **Debugging Strategy:** When a tool fails, add extensive logging to understand its internal state before attempting a fix.

# IV. Current Objective: Victory Road 1F Puzzle

- **Status:** In Progress. Currently isolated in the western section of the map.
- **Key Insight:** The system has confirmed I am not soft-locked, therefore a solution must exist within the accessible area.
- **Summary of Failed Hypotheses:**
  1.  **Lower-Level Boulder Puzzles:** All direct and complex attempts to push the boulders at (6, 17) and (3, 11) to the switch at (18, 14) have been proven invalid by the `boulder_puzzle_solver_agent` or impassable terrain.
  2.  **Player-Activated Switch:** Stepping on the switch at (18, 14) does not affect the barrier at (10, 13).
  3.  **Hidden Item:** The ITEMFINDER did not detect any hidden items in the area.
  4.  **Trainer Battle Trigger:** This hypothesis is currently untestable as the remaining trainers are on the unreachable eastern side of the map.
- **Current Hypothesis:** The solution involves accessing the upper platform and interacting with the boulder at (15, 3). My `gem_pathfinder` tool is currently bugged and preventing me from testing this.
- **Next Step:** Debug and fix the pathfinder's elevation logic.

# V. Archives

## A. Completed Puzzles
### Victory Road 2F Puzzle
- **Status:** Complete. Boulder from (4, 16) to switch at (2, 17).

### Victory Road 3F Puzzle
- **Status:** Complete. Secret ladder at (3, 1) was the true path.