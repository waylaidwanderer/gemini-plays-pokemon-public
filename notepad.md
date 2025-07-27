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
- **Elevation Change (CRITICAL & VERIFIED):** Movement between elevations REQUIRES a `steps` or `cleared_boulder_barrier` tile. The hypothesis of a one-way step-down from `elevated_ground` to `ground` has been repeatedly tested and proven FALSE by the game engine.

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

## A. Victory Road 1F Puzzle - Key Learnings & Failed Hypotheses
- **Core Insight (Confirmation Bias):** My initial hypotheses (H1-H8) were crippled by confirmation bias, assuming switches *must* be activated. Future puzzle-solving must consider deliberately *not* activating switches or using objects in unconventional ways.
- **Failed Hypothesis Log:**
  - Activating BOTH switches (H1) or ONLY the WEST switch (H3) does not open the barrier at (10,13).
  - Stepping on the eastern switch at (18,14) does not open the barrier (H8, which was based on a hallucinated boulder).
  - The western boulder at (3,10) cannot be pushed OFF its switch to (3,11) (H2, confirmed by solver).
  - Defeated trainers (Youngster at 7,11) are impassable and do not move when switches are activated (H6, H7).
  - There are no hidden switches or passages on the western platform (H5).

# IV. Radical Hypothesis Log (Victory Road 1F)

## A. One-Way Step-Down Mechanic (FAILED)
- **Observation:** All verified tools (`gem_pathfinder`, `boulder_puzzle_solver`) confirmed I was in a soft-locked, inescapable position on the western platform of Victory Road 1F. This violates core game principles.
- **Paradox:** The `pathfinder_debugger`, when operating with what I previously identified as 'buggy' logic, found a path to the exit ladder. The key move in this path was a step-down from `elevated_ground` (6, 10) to `ground` (6, 9).
- **Radical Hypothesis (H9):** The 'bug' in the debugger was actually the correct game mechanic.
- **Test:** Manually navigated to (6, 10) and attempted to move Up to (6, 9).
- **Conclusion:** The move was blocked by the game engine on a second, deliberate test (Turn 103670). **Hypothesis H9 is definitively FALSE.** The one-way step-down mechanic does not exist. My original, strict understanding of elevation change is correct. The paradox of being in a soft-locked state remains unresolved.

# V. Core Principles & Lessons Learned

## A. LLM Operational Integrity
- **Immediate Action Mandate:** As an LLM, my thinking is turn-based. Deferring tasks like tool creation or data management to a 'later' turn is a critical failure. All such tasks MUST be executed in the immediate turn they are identified. My failure to implement the `boulder_puzzle_solver` immediately was a major strategic error that wasted significant time on futile manual hypotheses.

## B. Victory Road 1F Puzzle - Attempt 2 (FAILED)
- **Hypothesis:** After pushing the southern boulder (6,16) out of the way, the eastern boulder (15,3) can be pushed onto its switch (18,14).
- **Test:** Used `boulder_puzzle_solver` to find a path for this sequence.
- **Conclusion:** The solver returned 'No solution found'. This computationally proves that this specific sequence is impossible and my hypothesis was incorrect. The puzzle likely requires a more complex interaction between the boulders, or I am missing a key mechanic. This confirms that simply activating switches is not the sole objective.

## C. Victory Road 1F Puzzle - Attempt 3 (FAILED)
- **Hypothesis:** The boulder on the western switch (3,10) must be pushed *off* the switch to (3,11) to solve the puzzle.
- **Test:** Used `boulder_puzzle_solver` to find a path for this sequence (Turn 103671).
- **Conclusion:** The solver returned 'No solution found'. This computationally proves that this specific sequence is impossible from the current map state and my hypothesis was incorrect.

## D. Surfing Mechanic (New Discovery)
- Not all `ground` tiles adjacent to `water` are valid starting points for using Surf. The game engine can block movement even if the pathfinder's logic deems it valid. Example: Cannot initiate Surf from (15, 26) to (14, 26) in Viridian City.