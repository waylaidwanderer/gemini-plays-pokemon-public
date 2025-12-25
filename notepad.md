# Ice Path Strategy (B1F)

## Current Status
- **Position:** Player at (12, 11).
- **Goal:** Solve B1 (Top Right Boulder) at (11, 7).
- **Puzzle State:**
  - **B1:** (11, 7).
  - **B2:** (7, 8) (Off-screen).
  - **B3:** Unknown/Gone (Not at 9, 11).
  - **B4:** (17, 7).

## Immediate Plan
1.  **Navigate to (11, 8):**
    - Path: Move North to (12, 8), then Left to (11, 8).
    - This positions me below B1.
2.  **Solve B1:**
    - Push B1 UP to (11, 5).
    - Navigate around to (12, 5).
    - Push B1 LEFT to (10, 5).
    - Navigate to (10, 6) and push UP to (10, 1).
    - Push RIGHT to (11, 1).
    - Push DOWN into Pit (11, 2).