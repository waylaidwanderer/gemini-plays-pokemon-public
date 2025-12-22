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
- Test S1 (1,0,0):
  - (16,6), (17,6): OPEN
  - (12,8): CLOSED
  - (Others): Same as baseline. (Verified Turn 10626)
  - Note: Row 7 is a permanent floor row, not a shutter row.
- Test S2 (0,1,0):
  - (10,6): OPEN
  - (6,8): OPEN
  - (12,8): CLOSED
  - (Others): Same as baseline.
- Test S3 (0,0,1):
  - (2,6), (3,6): OPEN
  - (Others): Same as baseline.

# Final Puzzle Logic (Verified)
- S3 toggles: (2,6), (3,6)
- S2 toggles: (10,6), (6,8), (12,8)
- S1 toggles: (16,6), (17,6), (16,7), (17,7), (12,8)
- Baseline (0,0,0): (12,8) is the ONLY open shutter.
- Solution (3-2-1 Order):
  1. Press S3 (ON) -> Opens (2,6), (3,6). (12,8) remains OPEN.
  2. Press S2 (ON) -> Opens (10,6), (6,8). Closes (12,8).
  3. Press S1 (ON) -> Opens (16,6), (17,6). Opens (12,8).
  Result: ALL paths open.

# Current Strategy: Reset and Execute
1. Shutter Report (10683) shows an inconsistent state (only (6,8) open, (12,8) closed).
2. Toggling Switch 3 OFF to begin a full reset of all switches (S1, S2, S3) to OFF.
3. Will visit S2 and S1 to confirm they are OFF.
4. Once all are OFF, execute 3-2-1 sequence (S3 -> S2 -> S1) without interruption.
5. Enter Warehouse.

# Area Notes
- Warehouse Entrance: Southeast quadrant (likely Map 3_55).
- EXIT: (21, 29) leads back to Goldenrod City. Do NOT use.

# Lessons Learned
- Verify shutter states visually by walking to them.
- 3-2-1 sequence (S3 -> S2 -> S1) is the rumored solution.
- The path to the warehouse is likely in the southeast area behind the shutters.