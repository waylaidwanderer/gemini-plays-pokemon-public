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
- **Dynamic Map Elements:** Some map elements, like trees, can appear dynamically based on player movement or other triggers (e.g., Fuchsia City at (19,20) and (17,12)).

# III. Tool Development & Usage

## A. `pathfinder` Tool
- **Status:** Implemented and refined. The tool can now find paths that include `cuttable` trees.
- **Usage Note:** The tool correctly identifies paths through HM obstacles, but I must manually stop and use the HM from the menu when I reach the obstacle tile before continuing along the path.

## B. Agent & Tool Usage Notes
- **`training_spot_advisor_agent`:** I need to use this agent to plan my training strategy for Giovanni. This is a high priority.

# IV. Puzzle-Solving Hypotheses

## A. Fuchsia City Secret Pokémon (at (26, 7))
- **Observation:** An item ball at (26, 7) is in an enclosed area. A Youngster at (25, 9) states, "That item ball in there is really a POKéMON."
- **Hypothesis 1:** The signs next to the other Pokémon exhibits must be read in a specific order to unlock the enclosure.
- **Test 1:** Read the Fossil sign at (8, 8).
- **Result 1:** Reading the sign displayed information about Omanyte. No other observable effect.
- **Test 2:** Read the Kangaskhan sign at (14, 8).
- **Result 2:** Reading the sign displayed information about Kangaskhan. No other observable effect.
- **Test 3:** Read the Slowpoke sign at (32, 14).
- **Result 3:** Reading the sign displayed information about Slowpoke. No other observable effect.
- **Hypothesis 2 (Alternative):** Interaction with the Pokémon in the enclosures is required, not the signs.
- **Hypothesis 3 (Alternative):** A specific Pokémon must be in the party to trigger an event.

# V. Training Plan

## A. Goal: Train party to level cap 55 for Giovanni.
- **Action:** Use `training_spot_advisor_agent` to identify the best training locations. Potential locations to consider: Seafoam Islands, Victory Road (once accessible), Route 22.