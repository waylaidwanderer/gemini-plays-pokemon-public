# Tile Mechanics
- FLOOR: Standard traversable tile.
- WALL / TREE / MOUNTAIN / HEADBUTT_TREE: Impassable collision.
- WATER: Requires Surf (HM03) to traverse. Interact with water edge or use from menu.
- CUT_TREE: Requires Cut (HM01) to clear. Impassable otherwise. Regrows whenever the map is reloaded (e.g., entering/exiting Mount Mortar).
- LEDGE: One-way jump (usually South). Cannot be jumped from below.
- FLOOR_UP_WALL: One-way barrier. Cannot be entered from below. Verified at (50, 14).
- TALL_GRASS: Traversable tile. Triggers wild encounters. Verified at (46, 12).
- CAVE: Warp tile leading to internal maps. Verified at (10, 5).
- WARP_CARPET_LEFT / WARP_CARPET_RIGHT: Map transition tiles. Verified at (0, 8) and (60, 7).
- MART_SHELF: Impassable collision. Verified at (3, 5).
- COUNTER: Interaction tile for NPCs. Verified at (2, 3).

# Suicune Capture Strategy (Pokemon Crystal)
## Primary Goal: Capture Suicune (Roamer)
- Status: Roaming (Confirmed via Pokedex dot and Tin Tower event history).
- Location: Route 42 (Current).
- Lead: XENON (Gastly, Lv18) - Speed: 36.
- Strategy: Repel Trick in Route 42 tall grass.
- **CRITICAL**: Suicune will flee immediately. Mean Look is required on Turn 1.
- Note: If Suicune is faster than 36 Speed, it will flee before Mean Look can be used.

## Repel Trick Active Hunt (Started Turn 15841)
- Lead: XENON (Gastly, Lv18).
- Location: Route 42 Grass (50, 12).
- Status: Suicune confirmed on Route 42 (Turn 15830).
- Super Repel: Active (Turn 15839).
- Step 1: Pace in grass at (50, 12) <-> (51, 12) using wild_encounter_looper.
- Step 2: Turn 1 of battle: MEAN LOOK.

## Party Strategy
- XENON (Gastly, Lv18): Lead for Mean Look/Hypnosis.
- KIMCHI (Gloom): Cut.
- Ravioli (Krabby): Surf.

## Items
- Great Ball: 29. Main capture tool.
- Pokeball: 2.
- Super Repel: 7.
## Reflection Lessons (Turn 15842)
- Fly Menu Navigation: Fly map movement is not a simple coordinate grid; it's a linked list of cities. Moving "Up" cycles through the known locations.
- Repel Trick Persistence: Repel effects persist across map transitions. Check effect status before using a new one to save money.
- Roamer Movement: Roamers like Suicune only move when the player crosses a map boundary (Warp Carpet or Warp). Staying on the same map and pacing is the best way to force an encounter.

## Error Analysis: Fly Map overshoot
- Observation: Repeatedly failed to land on Mahogany Town by guessing directional inputs.
- Root Hypothesis:fly map is a grid.
- Conclusion: Hypothesis denied. It's a structured list.
- Lesson: Move one step at a time and verify the destination name on screen.