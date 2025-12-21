# Tile Mechanics
- FLOOR: Traversable.
- WALL/SHUTTER: Impassable when CLOSED (WALL collision), traversable when OPEN (FLOOR collision).

# Puzzle: Goldenrod Underground Switch Puzzle
- Goal: Reach the Underground Warehouse (Map 3_55).
- Strategy: Systematic testing of switches to determine shutter logic.

## Systematic Testing
- Baseline (0, 0, 0): (2,6) OPEN, (10,6) CLOSED, (16,6) CLOSED, (6,8) CLOSED, (12,8) OPEN, (6,9) OPEN.

### Test 1: Switch 1 (16, 1) -> ON
- Status: Complete.
- Observations (compared to baseline 0,0,0):
  - (16, 6): OPEN (Was CLOSED).
  - (2, 6): CLOSED (Was OPEN).
  - (6, 9): CLOSED (Was OPEN).
  - (12, 8), (10, 6), (6, 8): No change.

### Test 2: Switch 2 (10, 1) -> ON
- Status: Moving to turn Switch 1 OFF first.
- Observations: PENDING.

# Area Notes
- Warehouse Entrance: South-east unseen area.
- Return Ladders: (23, 3), (21, 25), and (5, 25) lead to 3_53.
- Key NPCs: Rocket Girl (19, 12), Emergency Switch (20, 11).