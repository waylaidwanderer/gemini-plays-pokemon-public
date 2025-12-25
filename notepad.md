# Ice Path Strategy (B1F)

## Current Status
- **Position:** Player at (10, 1).
- **Goal:** Solve B1 (Top Right Boulder).
- **Puzzle State:**
  - **B1:** At (10, 3).
  - **B2:** (7, 8).
  - **B4:** (17, 7).

## Current Status
- **Position:** Player at (13, 2).
- **Goal:** Solve B2 (Bottom Left Boulder).
- **Puzzle State:**
  - **B1:** Solved (In Pit 11, 2).
  - **B2:** At (7, 8).
  - **B4:** At (17, 7).

## B2 Strategy
1.  **Navigate to (8, 8):**
    - Path: (12, 2) -> (12, 1) -> (2, 1) -> (2, 3) -> (5, 3) -> (5, 9) -> (8, 9) -> (8, 8).
2.  **Push Left:** Push B2 from (7, 8) to (5, 8).
3.  **Push Up:** Push B2 from (5, 8) to (5, 7).
4.  **Push Left:** Push B2 into Pit (4, 7).

## Finishing Plan
- After B2 is done, check B4 at (17, 7).
- B4 needs to go to Pit (12, 13) or similar? Check map later.