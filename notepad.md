# Ice Path Strategy (B1F)

## Current Status
- **Position:** Player at (11, 1). (After pushing B1).
- **Goal:** Solve B1 (Top Right Boulder).
- **Puzzle State:**
  - **B1:** (11, 1).
  - **B2:** (7, 8).
  - **B4:** (17, 7).

## Finishing Plan
1.  **Navigate to (11, 0):**
    - From (11, 1) (if player follows): or (9, 1) (if player stays).
    - If player at (10, 1): Left to (6, 1) -> Down to (6, 6) -> Right to (10, 6) -> Up to (10, 0) -> Right to (11, 0).
2.  **Push Down:**
    - Push B1 Down into Pit (11, 2).
3.  **Next:** Solve B2.