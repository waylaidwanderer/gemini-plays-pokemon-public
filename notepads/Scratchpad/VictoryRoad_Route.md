# Scratchpad: Victory Road Route & Puzzle States
- Route Started: Turn 107326 | Timestamp: Friday, June 19, 2026 at 12:25 PM PDT
- Current Position: (19, 0) on Victory Road 3F East (Map 0_198) | Turn: 107646

## Scientific Testing Plan for Victory Road Exit
We must locate the exact exit warp tile by systematically investigating the 3F East northeast corner.

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
- **Routing Strategy**:
  - We cannot reach the (26, 8) ladder directly on 3F East because the (Columns 26-28, Rows 7-9) pocket is completely isolated on 3F East.
  - Instead, we must:
    1. Walk from (27, 5) -> Up 3 to (27, 2) -> Left 4 to (23, 2) -> Down 5 to (23, 7) on 3F East.
    2. Take the (23, 7) ladder DOWN to 2F East (lands at (23, 7) on 2F East).
    3. On 2F East, walk from (23, 7) to the ladder at (27, 7).
    4. Take the (27, 7) ladder UP to 3F East (lands at (26, 8) on 3F East).
    5. Take the (26, 8) ladder DOWN to 2F East (lands at (27, 7) on 2F East). Wait, why? Ah! Because taking the (26, 8) ladder down from 3F East lets us test if there's any other way or if the exit is there.
- **Status**: Active. Backtracking to (23, 7) ladder on 3F East.

### Hypothesis 3: 1F East Northeast Corner (On Hold)
- **Hypothesis**: The true exit is on 1F East.
- **Status**: On hold pending results of Hypothesis 2.

## Current Pathing Instructions:
- We have fully exhausted and disproved the 3F East northeast corner. We are now backtracking to the ladder at (26, 8) to descend to 2F East and test the northeast corner there.