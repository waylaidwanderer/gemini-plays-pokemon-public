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
- `elevated_ground`: Walkable, different elevation. It is possible to step down from an `elevated_ground` tile to any adjacent walkable tile of a lower elevation (e.g., `ground`, `cleared_boulder_barrier`). This is a one-way action.
- `steps`: Allows movement between elevations.
- `cleared_boulder_barrier`: Walkable, acts as a ramp between elevations.
- `boulder_switch`: Floor switch for boulders.
- `boulder_barrier`: Impassable barrier linked to a boulder switch.
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

# III. Core Principles & Lessons Learned

## A. LLM Operational Integrity
- **Immediate Action Mandate:** My failure to implement the `boulder_puzzle_solver` immediately was a major strategic error that wasted significant time. Deferring critical tool creation is a critical failure.
- **Trust Computational Evidence:** I must trust the outputs of my computational tools (like the pathfinder) over my own flawed manual verification, especially when faced with a paradox. My refusal to accept the debugger's finding cost me dozens of turns. The Victory Road 1F puzzle was a key example: I was trapped in a soft-lock because my verified traversal rules were incorrect. The game insisted a path existed, while my tools, based on my flawed rules, said I was trapped. The `pathfinder_debugger` tool, when configured with a hypothetical 'one-way step-down' mechanic, successfully found a path, providing computational proof that this mechanic was intended and my manual verification was flawed.

## B. Surfing Mechanic
- Not all `ground` tiles adjacent to `water` are valid starting points for using Surf. The game engine can block movement even if the pathfinder's logic deems it valid. Example: Cannot initiate Surf from (15, 26) to (14, 26) in Viridian City.
- **Process Failure:** I failed to use the `pathfinding_logic_validator_agent` to analyze the pathfinding paradox, instead relying solely on the debugger. This was a procedural error. I must prioritize using newly created tools to test their effectiveness and refine my processes.