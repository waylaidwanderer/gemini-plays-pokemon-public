# Team Rocket HQ - Murkrow Puzzle

## STATUS: EXECUTING "COL 25 RATCHET"
**Goal**: Place M at (22, 14) (Boss Door) or (23, 14).
**Current State**: P(28, 16), M(28, 1).

## Step 1: Navigate to Col 25 & Align Y
- **Action**:
  - Left 3 to (25, 16).
    - M Left 3 to (25, 1).
  - Up 1 to (25, 15).
    - M Down 1 to (25, 2).
  - *State*: P(25, 15), M(25, 2).

## Step 2: Ratchet M Down (Col 25)
- **Action**:
  - Push UP against Wall (25, 14) x12.
  - P blocked. M moves Down (2 -> 14).
  - *State*: P(25, 15), M(25, 14).

## Step 3: Shift to Door
- **Action**:
  - Left 3 to (22, 15).
    - M Left 3 to (22, 14).
    - *Note*: If (22, 14) is blocked by Door, M stops at (23, 14).
  - *State*: P(22, 15), M(22/23, 14).

## Step 4: Solve
- **Action**: Interact Up (A).