# Team Rocket HQ - Murkrow Puzzle

## STATUS: EXECUTING "NORTH-SIDE RATCHET"
**Goal**: Open Boss Door at (22, 14).
**Target State**: P(22, 11), M(22, 13).

## Step 1: Invert Y
- **Current**: P(1, 16).
- **Action**:
  - Up to (1, 1). M Down to (1, 16).
  - Down to (1, 16). M Up to (1, 1).
  - *State*: P(1, 16), M(1, 1).

## Step 2: Traverse & Dodge (Avoid Warp 5,15 & Statue 6,1)
- **Action**:
  - Up 1 to (1, 15). M Down 1 to (1, 2).
  - Right to (4, 15). M Right to (4, 2).
  - Down to (4, 16). M Up to (4, 1).
  - Right to (7, 16). M Right to (5, 1) (Blocked by Statue at 6,1).
  - Up to (7, 15). M Down to (5, 2).
  - Right to (29, 15). M Right to (29, 2) (Resync X).
  - *State*: P(29, 15), M(29, 2).

## Step 3: Position & Ratchet
- **Action**:
  - Left to (22, 15). M Left to (22, 2).
  - Up to (22, 11). M Down to (22, 6).
  - Push UP against Wall (22, 10) x7.
  - M moves Down (6 -> 13).
  - *State*: P(22, 11), M(22, 13).

## Step 4: Solve
- **Action**:
  - Push Up x1 (Try to force M to 14).
  - Move Down to (22, 12).
  - Interact with M/Door.