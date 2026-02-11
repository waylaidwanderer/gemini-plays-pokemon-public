# Team Rocket HQ - Murkrow Puzzle

## STATUS: EXECUTING "NORTH RATCHET (COL 4 VARIANT)"
**Goal**: Open Boss Door at (22, 14) from (22, 13).
**Strategy**: Sync X Left, Invert Y on Col 4, Traverse North.

## Step 1: Reach (1, 16) [IN PROGRESS]
- **Current**: P(3, 12). M(3, 1).
- **Action**:
  - Left to (1, 12) (Voltorb Trap).
  - Down to (1, 16).
  - *Target*: P(1, 16), M(1, 1).

## Step 2: Invert Y (Col 4)
- **Reason**: Col 1 blocked at (1, 5). Col 2 blocked by Grunt. Col 3 blocked by Stairs.
- **Action**:
  - Right to (4, 16). M to (4, 1).
  - Up to (4, 1). M Down to (4, 16).
  - *State*: P(4, 1), M(4, 16).

## Step 3: Traverse & Align
- **Action**:
  - Right to (22, 1). M Right to (22, 16).
  - Down to (22, 13). M Up to (22, 4).
  - *State*: P(22, 13), M(22, 4).

## Step 4: Ratchet & Solve
- **Action**:
  - Push UP against Door (22, 14) x8.
    - P blocked. M moves Down (4 -> 12).
  - *State*: P(22, 13), M(22, 12).
  - Interact Down (Door).