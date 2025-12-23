# Suicune Capture Strategy (Crystal Version)
## Primary Goal: Capture Suicune
- Step 1: Obtain Clear Bell. (COMPLETE)
- Step 2: Access Tin Tower. Defeat the Wise Trio. (COMPLETE)
- Step 3: Encounter Suicune at Tin Tower. (COMPLETE - It fled).
- Step 5: Prepare Catcher. XENON (Gastly) with Mean Look + Hypnosis. (Target: Lv18+ for Repel efficiency).

## Roamer Mechanics & Interception
- Roamers move between adjacent maps whenever the player crosses a map boundary.
- Interception: Identify roamer's map via Pokédex. Stay on that map and pace in grass/water.
- Battle Strategy: XENON (Gastly) uses Mean Look immediately to trap. Hypnosis to sleep.
- Repel Trick: Lead PKMN level must be STRICTLY HIGHER than local wild PKMN. Route 42 locals reach Lv17, so XENON (Lv17) is not 100% effective. Target: Lv18.

## Financial Strategy
- Current Funds: ¥41.
- Plan: Sell 9 Super Potions in Mahogany Town to fund Super Repels.
- Alternative: Find and defeat undefeated trainers.

## Tile Mechanics Scientific Testing
### FLOOR_UP_WALL Verification
- **Observation**: Tiles labeled FLOOR_UP_WALL exist on Route 42.
- **Hypothesis**: These tiles allow movement North but block movement South, East, and West.
- **Test 1**: Attempt to move South onto (50, 14) from (50, 13).
- **Result 1**: Movement blocked. (Turn 15363).
- **Conclusion 1**: Entering from the North is impossible.
- **Test 2**: Attempt to move North onto (59, 8) from (59, 9).

## Global Tile Mechanics
- FLOOR, TALL_GRASS, DIRT, SAND: Traversable.
- WALL, FENCE, MOUNTAIN, MART_SHELF, COUNTER: Impassable.
- FLOOR_UP_WALL: Asserted North only (Route 42).
- LEDGE: One-way jump South.
- WATER: Requires Surf (HM03).
- HEADBUTT_TREE: Impassable; can be Headbutted.
- CUT_TREE: Impassable; requires Cut (HM01).
- WARP: Map transition (Doors, Stairs, Cave Entrances).

## Route 42 Notes
- Requirements: Surf (Ravioli), Cut (KIMCHI).
- Pacing coordinate for encounters: (50, 12).
- Adjacent Maps: Ecruteak City (1_1), Mahogany Town (2_7), Mt. Mortar (3_1).

## Progress Log
- Lv17 XENON training complete. (Turn 15201)
- CRITICAL: Out of Repels and funds. (Turn 15361)
- Heading to Mahogany Town to sell items and restock. (Turn 15364)