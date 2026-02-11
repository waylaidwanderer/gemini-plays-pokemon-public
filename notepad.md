# Team Rocket HQ - Murkrow Puzzle

## STATUS: EXECUTING "STATUE DODGE & MACHINE RATCHET"
**Goal**: Open Boss Door at (22, 14).
**Strategy**: Invert Y, Desync on Statue (6,1), Resync on Right Wall, Ratchet on Machine (22,15).

## Step 1: Sync X (Col 1) [DONE]
- P(1, 2), M(1, 2).

## Step 2: Invert Y & Desync X
- **Action**:
  - Down to (1, 16). M Up to (1, 1).
  - Right to (6, 16).
    - P moves to (6, 16).
    - M blocked by Statue (6, 1). M stays (5, 1).
  - *State*: P(6, 16), M(5, 1).

## Step 3: Shift & Resync X
- **Action**:
  - Up 1 to (6, 15). M Down 1 to (5, 2).
  - Right to (29, 15).
    - P -> (29, 15).
    - M -> (29, 2). (Resyncs X).
  - *State*: P(29, 15), M(29, 2).

## Step 4: Position & Ratchet
- **Action**:
  - Left to (22, 15). M Left to (22, 2).
  - Push UP against Machine (22, 15) x12.
    - P blocked. M moves Down (2 -> 14). (Or 1->13 if logic differs).
    - *Note*: If M is at (22, 2), Up push moves M to (22, 3)...(22, 14).
  - *State*: P(22, 15), M(22, 14).

## Step 5: Solve
- **Action**: Interact Up (A).