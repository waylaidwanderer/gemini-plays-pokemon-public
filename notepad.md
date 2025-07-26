# I. Game Mechanics & Traversal

## A. Core Rules
- **Level Cap:** The level cap with 8 badges is 65.
- **"No Will to Fight" Message:** Appears when the party menu cursor is on a fainted Pokémon.
- **HM Usage:** HMs are used from the party menu. Fainted Pokémon can use field moves.
- **PC Interaction:** To use a PC, stand directly below it, face up, and press 'A'.
- **Defeated Trainers:** Often become impassable objects, but this is not a universal rule (e.g., Super Nerd in Rock Tunnel was traversable).

## B. Boulder Pushing
- **Activation:** Activate Strength from the party menu.
- **Execution:** Face the boulder and press the directional button. The player does not move.

## C. Tile Glossary & Movement
- **`ground`**: Standard walkable tile.
- **`grass`**: Wild Pokémon encounters.
- **`water`**: Requires SURF.
- **`impassable`**: Wall.
- **`elevated_ground`**: Walkable, different elevation.
- **`steps`**: Allows movement between elevations.
- **`cleared_boulder_barrier`**: Walkable, acts as a ramp between elevations.
- **`boulder_switch`**: Floor switch for boulders.
- **`boulder_barrier`**: Impassable barrier linked to a boulder switch. Tested and confirmed impassable at (10, 13).
- **`hole`**: Drops to a lower floor.
- **`spinner`**: Forces movement.
- **Elevation Change:** Only possible on `steps` or `cleared_boulder_barrier` tiles. Moving from `elevated_ground` to `ground` is not possible without these tiles.

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

## B. Known Trainer Rosters
### Victory Road 3F
- **Cool Trainer M (DEFEATED @ 29,6):** CHARIZARD (Lv52), MAGNETON (Lv52), TENTACRUEL (Lv52)
- **Cool Trainer F (DEFEATED @ 14,4):** WIGGLYTUFF (Lv54), CLEFABLE (Lv54), CHANSEY (Lv54), EEVEE (Lv57)

# III. Puzzle Solutions & Learnings

- **Victory Road 1F Puzzle (Learning):** The correct solution requires solving both the western and eastern boulder puzzles to clear the barrier at (10, 13). The western puzzle involves pushing the boulder at (3, 11) to the switch at (3, 10). The eastern puzzle requires pushing the boulder from the upper platform to its switch. This confirms that complex, multi-step solutions are possible.
- **Boulder Puzzle Reset:** Leaving and re-entering a floor resets all boulders to their original positions. This is a core mechanic for solving boulder puzzles and escaping self-inflicted traps.
- **Elevation Change (Correction):** My hypothesis that one can step down from `elevated_ground` to `ground` was tested and proven false by the game engine. Movement between elevations is only possible on `steps` or `cleared_boulder_barrier` tiles.

# IV. Future Development Ideas

- **Systematic Search Manager Agent:** Create an agent to manage the process of systematically testing tiles (e.g., for hidden passages). It would take a list of target coordinates, track which have been tested, and suggest the next logical target to ensure a complete and efficient search.
- **Soft-Lock Analyzer Tool:** Develop a tool that programmatically analyzes the `map_xml_string` to check for escape routes. It could test paths to all exits considering all known traversal mechanics, including unconventional ones like Dig or checking for required items like Escape Ropes.