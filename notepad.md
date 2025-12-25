# Ice Path Strategy (B1F)

## Current Status
- **Position:** Player at (10, 5).
- **Goal:** Solve B1 (Top Right Boulder).
- **Puzzle State:**
  - **B1:** (11, 5).
  - **B2:** (7, 8).
  - **B4:** (17, 7).

## Immediate Plan
1.  **Navigate around to (12, 5):**
    - **Step 1:** Slide Up to (10, 0). (Next Action)
    - **Step 2:** Walk/Slide to (12, 5) via (12, 1).
      - Path: (10, 0) -> (11, 0) -> (11, 1) -> (12, 1) -> (12, 5).
2.  **Push B1 Left to (10, 5):**
    - From (12, 5), push Left.
3.  **Solve B1:**
    - Navigate to (10, 6) -> Push Up to (10, 1).
    - Push Right to (11, 1).
    - Push Down into Pit (11, 2).