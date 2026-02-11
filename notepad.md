# Team Rocket HQ - Murkrow Puzzle

## STATUS: EXECUTING "STATUE DESYNC TRAVERSE"
**Goal**: Open Boss Door at (22, 14).
**Strategy**: Use Statue (6,1) to block P, allowing M to pass Warp (5,15) on Row 16. Then Sync X on Right Wall.

## Step 1: Statue Desync (Current)
- **Current**: P(4, 1), M(4, 16).
- **Action**:
  - Right 1 to (5, 1). M to (5, 16).
  - Push Right (into Statue 6,1) x3.
    - P blocked.
    - M moves Right: (5, 16) -> (6, 16) -> (7, 16) -> (8, 16).
  - *State*: P(5, 1), M(8, 16). (M passed Warp).

## Step 2: Traverse
- **Action**:
  - Down to (5, 2). M Up to (8, 15).
  - Right to (7, 2). M Right to (10, 15).
  - Up to (7, 1). M Down to (10, 16).
  - Right to (29, 1).
    - P -> (29, 1).
    - M -> (29, 16). (Both hit wall).
  - *State*: P(29, 1), M(29, 16).

## Step 3: Align & Ratchet
- **Action**:
  - Left 7 to (22, 1). M Left to (22, 16).
  - Down to (22, 11). M Up to (22, 6).
  - Push UP (22, 10). M Down to (22, 13).
  - Interact.