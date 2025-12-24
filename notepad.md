# Tile Mechanics
- **Ice Tiles (Light Blue):** Player slides until hitting an obstacle.
- **Boulders on Ice:** Verified: They DO NOT slide. They move 1 tile per push.
- **Strength Push:** Player does not automatically step forward.

# Ice Path Strategy (B1F)

## Current Status
- **Position:** Player at (10, 5).
- **Goal:** Solve B1 (Top Right Boulder).
- **Puzzle State:**
  - **B1:** (10, 4).
  - **B2:** (7, 8).
  - **B3:** (9, 11).
  - **B4:** (17, 7).

## Master Plan
1.  **Push B1 UP to (10, 1):**
    - Execute Up x5.
    - Final State: B1 at (10, 1), Player at (10, 3) or (10, 2).
2.  **Navigate Around:**
    - Go South to Row 15 -> West to Left Side -> North to Row 1 -> East to (9, 1).
3.  **Finish B1:**
    - Push Right to (11, 1).
    - Push Down to (11, 2) (Pit).
4.  **Next:** Solve B2.