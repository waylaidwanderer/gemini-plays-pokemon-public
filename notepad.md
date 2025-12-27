# Suicune Quest Strategy (Crystal Version)
- **Status:** All overworld sightings (Burned Tower, Cianwood, Route 42, Route 36) confirmed via "Tin Tower shook" dialogue (Turn 27084).
- **Current Objective:** Defeat the Wise Trio to access Suicune in Tin Tower.
- **Problem:** Wise Trio is missing from Map 4_2 despite "shook" dialogue.
- **Hypothesis:** A specific NPC interaction or event flag is missing.
- **Plan:** 
  1. Use `suicune_tracker_v2` to verify exact requirements.
  2. Re-check the Tin Tower entrance at (37, 7) on Map 4_9.

## Tile Mechanics - Global
- **FLOOR**: Standard walkable tile. Traversable.
- **WALL / VOID / HEADBUTT_TREE**: Impassable terrain.
- **WATER**: Traversable via SURF.
- **CUT_TREE**: Requires CUT to clear.
- **LEDGE_HOP / LEDGE**: One-way traversal (jump). Impassable from most directions.
- **DOOR / STAIRS / LADDER**: Warp tiles.
- **WARP_CARPET**: Map transition tile.

## Key Discoveries & Lessons Learned
- **Dialogue Triggers:** "The Tin Tower shook!" is the definitive narrative flag that all overworld sightings are complete.
- **Sequential Requirements:** Clear Bell + Sightings -> "Shook" dialogue -> Wise Trio Battle -> Suicune Encounter.
- **NPC Solidity:** NPCs are solid objects; paths must detour around them.
- **Map Transitions:** Leaving a map from specific coordinates triggers transitions (e.g., Ecruteak (18, 11) -> Tin Tower Gatehouse).
- **Wise Trio Location:** They are supposed to be in Map 4_2, but were not found there on Turn 27087. Re-checking prerequisites.

## Trainer & Party Info
- **Lead:** Calcifer (Typhlosion) Lv45 with Thunderpunch.
- **Wise Trio Battle Team:** Noctowl (Lv32) and Kadabra (Lv32) - *Note: These are planned targets, not current party members.*
- **Current Party:** Typhlosion, Pidgey, Graveler, Krabby, Gloom, Gastly.