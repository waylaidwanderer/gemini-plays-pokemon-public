# Tile Mechanics
- FLOOR: Traversable.
- WALL/SHUTTER: Impassable when CLOSED (WALL collision), traversable when OPEN (FLOOR collision).

# Puzzle: Goldenrod Underground Switch Puzzle
- Goal: Reach the Underground Warehouse (Map 3_55).
- Strategy: Systematic testing of switches to determine shutter logic.

## Systematic Testing
- Baseline (0, 0, 0): ALL SHUTTERS CLOSED.
  - (2, 6): CLOSED (Visual confirmed Turn 9957)
  - (10, 6): CLOSED (Collision confirmed Turn 9956)
  - (16, 6): CLOSED (Confirmed Turn 9954)
  - (6, 8): CLOSED (Visual confirmed Turn 9957)
  - (12, 8): CLOSED (Confirmed Turn 9953)
  - (6, 9): CLOSED (Visual confirmed Turn 9957)

### Test 1: Switch 1 (16, 1) -> ON
- Status: Complete.
- Observations (compared to baseline 0,0,0):
  - (16, 6): OPEN (Was CLOSED).
  - (2, 6): CLOSED (No change).
  - (6, 9): CLOSED (No change).
  - (12, 8), (10, 6), (6, 8): No change.
  - NOTE: Need to re-verify Switch 1 effects if I was wrong about (2, 6) and (6, 9) baseline.

### Test 2: Switch 2 (10, 1) -> ON
- Status: Observation phase.
- Observations (compared to baseline 0,0,0):
  - (10, 6): OPEN (Visual confirmed Turn 9963).
  - (2, 6): ?
  - (16, 6): ?
  - (6, 8): ?
  - (12, 8): ?
  - (6, 9): ?

# Area Notes
- Warehouse Entrance: South-east unseen area.
- Return Ladders: (23, 3), (21, 25), and (5, 25) lead to 3_53.
- Key NPCs: Rocket Girl (19, 12), Emergency Switch (20, 11).