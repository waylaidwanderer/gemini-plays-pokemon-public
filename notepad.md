# Suicune Capture Strategy (Crystal Version)
## Primary Goal: Capture Suicune
- Status: Confirmed on Route 42. Training XENON (Gastly) to Lv18 for Repel Trick.
- Catcher: XENON (Gastly) - Mean Look (Trap) + Hypnosis (Sleep). 
- Repel Trick: Lead PKMN must be Lv18 on Route 42 to block Lv13-17 wilds. (Suicune is Lv40).

## Training Log: XENON to Lv18
- **Start Turn**: 15504 (Tuesday, Dec 23, 1:00 PM)
- **Current Status**: Lv17 (3592 EXP). Needs 207 more EXP for Lv18 (3799 total).

## Battle Tactics: Suicune (Lv40)
- Moveset: Gust, Leer, Bubblebeam, Rain Dance. (Does NOT know Roar).
- Strategy: Mean Look on Turn 1 to trap. Hypnosis to induce sleep.
- Note: Ghost-types are NOT immune to status moves like Roar or Leer, but Suicune lacks phazing moves in Crystal.
- Status: Trapping is viable.

## Map Mechanics: Route 42
- **Adjacent Maps**: Ecruteak City (1_1), Mahogany Town (2_7), Mt. Mortar (3_1).
- **Unique Tiles**: FLOOR_UP_WALL (Verified impassable from North, hypothesized passable from South).
- **Navigation**: Ledge at (y=14) requires North path (y=7) for access to South grass.

## Global Tile Mechanics (Summary)
- TALL_GRASS: Triggers wild encounters.
- WATER: Requires Surf (HM03).
- LEDGE: One-way jump South.
- WARP: Map transition.
- Standard Collision: WALL, FENCE, TREE, MOUNTAIN, COUNTER (Impassable).

## Strategy & Lessons
- **Roamer Movement**: Roamers move between adjacent maps on map boundary cross. Re-verify location via Pokédex after every battle and map transition.
- **Menu Reliability**: Keep menu sequences to 1-3 buttons of a single type (directional OR action) to avoid system truncation.
- **Roamer Strategy**: Status moves like Roar affect Ghost-types in Gen 2, but Suicune (Lv40) lacks phazing moves in Crystal. Trapping is viable.