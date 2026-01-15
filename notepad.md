## Plan: Reach North Plateau (Sea Route)
- Step 1: Surf to (27, 10) then (23, 10). <- CURRENT TASK
- Step 2: Surf North to (23, 8) to bypass Buoy Wall (X=22, Row 9-15).
- Step 3: Surf West to (16, 8) then South to land at (16, 12).
- Step 4: Walk to (14, 10) for Suicune sighting.

## Tile Mechanics (Verified)
- FLOOR: Traversable.
- WALL: Impassable.
- WATER: Requires Surf.
- BUOY: Impassable (Verified Turn 49063: Movement blocked Up at (23, 10) into BUOY).
- LEDGE_HOP_DOWN: One-way jump (North to South).
- FLOOR_UP_WALL: Impassable cliff face.

## Navigation Notes
- Buoy Wall 1: X=26, Row 0-9. Bypass at Row 10.
- Buoy Wall 2: X=22, Row 9-15. Bypass at Row 8.
- Ledge: (10, 15) blocks direct North path from center.
- Landing: (16, 12) is the target landing spot from the sea.
- Suicune Trigger: (14, 10).

## Battle Strategy: Eusine
- Strategy: Lead with XENON (44) for Hypnosis/Confuse Ray. Night Shade for fixed damage. GORP (50) for tanking.

## Technical Status
- find_path_v6_fixed: Failing with 'sandbox not running' errors.
- Super Repel: Active (approx. 50 steps remaining).