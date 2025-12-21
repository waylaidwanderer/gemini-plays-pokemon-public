# Tile Mechanics
- FLOOR: Traversable.
- WALL/SHUTTER: Impassable when CLOSED (WALL collision), traversable when OPEN (FLOOR collision).

# Puzzle: Goldenrod Underground Switch Puzzle
- Goal: Reach the Underground Warehouse (Map 3_55).
- Strategy: Systematic testing of switches to determine shutter logic.

## Systematic Testing
- Baseline (0, 0, 0): (2,6) CLOSED, (10,6) CLOSED, (16,6) CLOSED, (6,8) CLOSED, (12,8) OPEN.

### Test 1: Switch 1 (16, 1) -> ON
- Status: Observation phase.
- Observations:
  - (16, 6): OPEN (Confirmed standing on it Turn 9937).
  - (12, 8): Moving to verify.
  - (10, 6): ?
  - (2, 6): ?
  - (6, 8): ?

# Area Notes
- Warehouse Entrance: South-east unseen area.
- Return Ladders: (23, 3), (21, 25), and (5, 25) lead to 3_53.
- Key NPCs: Rocket Girl (19, 12), Emergency Switch (20, 11).