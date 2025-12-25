# Ice Path Strategy (B1F)

## Current Status
- **Position:** Player at (12, 4).
- **Goal:** Solve B1 (Top Right Boulder).
- **Puzzle State:**
  - **B1:** (12, 5). (Target: 10, 5).
  - **B2:** (7, 8).
  - **B4:** (17, 7).

## Recovery Plan (Execution)
1.  **Navigate to (13, 5) & Push:**
    - **Step 1:** Slide Right to (13, 4).
    - **Step 2:** Slide Down to (13, 5).
    - **Step 3:** Push Left (B1 to 11, 5).
    - **Step 4:** Move Left to (12, 5).
    - **Step 5:** Push Left (B1 to 10, 5).
2.  **Solve B1:**
    - **Step 1:** Navigate to (10, 6) via Top Loop: (12, 5) -> (12, 1) -> (10, 1) -> (10, 6).
    - **Step 2:** Push Up to (10, 1).
    - **Step 3:** Push Right to (11, 1).
    - **Step 4:** Push Down to Pit (11, 2).