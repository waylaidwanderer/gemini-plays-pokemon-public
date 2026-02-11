# Team Rocket HQ - Murkrow Puzzle

## STATUS: RECOVERING & EXECUTING STATUE DESYNC
**Goal**: Open Boss Door at (22, 14).
**Strategy**: P Top/M Bottom -> Desync X on Statue -> Revert -> Solve.

## Step 1: Re-enter & Invert Y (Double Lap)
- **Current**: 3_48 (5, 7). Need to enter 3_49.
- **Action 1**: Go to (7, 3) and enter.
- **Action 2**: Left to (4, 2).
- **Action 3**: Down to (4, 16).
  - *State*: P(4, 16), M(4, 1).
- **Action 4**: Up to (4, 1).
  - *State*: P(4, 1), M(4, 16).

## Step 2: Statue Desync (P blocked)
- **Action**:
  - Right to (5, 1). M to (5, 16).
  - Push RIGHT against Statue (6, 1) x18.
    - P blocked at (5, 1).
    - M moves Right (5 -> 23).
  - *State*: P(5, 1), M(23, 16).

## Step 3: Revert Y & Block M
- **Action**:
  - Down to (5, 16). M Up to (23, 1).
  - Right to (22, 16).
    - M Right (23 -> 23 blocked by Statue 24,1).
  - *State*: P(22, 16), M(23, 1).

## Step 4: Ratchet & Solve
- **Action**:
  - Up to (22, 11). M Down to (23, 6).
  - Push UP (22, 10) x8. M Down to (23, 13).
  - Down to (22, 12).
  - Interact Right (M) / Down (Door).