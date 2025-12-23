# Suicune Capture Strategy (Crystal Version)
## Primary Goal: Capture Suicune
- Status: Confirmed on Route 42. Training XENON (Gastly) to Lv18 for Repel Trick.
- Catcher: XENON (Gastly) - Mean Look (Trap) + Hypnosis (Sleep). Immune to Roar.
- Repel Trick: Lead PKMN must be Lv18 on Route 42 to block Lv13-17 wilds. (Suicune is Lv40).

## Training Log: XENON to Lv18
- **Start Turn**: 15504 (Tuesday, Dec 23, 1:00 PM)
- **Current Status**: Lv17 (3436 EXP). Needs 363 more EXP for Lv18 (3799 total).
- **Recent Battles**: Ekans (Turn 15594), Spearow (Turn 15581), Rattata (Turn 15523).

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
- **Roamer Immunity**: Ghost-types are immune to Roar (Normal), preventing Suicune from ending the battle. Trapping is viable.