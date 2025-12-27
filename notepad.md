## Suicune Quest Strategy (Crystal Version)
- Status: All overworld sightings confirmed complete via "Tin Tower shook" dialogue (Turn 26214, 26920).
- Current Objective: Defeat the Wise Trio to access Suicune in Tin Tower.
- Wise Trio Locations (Tin Tower 1F - Map 3_4):
  - Sage Gaku: (11, 11)
  - Sage Masa: (14, 6)
  - Sage Koji: (5, 9)
- Strategy: Talk to all three Sages in Tin Tower 1F. If they don't battle, verify if another NPC trigger (Morty, Eusine, or Dance Theater) is required.

## Strategy for Wise Trio Battle
- Pokémon: Noctowl (Lv32) and Kadabra (Lv32).
- Lead: Calcifer (Typhlosion) with Thunderpunch.

## Tile Mechanics - Global
- **FLOOR**: Standard walkable tile. Traversable.
- **WALL / VOID / HEADBUTT_TREE**: Impassable terrain.
- **WATER**: Traversable via SURF.
- **CUT_TREE**: Requires CUT to clear.
- **LEDGE_HOP / LEDGE**: One-way traversal (jump). Impassable from most directions.
- **DOOR / STAIRS / LADDER**: Warp tiles.
- **WARP_CARPET**: Map transition tile.

## Key Discoveries & Lessons Learned
- **Dialogue Triggers:** "The Tin Tower shook!" is the definitive narrative flag that all overworld sightings (Burned Tower, Cianwood, Route 42, Route 36) are complete and registered by the game engine.
- **Sequential Requirements:** Clear Bell + Sightings -> "Shook" dialogue -> Wise Trio Battle -> Suicune Encounter.
- **NPC Solidity:** NPCs are solid objects; paths must detour around them.
- **Map Transitions:** Leaving a map from specific coordinates triggers transitions (e.g., Ecruteak (18, 11) -> Tin Tower Gatehouse).