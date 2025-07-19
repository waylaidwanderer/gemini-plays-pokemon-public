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
- **Cuttable Tree:** Requires HM Cut to pass. Becomes `ground` after cutting, but respawns on map change.
- **Water:** Requires HM Surf to traverse. To use Surf from a land tile, you must be standing on a ground tile that is adjacent to a water tile, face the water, and use the HM from the party menu.
- **Boulder:** Requires HM Strength to move.
- **Hole:** Warps player to a lower floor.
- **Ladder (Up/Down):** Warps player between floors.
- **Steps:** Allows vertical and horizontal movement between 'steps' and adjacent 'ground' or 'elevated_ground' tiles.
- **Spinner:** Forces movement in a specific direction.
- **Elevated Ground:** Walkable ground at a different elevation. HM Surf cannot be initiated from this tile type.

## B. General Heuristics & Rules
- **PC Interaction:** To use a PC, stand on the tile directly below it, face up, and press 'A'.
- **HM Usage:** HMs are used from the party menu outside of battle. The game does not automatically use an HM when you walk into an obstacle; you must manually stop and use it from the menu.
- **Party Planning:** Always confirm all required HMs (Fly, Surf, Strength, Cut) are present in the party *before* leaving a Pokémon Center to travel to a new area.
- **Dynamic Map Elements:** Some map elements, like trees, can appear dynamically based on player movement or other triggers (e.g., Fuchsia City at (19,20) and (17,12)).

# III. Tool Development & Usage

## A. `pathfinder` Tool
- **Game Mechanic Limitation:** The tool plans paths over traversable terrain. It does not account for game mechanics that require manual intervention, such as using an HM like Surf or Cut from the party menu. I must manually use HMs when at the edge of an obstacle to transition to a new terrain type (e.g., ground to water).

## B. Agent & Tool Usage Notes
- Proximity of recommended locations from agents should be considered for efficiency.

# IV. Puzzle-Solving Hypotheses

## A. Fuchsia City Secret Pokémon (at (26, 7))
- **Observation:** An item ball at (26, 7) is in an enclosed area. A Youngster at (25, 9) states, "That item ball in there is really a POKéMON."
- **Hypothesis 1 (Failed):** The signs next to the other Pokémon exhibits must be read in a specific order to unlock the enclosure.
- **Hypothesis 2 (Untested):** Interaction with the Pokémon in the enclosures is required, not the signs.
- **Hypothesis 3 (Untested):** A specific Pokémon must be in the party to trigger an event.

# V. Strategic Notes

## A. Training for Giovanni
- **Strategy:** The lower floors of Seafoam Islands (B3F and B4F) contain high-level wild Pokémon suitable for training the party to the level cap of 55.

# VI. Future Development Ideas

## A. `dungeon_solver` Tool
- **Concept:** A tool that can find the optimal path through a multi-floor dungeon. 
- **Inputs:** Starting map ID/coordinates and ending map ID/coordinates.
- **Functionality:** Would need to parse multiple map XMLs and build a graph that connects them via warps (ladders, holes, etc.) to find the shortest path between any two points in the dungeon complex.
- **Pathfinder Bug Fix:** The `pathfinder` tool was generating invalid paths. I have rewritten the `get_neighbors` function and improved the logic for handling impassable targets. The tool should now be more reliable.