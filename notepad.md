# I. Game Mechanics & Traversal

## A. Core Rules
- **Level Cap:** The level cap with 8 badges is 65.
- **"No Will to Fight" Message:** Appears when the party menu cursor is on a fainted Pokémon.
- **HM Usage:** HMs are used from the party menu. Fainted Pokémon can use field moves.
- **PC Interaction:** To use a PC, stand directly below it, face up, and press 'A'.
- **Defeated Trainers:** Some defeated trainers are traversable objects (e.g., Youngster in Victory Road 1F).

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
- **`ladder_up`**: Warp tile that leads to a higher floor.
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

- **Victory Road 1F Puzzle - Hypothesis History**
  - **H1 (Both Switches ON):** Pushing both the western boulder (at 3,11 to 3,10) and the eastern boulder (at 17,13 to 18,14) onto their switches resulted in the barrier at (10,13) remaining closed. **CONCLUSION: FAILED.**
  - **H2 (Toggle Switch):** The switch at (3,10) is a toggle, and the boulder must be pushed off it. **CONCLUSION: UNTESTABLE/FAILED.** It is physically impossible to push the boulder off the switch at (3,10) as the required push positions are impassable walls.
  - **H3 (Western Switch Only):** Pushed ONLY the western boulder (from 3,11 to 3,10) onto its switch. RESULT: The barrier at (10,13) remained closed. **CONCLUSION: FAILED.**
  - **H4 (Talk to defeated Youngster):** After getting trapped by pushing the boulder to (6, 17), talked to the defeated Youngster at (7, 11) again. RESULT: He repeated his post-battle dialogue. No event was triggered. **CONCLUSION: FAILED.**
  - **H5 (Hidden Switch/Passage):** Searched for a hidden pressure plate or secret passage on the western platform. **CONCLUSION: FAILED.** The Overwatch system confirmed this was a hallucination, as no such objects exist in the game state.
  - **H6 (Defeated Trainers Traversable):** The defeated Cool Trainer M at (4,3) and the Youngster at (7,11) are traversable objects. **CONCLUSION: FAILED.** Attempting to walk onto the Youngster at (7,11) was blocked by the game engine, proving defeated trainers are impassable obstacles. This invalidates the entire western path solution.
- **Boulder Puzzle Reset:** Leaving and re-entering a floor resets all boulders to their original positions. This is a core mechanic for solving boulder puzzles and escaping self-inflicted traps.
- **Puzzle Solving Insight (Confirmation Bias):** My current hypotheses all assume activating switches is the solution. If these fail, I must test hypotheses where switches are deliberately left *unactivated* or boulders are used to block paths elsewhere.

# IV. Future Agent & Tool Ideas
- **Boulder Puzzle Solver Tool:** Create a custom tool that can analyze the map layout (`map_xml_string`) to find a sequence of pushes to solve boulder puzzles. This is a computational task, not a reasoning one, so a tool is the correct implementation. Input would be boulder, switch, and barrier coordinates. Output would be a list of push actions.