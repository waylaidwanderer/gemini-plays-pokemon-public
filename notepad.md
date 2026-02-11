# Team Rocket HQ - Murkrow Puzzle

## STATUS: EXECUTING "COL 4 INVERT"
**Goal**: Open Boss Door at (22, 14).
**Strategy**: Use Col 4 to invert Y, then Statue Bumping to sync X.

## Step 3: Align & Sync (Current)
- **Current**: P(5, 1), M(29, 16).
- **Action**:
  - Down 1 to (5, 2). M Up to (29, 15).
  - Right 24 to (29, 2). M Right (Bump).
  - *State*: P(29, 2), M(29, 15).
  - Left 7 to (22, 2).
    - M Left to (23, 15) (Blocked by Machine at 22, 15).
  - *State*: P(22, 2), M(23, 15).

## Step 4: Approach & Solve
- **Action**:
  - Down to (22, 13).
    - M tries Up (23, 15 -> 23, 14).
    - Blocked by Wall at (23, 14). M stays (23, 15).
  - *State*: P(22, 13), M(23, 15).
  - Interact Down (Boss Door) or Talk to M?
  - *Fallback*: If fails, M needs to be at (22, 12).
    - Requires P at (22, 13) and M at (22, 10) (Ratchet from 22, 4).