# Suicune Capture Strategy (Crystal Version)
## Primary Goal: Capture Suicune
- Status: Scripted encounter sequence in progress.
- Catcher: XENON (Gastly) - Mean Look (Trap) + Hypnosis (Sleep). 
- Encounter Type: Overworld sprite at specific locations. Does NOT roam in grass until after Tin Tower event.
- Current Target: Route 42 middle island (requires Cut and Surf).

## Repel Trick Execution Plan (Post-Tin Tower)
- Lead PKMN must be Lv18 on Route 42 to block Lv13-17 wilds. (Suicune is Lv40).
- Only applicable once Suicune begins roaming.

## Battle Tactics: Suicune (Lv40)
- Moveset: Gust, Leer, Bubblebeam, Rain Dance. (Does NOT know Roar).
- Strategy: Mean Look on Turn 1 to trap. Hypnosis to induce sleep.
- Note: Ghost-types are NOT immune to status moves like Roar or Leer, but Suicune lacks phazing moves in Crystal.

## Map Mechanics: Route 42
- **Adjacent Maps**: Ecruteak City (1_1), Mahogany Town (2_7), Mt. Mortar (3_1).
- **Navigation**: 
  - Center island reachable via Surf at (14, 12) or Cut tree at (24, 13).
  - Ledge at (y=14) requires North path (y=7) for access to South grass.
- **Tile Mechanics**:
  - FLOOR_UP_WALL: Impassable from North.
  - TALL_GRASS: Triggers wild encounters (Lv13-17).
  - WATER: Requires Surf (HM03).
  - CUT_TREE: Requires Cut (HM01).

## Global Tile Mechanics (Summary)
- TALL_GRASS: Triggers wild encounters.
- WATER: Requires Surf (HM03).
- LEDGE: One-way jump South.
- WARP: Map transition.
- Standard Collision: WALL, FENCE, TREE, MOUNTAIN, COUNTER (Impassable).

## Strategy & Lessons
- **Roamer Movement**: Roamers move between adjacent maps on map boundary cross. Re-verify location via Pokédex after every battle and map transition.
- **Menu Reliability**: Keep menu sequences to 1-3 buttons of a single type (directional OR action) to avoid system truncation.
- **Suicune Encounters**: 
  1. North of Cianwood (Seen).
  2. Route 42 middle island (Next).
  3. Route 36.
  4. Tin Tower.