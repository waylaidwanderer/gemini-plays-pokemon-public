# Team Rocket HQ - Murkrow Puzzle

## STATUS: EXECUTING "WARP SHORTCUT & RIGHT RESYNC"
**Goal**: Open Boss Door at (22, 14).
**Strategy**: Use Warp (5, 15) to reach (25, 2), then Execute Right Wall Resync.

## Step 1: Take Warp (5, 15)
- **Current**: P(5, 13).
- **Action**: Down 2 to (5, 15).
  - *Result*: Warps to (25, 2).
  - *Assumption*: Murkrow follows or can be resynced.

## Step 2: Sync X (Right Wall)
- **Action**:
  - Right to (28, 2).
    - P(28, 2).
    - M moves Right. Syncs at 28.
  - *State*: P(28, 2), M(28, 2).

## Step 3: Invert & Offset
- **Action**:
  - Down to (28, 16). M Up to (28, 1).
  - Left to (22, 16).
    - M Left to (25, 1) (Blocked by Statue 24,1).
  - *State*: P(22, 16), M(25, 1).

## Step 4: Ratchet & Resync
- **Action**:
  - Up to (22, 11). M Down to (25, 6).
  - Push UP (22, 10) x10. M Down (6 -> 14).
  - Right to (28, 11). M Right to (28, 14) (Blocked by Wall).
  - *State*: P(28, 11), M(28, 14).

## Step 5: Solve
- **Action**:
  - Left to (22, 11). M Left to (22, 14).
  - Down to (22, 12). M Up to (22, 13).
  - Interact Down.