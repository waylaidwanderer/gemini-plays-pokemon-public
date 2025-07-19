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

# III. Tool Development & Debugging

## A. `pathfinder` Tool
- **Bug Identified (Turn 85081):** The tool fails to find paths in areas with 'steps' tiles (e.g., Seafoam Islands 1F). 
- **Hypothesis:** The `is_walkable` function did not correctly identify 'steps' tiles as traversable from adjacent 'ground' or 'elevated_ground' tiles.
- **Action (Turn 85088):** Updated the script to include logic for 'steps' traversal. The tool needs further rigorous testing.

## B. Future Agent & Tool Ideas
- **Grinding Session Analyst:** An agent to determine if a training location is efficient based on EXP gain over time, factoring in encounter rate and battle length.
- **Self Reflection Agent:** An agent that could analyze my last 50 turns and provide a critique based on my core principles, automating the reflection process.