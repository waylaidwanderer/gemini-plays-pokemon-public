- **Elevated Ground:** Walkable ground at a different elevation. Cannot use Surf from this tile type.
- **Gate (`gate_offscreen`, `closed_gate`, `open_gate`):** Barriers that may open or close.
- **Boulder Switch:** A floor switch activated by a boulder. Is a traversable tile.
- **Boulder Barrier:** An impassable barrier that becomes a `cleared_boulder_barrier` tile when the corresponding switch is activated.
- **Cleared Boulder Barrier (Corrected):** Functions as a one-way ramp. It can only be entered from a `steps` tile when moving from `ground` to `elevated_ground`. It is impassable from adjacent `ground` tiles and cannot be used to move down from `elevated_ground` to `ground`.

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

## B. Current Trainer Rosters & Movesets

### Cool Trainer M (Victory Road 3F)
- **Location:** (29, 6)
- **Team:** CHARIZARD (Lv52), MAGNETON (Lv52)

## C. Battle Lessons & Insights
- **Level Disparity:** A large level gap can be more dangerous than type immunity.
- **Misleading Battle Text:** On-screen text for move effectiveness can be incorrect. The actual damage calculation follows my verified type chart.
- **Ground-Type Immunity Extension:** Ground-types are immune to Electric-type *status* moves (like THUNDER WAVE).
- **Elixer Mechanic (Correction):** Elixers only restore PP, not HP.

# III. World Navigation & Puzzles

## A. Current Strategy: Victory Road 1F Puzzle
- **Conclusion (Southern Area):** The southern puzzle area is a confirmed, inescapable dead end. Persisting is illogical.
- **Objective:** Push the boulder from its current position to the switch at (18, 14). This will clear the boulder barrier at (10, 13) and open the path to the next floor.
- **Method:** I must reactivate Strength from the party menu before every individual push.
- **Solver Plan:**
  1. Push boulder at (10, 15) right to (11, 15). **(Complete)**
  2. Push boulder at (11, 15) right to (12, 15). **(Complete)**
  3. Push boulder at (12, 15) right to (13, 15). **(Complete)**
  4. Push boulder at (13, 15) right to (14, 15). **(Complete)**
  5. Push boulder at (14, 15) right to (15, 15). **(Complete)**
  6. Push boulder at (15, 15) right to (16, 15). **(Complete)**
  7. Push boulder at (16, 15) right to (17, 15). **(Complete)**
  8. Move to (17, 16). **(Complete)**
  9. Push boulder at (17, 15) up to (17, 14). **(Complete)**
  10. Push boulder at (17, 14) up to (17, 13). **(Complete)**
  11. Move to (16, 13). **(Complete)**
  12. Push boulder at (17, 13) right to (18, 13). **(Complete)**
  13. Move to (18, 12). **(Complete)**
  14. Push boulder at (18, 13) down to (18, 14). **(Complete)**

# IV. Agent & Tool Development

## A. Future Development Ideas
- **Puzzle Executor Agent:** Create an agent to take a `boulder_puzzle_solver` solution and generate the full sequence of button presses to execute it automatically, including menuing to reactivate Strength. This would automate tedious, repetitive puzzle-solving.
- **Pokedex Analysis (Review):** Review `team_composition_advisor_agent` capabilities before creating a new Pokedex agent to avoid redundancy.

## B. Development Backlog
*No outstanding bugs. All tools are currently functional.*