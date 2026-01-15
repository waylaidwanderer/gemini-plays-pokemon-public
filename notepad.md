## Plan: Reach North Plateau (Sea Route)
- Step 1: Surf North at X=27 to Row 8. <- CURRENT TASK
- Step 2: Surf West at Row 8 to X=16.
- Step 3: Surf South at X=16 to (16, 11) and land.
- Step 4: Walk to (14, 10) to trigger Suicune sighting.

## Tile Mechanics (Verified)
- FLOOR: Traversable.
- WALL: Impassable.
- WATER: Requires Surf.
- BUOY: Impassable (Verified Turn 49063: Movement blocked Up at (23, 10) into BUOY).
- LEDGE_HOP_DOWN: One-way jump (North to South).
- FLOOR_UP_WALL: Impassable cliff face.

## Navigation Notes
- Buoy Wall: X=22-26, Row 9. Bypass at X=27.
- Ledge: (10, 15) blocks direct North path from center.
- Landing: (16, 11) is the target landing spot from the sea.
- Suicune Trigger: (14, 10).

## Battle Strategy: Eusine
- Party Status: XENON (44), Calcifer (64), KIMCHI (52), GNEISS (55), GORP (50), ICARUS (19).
- Strategy: Lead with XENON for Hypnosis/Confuse Ray to disrupt and Night Shade for fixed damage. Use GORP for tanking.

## Technical Status
- find_path_v6_fixed: Failing with 'sandbox not running' errors. Manual navigation required.
- Super Repel: Active since Turn 49046.