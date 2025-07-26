# I. Core Knowledge Base

## A. Game Mechanics & Traversal
- **Boulder Pushing:** Activate Strength, face the boulder, and press the directional button. The player does not move.
- **Elevation Change:** Only possible on `steps` or `cleared_boulder_barrier` tiles.
- **Defeated Trainers:** Often become impassable objects.
- **Special NPC Interaction:** Some puzzles require walking *through* an NPC.
- **"No Will to Fight" Message:** Cursor is on a fainted Pokémon in the party menu.

## B. Tile Glossary
- **`ground`**: Standard walkable tile.
- **`grass`**: Wild Pokémon encounters.
- **`water`**: Requires SURF.
- **`impassable`**: Wall.
- **`elevated_ground`**: Walkable, different elevation.
- **`steps`**: Allows movement between elevations.
- **`boulder_switch`**: Floor switch for boulders.
- **`boulder_barrier`**: Impassable until switch is activated.
- **`cleared_boulder_barrier`**: Walkable, acts as a ramp.
- **`hole`**: Drops to a lower floor.
- **`spinner`**: Forces movement.

## B. General Rules & Heuristics
- **PC Interaction:** To use a PC, stand directly below it, face up, and press 'A'.
- **HM Usage:** HMs are used from the party menu. Fainted Pokémon can use field moves.
- **"No Will to Fight" Message (Correction):** Appears when the party menu cursor is on a fainted Pokémon.
- **Level Cap:** The level cap with 8 badges is 65.
- **Special NPC Interaction:** Certain puzzles may require walking *through* an NPC rather than interacting with them (e.g., Summer Beach House, Rock Tunnel Super Nerd).

# II. Battle Intel

## A. Type Effectiveness Chart (Verified)
- **Super Effective (2x):** Psychic > Ghost, Poison; Ghost > Psychic; Electric > Rock, Water; Flying > Grass, Poison, Fighting; Ice > Ground, Grass, Flying, Dragon; Ground > Poison, Fire, Electric, Rock; Rock > Fire, Ice, Flying, Bug; Fighting > Normal, Rock, Ice; Water > Fire, Ground, Rock; Grass > Water, Ground, Rock; Bug > Grass, Poison, Psychic; Poison > Grass, Bug.
- **Not Very Effective (0.5x):** Normal !> Rock; Electric !> Grass, Electric, Dragon; Rock !> Psychic; Psychic !> Psychic; Poison !> Poison, Ground, Rock, Ghost; Ice !> Water, Ice, Fire; Fighting > Poison, Flying, Psychic, Bug; Water !> Water, Grass, Dragon; Grass !> Fire, Grass, Poison, Flying, Bug, Dragon.
- **Immune (0x):** Flying immune to Ground; Ground immune to Electric; Ghost immune to Normal, Fighting.
- **Type Correction (Psychic vs. Rock):** Psychic-type moves deal NEUTRAL (1x) damage to Rock-type Pokémon, not 'not very effective' as previously assumed.

## B. Known Trainer Rosters & Movesets

### Victory Road

#### Victory Road 1F
*(No trainers defeated yet)*

#### Victory Road 2F
*(No trainers defeated yet)*

#### Victory Road 3F
- **Cool Trainer M (DEFEATED)**
  - **Location:** (29, 6)
  - **Team:** CHARIZARD (Lv52), MAGNETON (Lv52), TENTACRUEL (Lv52)
- **Cool Trainer F (DEFEATED)**
  - **Location:** (14, 4)
  - **Team:** WIGGLYTUFF (Lv54), CLEFABLE (Lv54), CHANSEY (Lv54), EEVEE (Lv57)

# III. Core Gameplay Lessons & Reflections

- **Core Principle: Fix, Don't Defer.** Critical tools with known bugs MUST be fixed immediately. Deferring fixes is a strategic failure.
- **Core Principle: Address critiques immediately.** When a tool is identified as faulty by an external check (like the overwatch system), fixing it becomes the absolute highest priority.
- **Core Principle: Verify, Then Trust.** Tool outputs and personal assumptions are hypotheses, not facts. They must be verified against the game state before being trusted.
- **Core principle: Agent vs. Tool.** Agents are for reasoning and planning. Tools are for computation and data processing. A task that can be solved with code MUST be a tool, not an agent.
- **Core Principle: Verify Reachability.** Before forming a complex navigation plan, use the pathfinder to verify that key points are actually reachable to avoid building strategies on flawed assumptions.

# IV. Tool Development Notes
- **`boulder_puzzle_solver`:** Current version is only for single-boulder puzzles. A future version needs to handle multi-boulder, multi-stage puzzles like the one on Victory Road 1F.
- **`gem_pathfinder`:** The cost calculation for pathing should be improved to account for the extra actions required for HMs like Surf, making land routes more preferable when efficient.

## E. Current Puzzles & Hypotheses
### Victory Road 1F Boulder Puzzle
- **Hypothesis 1 (Failed - 14 attempts):** Push the eastern boulder at (6, 17) to the switch at (18, 14). The `boulder_puzzle_solver` tool failed repeatedly (JSON error, NameError, Timeout) and is unreliable for this puzzle. The switch is confirmed to be unreachable from my current position. Abandoning automated solving.
- **Hypothesis 2 (Active):** The western switch at (3, 10) must be activated first. The immediate goal is to solve this puzzle by pushing the boulder at (3, 11) onto the switch.

## F. Agent Ideas
- **Puzzle Hypothesis Tester:** An agent that takes hypotheses from the generator and uses tools like `boulder_puzzle_solver` to programmatically test them.