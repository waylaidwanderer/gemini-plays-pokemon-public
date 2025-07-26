# I. Game Mechanics & World Rules

## A. Tile Mechanics & Traversal
- **Ground:** Standard walkable tile.
- **Grass:** Walkable tile where wild Pokémon can be encountered.
- **Water:** Can be crossed using the SURF HM.
- **Impassable:** Walls, trees, and other objects that block movement.
- **Elevated Ground:** Walkable ground at a different elevation.
- **Gate (`gate_offscreen`, `closed_gate`, `open_gate`):** Barriers that may open or close.
- **Boulder Switch:** A traversable floor switch activated by a boulder.
- **Boulder Barrier:** An impassable barrier that becomes a `cleared_boulder_barrier` tile when the corresponding switch is activated.
- **Cleared Boulder Barrier:** A traversable ground tile that appears after a boulder puzzle is solved.
- **Steps:** Allows two-way vertical movement between `ground` and `elevated_ground` tiles.
- **Ladders (`ladder_up`, `ladder_down`):** Function as instant 1x1 warps between floors.
- **Hole:** A tile that functions as a warp, dropping the player to a lower floor.
- **Spinner (`spinner_`...):** Forces movement in the specified direction.
- **Boulder Pushing Mechanic (FINAL CORRECTION):** After activating Strength, stand adjacent to a boulder and face it. Pressing the directional button towards the boulder pushes it one tile. The player character **remains in their original position** and does NOT move into the boulder's previous space.
- **Elevation Traversal (Correction):** Movement between 'elevated_ground' and 'ground' is ONLY possible via 'steps' tiles. It is not possible to 'step down' from a ledge-like edge of an elevated area.

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

### Cool Trainer M (Victory Road 3F) - DEFEATED
- **Location:** (29, 6)
- **Team:** CHARIZARD (Lv52), MAGNETON (Lv52), TENTACRUEL (Lv52)

### Cool Trainer F (Victory Road 3F) - DEFEATED
- **Location:** (14, 4)
- **Team:** WIGGLYTUFF (Lv54), CLEFABLE (Lv54), CHANSEY (Lv54), EEVEE (Lv57)

# III. Core Gameplay Lessons & Reflections

- **Core Principle: Fix, Don't Defer.** Critical tools with known bugs MUST be fixed immediately. Deferring fixes is a strategic failure.
- **Core Principle: Address critiques immediately.** When a tool is identified as faulty by an external check (like the overwatch system), fixing it becomes the absolute highest priority.
- **Core Principle: Verify, Then Trust.** Tool outputs and personal assumptions are hypotheses, not facts. They must be verified against the game state before being trusted.
- **Core Principle: Agent vs. Tool.** Agents are for reasoning and planning. Tools are for computation and data processing. A task that can be solved with code MUST be a tool, not an agent.
- **Core Principle: Verify Reachability.** Before forming a complex navigation plan, use the pathfinder to verify that key points are actually reachable to avoid building strategies on flawed assumptions.

# IV. Current Plans & Hypotheses

## Victory Road 1F Puzzle Strategy
**Current State:** Stuck. All direct attempts to solve the puzzle have failed. My custom solver tool was flawed.
**New Plan:**
1.  **Strategic Reset:** Exit Victory Road 1F to Route 23 and re-enter. This will reset all boulders to their starting positions.
2.  **Re-evaluate with New Hypotheses:** Approach the reset puzzle with the following fresh hypotheses, to be tested one by one:
    *   **Hypothesis A (Deactivation):** The boulder on the switch at (3, 10) must be *removed* first. This might reconfigure the puzzle, possibly opening a new path for another boulder.
    *   **Hypothesis B (Verticality):** The boulder at (15, 3) on the elevated platform needs to be pushed off a ledge or through a hidden hole to the ground floor.
    *   **Hypothesis C (Red Herring):** The boulder barrier at (10, 13) is a distraction. The real solution involves activating the switch at (18, 14) to open a different, hidden path.

# V. Tool Development Backlog

- **`boulder_puzzle_solver` (CRITICAL PRIORITY):** Current implementation is a non-functional placeholder that has been reverted multiple times. Manual solving is a temporary workaround. A robust, generalized, algorithm-based solver that can parse map data is required to prevent future roadblocks. This is the #1 development priority after clearing the current Victory Road 1F puzzle.