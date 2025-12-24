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
1.  **Verify Boulder Mechanics:** Attempt to push Boulder 1 UP from (10, 6).
    - If it moves 1 tile: **Boulders Don't Slide.** (Easy solve).
    - If it slides far: **Boulders Slide.** (Complex solve).
    - If it doesn't move: **Activate Strength.**
2.  **Current Action:** Push Up.
3.  **Next:** React to boulder movement.