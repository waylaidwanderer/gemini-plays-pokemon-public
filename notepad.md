# I. Battle Intel

## A. Type Effectiveness Chart (Verified)
- **Super Effective (2x):** Psychic > Ghost, Poison; Ghost > Psychic; Electric > Rock, Water; Flying > Grass, Poison, Fighting; Ice > Ground, Grass, Flying, Dragon; Ground > Poison, Fire, Electric, Rock; Rock > Fire, Ice, Flying, Bug; Fighting > Normal, Rock, Ice; Water > Fire, Ground, Rock; Grass > Water, Ground, Rock; Bug > Grass, Poison, Psychic; Poison > Grass, Bug.
- **Not Very Effective (0.5x):** Normal !> Rock; Electric !> Grass, Electric, Dragon; Rock !> Ground, Fighting; Psychic !> Psychic; Poison !> Poison, Ground, Rock, Ghost; Ice !> Water, Ice, Fire; Fighting !> Poison, Flying, Psychic, Bug; Water !> Water, Grass, Dragon; Grass !> Fire, Grass, Poison, Flying, Bug, Dragon.
- **Immune (0x):** Flying immune to Ground; Ground immune to Electric; Ghost immune to Normal, Fighting.

## B. Trainer Rosters & Movesets
### Giovanni (Viridian Gym)
- **Dugtrio (Lv53):** Knows Rock Slide, Earthquake, Fissure, Slash.
- **Nidoqueen (Lv54):** Knows Body Slam, Earthquake, Thunderbolt, Ice Beam.
- **Nidoking (Lv54):** Knows Blizzard, Earthquake, Thunderbolt, Ice Beam.
- **Persian (Lv55):** Knows Bubblebeam, Slash, Hyper Beam, Thunderbolt.

# II. Game Mechanics & Discoveries

## A. Verified Tile Mechanics
- **Ground:** Standard walkable tile.
- **Impassable:** Walls, objects, etc. Cannot be entered.
- **Grass:** Tall grass for wild Pokémon encounters.
- **Ledge:** Can be jumped down (one-way). Moving down into a ledge tile moves the player two tiles down.
- **Cuttable Tree:** Requires HM Cut to pass. Respawns on map change.
- **Water:** Requires HM Surf to traverse. To use Surf from a land tile, you must be standing on a ground tile that is adjacent to a water tile, and you must be facing the water tile.
- **Boulder:** Requires HM Strength to move.
- **Hole:** Warps player to a lower floor.
- **Ladder (Up/Down):** Warps player between floors. Some ladders require stepping off and back on the tile to function.
- **Steps:** Allows vertical and horizontal movement between 'steps' and adjacent 'ground' or 'elevated_ground' tiles.
- **Spinner:** Forces movement in a specific direction.

## B. General Heuristics & Rules
- **PC Interaction:** To use a PC, stand on the tile directly below it, face up, and press 'A'.
- **HM Usage:** HMs are used from the party menu outside of battle.
- **Party Planning:** Always confirm all required HMs (Fly, Surf, Strength, Cut) are present in the party *before* leaving a Pokémon Center to travel to a new area.
- **Dynamic Map Elements:** Some map elements, like trees, can appear dynamically based on player movement or other triggers (e.g., Fuchsia City at (19,20)).

# III. Tool Development & Debugging

## A. `pathfinder` Tool Development
- **Status:** CRITICAL FAILURE. The current approach of using `run_code` with a temporary script is inefficient and error-prone. This violates core principles.
- **Action Required:** The immediate, top-priority task is to define a robust, reusable `pathfinder` tool using `define_tool`. The script must be properly debugged to handle scope, syntax, and data structure issues that have caused repeated failures.

## B. Agent & Tool Usage Notes
- **`training_spot_advisor_agent`:** This agent is underutilized. I need to create an opportunity to use it to validate its effectiveness, especially since training is a current goal.
- **Debugging Best Practices:** In case of tool failure, the first step must be to use `run_code` with detailed print statements to trace execution. Avoid repeated, blind redefinitions. Use `code_debugger_agent` to analyze errors.

# IV. Puzzle-Solving Hypotheses

## A. Fuchsia City Secret Pokémon (at (26, 7))
- **Observation:** An item ball at (26, 7) is in an enclosed area. A Youngster at (25, 9) states, "That item ball in there is really a POKéMON."
- **Hypothesis 1:** The signs next to the other Pokémon exhibits must be read in a specific order to unlock the enclosure.
- **Test 1:** I will systematically visit and read each sign, starting with the Fossil sign at (8, 8), and check the enclosure after each interaction.
- **Result 1:** TBD.
- **Conclusion 1:** TBD.