# I. Game Mechanics & World Rules

## A. Tile Mechanics & Traversal
- **Ground:** Standard walkable tile.
- **Grass:** Walkable tile where wild Pokémon can be encountered.
- **Water:** Can be crossed using the SURF HM.
- **Impassable:** Walls, trees, and other objects that block movement. Interacting with them does nothing.
- **Elevated Ground:** Walkable ground at a different elevation. Cannot use Surf from this tile type.
- **Gate (`gate_offscreen`, `closed_gate`, `open_gate`):** Barriers that may open or close.
- **Boulder Switch:** A traversable floor switch activated by a boulder.
- **Boulder Barrier:** An impassable barrier that becomes a `cleared_boulder_barrier` tile when the corresponding switch is activated.
- **Cleared Boulder Barrier:** A traversable ground tile that appears after a boulder puzzle is solved. It allows movement between different elevations, acting like a ramp.
- **Steps:** Allows two-way vertical movement between `ground` and `elevated_ground` tiles. Pushing boulders onto them is not possible.
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
- **Core Principle: Fix, Don't Defer.** Critical tools with known bugs MUST be fixed immediately. Deferring fixes is a strategic failure. Repeatedly submitting identical, broken code is a critical error.
- **Core Principle: Address critiques immediately.** When a tool is identified as faulty by an external check (like the overwatch system), fixing it becomes the absolute highest priority. Do not defer or make repeated, identical failed attempts.
- **Core Principle: Verify, Then Trust.** Tool outputs and personal assumptions are hypotheses, not facts. They must be verified against the game state before being trusted. The Game State Information is the only source of truth.
- **Core Principle: Agent vs. Tool.** Agents are for reasoning and planning. Tools are for computation and data processing. A task that can be solved with code (like simulating a puzzle) MUST be a tool, not an agent.
- **Core Principle: Verify Reachability.** Before forming a complex navigation plan, use the pathfinder to verify that key points (like ladders, stairs, or puzzle elements) are actually reachable from the current position to avoid building strategies on flawed assumptions.
- **Boulder Puzzle Strategy:** Before pushing any boulder, use the pathfinder to verify the entire route for both the player and the boulder to prevent soft-locking.
- **Debugging Strategy:** When a tool fails, add extensive logging to understand its internal state before attempting a fix. Or, manually test the game mechanics to gather ground-truth data.
- **Victory Road 1F Western Platform:** Confirmed to be a dead-end trap. The puzzle involving pushing the boulder at (6,17) only serves to let you escape the area, not to progress.

# IV. Archives

## A. Completed Puzzles
### Victory Road 1F Puzzle (Western Trap)
- **Status:** Escaped. Pushed boulder at (6,17) to (8,17) to access southern exit.

### Victory Road 2F Puzzle
- **Status:** Complete. Boulder from (4, 16) to switch at (2, 17).

### Victory Road 3F Puzzle
- **Status:** Complete. Secret ladder at (3, 1) was the true path.

# V. Current Puzzle: Victory Road 1F (Eastern Section)

**Hypothesis:** The eastern boulder puzzle is the correct path forward.

**Test Plan:**
1. Re-enter Victory Road 1F from the main entrance at (9, 18).
2. Navigate to the eastern boulder at (15, 3).
3. Push the boulder onto the switch at (18, 14).
4. Navigate to (9, 13) to check if the barrier at (10, 13) is open.
5. If open, proceed to the main ladder at (2, 2).