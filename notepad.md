# Team Rocket HQ - Murkrow Puzzle

## STATUS: EXECUTING COL 26 STRATEGY
**Goal**: Open Boss Door at (22, 14) from (22, 13).
**Condition**: M must be at (22, 15) when P is at (22, 13).

## Step 1: Navigate to Bottom Right
- **Current**: (3, 2).
- **Route**:
  1. Right to (26, 2).
  2. Down to (26, 9) (Blocked).
  3. Left to (22, 9).
  4. Down to (22, 16).
  5. Right to (26, 16).

## Step 2: Sync X & Setup
- **Action**:
  - Move Right to (28, 16) (Wall). M Syncs X.
  - Move Left to (26, 16). State: P(26, 16), M(26, 16).
  - Move Up to (26, 12). M tries Down (Blocked), stays (26, 16).
  - State: P(26, 12), M(26, 16).

## Step 3: The Magic Move
- **Action**:
  - Move Down to (26, 13). M moves Up to (26, 15).
  - State: P(26, 13), M(26, 15).

## Step 4: Unlock
- **Action**:
  - Left to (22, 13). M follows to (22, 15).
  - Face Up (Door). Interact.