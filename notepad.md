# Team Rocket HQ - Murkrow Puzzle

## STATUS: EXECUTING "NORTH RATCHET (STATUE DODGE VARIANT)"
**Goal**: Open Boss Door at (22, 14).
**Strategy**: Sync X Left, Invert Y on Col 4, Statue Dodge to Resync X Right, Loop North, Ratchet.

## Step 3: Statue Dodge & Resync X [IN PROGRESS]
- **Current**: P(4, 16), M(4, 1).
- **Action**:
  1. Right to (6, 16).
     - P(6, 16). M(5, 1) (Blocked by Statue 6, 1).
  2. Up to (6, 15).
     - M Down to (5, 2). (M passes Statue).
  3. Right to (29, 15).
     - P to (29, 15). M to (29, 2). (Resyncs X).
  - *Target State*: P(29, 15), M(29, 2).

## Step 4: Loop to North
- **Action**:
  - Up to (29, 2). M Down to (29, 15).
  - Left to (22, 2). M Left to (22, 15).
  - *State*: P(22, 2), M(22, 15).

## Step 5: Ratchet & Solve
- **Action**:
  - Down to (22, 11). M Up to (22, 6).
  - Push UP (22, 10) x8.
    - P blocked at 11. M moves Down (6 -> 14).
  - *State*: P(22, 11), M(22, 14).
  - Down to (22, 12). M Up to (22, 13).
  - Down to (22, 13). M Up to (22, 12).
  - Interact Down (Door).