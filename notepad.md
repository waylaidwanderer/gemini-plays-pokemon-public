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

# II. Strategic Plans

## A. Plan to Defeat Giovanni
1.  **Analyze Roster:** Use `team_composition_advisor_agent` for an optimal team recommendation.
2.  **Assemble Team:** Withdraw recommended Pokémon from the PC.
3.  **Navigate Gym:** Find the path to Giovanni at (3, 2).
4.  **Battle Strategy:** Use `battle_strategist_agent` for turn-by-turn advice.

## B. Plan to Train for Giovanni
1.  **Level Goal:** Train the party to the level cap of 55.
2.  **Location Scouting:** My `training_spot_advisor_agent` recommended Seafoam Islands as the top priority. I am currently investigating this.
    - **Hypothesis:** Seafoam Islands contains high-level wild Pokémon suitable for training.
    - **Test:** Explore the area, battle wild Pokémon, and check their levels and EXP yield.

# III. Game Mechanics & Discoveries

## A. Tile Mechanics
- **ground:** Walkable.
- **elevated_ground:** Walkable, often requires `steps` to access.
- **steps:** Allows vertical movement between `ground` and `elevated_ground`.
- **water:** Crossable using Surf.
- **impassable:** Walls, rocks, etc. Cannot be entered.
- **ledge:** One-way downward traversal.
- **hole:** Warps to a lower floor.
- **ladder_up / ladder_down:** Warps between floors.
- **boulder:** Movable with Strength.
- **Route 19 Surfing:** Surfing is not possible from every shoreline tile. Specific locations must be used.

## B. General Heuristics
- **PC Interaction:** To use a PC, stand on the tile directly below it, face up, and press 'A'.
- **HM Usage:** HMs are used from the party menu outside of battle.
- **Route 19 Surfing:** Surfing is not possible from every shoreline tile. Specific locations must be used.