# Suicune Capture Strategy (Crystal Version)
## Primary Goal: Capture Suicune
- Step 1: Obtain Clear Bell. (COMPLETE)
- Step 2: Access Tin Tower. Defeat the Wise Trio. (COMPLETE)
- Step 3: Encounter Suicune at Tin Tower. (COMPLETE - It fled).
- Step 4: Track Suicune via Pokédex. (COMPLETE: Confirmed on Route 42).
- Step 5: Prepare Catcher. XENON (Gastly) with Mean Look + Hypnosis. (Target: Lv18 for Repel efficiency).
- **Timestamp**: Suicune Hunt started Turn 15201, Tuesday, Dec 23, 1:00 PM.

## Roamer Mechanics & Interception
- Roamers move between adjacent maps whenever the player crosses a map boundary.
- Interception: Identify roamer's map via Pokédex. Stay on that map and pace in grass/water.
- Battle Strategy: XENON (Gastly) uses Mean Look immediately to trap. Hypnosis to sleep.
- Repel Trick: Lead PKMN level must be Lv18 for 100% efficiency on Route 42. (XENON is Lv17).

## Training Plan (XENON to Lv18)
- Objective: Reach Lv18 to maximize Repel Trick efficiency on Route 42.
- Method: Defeat local wild Pokémon or trainers.
- Status: XENON is Lv17.

## Tile Mechanics Scientific Testing
### FLOOR_UP_WALL Verification
- **Observation**: Tiles labeled FLOOR_UP_WALL exist on Route 42.
- **Hypothesis**: These tiles allow movement North but block movement South, East, and West.
- **Test 1**: Attempt to move South onto (50, 14) from (50, 13).
- **Result 1**: Movement blocked. (Turn 15363).
- **Conclusion 1**: Entering from the North is impassable.
- **Test 2**: Attempt to move North onto (59, 8) from (59, 9).
- **Status 2**: Deferred.

## Global Tile Mechanics
- FLOOR, TALL_GRASS, DIRT, SAND: Traversable.
- WALL, FENCE, MOUNTAIN, MART_SHELF, COUNTER: Impassable.
- FLOOR_UP_WALL: Verified Impassable from North. Hypothesized Traversable from South.
- LEDGE: One-way jump South.
- WATER: Requires Surf (HM03).
- HEADBUTT_TREE: Impassable; can be Headbutted.
- CUT_TREE: Impassable; requires Cut (HM01).
- WARP: Map transition (Doors, Stairs, Cave Entrances).

## Lessons Learned
- **Custom Tool Hygiene**: find_path_v2 must return button strings if autopress_buttons is true. Fix applied Turn 15375.
- **Navigation**: Route 42 ledge requires going around through the North path (y=7) to reach the South area.
- **Menu Navigation**: When a menu has multiple options on the same row (e.g., Pokédex PAGE/AREA/CRY), explicitly use directional buttons to move the cursor before pressing A. (Turn 15426).
- **Roamer Hunting**: Roamers move every time you cross a map boundary. Always re-verify location immediately after entering a new map. (Turn 15426).

## Route 42 Notes
- Requirements: Surf (Ravioli), Cut (KIMCHI).
- Pacing coordinate for encounters: (50, 12).
- Adjacent Maps: Ecruteak City (1_1), Mahogany Town (2_7), Mt. Mortar (3_1).
## Battle Tactics: Suicune vs Gastly
- Suicune (Lv40) in Crystal knows Bubblebeam, Rain Dance, Gust, and Roar.
- XENON (Gastly) is Ghost-type, making it immune to Roar. This prevents Suicune from forcing XENON out or ending the battle via Roar, even when trapped by Mean Look.
- Mean Look is the priority move to prevent Suicune from fleeing.
- Hypnosis will be used to keep Suicune immobile for capture.
- Status: XENON is Lv17 (Correcting previous turn's Lv15 hallucination). Training to Lv18 for Repel Trick.
- **Roamer Immunity Check**: Roar (Normal) vs Ghost (Immune). Trapping confirmed viable.
## Training Log: XENON to Lv18
- **Start Turn**: 15504
- **Current Status**: Lv17 (3263 EXP). Needs 536 more EXP for Lv18.
- **Goal**: Reach Lv18 to enable Repel Trick on Route 42 (Wild Pokemon levels are 13-17, Suicune is 40).

## Tile Mechanics
- Route 42 (59, 8): FLOOR_UP_WALL. Hypothesized traversable from South. Verification pending.
- TALL_GRASS: Traversable. Triggers wild encounters.
- WATER: Traversable with Surf. Triggers wild encounters.
- FLOOR: Standard traversable ground.
- WALL: Impassable boundary.
- HEADBUTT_TREE: Impassable; can be Headbutted.
- CUT_TREE: Impassable; requires Cut (HM01).
- LEDGE: One-way jump South. Verified.
- WARP: Map transition. Verified.