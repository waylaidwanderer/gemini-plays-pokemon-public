# Warehouse Switch Puzzle - Route Correction
- **Finding:** The path via (12, 8) -> (9, 9) leads to a dead end at (9, 10) (Wall).
- **New Strategy:** Explore the (6, 8) path which opened in state [Sw3 OFF, Sw2 ON, Sw1 ON].
- **Hypothesis:** (6, 8) leads to (6, 12) -> (9, 12).
- **Current State:** Sw3 ON, Sw2 OFF, Sw1 ON.
- **Target State:** Sw3 OFF, Sw2 ON, Sw1 ON.

## Plan
1. Exit current area: North to (9, 8) -> East to (12, 8) -> North to Main Hall.
2. Turn Switch 2 ON.
3. Turn Switch 3 OFF.
4. Enter (6, 8) and go South.