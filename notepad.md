# I. Game Mechanics & Traversal

## A. Core Rules
- **Level Cap:** The level cap with 8 badges is 65.
- **"No Will to Fight" Message:** Appears when the party menu cursor is on a fainted Pokémon.
- **HM Usage:** HMs are used from the party menu. Fainted Pokémon can use field moves.
- **PC Interaction:** To use a PC, stand directly below it, face up, and press 'A'.

## B. Boulder Pushing (Corrected)
- **Activation:** Activate Strength from the party menu.
- **Execution:** Face the boulder and press the directional button. The boulder moves one tile, but the player's position does not change.
- **Reset Mechanic:** Leaving and re-entering a floor resets all boulders to their original positions.

## C. Tile Glossary & Movement
- `ground`: Standard walkable tile.
- `grass`: Wild Pokémon encounters.
- `water`: Requires SURF.
- `impassable`: Wall.
- `elevated_ground`: Walkable, different elevation. Movement between `elevated_ground` and lower elevations is only possible via `steps` or `cleared_boulder_barrier` tiles. One-way step-downs from `elevated_ground` are NOT possible.
- `steps`: Allows movement between elevations.
- `boulder_switch`: Floor switch for boulders.
- `boulder_barrier`: Impassable barrier linked to a boulder switch.
- `hole`: Drops to a lower floor. Pushing a boulder into one causes it to appear on the floor below, potentially landing on a switch or creating a new path.
- `spinner`: Forces movement.
- `ladder_up`: Warp tile that leads to a higher floor.
- `ladder_down`: Warp tile that leads to a lower floor.

# II. Battle Intel

## A. Type Effectiveness Chart (Verified)
- **Super Effective (2x):**
  - Psychic > Ghost, Poison
  - Ghost > Psychic
  - Electric > Rock, Water
  - Flying > Grass, Poison, Fighting
  - Ice > Ground, Grass, Flying, Dragon
  - Ground > Poison, Fire, Electric, Rock
  - Rock > Fire, Ice, Flying, Bug
  - Fighting > Normal, Rock, Ice
  - Water > Fire, Ground, Rock
  - Grass > Water, Ground, Rock
  - Bug > Grass, Poison, Psychic
  - Poison > Grass, Bug
- **Not Very Effective (0.5x):**
  - Normal !> Rock
  - Electric !> Grass, Electric, Dragon
  - Rock !> Psychic
  - Psychic !> Psychic
  - Poison !> Poison, Ground, Rock, Ghost
  - Ice !> Water, Ice, Fire
  - Fighting > Poison, Flying, Psychic, Bug
  - Water !> Water, Grass, Dragon
  - Grass !> Fire, Grass, Poison, Flying, Bug, Dragon
- **Immune (0x):**
  - Flying immune to Ground
  - Ground immune to Electric
  - Ghost immune to Normal, Fighting
- **Type Correction (Psychic vs. Rock):** Psychic-type moves deal NEUTRAL (1x) damage to Rock-type Pokémon.

## B. Trainer Rosters
- **Burglar (Victory Road 1F):** FLAREON (Lv53), TENTACRUEL (Lv53), NINETALES (Lv53), DEWGONG (Lv53)

# III. Core Principles & Lessons Learned

## A. Tool Development & Logic Validation
- **Trust the Game Engine:** The game engine is the ultimate source of truth. My pathfinder's logic, which allowed for a one-way step-down from `elevated_ground`, was proven wrong when the game engine blocked the move at Victory Road 3F (10, 3). If a tool's output contradicts the engine's behavior, the tool's logic is flawed and must be corrected immediately. My previous 'lesson' about trusting computational evidence was based on a faulty premise.

## B. Surfing Mechanic
- Not all `ground` tiles adjacent to `water` are valid starting points for using Surf. The game engine can block movement even if the pathfinder's logic deems it valid. Example: Cannot initiate Surf from (15, 26) in Viridian City.

# IV. Puzzle Solutions & Hypotheses

## Victory Road 1F - Resetting Barrier
- **Observation:** The boulder barrier at (10, 13) reset itself after I left and re-entered the floor.
- **Hypothesis:** This barrier might reset every time I leave and re-enter Victory Road 1F. This needs to be tested to understand the puzzle mechanics of this area fully.

## Victory Road 2F - Western Trap
- **Puzzle:** A barrier at (8, 9) and (8, 10) blocks eastward progress.
- **Failed Hypothesis:** Pushing the western boulder at (4, 16) to the switch at (2, 17) would immediately open the barrier. This was proven false.
- **Solution:** The puzzle requires a two-step "prime and trigger" mechanic. Pushing the boulder onto the switch at (2, 17) primes the trap. Leaving the floor and re-entering triggers the event, opening the barrier.

## Victory Road 3F - Central Boulder
- **Puzzle:** A boulder at (14, 13) blocks a hole at (14, 15).
- **Solution:** Push the boulder south two times into the hole. This causes a change on the floor below (Victory Road 2F).

## Victory Road 3F - Northern Boulder
- **Puzzle:** A boulder at (23, 4) blocks the path to a switch at (23, 7).
- **Solution:** Push the boulder south three times onto the switch. This opens the boulder barrier at (8, 11).