## Plan: Reach Suicune at (14, 10)
- Step 1: Reach (12, 28) and Surf North. <- CURRENT TASK
- Step 2: Land at (12, 19).
- Step 3: Walk zigzag through town gaps to (14, 10):
  - (12, 19) -> (12, 16) -> (11, 16) -> (11, 15) gap -> (11, 14).
  - (11, 14) -> (13, 14) -> (13, 13) gap -> (13, 12).
  - (13, 12) -> (14, 12) -> (14, 10).
- Step 4: Trigger Suicune sighting.

## Tile Mechanics (Verified)
- FLOOR: Traversable.
- WALL: Impassable.
- WATER: Requires Surf.
- LEDGE_HOP_DOWN: One-way jump (North to South).
- FLOOR_UP_WALL: Impassable cliff face.
- BUOY: Impassable hard wall.

## Navigation Notes
- Row 15 Gap: (11, 15) is the only northward passage at Row 15 in this sector.
- Row 13 Gap: (13, 13) is the only northward passage at Row 13 in this sector.
- Ledge (10, 15): Blocks direct northward progress from town center.
- (12, 13) and (11, 13) are WALL tiles.

## Battle Strategy: Eusine
- Lead with Calcifer (Lv 64 Typhlosion). Use Flamethrower.

## Technical Status
- Python Sandbox: Container not running. Tools offline.
- Super Repel: Active (Used Turn 49091).