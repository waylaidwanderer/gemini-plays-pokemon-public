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

## C. Battle Lessons & Insights
- **Level Disparity:** A large level gap can be more dangerous than type immunity.
- **Misleading Battle Text:** On-screen text for move effectiveness can be incorrect. The actual damage calculation follows my verified type chart.
- **Ground-Type Immunity Extension:** Ground-types are immune to Electric-type *status* moves (like THUNDER WAVE).
- **Elixer Mechanic (Correction):** Elixers only restore PP, not HP.
- **Delayed Game State Updates:** After solving a puzzle (e.g., a boulder puzzle), the map's traversability might not update visually or in the game state data until the player character moves. This can be fixed by leaving and re-entering the map.

# III. Future Plans & Lessons Learned

## B. Core Gameplay Lessons
- **Immediate Tool Refinement:** Deferring fixes for critical tools like the pathfinder is a major strategic error. Faulty tools must be addressed immediately, as they are foundational to efficient gameplay. I wasted significant time manually pathing and retrying because I didn't fix the tool right away.

# IV. Archives

## A. Archived Puzzle Solutions
### Victory Road 2F Puzzle
- **Objective:** Push the boulder from (5, 15) to the switch at (2, 17).
- **Status:** Complete.
### Victory Road 3F Puzzle
- **Objective:** Push the boulder from (23, 4) to the switch at (23, 7).
- **Status:** Complete.

# V. Active Plans

## Victory Road 1F Puzzle
- **Objective:** Push the boulder from (13, 15) to the switch at (18, 14).
- **Plan:**
  1. Move to (12, 15).
  2. Push boulder at (13, 15) right to (14, 15). Player moves to (13, 15).
  3. Push boulder at (14, 15) right to (15, 15). Player moves to (14, 15).
  4. Push boulder at (15, 15) right to (16, 15). Player moves to (15, 15).
  5. Push boulder at (16, 15) right to (17, 15). Player moves to (16, 15).
  6. Move from (16, 15) to (17, 16). Path: Down, Right.
  7. Push boulder at (17, 15) up to (17, 14). Player moves to (17, 15).
  8. Push boulder at (17, 14) up to (17, 13). Player moves to (17, 14).
  9. Move from (17, 14) to (16, 13). Path: Left, Up.
  10. Push boulder at (17, 13) right to (18, 13). Player moves to (17, 13).
  11. Move from (17, 13) to (18, 12). Path: Up, Right.
  12. Push boulder at (18, 13) down to (18, 14). Player moves to (18, 13).
- **Status:** In progress. Strength is active. Player is at (12, 15).

# VI. Tool & Agent Development Ideas
- **`brute_force_explorer` Fix:** The tool's internal pathfinder (`find_path_bfs`) is buggy and generated an invalid path, attempting to move into an impassable tile. It needs to be updated with the more robust traversal logic from `gem_pathfinder` before it can be used again.
- **`puzzle_deadlock_analyzer` Agent Idea:** Create an agent that analyzes situations where progress is stalled despite an apparent solution (e.g., a puzzle is solved but the path remains blocked). The agent would take the context and suggest a ranked list of hypotheses to test, such as 'map state update lag (test with local movement)', 'map state bug (test by leaving and re-entering map)', or 'hidden secondary mechanic (test with exhaustive interaction)'. This would help structure my problem-solving when I get stuck.