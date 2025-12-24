# Ice Path Strategy
- **Current State:** At (15, 14).
- **Goal:** Solve North Ice Room puzzle to reach (16, 8) Floor.
- **Corrected Solution Sequence:**
  1. **Up** to (15, 12) [Stop at Wall 15,11].
  2. **Left** to (9, 12) [Stop at Rock 8,12].
  3. **Up** to (9, 2) [Stop at Wall 9,1].
  4. **Left** to (8, 2) [Stop at Rock 7,2].
  5. **Down** to (8, 11) [Stop at Rock 8,12].
  6. **Left** to (7, 11) [Stop at Rock 6,11].
  7. **Up** to (7, 3) [Stop at Rock 7,2].
  8. **Left** to (2, 3) [Stop at Wall 1,3].
  9. **Down** to (2, 5) [Stop at Rock 2,6].
  10. **Right** to (11, 5) [Stop at Rock 12,5].
  11. **Down** to (11, 8) [Stop at Rock 11,9].
  12. **Right** to (16, 8) [Exit to Floor].

# Map Structure
- **North Ice Room:** Puzzle leading to Central Floor (Row 8-9).
- **Central Floor (16-21, 8-9):** Access to Center Ice (x=22+).
- **Center Ice:** Path to NE Ladder (x=18-34, y=2-4).