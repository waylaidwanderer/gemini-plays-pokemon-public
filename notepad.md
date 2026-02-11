# Team Rocket HQ - Murkrow Puzzle

## STATUS: EXECUTING "LEFT-SIDE DOOR RATCHET"
**Goal**: Open Boss Door at (22, 14).
**Target State**: P(22, 15), M(22, 13).

## Step 1: Sync X (Col 1) [COMPLETED]
- P synced at X=1.

## Step 2: Invert Y (Battle Path) [MODIFIED]
- **Issue**: Blockage/Loop at (1, 5). Possible warp or invisible wall.
- **New Path**: Switch to Column 3 for descent.
- **Action**:
  - P(1, 4) -> Up to (1, 3).
  - Right to (3, 3).
  - Down to (3, 16).
  - Left to (1, 16).
  - *Result*: P(1, 16), M(1, 1). (Same outcome).

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