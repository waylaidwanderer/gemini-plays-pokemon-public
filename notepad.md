# Team Rocket HQ - Murkrow Puzzle

## STATUS: EXECUTING "THE MACHINE RATCHET"
**Goal**: Open Boss Door at (22, 14).
**Strategy**: Position P at (22, 16), M at (22, 13). Interact with Machine at (22, 15).

## Step 1: Align on Col 22
- **Current**: P(25, 15), M(25, 2).
- **Action**:
  - Left 2 to (23, 15). M to (23, 2).
  - Down 1 to (23, 16). M to (23, 1).
  - Left 1 to (22, 16). M to (22, 1).
  - *State*: P(22, 16), M(22, 1).

## Step 2: The Ratchet
- **Action**:
  - Push UP against Machine (22, 15) x12.
  - P blocked. M moves Down (1 -> 13).
  - *State*: P(22, 16), M(22, 13).

## Step 3: Solve
- **Action**: Interact Up (A).