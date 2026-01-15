## Strategy: Exploratory Reveal of Northern Plateau
**Start Turn:** 48900 (Quest: Trigger Suicune Overworld Sighting)

Current mental map indicates no valid path to (14, 10) through seen tiles. Priority is revealing unseen tiles adjacent to the plateau to identify the entrance.

### Step-by-Step Execution Plan
1. Move to the Surf point at (13, 16) and Surf East. <- CURRENT TASK
2. Navigate North to Row 8, cross West to X=21, then South to Row 11.
3. Explore (18, 11) and (17, 11) to reveal the plateau entrance.
4. Re-evaluate path to (14, 10) once more of the map is visible.

## Tile Mechanics: Cianwood City
- FLOOR: Standard traversable ground.
- WALL: Impassable barrier.
- WATER: Traversable only with Surf HM.
- BUOY: Impassable water barrier.
- FLOOR_UP_WALL: One-way ledge. Blocks DOWN movement (Y to Y+1). Allows UP and East-West movement. (Verified at (6, 46)).
- LEDGE_HOP_DOWN: One-way jump South. Impassable from the North side.

## Failed Hypotheses & Lessons
- Terrestrial Zig-Zag (South): Blocked by unseen barriers or ledges. BFS reports no path.
- Great Sea Bypass (Route 40): Dead end on the West.
- Inner Channel South: Blocked at Row 15 by solid buoy line.

## Inventory Check
- Super Repel: 4 remaining. Applied turn 49346.
- Party: Calcifer (Lv 64) leads. Ready for Eusine.