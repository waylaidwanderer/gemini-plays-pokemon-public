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

# II. Strategic Plans & Checklists

## A. Plan to Defeat Giovanni
1.  **Level Goal:** Train the party to the level cap of 55. This is the top priority.
2.  **Location Scouting:** Seafoam Islands is the primary candidate for a training spot.
3.  **Assemble Team:** Once leveled, use `team_composition_advisor_agent` for an optimal team recommendation.
4.  **Navigate Gym:** Find the path to Giovanni at (3, 2).
5.  **Battle Strategy:** Use `battle_strategist_agent` for turn-by-turn advice.

## B. Plan to Explore Seafoam Islands for Training
1.  **Hypothesis:** The main part of Seafoam Islands, containing the boulder puzzles and likely better training spots, is accessed via the western entrance on Route 20. The eastern entrance (accessed from Route 19) is a separate, dead-end section.
2.  **Test:**
    - Exit the current eastern section of the cave.
    - Fly to Cinnabar Island.
    - Surf east to the western part of Route 20.
    - Find and enter the western cave entrance.
    - Explore this new area for high-level wild Pokémon.

# III. Game Mechanics & Discoveries

## A. Verified Tile Mechanics
- **Ledge:** Can be jumped down (one-way). Moving down into a ledge tile moves the player two tiles down.
- **Cuttable Tree:** Requires HM Cut to pass. Respawns on map change.
- **Water:** Requires HM Surf to traverse.
- **Boulder:** Requires HM Strength to move.

## B. General Heuristics & Rules
- **PC Interaction:** To use a PC, stand on the tile directly below it, face up, and press 'A'.
- **HM Usage:** HMs are used from the party menu outside of battle.
- **Surfing:** To use Surf from a land tile, you must be standing on a ground tile that is adjacent to a water tile, and you must be facing the water tile.
- **Party Planning:** Always confirm all required HMs (Fly, Surf, Strength, Cut) are present in the party *before* leaving a Pokémon Center to travel to a new area.