# Suicune Quest (Cianwood)
- **Start Turn:** 48900
- **Timestamp:** Turn 49381 (Resumed)
- **Status:** Back in city at (12, 49). Executing Western Corridor path.

## Execution Plan (Direct Path)
1. Walk to (12, 28) and Surf North. <- CURRENT TASK
2. Land at (12, 19).
3. Walk North to (14, 10) via Row 12 corridor.
4. Trigger Suicune sighting.

## Strategy: Western Corridor Path
The northern plateau is only accessible from the far west (X=2). The city is a maze of walls and ledges. I am using a custom pathfinding tool to identify the most efficient route through the barriers.

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