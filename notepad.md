# Team Rocket HQ - Murkrow Puzzle

## STATUS: EXECUTING "COL 4 INVERT"
**Goal**: Open Boss Door at (22, 14).
**Strategy**: Use Col 4 to invert Y, then Statue Bumping to sync X.

## Step 1: Invert Y at Col 4
- **Current**: P(1, 16), M(1, 1).
- **Action**:
  - Right to (4, 16). M to (4, 1).
  - Up to (4, 1). M Down to (4, 16).
  - *State*: P(4, 1), M(4, 16).

## Step 2: Statue Bump Traverse
- **Action**:
  - Push RIGHT against Statue (6, 1) x25.
  - P blocked at (5, 1).
  - M moves Right on Row 16 to (29, 16).
  - *State*: P(5, 1), M(29, 16).

## Step 3: Align & Sync
- **Action**:
  - Down to (5, 2). M Up to (29, 15).
  - Right to (29, 2). M Right (Bump).
  - *State*: P(29, 2), M(29, 15).
  - Left to (22, 2). M Left to (22, 15).
  - *State*: P(22, 2), M(22, 15).

## Step 4: Ratchet & Solve
- **Action**:
  - Down to (22, 11). M Up to (22, 9) (Blocked by 8).
  - Push UP (22, 10). M Down to (22, 13).
  - Interact Down.