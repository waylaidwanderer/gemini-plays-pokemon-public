# Ice Path Strategy (B1F)

## Current Status
- **Position:** Player at (10, 5).
- **Goal:** Solve B1 (Top Right Boulder).
- **Puzzle State:**
  - **B1:** (12, 5).
  - **B2:** (7, 8).
  - **B4:** (17, 7).

## Optimized Plan
1.  **Navigate to (13, 5) via (9, 3):**
    - **Step 1:** Slide Left to (9, 5).
    - **Step 2:** Slide Up to (9, 3).
    - **Step 3:** Slide Right to (12, 3).
    - **Step 4:** Slide Up to (12, 1).
    - **Step 5:** Slide Down to (12, 4) (Hit B1 at 12, 5).
    - **Step 6:** Slide Right to (13, 4).
    - **Step 7:** Slide Down to (13, 5).
2.  **Push B1 Left:**
    - From (13, 5), push Left x2. B1 goes to (10, 5).
3.  **Finish:**
    - Navigate to (10, 6) -> Push Up to (10, 1) -> Right to (11, 1) -> Down to (11, 2).