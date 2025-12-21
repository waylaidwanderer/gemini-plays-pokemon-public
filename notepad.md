# Tile Mechanics
- FLOOR: Traversable.
- WALL/SHUTTER: Impassable when CLOSED (WALL collision), traversable when OPEN (FLOOR collision).

# Puzzle: Goldenrod Underground Switch Puzzle
- Goal: Reach the Underground Warehouse (Map 3_55).
- Strategy: Systematic testing of switches to determine shutter logic.

## Systematic Testing
- Baseline (0, 0, 0): ALL SHUTTERS CLOSED.
  - (2, 6), (10, 6), (16, 6), (6, 8), (12, 8), (6, 9): CLOSED.

### Test 1: Switch 1 (16, 1) -> ON (1, 0, 0)
- Status: Complete.
- Observations: (16, 6) OPEN, (12, 8) OPEN. Others CLOSED.

### Test 2: Switch 2 (10, 1) -> ON (0, 1, 0)
- Status: Complete.
- Observations: (10, 6), (10, 7), (11, 6), (11, 7) OPEN. (6, 8), (6, 9) OPEN. Others CLOSED.

### Test 3: Switch 3 (2, 1) -> ON (0, 0, 1)
- Status: Complete (Turn 9985).
- Observations: (2, 6), (3, 6) OPEN. Others CLOSED.

### Test 4: Switch 3 ON, Switch 2 ON (0, 1, 1)
- Status: Observation phase (Started Turn 10003).
- Strategy: Combining S3 (far left) and S2 (middle/left) to clear both shutter rows.

# Area Notes
- Warehouse Entrance: South-east unseen area.
- Return Ladders: (23, 3), (21, 25), and (5, 25) lead to 3_53.
- Key NPCs: Rocket Girl (19, 12), Emergency Switch (20, 11).