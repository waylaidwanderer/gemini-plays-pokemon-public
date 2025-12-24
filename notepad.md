# Tile Mechanics
- **Ice Tiles (Light Blue):** Player slides until hitting an obstacle.
- **Boulders on Ice:** Behavior to be verified (Hypothesis: They slide).

# Ice Path Strategy (B1F)

## Current Status
- **Position:** Player at (11, 8).
- **Goal:** Solve B1 (Top Right Boulder).
- **Puzzle State:**
  - **B1:** (11, 7).
  - **B2:** (7, 8).
  - **B3:** (9, 11).
  - **B4:** (17, 7).

## Master Plan
1.  **B1 Solve (Detailed):**
    - Push B1 Up from (11, 7) to (11, 5). (Stops at Wall 11, 4).
    - Loop around to (12, 5): (11, 6) -> (10, 6) -> (10, 1) -> (13, 1) -> (13, 5) -> (12, 5).
    - Push B1 Left to (10, 5).
    - Loop to (10, 6): (11, 5) -> (11, 6) -> (10, 6).
    - Push B1 Up to (10, 2).
    - Loop to (9, 2): (10, 3) -> (9, 3) -> (9, 2).
    - Push B1 Right into Pit (11, 2).
2.  **Next:** Solve B2.
- **Strength Push:** Pushing a boulder moves the boulder 1 tile. The player does NOT automatically step into the vacated tile; a separate input is required.