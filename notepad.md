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
1.  **Analyze Roster:** Use `team_composition_advisor_agent` for an optimal team recommendation.
2.  **Assemble Team:** Withdraw recommended Pokémon from the PC.
3.  **Navigate Gym:** Find the path to Giovanni at (3, 2).
4.  **Battle Strategy:** Use `battle_strategist_agent` for turn-by-turn advice.

## B. Plan to Train for Giovanni
1.  **Level Goal:** Train the party to the level cap of 55.
2.  **Location Scouting:** My `training_spot_advisor_agent` recommended Seafoam Islands. My initial approach was flawed.
    - **Flawed Hypothesis (Disproven):** The path to Seafoam Islands is through Route 21 and the western part of Route 20. I attempted this multiple times and confirmed the western part of Route 20 is an isolated dead-end.
    - **New Hypothesis:** The correct path to the main part of Seafoam Islands is via Route 19, south of Fuchsia City.
    - **Test:** Travel to Fuchsia City, surf south on Route 19, and see if it connects to the main, eastern part of Route 20 where the cave entrance is located.

## C. Current Plan: Correcting Course to Seafoam Islands
1.  **Return to Cinnabar:** Navigate from the current position on Route 20 back to Cinnabar Island.
2.  **Fly to Fuchsia City:** Use Fly to travel to Fuchsia City.
3.  **Surf South:** Take the southern map connection from Fuchsia City to Route 19 and begin surfing.
4.  **Explore Route 19/20:** Navigate the eastern sea route to find the main entrance to Seafoam Islands.

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