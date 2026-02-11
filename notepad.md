# Team Rocket HQ - Murkrow Puzzle

## STATUS: REPOSITIONING TO NORTH
**Goal**: Open Boss Door at (22, 14) from the North side (22, 13).
**Current**: P(22, 16) blocked by Statue. M(22, 13).

## Step 1: Return to Col 1
- **Action**:
  - Clear text (B).
  - Left 21 to (1, 16).
  - *State*: P(1, 16), M(1, 13).

## Step 2: Desync Y (Top/Bottom)
- **Action**:
  - Up to (1, 1) (Hit Top).
    - M moves Down to (1, 16) (Hit Bottom).
  - Down to (1, 13).
    - M moves Up to (1, 4).
  - *State*: P(1, 13), M(1, 4).

## Step 3: Approach Door
- **Action**:
  - Right to (22, 13).
    - M Right to (22, 4).
  - *State*: P(22, 13), M(22, 4).

## Step 4: Ratchet & Solve
- **Action**:
  - Push UP against Wall (22, 10).
  - M moves Down to (22, 13).
  - Side-step to P(22, 13), M(22, 11).
  - Interact Down.