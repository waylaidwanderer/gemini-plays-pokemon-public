# Ice Path Strategy (B1F)

## Current Status
- **Position:** Player at (6, 1).
- **Goal:** Reach B1 at (11, 7) to solve it.
- **Puzzle State:** All Boulders Reset.
  - **B1:** (11, 7).
  - **B2:** (7, 8).
  - **B3:** (9, 11).
  - **B4:** (17, 7).

## Master Plan
1.  **Navigate:** Go South via West Side (Col 5) to (9, 10).
2.  **Traverse:** Go South to Row 16 -> East to Col 12 -> North to (11, 8).
3.  **B1 Solve:**
    - Push B1 Up to (11, 5).
    - Go Left to (10, 5) -> Up to (10, 1) -> Right to (11, 1).
    - Push Down into Pit (11, 2).
4.  **B2 Solve:**
    - Go to (8, 8). Push B2 Left to (5, 8).
    - Go around to (5, 9). Push Up to (5, 6).
    - Go North to Row 1 -> West to (6, 6). Push Left to (4, 6) -> Down to Pit (4, 7).
5.  **B3 & B4:** Solve subsequently.

## Immediate Action
- Navigate to (9, 10).