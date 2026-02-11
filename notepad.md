# Team Rocket HQ - Murkrow Puzzle

## STATUS: EXECUTING "NORTH APPROACH - CROSS Y"
**Goal**: Open Boss Door at (22, 14).
**Strategy**: Cross M and P vertically in Col 1 (Battle Path), then traverse to Door.

## Step 1: Cross Y (Col 1)
- **Current**: P(1, 1), M(1, 16).
- **Action**: Down to (1, 13).
  - P moves `1 -> 13`.
  - M moves `16 -> 4`.
  - *Expect*: Battles at (1, 8), (1, 12), (1, 13).
  - *State*: P(1, 13), M(1, 4).

## Step 2: Traverse & Align
- **Action**:
  - Right to (22, 13). M Right to (22, 4).
  - *State*: P(22, 13), M(22, 4).

## Step 3: Ratchet & Solve
- **Action**:
  - Move Up to (22, 11). M Down to (22, 6).
  - Push UP against Wall (22, 10) x6.
    - M moves Down (6 -> 12).
  - *State*: P(22, 11), M(22, 12).
  - Move Down to (22, 12).
  - Interact.