# Team Rocket HQ - Murkrow Puzzle

## STATUS: EXECUTING "LEFT-SIDE DOOR RATCHET"
**Goal**: Open Boss Door at (22, 14).
**Target State**: P(22, 15), M(22, 13).

## Step 1: Sync X (Col 1) [IN PROGRESS]
- **Current**: P(21, 2), M(1, 2).
- **Action**: Move Left to (1, 2).
  - *Note*: Statue Alarm at (6, 1) might trigger battle at (6, 2).
  - *Note*: M is already at X=1 (bonked against wall). P needs to catch up.

## Step 2: Invert Y (Battle Path)
- **Action**: Down to (1, 16).
  - P(1, 2) -> (1, 16).
  - M(1, 2) -> (1, 1). M stays at top.

## Step 3: Desync X (Use Grunt at 2,4)
- **Action**:
  - P Up to (1, 13). M Down to (1, 4).
  - P Right to (22, 13). M Blocked at (1, 4) by Grunt at (2, 4).
  - *State*: P(22, 13), M(1, 4).

## Step 4: Ratchet Y (Drop M)
- **Action**:
  - P Up to (22, 11). M Down to (1, 6).
  - P Push Up against Wall (22, 10). M Down to (1, 15).
  - *State*: P(22, 11), M(1, 15).

## Step 5: Resync X (Right)
- **Action**:
  - P Push Right against Wall (23, 11). M Right to (22, 15).
  - *State*: P(22, 11), M(22, 15).

## Step 6: Convergence & Solve
- **Action**:
  - P Down to (22, 13). M Up to (22, 13).
  - P Left -> (21, 13). M Left -> (21, 13).
  - P Down -> (21, 15). M Up -> (21, 11).
  - P Right -> (22, 15). M Right -> (22, 11).
  - P Push Up (Door). M Down -> 12...13...14.
  - Interact (A).