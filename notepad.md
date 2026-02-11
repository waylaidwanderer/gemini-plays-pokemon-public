# Team Rocket HQ - Murkrow Puzzle

## STATUS: EXECUTING "STATUE DESYNC & COL 23 TARGET"
**Goal**: Place M at (23, 13), P at (22, 12).
**Strategy**: Use Statue (6,1) to block P, move M to (23, 16). Invert Y. Use Statue (24,1) to block M.

## Step 1: Reach (4, 16) & Invert Y
- **Current**: P(7, 15).
- **Action**:
  - Left to (4, 15). M to (3, 2).
  - Up to (4, 1). M Down to (4, 16).
  - *State*: P(4, 1), M(4, 16).

## Step 2: Statue Desync (Left)
- **Action**:
  - Right to (5, 1). M to (5, 16).
  - Push RIGHT against Statue (6, 1) x18.
    - P blocked at (5, 1).
    - M moves Right (5 -> 23).
  - *State*: P(5, 1), M(23, 16).

## Step 3: Revert Y & Block M (Right)
- **Action**:
  - Down to (5, 16). M Up to (23, 1).
  - Right to (22, 16).
    - P moves (5 -> 22).
    - M moves Right (23 -> 40).
    - M blocked by Statue (24, 1). M stays (23, 1).
  - *State*: P(22, 16), M(23, 1).

## Step 4: Ratchet & Solve
- **Action**:
  - Up to (22, 11). M Down to (23, 6).
  - Push UP (22, 10) x8. M Down to (23, 13).
  - Down to (22, 12). M Up to (23, 12).
  - Interact Right.