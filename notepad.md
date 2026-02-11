# Team Rocket HQ - Murkrow Puzzle

## STATUS: EXECUTING "STATUE DESYNC (COL 4 INVERT)"
**Goal**: Place M at (23, 13) or (22, 13).
**Strategy**: Invert Y on Col 4, Desync X on Statue (6,1).

## Step 1: Re-enter & Invert Y
- **Current**: 3_48 (7, 3).
- **Action**:
  - Down to 3_49 (7, 2).
  - Left to (4, 2).
  - Down to (4, 16). (M to 4, 1).
  - Up to (4, 1). (M to 4, 16).
  - *State*: P(4, 1), M(4, 16).

## Step 2: Statue Desync (Left)
- **Action**:
  - Right to (5, 1). (M to 5, 16).
  - Push RIGHT against Statue (6, 1) x18.
    - P blocked. M moves Right (5 -> 23).
  - *State*: P(5, 1), M(23, 16).

## Step 3: Revert Y & Block M
- **Action**:
  - Down to (5, 16). (M to 23, 1).
  - Right to (22, 16).
    - M Right (23 -> 23 blocked by Statue 24,1).
  - *State*: P(22, 16), M(23, 1).

## Step 4: Ratchet & Solve
- **Action**:
  - Up to (22, 11). M Down to (23, 6).
  - Push UP (22, 10) x8. M Down to (23, 13).
  - Down to (22, 12).
  - Interact Right (M) / Down (Door).