# Team Rocket HQ - Murkrow Puzzle

## STATUS: EXECUTING "STATUE DODGE & MACHINE RATCHET"
**Goal**: Open Boss Door at (22, 14).
**Strategy**: Invert Y, Desync on Statue (6,1), Resync on Right Wall, Ratchet on Machine (22,15).

## Step 1: Sync X (Col 1)
- **Current**: P(27, 2). M(7, 2).
- **Action**:
  - Left 26 to (1, 2).
  - *State*: P(1, 2), M(1, 2).

## Step 2: Invert Y & Desync X
- **Action**:
  - Down to (1, 16). M Up to (1, 1).
  - Right to (6, 16).
    - P moves to (6, 16).
    - M blocked by Statue at (6, 1). M stays at (5, 1).
  - *State*: P(6, 16), M(5, 1).

## Step 3: Resync X (Right Wall)
- **Action**:
  - Right to (29, 16).
    - P moves to (29, 16).
    - M moves to (29, 1). (Resyncs X).
  - *State*: P(29, 16), M(29, 1).

## Step 4: Position & Ratchet
- **Action**:
  - Left to (22, 16). M Left to (22, 1).
  - Push UP against Machine (22, 15) x12.
    - P blocked. M moves Down (1 -> 13).
  - *State*: P(22, 16), M(22, 13).

## Step 5: Solve
- **Action**: Interact Up (A).