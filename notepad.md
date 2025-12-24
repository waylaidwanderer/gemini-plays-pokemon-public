# Tile Mechanics
- **Ice Tiles (Light Blue):** Player slides until hitting an obstacle.
- **Boulders on Ice:** Verified: They DO NOT slide. They move 1 tile per push.
- **Strength Push:** Player does not automatically step forward.

# Ice Path Strategy (B1F)

## Current Status
- **Position:** Player at (10, 3).
- **Goal:** RESET PUZZLE via Pit (11, 2).
- **Reason:** Boulder 1 is stuck at (10, 6) (pushed down by mistake).
- **Puzzle State:** BRICKED.

## Recovery Plan
1.  **Reset:** Enter Pit at (11, 2).
    - Path: Up (Slide to 10, 1) -> Right (11, 1) -> Down (11, 2).
2.  **Return:** Navigate back to B1F.
3.  **Retry Solution:**
    - **Move B1 to (11, 5):**
        - From (11, 1): Left to (10, 1) -> Down (Slide) to (10, 4) -> Left (Slide) to (9, 4) -> Down (Slide) to (9, 5) -> Push Right.
    - **Reposition:**
        - Go (10, 5) -> (10, 6) -> (11, 6) -> (10, 6) -> (10, 1) -> (12, 1) -> (12, 5).
        - Push Left.
    - **Solve:**
        - Go (11, 5) -> (11, 6) -> (10, 6).
        - Push Up to (10, 1).
        - Push Right to (11, 1).
        - Push Down to Pit (11, 2).