# Scratchpad: Victory Road Route & Puzzle States
- Route Started: Turn 107326 | Timestamp: Friday, June 19, 2026 at 12:25 PM PDT
- Current Position: (22, 0) on Victory Road 3F East (Map 0_198) | Turn: 107624

## Scientific Testing Plan for Victory Road Exit
We must locate the exact exit warp tile by systematically investigating the 3F East northeast corner.

### Hypothesis 1: 3F East Northeast Corner (Active)
- **Hypothesis**: The true exit of Victory Road is on the 3rd Floor (3F) East in the northeast corner (Columns 27-28, Rows 0-2).
- **Testing Method**:
  1. Push Boulder C2 at (24, 10) Left to (22, 10). (Completed!)
  2. Walk Left along Row 13 to (13, 13) and bypass central walls. (Completed!)
  3. Push Boulder C4 at (13, 12) Up to (13, 11) to clear Column 13. (Completed!)
  4. Walk Up Column 13 to Row 2. (Completed!)
  5. Walk Right along Row 2 to (27, 2). (Completed!)
  6. Systematically step on (27, 2), (28, 2), (27, 1), (28, 1), (27, 0), and (28, 0) and check for transition to Route 23 North (Map 0_34).
- **Empirical Test Results on 3F East**:
  - (28, 2): Stepped on at Turn 107581. Result: No warp triggered.
  - (28, 1): Stepped on at Turn 107589. Result: No warp triggered.
  - (28, 0): Pressed Up at Turn 107590. Result: BUMPED (solid rock wall).
  - (27, 0): Pressed Up at Turn 107599. Result: BUMPED (solid rock wall).
  - (26, 0): Pressed Up at Turn 107602. Result: BUMPED (solid rock wall).
  - (25, 0): Pressed Up at Turn 107606. Result: BUMPED (solid rock wall).
  - (24, 0): Pressed Up at Turn 107610. Result: BUMPED (solid rock wall).
  - (23, 0): Pressed Up at Turn 107617. Result: BUMPED (solid rock wall).
  - (22, 0): Pressed Up at Turn 107621. Result: BUMPED (solid rock wall).
- **Conclusion**: Hypothesis 1 is completely DISPROVEN. No exit warp exists on 3rd Floor (3F) East Row 0 or Row 1 on Columns 24-28.

### Hypothesis 2: 2F East Northeast Corner (Active)
- **Hypothesis**: The exit is at (28, 1) on 2F East, reached by taking the ladder at (26, 8) on 3F East down to (27, 7) on 2F East.
- **Status**: Active. We must backtrack to the (26, 8) ladder to descend.

### Hypothesis 3: 1F East Northeast Corner (On Hold)
- **Hypothesis**: The true exit is on 1F East.
- **Status**: On hold pending results of Hypothesis 2.

## Current Pathing Instructions:
- Backtrack Left to Column 23, then Down to the ladder at (26, 8) on 3F East to descend to 2F East.