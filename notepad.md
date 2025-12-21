# Tile Mechanics
- FLOOR: Traversable.
- WALL: Impassable.
- SHUTTER: Impassable when CLOSED (WALL), traversable when OPEN (FLOOR).

# Puzzle: Goldenrod Underground Switch Puzzle
- Goal: Reach the Underground Warehouse (Map 3_55).
- Strategy: Systematic testing of switches to determine shutter logic.

## Failed Attempts
1. Attempt 1 (Turn 9901): Sequence 3-ON -> 2-ON -> 1-ON.
   - Result: Shutters (10, 6), (16, 6), (6, 8) CLOSED. Path BLOCKED.

## Switch Testing Log
- Phase: Reset to Baseline (All OFF)
- Turn 9911: Switch 2 -> OFF.
- Turn 9917: Switch 3 -> OFF.
- Turn 9920: Moving to Switch 1 (16, 1) to turn it OFF.

## Verified Baseline (All Switches OFF) - PENDING VERIFICATION
- Expected Shutter States (to be verified after Switch 1 is OFF):
  - (2, 6): ?
  - (10, 6): ?
  - (16, 6): ?
  - (12, 8): ?
  - (6, 8): ?

# Area Notes
- Warehouse Entrance: South-east unseen area.
- Return Ladders: (23, 3), (21, 25), and (5, 25) lead to 3_53.
- Key NPCs: Rocket Girl (19, 12), Emergency Switch (20, 11).