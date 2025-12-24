# Tile Mechanics
- **Ice Tiles (Light Blue):** Player slides until hitting an obstacle.
- **Boulders on Ice:** Verified: They DO NOT slide. They move 1 tile per push.
- **Strength Push:** Player does not automatically step forward.

# Ice Path Strategy (B1F)

## Current Status
- **Position:** Player at (11, 6).
- **Goal:** Solve B1 (Top Right Boulder).
- **Puzzle State:**
  - **B1:** (10, 1). (Pushed up successfully).
  - **B2:** (7, 8).
  - **B3:** (9, 11).
  - **B4:** (17, 7).

## Master Plan (Corrected)
1.  **Navigate Around to (9, 1):**
    - Path: (11, 6) -> (11, 16) -> (6, 16) -> (6, 1) -> (9, 1).
    - Note: (10, 0) and (11, 0) are FLOORS. This allows pushing down.
2.  **Finish B1:**
    - Push Right to (11, 1).
    - Move to (11, 0) (via 10, 0).
    - Push Down into Pit (11, 2).
3.  **Next:** Solve B2.