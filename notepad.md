# Ice Path Strategy (B1F)

## Current Status
- **Position:** Player at (10, 5).
- **Goal:** Solve B1 (Top Right Boulder).
- **Puzzle State:**
  - **B1:** (12, 5). (Target: 10, 5).
  - **B2:** (7, 8).
  - **B4:** (17, 7).

## Immediate Plan
1.  **Navigate to (13, 5):**
    - **Step 1:** Slide Up to (10, 0).
    - **Step 2:** Move Right to (11, 0) -> Down to (11, 1) -> Right to (12, 1).
    - **Step 3:** Slide Down to (12, 4) (Hit B1 at 12, 5).
    - **Step 4:** Move Right to (13, 4) -> Slide Down to (13, 5) (Hit Wall at 13, 6).
2.  **Push B1 Left:**
    - From (13, 5), push Left x2. B1 goes to (10, 5).
3.  **Finish:**
    - Navigate to (10, 6) -> Push Up to (10, 1) -> Right to (11, 1) -> Down to (11, 2).