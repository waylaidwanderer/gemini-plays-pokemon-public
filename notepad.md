# Ice Path Strategy (B1F)

## Current Status
- **Position:** Player at (10, 4).
- **Goal:** Solve B1 (Top Right Boulder).
- **Puzzle State:**
  - **B1:** (12, 5).
  - **B2:** (7, 8).
  - **B4:** (17, 7).

## Execution Plan (Sliding)
1.  **Navigate to (12, 4):**
    - From (10, 4): Slide Left to (9, 4).
    - Slide Up to (9, 3).
    - Slide Right to (12, 3).
    - Slide Up to (12, 1).
    - Slide Down to (12, 4) (Hit B1 at 12, 5).
2.  **Position at (13, 5):**
    - From (12, 4): Slide Right to (13, 4).
    - Slide Down to (13, 5).
3.  **Push B1 Left:**
    - Push Left x2. B1 to (10, 5).
4.  **Finish:**
    - Navigate to (10, 6) -> Push Up to (10, 1) -> Right to (11, 1) -> Down to (11, 2).