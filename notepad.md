# Tile Mechanics
- **Ice Tiles (Light Blue):** Player slides until hitting an obstacle.
- **Boulders on Ice:** Verified: They DO NOT slide. They move 1 tile per push.
- **Strength Push:** Player does not automatically step forward.

# Ice Path Strategy (B1F)

## Current Status
- **Position:** Player at (11, 1). (Interrupted by Battle).
- **Goal:** Solve B1 (Top Right Boulder).
- **Puzzle State:**
  - **B1:** (10, 5).
  - **B2:** (7, 8).
  - **B3:** (9, 11).
  - **B4:** (17, 7).

## Master Plan (Solution Found)
1.  **Move B1 to (11, 5):**
    - Current: At (11, 1).
    - Action: Left to (10, 1) -> Down (Slide) to (10, 4) -> Left (Slide) to (9, 4) -> Down (Slide) to (9, 5) -> Push Right.
    - Result: B1 at (11, 5). Player at (10, 5).
2.  **Move B1 back to (10, 5) (positioning player):**
    - Go to (11, 6).
      - Path: (10, 5) -> (10, 6) -> Slide Right to (11, 6).
    - Push B1 Left to (10, 5).
      - Player ends at (11, 5).
3.  **Get below B1:**
    - Go (11, 5) -> (11, 6) -> Slide Left to (10, 6).
4.  **Solve:**
    - Push Up to (10, 1).
    - Push Right to (11, 1).
    - Push Down to Pit (11, 2).