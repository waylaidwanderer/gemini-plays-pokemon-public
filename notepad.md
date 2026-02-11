# Team Rocket HQ - Murkrow Puzzle

## STATUS: EXECUTING "NORTH RATCHET (COL 4 VARIANT)"
**Goal**: Open Boss Door at (22, 14).
**Strategy**: Sync X Left, Invert Y on Col 4, Resync X Right, Ratchet.

## Step 1: Reach (1, 16) [COMPLETED]
- **Current**: P(1, 16), M(1, 1).
- **Action**: Arrived via Col 1/3.

## Step 2: Invert Y (Col 4) [IN PROGRESS]
- **Current**: P(4, 16). M(4, 1).
- **Action**:
  - Up to (4, 1).
    - M Down to (4, 16).
  - *State*: P(4, 1), M(4, 16).

## Step 3: Traverse East & Resync
- **Action**:
  - Down to (4, 2). M Up to (4, 15).
  - Right to (28, 2). M Right to (28, 15).
  - *State*: P(28, 2), M(28, 15).

## Step 4: Swap Y (Right Side)
- **Action**:
  - Down to (28, 13). M Up to (28, 4).
  - *State*: P(28, 13), M(28, 4).

## Step 5: Align & Ratchet
- **Action**:
  - Left to (22, 13). M Left to (22, 4).
  - Push UP against Door (22, 14) x8.
    - M moves Down to (22, 12).
  - *State*: P(22, 13), M(22, 12).
  - Interact Down.