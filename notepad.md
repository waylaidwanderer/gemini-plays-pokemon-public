## Strategy: Inner Channel Zig-Zag to Suicune
**Start Turn:** 48900 (Quest: Trigger Suicune Overworld Sighting)

Cianwood's buoy walls (X=26, X=22, X=19) must be bypassed using specific gaps:
1. X=26 Wall Gap: Row 10-14 (Target: (25, 10))
2. X=22 Wall Gap: Row 16-24 (Target: (21, 16))
3. X=19 Wall Gap: Row 16-17 (Target: (18, 16))

### Execution Plan
1. Surf to (25, 10) via gap at (26, 10). - DONE
2. Surf to (21, 16) via gap at (22, 16). - DONE
3. Surf to (18, 18) via gap at (19, 18). <- CURRENT TASK
4. Surf North to (18, 16), then West to (13, 16) to land.
5. Walk to (14, 10) to trigger Suicune sighting.

## Tile Mechanics
- FLOOR: Standard ground.
- WALL: Impassable.
- WATER: Surf required.
- BUOY: Impassable water barrier.
- FLOOR_UP_WALL: Impassable from North (blocks Down).

## Failed Hypotheses
- Row 8 Bypass: Blocked by BUOY at (26, 8).
- Route 40 Bypass: Dead end on the West.
- Southern Crossing: Blocked by multiple FLOOR_UP_WALL lines.

## Inventory Check
- Super Repel: 5 remaining. Last applied turn 49278. (~10 steps remaining per Overwatch).
- Party: Calcifer (Lv 64) leads. Ready for Eusine.