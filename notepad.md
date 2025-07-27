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
  - The western boulder at (3,10) cannot be pushed OFF its switch (H2).
  - Defeated trainers (Youngster at 7,11) are impassable and do not move when switches are activated (H6, H7).
  - There are no hidden switches or passages on the western platform (H5).

## B. Puzzle Solving Insight (Confirmation Bias)
My previous hypotheses all assumed activating switches is the solution. If these fail, I must test hypotheses where switches are deliberately left *unactivated* or boulders are used to block paths elsewhere.
- `ladder_up`: Warp tile that leads to a higher floor.
- `ladder_up`: Warp tile that leads to a higher floor.
- `ladder_up`: Warp tile that leads to a higher floor.