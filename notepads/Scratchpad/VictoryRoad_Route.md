# Scratchpad: Victory Road Route & Puzzle States
- Route Started: Turn 107326 | Timestamp: Friday, June 19, 2026 at 12:25 PM PDT
- Current Position: (23, 7) on Victory Road 2F East (Map 0_194) | Turn: 107686

## Scientific Testing Plan for Victory Road Exit
We must locate the exact exit warp tile by systematically investigating the 2F East northeast corner.

### Hypothesis 1: 3F East Northeast Corner (Completed Testing)
- **Hypothesis**: The true exit of Victory Road is on the 3rd Floor (3F) East in the northeast corner (Columns 20-28, Rows 0-2).
- **Testing Method**: Systematically step on and test Row 0 and Row 1 candidate tiles.
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
  - (21, 0): Pressed Up at Turn 107632. Result: BUMPED (solid rock wall).
  - (20, 0): Pressed Up at Turn 107639. Result: BUMPED (solid rock wall).
  - (19, 0): Pressed Up at Turn 107645. Result: BUMPED (solid rock wall).
- **Conclusion**: Hypothesis 1 is completely DISPROVEN. No exit warp exists on 3rd Floor (3F) East Row 0 or Row 1 on Columns 20-28.

### Hypothesis 2: 2F East Northeast Corner (Active)
- **Hypothesis**: The exit is at (28, 1) on 2F East, reached by taking the ladder at (26, 8) on 3F East down to (27, 7) on 2F East.
- **Routing Strategy Audit**:
  - Note: (27, 7) on 2F East is inside a completely closed, isolated ground-level pocket on 2F East (bounded by Koga's plateau to the south and the Row 6 rock wall to the north). 
  - If we land at (27, 7) on 2F East, we cannot walk north to Row 1/Row 2 due to the Row 6 solid rock wall across Columns 24-28.
  - Therefore, to access the true northern part of 2F East on ground level, we must utilize the southern ground corridor at Row 16 to cross from 2F East to 2F West, and bypass the plateau.
  - Let's construct a complete unblocked pathing hypothesis via 2F West to reach the northern half of 2F East on ground level.
- **Status**: Active. Backtracking to 3F East via (23, 7) ladder to cross over to the west side.

### Hypothesis 3: 1F East Northeast Corner (On Hold)
- **Hypothesis**: The true exit is on 1F East.
- **Status**: On hold pending results of Hypothesis 2.

## Current Pathing Instructions:
- We are at (23, 7) on 2F East. We must climb back up to 3F East using the ladder at (23, 7) to start navigating towards the west side of 2F/3F.