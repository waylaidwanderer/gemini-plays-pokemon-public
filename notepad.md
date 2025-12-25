# Ice Path Strategy (B1F)

## Current Status
- **Position:** Player at (11, 3).
- **Goal:** Solve B1 (Top Right Boulder).
- **Puzzle State:**
  - **B1:** (12, 5). (Recoverable).
  - **B2:** (7, 8).
  - **B4:** (17, 7).

## Recovery Plan (Positioning for Left Push)
1.  **Navigate to (13, 5):**
    - **Step 1:** Slide Right to (12, 3). (Current Action)
    - **Step 2:** Slide Up to (12, 1).
    - **Step 3:** Slide Down to (12, 4) (Hit B1 at 12, 5).
    - **Step 4:** Slide Right to (13, 4).
    - **Step 5:** Slide Down to (13, 5).
2.  **Push B1 Left:**
    - Push Left x2. B1 moves to (10, 5).
3.  **Solve B1:**
    - Navigate to (10, 6) -> Push Up to (10, 1).
    - Push Right to (11, 1).
    - Push Down to Pit (11, 2).