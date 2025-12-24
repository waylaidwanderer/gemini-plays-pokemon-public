# Global Tile Mechanics
- FLOOR: Standard traversable tile.
- WALL / TREE / MOUNTAIN / HEADBUTT_TREE: Impassable collision.
- WATER: Requires Surf (HM03) to traverse. Interact with water edge or use from menu.
- CUT_TREE: Requires Cut (HM01) to clear. Impassable otherwise. Regrows whenever the map is reloaded (e.g., entering/exiting Mount Mortar).
- LEDGE: One-way jump (usually South). Cannot be jumped from below.
- TALL_GRASS: Traversable, but triggers wild Pokemon encounters.

# Suicune Capture Strategy (Pokemon Crystal)
## Primary Goal: Capture Suicune (Roamer)
- Status: Roaming (Confirmed via Pokedex dot and Tin Tower event history).
- Location: Route 42 (Current).
- Lead: XENON (Gastly, Lv18) - Speed: 36.
- Strategy: Repel Trick in Route 42 tall grass.
- **CRITICAL**: Suicune will flee immediately. Mean Look is required on Turn 1.
- Note: If Suicune is faster than 36 Speed, it will flee before Mean Look can be used.

## Repel Trick Procedure
1. Ensure Lv18 XENON is leading.
2. Activate Super Repel (blocks Lv13-17 wilds).
3. Pace in grass at (50, 12) until Suicune appears.
4. If Suicune moves maps, follow using `roamer_tracker_v2`.

## Party Strategy
- XENON (Gastly, Lv18): Lead for Mean Look/Hypnosis.
- KIMCHI (Gloom): Cut.
- Ravioli (Krabby): Surf.

## Items
- Super Repel: Active (approx 150 steps remaining).
- Great Ball: 29. Main capture tool.