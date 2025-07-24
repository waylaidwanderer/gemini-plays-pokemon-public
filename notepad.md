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
- **Boulder Puzzle Mechanics:** Boulders cannot be pushed directly into standard `water` tiles. They must be pushed into `hole` tiles to affect lower floors.
- **Pushing Boulders (Movement Anomaly):** Pushing a boulder does not always move the player character into the boulder's previous position. The player's position must be verified after every push.
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

# III. Active Plans & Puzzles

## Victory Road 1F Puzzle (Resetting)
- **Objective:** Push the boulder from (6, 16) to the switch at (18, 14).
- **Status:** Resetting puzzle after soft-lock. Must follow solver plan precisely.
- **Solver's Plan (Full Sequence):**
  1. Move to (6, 15), push boulder Down to (6, 17).
  2. Move to (5, 17), push boulder Right to (7, 17).
  3. Move to (6, 17), push boulder Right to (8, 17).
  4. Move to (9, 18), then to (8, 18), push boulder Up to (8, 16).
  5. Move to (8, 16), then to (7, 16), push boulder Right to (9, 16).
  6. Move to (10, 17), then to (9, 17), push boulder Up to (9, 15).
  7. Move to (10, 15), push boulder Right to (11, 15).
  8. Move to (11, 15), push boulder Right to (12, 15).
  9. Move to (12, 15), push boulder Right to (13, 15).
  10. Move to (13, 15), push boulder Right to (14, 15).
  11. Move to (14, 15), push boulder Right to (15, 15).
  12. Move to (15, 15), push boulder Right to (16, 15).
  13. Move to (17, 16), push boulder Up to (17, 15).
  14. Move to (17, 15), push boulder Up to (17, 14).
  15. Move to (16, 13), push boulder Right to (17, 13).
  16. Move to (18, 12), push boulder Down to (18, 13).

# IV. Core Gameplay Lessons
- **Immediate Tool Refinement:** Deferring fixes for critical tools like the pathfinder is a major strategic error. Faulty tools must be addressed immediately.
- **Trust Tool Outputs:** Deviating from a valid, tool-generated plan can lead to soft-locks and wasted time. I must trust my solver's output and follow its steps precisely.
- **Archived Puzzle Solutions:** Puzzles can reset upon re-entering a map. Archived solutions may be outdated. Always observe the current state of a puzzle before acting.

# V. Archives

## A. Archived Puzzle Solutions
### Victory Road 1F Puzzle (Initial)
- **Objective:** Push the boulder from (13, 15) to the switch at (18, 14).
- **Status:** Complete. (Reset upon map re-entry)
### Victory Road 2F Puzzle
- **Objective:** Push the boulder from (5, 15) to the switch at (2, 17).
- **Status:** Complete.
### Victory Road 3F Puzzle
- **Objective:** Push the boulder from (23, 4) to the switch at (23, 7).
- **Status:** Complete.