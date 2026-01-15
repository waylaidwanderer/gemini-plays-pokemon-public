## Strategy: Great Sea Bypass to Suicune
**Start Turn:** 48900 (Quest: Trigger Suicune Overworld Sighting)

The city is a maze of 'FLOOR_UP_WALL' barriers. I will Surf around the entire island via Route 40 to reach the West Beach.

### Step-by-Step Execution Plan
1. Surf North-East to Route 40 via the warp at Route 41 (42, 0). <- CURRENT TASK
2. In Route 40, Surf West to the edge of the map.
3. Surf South to enter the West Shore of Cianwood City.
4. Land on the beach and walk North to (14, 10) to trigger Suicune.

## Navigation: Route 41 Gaps
- Lane 1 (X=0-4) to Lane 2 (X=6-15): Gap at (5, 32).
- Lane 2 to Lane 3 (X=17-23): Gap at (16, 31).
- Lane 3 to Lane 4 (X=25-34): Gap at (24, 27).
- Lane 4 to Lane 5 (X=36-49): Gap at (35, 31).

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