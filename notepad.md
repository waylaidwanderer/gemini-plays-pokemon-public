# Tile Mechanics
- **Ice Tiles (Light Blue):** Player slides until hitting an obstacle.
- **Boulders on Ice:** Verified: They DO NOT slide. They move 1 tile per push.
- **Strength Push:** Player does not automatically step forward.

# Ice Path Strategy (B1F)

## Current Status
- **Position:** Player at (11, 7) -> Moving to (10, 6).
- **Goal:** Solve B1 (Top Right Boulder).
- **Puzzle State:**
  - **B1:** (11, 5). (Pushed Up).
  - **B2:** (7, 8).
  - **B3:** (9, 11).
  - **B4:** (17, 7).

## Master Plan (Verified)
1.  **Push B1 Up to (11, 5):**
    - Pushed Up. DONE.
2.  **Go around to (12, 5):**
    - Path: (11, 6) -> (10, 6) -> (10, 1) -> (12, 1) -> (12, 5).
3.  **Push B1 Left to (10, 5):**
    - From (12, 5), push Left.
4.  **Push B1 Up to (10, 1):**
    - From (10, 6), push Up.
5.  **Push B1 Right to (11, 1):**
    - From (9, 1), push Right.
6.  **Push B1 Down to Pit (11, 2):**
    - From (11, 0), push Down.
7.  **Next:** Solve B2.