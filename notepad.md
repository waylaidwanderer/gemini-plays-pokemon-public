# Team Rocket HQ - Murkrow Puzzle

## STATUS: REPOSITIONING TO NORTH
**Goal**: Open Boss Door at (22, 14).
**Method**: "Switch Desync" at (19, 11).

## Step 1: Return to Col 1 & Invert Y
- **Current**: P(22, 16), M(22, 13).
- **Action**:
  - Clear Text (B).
  - Left to (1, 16).
  - Up to (1, 1). M Down to (1, 16).
  - Down to (1, 16). M Up to (1, 1).
  - *State*: P(1, 16), M(1, 1).

## Step 2: Traverse to Col 22
- **Action**:
  - Right to (22, 16).
  - M Right to (22, 1). (Assumes M passes Alarm at 6,1).
  - *State*: P(22, 16), M(22, 1).

## Step 3: Ratchet & Desync
- **Action**:
  - Up to (22, 11). M Down to (22, 6).
  - Push UP against Wall (22, 10). M Down to (22, 13).
  - *State*: P(22, 11), M(22, 13).
  - Left to (20, 11). M Left to (20, 13).
  - Push LEFT against Switch (19, 11). M Left to (19, 13).
  - *State*: P(20, 11), M(19, 13).

## Step 4: Solve
- **Action**:
  - Right to (22, 11). M Right to (21, 13).
  - Down to (22, 12). M Up to (21, 12).
  - Interact Left (M), then Down (Door).