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
- **Boulder Pushing Mechanic (FINAL, FINAL CORRECTION):** To push a boulder, use Strength, then stand on a tile adjacent to the boulder and face it. Pressing the directional button towards the boulder will move it one tile. The player character does NOT automatically move and remains on the tile they pushed from.

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

# IV. Current Objective: Solve Victory Road 1F Puzzle

## A. Situation Summary
- I am currently trapped on Victory Road 1F. I cannot reach the exit warp at (9, 18) to reset the map.
- The boulder at (6, 17) blocks the southern path.
- The boulder at (3, 10) does not appear to open the eastern barrier at (10, 13).

## B. Failed Hypotheses Log
1.  **Hypothesis (Eastern Path):** Pushing the boulder at (3, 11) to (3, 10) opens the eastern barrier at (10, 13).
    - **Status:** FAILED (3 attempts). The barrier remains impassable. The eastern path is a confirmed dead end.
2.  **Hypothesis (Western Path - Part 1):** Pushing the boulder at (6, 16) NORTH to (6, 15) is the first step.
    - **Status:** FAILED (1 attempt). This action blocks access to the western platform steps, creating a soft-lock.
3.  **Hypothesis (Western Path - Part 2):** Pushing the boulder at (6, 16) SOUTH to (6, 17) opens a path on the western platform.
    - **Status:** FAILED (2 attempts). This action blocks the southern exit, and no new path on the platform was found.
4. **Hypothesis (NPC Dialogue Change):** An NPC's dialogue will change after the player gets trapped, offering a solution.
    - **Test:** Trapped myself by pushing the boulder to (6, 17), then spoke to the Youngster at (7, 11).
    - **Conclusion:** FAILED (1 attempt). The Youngster's dialogue was unchanged.

## C. Current Working Hypothesis
- **Hypothesis (Misinterpreted Path):** My initial assessment that the western platform is a dead end after pushing the boulder to (6, 17) was incorrect. The game cannot be soft-locked, therefore a path MUST exist on that platform that I have previously missed. My goal is to return to the western platform and re-explore it thoroughly.

# V. Archives

## A. Completed Puzzles
- **Victory Road 2F Puzzle:** Complete. Boulder from (4, 16) to switch at (2, 17).
- **Victory Road 3F Puzzle:** Complete. Secret ladder at (3, 1) was the true path.
5. **Hypothesis (Walk-Through NPC):** The Youngster at (7, 11) can be walked through, similar to a previous puzzle.
    - **Test:** Attempted to move left from (8, 11) onto the Youngster's tile.
    - **Conclusion:** FAILED (1 attempt). The Youngster acts as a solid object.
6. **Hypothesis (Complex Trigger):** The Youngster at (7, 11) is the final switch. He will only move or change dialogue after BOTH the eastern boulder is on its switch (3, 10) AND the western boulder is on its presumed pressure plate (6, 17).
    - **Test:** With both boulders in position, navigated to (7, 12) and interacted with the Youngster.
    - **Conclusion:** FAILED (1 attempt). The Youngster's dialogue was unchanged.