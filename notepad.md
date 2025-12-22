# Tile Mechanics
- FLOOR: Traversable.
- WALL: Impassable.
- SHUTTER: Dynamic collision. Impassable (WALL) when CLOSED, Traversable (FLOOR) when OPEN.
- Switch (2,1), (10,1), (16,1): Background objects. Interact from row 2 (facing UP).

# Underground Warehouse Puzzle
- Goal: Open path to Warehouse Entrance (Map 3_55).
- Start Turn: 10544.

# Systematic Shutter Mapping
- Baseline (0,0,0): S1=OFF, S2=OFF, S3=OFF.
  - (2,6): CLOSED
  - (3,6): CLOSED
  - (10,6): CLOSED
  - (16,6): CLOSED
  - (6,8): CLOSED
  - (12,8): OPEN
  - (17,6): CLOSED
  - (17,7): CLOSED
- Test S1 (1,0,0): ?
- Test S2 (0,1,0): ?
- Test S3 (0,0,1):
  - (2,6): OPEN
  - (3,6): OPEN
  - (Others): Same as baseline.

# Area Notes
- Warehouse Entrance: Southeast quadrant (likely Map 3_55).
- EXIT: (21, 29) leads back to Goldenrod City. Do NOT use.

# Lessons Learned
- Verify shutter states visually by walking to them.
- 3-2-1 sequence (S3 -> S2 -> S1) is the rumored solution.
- The path to the warehouse is likely in the southeast area behind the shutters.