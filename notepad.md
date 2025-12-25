# Ice Path Strategy (B1F)

## Current Status
- **Position:** Player at (10, 1).
- **Goal:** Solve B1 (Top Right Boulder).
- **Puzzle State:**
  - **B1:** (10, 1).
  - **B2:** (7, 8).
  - **B4:** (17, 7).

## Finishing Plan
1.  **Navigate to (9, 1):**
    - From (10, 1): Slide Down to (10, 6) -> Left to (6, 6) -> Up to (6, 1) -> Right to (9, 1).
2.  **Push Right:**
    - Push B1 to (11, 1).
3.  **Push Down:**
    - Go to (11, 0) (via 10, 0 -> 11, 0).
    - Push B1 Down into Pit (11, 2).
4.  **Next:** Solve B2.