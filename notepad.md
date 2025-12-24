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

## Master Plan (Corrected)
1.  **Get to Right Side:** DONE. (At 12, 5).
2.  **Push Sequence:**
    - Push Left to (10, 5). DONE.
    - Go to (10, 6). Push Up to (10, 1).
    - Go to (9, 1). Push Right to (11, 1).
    - Go to (11, 0). Push Down into Pit (11, 2).
3.  **Next:** Solve B2.
- **Strength Push:** Pushing a boulder moves the boulder 1 tile. The player does NOT automatically step into the vacated tile; a separate input is required.