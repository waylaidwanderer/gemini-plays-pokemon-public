# I. Game Mechanics & Traversal

## A. Core Rules
- **Level Cap:** The level cap with 8 badges is 65.
- **"No Will to Fight" Message:** Appears when the party menu cursor is on a fainted Pokémon.
- **HM Usage:** HMs are used from the party menu. Fainted Pokémon can use field moves.
- **PC Interaction:** To use a PC, stand directly below it, face up, and press 'A'.

## B. Boulder Pushing
- **Activation:** Activate Strength from the party menu.
- **Execution:** Face the boulder and press the directional button. The player does not move.
- **Reset Mechanic:** Leaving and re-entering a floor resets all boulders to their original positions. This is a core mechanic for solving boulder puzzles and escaping self-inflicted traps.

## C. Tile Glossary & Movement
- `ground`: Standard walkable tile.
- `grass`: Wild Pokémon encounters.
- `water`: Requires SURF.
- `impassable`: Wall.
- `elevated_ground`: Walkable, different elevation.
- `steps`: Allows movement between elevations.
- `cleared_boulder_barrier`: Walkable, acts as a ramp between elevations.
- `boulder_switch`: Floor switch for boulders.
- `boulder_barrier`: Impassable barrier linked to a boulder switch. Tested and confirmed impassable at (10, 13).
- `hole`: Drops to a lower floor.
- `spinner`: Forces movement.
- `ladder_up`: Warp tile that leads to a higher floor.

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

# III. Puzzle Solutions & Learnings

## A. Victory Road 1F Puzzle - In Progress
- **Current Status:** Attempting to solve the boulder puzzles. Previous hypotheses about a 'one-way step-down' mechanic were based on a faulty debugger and have been disproven by in-game testing. The path forward remains unclear, but I am now operating with corrected tools and a more rigorous, evidence-based approach.

# V. Core Principles & Lessons Learned

## A. LLM Operational Integrity
- **Immediate Action Mandate:** As an LLM, my thinking is turn-based. Deferring tasks like tool creation or data management to a 'later' turn is a critical failure. All such tasks MUST be executed in the immediate turn they are identified. My failure to implement the `boulder_puzzle_solver` immediately was a major strategic error that wasted significant time on futile manual hypotheses.

## D. Surfing Mechanic (New Discovery)
- Not all `ground` tiles adjacent to `water` are valid starting points for using Surf. The game engine can block movement even if the pathfinder's logic deems it valid. Example: Cannot initiate Surf from (15, 26) to (14, 26) in Viridian City.