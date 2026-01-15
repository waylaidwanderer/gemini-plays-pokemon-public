# Suicune Quest (Cianwood)
- **Start Turn:** 48900
- **Timestamp:** Turn 49381 (Resumed)
- **Status:** At (12, 28). Initiating southern bypass route via Surf.

## Execution Plan (Southern Bypass)
1. Use Surf at (12, 28). <- CURRENT TASK
2. Surf East to (27, 28), then South to (27, 51).
3. Land at (26, 51).
4. Walk West to (2, 51), then North to (2, 12).
5. Walk East to (14, 12), then North to (14, 10) to trigger Suicune.

## Strategy: Southern Bypass
The city is divided by multiple ledge lines (Row 34, 46, 48, 50) and wall lines. Terrestrial paths are blocked. The only way to reach the western corridor (X=2) is to Surf all the way to the southern edge of the map (Row 51) where the barriers end. Then, a clear walk leads to the northern plateau.

## Failed Hypotheses & Lessons
- Attempted Down move at (12, 49): Blocked by FLOOR_UP_WALL at (12, 50).
- Attempted Down move at (13, 49): Blocked by FLOOR_UP_WALL at (13, 50).
- Terrestrial Path (South): Blocked by ledge lines at Row 46, 48, 50.
- Terrestrial Path (West): Blocked by wall lines at X=11, 9, 5, 3.
- Inner Channel Water Path: Entirely blocked by buoy walls (Row 9, Row 25). Must use island hop.
- Island Hop Landing (13, 16): Dead end due to walls at Row 13/15.

## Tile Mechanics (Global)
- **FLOOR**: Traversable ground. No special effects.
- **WALL**: Impassable barrier.
- **WATER**: Requires Surf HM to traverse.
- **BUOY**: Impassable water barrier.
- **FLOOR_UP_WALL**: One-way ledge. Blocks DOWN (South) movement. Allows UP, LEFT, and RIGHT movement. (Verified at (6, 46), (7, 34)).
- **LEDGE_HOP_DOWN**: One-way jump South. Impassable from the North side.
- **DOOR**: Warp entry point. Leads to a different map.
- **BOULDER**: Requires Strength HM to push.
- **ROCK**: Small smashable rock. Requires Rock Smash HM.

## Failed Hypotheses & Lessons
- Terrestrial Path (South): Blocked by ledges.
- Great Sea Bypass (Route 40): Dead end on the West.
- Inner Channel South: Blocked at Row 15 by solid buoy line (except X=23).
- Inner Channel Water Path: Entirely blocked by buoy walls (Row 9, Row 25). Must use island hop.

## Inventory Check
- Super Repel: 4 remaining. Applied turn 49346. (~150 steps remaining).
- Party: Calcifer (Lv 64) leads. Ready for Eusine.

## Progress Summary
- All 16 Badges obtained.
- Elite Four defeated.
- Red defeated.
- Current Focus: Legendary Beast tracking.