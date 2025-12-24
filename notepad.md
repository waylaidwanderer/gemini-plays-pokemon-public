# Tile Mechanics
- **Ice Tiles (Light Blue):** Player slides until hitting an obstacle.
- **Boulders on Ice:** Verified: They DO NOT slide. They move 1 tile per push.
- **Strength Push:** Player does not automatically step forward.

# Ice Path Strategy (B1F)

## Current Status
- **Position:** Player at (10, 5).
- **Goal:** RESET PUZZLE (Boulder B1 stuck at 10, 1).
- **Error:** Pushed B1 too far North (to 10, 1 instead of 10, 2). Cannot push down due to Wall at 10, 0.

## Recovery Plan
1.  **Reset:** Jump into Pit at (12, 13).
2.  **Return:** Navigate back to B1F.
3.  **Retry B1:**
    - Push B1 Up to (11, 5).
    - Push Left to (10, 5).
    - Push Up to (10, 2) (**STOP HERE**).
    - Go around to (9, 2).
    - Push Right into Pit (11, 2).