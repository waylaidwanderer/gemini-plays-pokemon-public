## Strategy: Great Sea Bypass to Suicune
**Start Turn:** 48900 (Quest: Trigger Suicune Overworld Sighting)

The city is a maze of 'FLOOR_UP_WALL' barriers. I will Surf around the entire island via Route 41 to reach the West Beach.

### Step-by-Step Execution Plan
1. Surf East to re-enter Route 41 at (29, 32). <- CURRENT TASK
2. Surf around the island's southern or northern tip to reach the West Shore.
3. Re-enter Cianwood City from the West and land on the beach at (2, 35).
4. Walk North to (14, 10) to trigger Suicune.

## Tile Mechanics: Cianwood City
- FLOOR: Standard traversable ground.
- WALL: Standard impassable barrier.
- WATER: Traversable only with Surf HM.
- BUOY: Impassable water barrier.
- DOOR: Warp point to building interior.
- LEDGE_HOP_DOWN: One-way jump South. Impassable from the North side (cannot jump back up).
- FLOOR_UP_WALL: Impassable from the North. Behaves like a wall when moving Down into it.

## Failed Hypotheses & Lessons
- Inner Channel North (X=13-17): Blocked at Row 15 by a solid wall of WALL tiles.
- City Corridor North: Blocked by recurring 'FLOOR_UP_WALL' barriers at Rows 46, 48, and 50.
- X=12 Corridor: Blocked at (12, 50) by 'FLOOR_UP_WALL'.
- X=20 Corridor: Blocked by 'WALL' at (20, 46-49).

## Inventory Check
- Super Repel: 7 remaining. Last applied turn 49241. (~200 steps available).

## Battle Strategy: Eusine
- Lead: Calcifer (Lv 64 Typhlosion).
- Strategy: Sweep with Flamethrower. OHKO potential on most targets.