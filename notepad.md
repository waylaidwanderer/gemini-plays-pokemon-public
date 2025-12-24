# Tile Mechanics
- **Ice Tiles (Light Blue):** Player slides until hitting an obstacle.
- **Boulders on Ice:** Verified: They DO NOT slide. They move 1 tile per push.
- **Strength Push:** Player does not automatically step forward.

# Ice Path Strategy (B1F)

## Current Status
- **Position:** Player at (11, 6).
- **Goal:** Reach (11, 8) to push B1 UP.
- **Puzzle State:** Reset Verified (B1 at 11, 7).

## Master Plan (Solution Found & Verified Path)
1.  **Navigate to (11, 8):**
    - **Step 1:** Go East to (9, 9), then South to (9, 10). DONE.
    - **Step 2:** Check for Boulder 3 at (9, 11).
      - If present: Push DOWN to (9, 12). Go around: (9, 11) -> (10, 11) -> (10, 13) -> (9, 13).
      - If absent: Walk straight South to (9, 16).
    - **Step 3:** Go South to (9, 16) -> Slide East to (18, 16).
    - **Step 4 (East Side):**
      - West to (17, 16) -> Up to (17, 14) -> Left to (13, 14).
      - Up to (13, 11) -> Left to (12, 11) -> Up to (12, 8) -> Left to (11, 8).
2.  **Solve B1 (Verified: Boulders don't slide):**
    - Push Up to (11, 5).
    - Go to (10, 5). Push Right to (12, 5).
    - Go to (12, 6). Push Up to (12, 1).
    - Go to (13, 1). Push Left to (11, 1).
    - Go to (11, 0). Push Down to Pit (11, 2).