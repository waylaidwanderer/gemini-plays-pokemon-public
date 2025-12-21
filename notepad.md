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

### Test 4: Switch 3 ON, Switch 2 ON (0, 1, 1)
- Status: Complete. 
- Observations: Path to Warehouse Entrance (18, 6) remains blocked by CLOSED shutters at (16, 6) and (12, 8).

### Final Sequence: 3-2-1
- Step 1: Switch 3 ON (Turn 9993).
- Step 2: Switch 2 ON (Turn 10002).
- Step 3: Switch 1 ON (Started Turn 10019).
- Result (1, 1, 1): (2,6) OPEN, (10,6) CLOSED, (16,6) CLOSED. BLOCKED.

### Order Testing
- Goal: Find order that opens (10,6) or (16,6).

# Area Notes
- Warehouse Entrance: South-east unseen area.
- Return Ladders: (23, 3), (21, 25), and (5, 25) lead to 3_53.
- Key NPCs: Rocket Girl (19, 12), Emergency Switch (20, 11).