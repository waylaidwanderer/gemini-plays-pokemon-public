# Tile Mechanics
- FLOOR: Standard traversable tile.
- WALL / TREE / MOUNTAIN / HEADBUTT_TREE: Impassable collision.
- WATER: Requires Surf (HM03) to traverse. Interact with water edge or use from menu.
- CUT_TREE: Requires Cut (HM01) to clear. Impassable otherwise. Regrows whenever the map is reloaded (e.g., entering/exiting Mount Mortar).
- LEDGE: One-way jump (usually South). Cannot be jumped from below. Verified by attempting to walk North onto ledge tiles.
- FLOOR_UP_WALL: One-way barrier. Cannot be entered from below. Verified at (50, 14) on Route 42.
- TALL_GRASS: Traversable tile. Triggers wild encounters. Verified at (46, 12) on Route 42.
- CAVE: Warp tile leading to internal maps. Verified at (10, 5) on Route 42.
- WARP_CARPET_LEFT / WARP_CARPET_RIGHT: Map transition tiles. Verified at (0, 8) and (60, 7) on Route 42.
- MART_SHELF: Impassable collision. Verified at (3, 5) in Mahogany Mart.
- COUNTER: Interaction tile for NPCs. Stand in front and face NPC to interact. Verified at (2, 3) in Mahogany Mart.

# Suicune Capture Strategy (Pokemon Crystal)
## Primary Goal: Capture Suicune (Roamer)
- Status: Roaming (Confirmed via Pokedex dot and Tin Tower event history).
- Last Seen: Route 44 (Turn 15957).
- Lead: XENON (Gastly, Lv18) - Speed: 36.
- Strategy: Repel Trick in tall grass.
- **CRITICAL**: Suicune will flee immediately. Mean Look is required on Turn 1.
- Note: If Suicune is faster than 36 Speed, it will flee before Mean Look can be used.

## Training Phase (Started Turn 15902)
- Target: Route 44 (East of Mahogany Town).
- Goal: Level XENON (Gastly) to outspeed Lv40 Roamers.

## Region Map IDs (Johto - Corrected)
- Route 38: 2_1, Route 39: 2_2, Olivine City: 2_3, Ecruteak City: 2_4
- Route 42: 2_5, Route 44: 2_6, Mahogany Town: 2_7, Route 40: 2_8
- Route 41: 2_9, Cianwood City: 2_10, Lake of Rage: 2_11, Route 43: 2_24 (Estimate, need to verify)
- Blackthorn City: 2_13, Route 45: 2_14, Route 46: 2_15, Silver Cave: 2_16
- Route 29: 1_2, Route 30: 1_4, Route 31: 1_5, Violet City: 1_6
- Route 32: 1_7, Route 33: 1_9, Azalea Town: 1_10, Route 34: 1_12
- Goldenrod City: 1_13, Route 35: 1_14, Route 36: 1_16, Route 37: 1_17
- Mt Mortar: 3_1

## Observed Movesets
- Natu (Psychic Phil): Future Sight, Night Shade.

## Reflection Lessons (Turn 15842)
- Fly Menu Navigation: Fly map movement is not a simple coordinate grid; it's a linked list of cities. Moving "Up" cycles through the known locations.
- Repel Trick Persistence: Repel effects persist across map transitions. Check effect status before using a new one to save money.
- Roamer Movement: Roamers move when the player crosses a map boundary (Warp Carpet or Warp).

# Roamer Hunting Mechanics
- Repel Trick: Lead Pokemon level must be higher than area wild Pokemon (Max Lv17 on Route 42 grass) but lower than Roamer level (Lv40). Repel will then only allow Roamer encounters.
- Speed Check: XENON (Lv18, Speed 36) is confirmed too slow to use Mean Look before Raikou/Suicune flee. Lv40 Roamers have significantly higher speed.
- Strategy Update: Need to level XENON or find a faster trapper before continuing the hunt. Current pacing is ineffective for capture.
- Quick Claw: Not in inventory. Check future locations for this item.