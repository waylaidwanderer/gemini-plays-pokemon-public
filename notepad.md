# Tile Mechanics
- **Ice Tiles (Light Blue):** Player slides until hitting an obstacle.
- **Boulders on Ice:** Verified: They DO NOT slide. They move 1 tile per push.
- **Strength Push:** Player does not automatically step forward.

# Ice Path Strategy (B1F)

## Current Status
- **Position:** Player at (10, 5).
- **Goal:** RESET PUZZLE (Boulder B1 stuck at 10, 1).
- **Error:** Pushed B1 too far North (to 10, 1 instead of 10, 2). Cannot push down due to Wall at 10, 0.

# Recovery Plan (B2F -> B1F)
1.  **Goal:** Return to B1F via Ladder at (17, 1) (Leads to 17, 3 near Puzzle).
2.  **Collect:** Item at (0, 2) and Item at (8, 9).
3.  **Path:**
    - Slide RIGHT from (1, 0) to (16, 0). DONE.
    - Walk to (17, 1) (Ladder).
    - Skip Item at (8, 9) for now (hard to reach).