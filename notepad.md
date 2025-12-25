# Ice Path Strategy (B1F)

## Current Status
- **Position:** Player at (11, 8).
- **Goal:** Solve B1 (Top Right Boulder).
- **Puzzle State:**
  - **B1:** (11, 6). (Moved up 1 tile).
  - **B2:** (7, 8).
  - **B3:** Unknown/Gone.
  - **B4:** (17, 7).

## Immediate Plan
1.  **Push B1 Up to (11, 5):**
    - Current: B1 at (11, 6), Player at (11, 8).
    - Action: Move Up to (11, 7), then Push Up.
2.  **Navigate around to (12, 5):**
    - Path: (11, 6) -> (10, 6) -> (10, 1) -> (12, 1) -> (12, 5).
3.  **Push B1 Left to (10, 5):**
    - From (12, 5), push Left.
4.  **Solve B1:**
    - Navigate to (10, 6) -> Push Up to (10, 1).
    - Push Right to (11, 1).
    - Push Down into Pit (11, 2).