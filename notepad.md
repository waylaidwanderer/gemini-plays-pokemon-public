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

## Master Plan (Solution Found - Adjusted for (11, 3))
1.  **Move B1 to (11, 5):**
    - From (11, 3): Slide Left to (9, 3) -> Slide Down to (9, 5).
    - Push Right (B1 to 11, 5).
2.  **Move B1 back to (10, 5) (positioning player):**
    - Move to (10, 5) -> Slide Down to (10, 6).
    - Slide Up to (10, 1) -> Slide Right to (12, 1) -> Slide Down to (12, 5).
    - Push Left (B1 to 10, 5).
3.  **Get below B1:**
    - Go (11, 5) -> Slide Down to (11, 6) -> Slide Left to (10, 6).
4.  **Solve:**
    - Push Up to (10, 1).
    - Push Right to (11, 1).
    - Push Down to Pit (11, 2).