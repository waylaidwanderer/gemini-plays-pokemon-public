# Ice Path Strategy (B1F)

## Current Status
- **Position:** Player at (11, 8).
- **Goal:** Solve B1 (Top Right Boulder).
- **Action:** ACTIVATE STRENGTH and Push B1 Up to (11, 5).
- **Puzzle State:**
  - **B1:** (11, 7) -> (11, 5).
  - **B2:** (7, 8).
  - **B4:** (17, 7).

## B1 Solution Path (Verified)
1.  **Push B1 Up:** (11, 8) -> Push Up x2 -> B1 at (11, 5).
2.  **Navigate to (12, 5):**
    - (11, 6) -> Left to (10, 6) -> Up to (10, 1) -> Right to (12, 1) -> Down to (12, 5).
3.  **Push B1 Left:** To (10, 5).
4.  **Finish:**
    - Navigate to (10, 6) -> Push Up to (10, 1) -> Right to (11, 1) -> Down to (11, 2).