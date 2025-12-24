# Tile Mechanics
- **Ice Tiles (Light Blue):** Player slides until hitting an obstacle.
- **Boulders on Ice:** Verified: They DO NOT slide. They move 1 tile per push.
- **Strength Push:** Player does not automatically step forward.

# Ice Path Strategy (B1F)

## Current Status
- **Position:** Player at (11, 8).
- **Goal:** Solve B1 (Top Right Boulder).
- **Puzzle State:**
  - **B1:** (11, 5). (Blocked by Wall at 11, 4).
  - **B2:** (7, 8).
  - **B3:** (9, 11).
  - **B4:** (17, 7).

## Master Plan (Revised)
1.  **Move B1 to Right Column (Col 12):**
    - Go to (10, 5).
    - Push B1 Right to (12, 5).
2.  **Move B1 Up:**
    - Go to (12, 6).
    - Push B1 Up to (12, 1).
3.  **Finish B1:**
    - Go to (13, 1).
    - Push Left to (11, 1).
    - Go to (11, 0).
    - Push Down into Pit (11, 2).
4.  **Next:** Solve B2.