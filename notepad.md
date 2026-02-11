# Team Rocket HQ - Murkrow Puzzle

## STATUS: EXECUTING "COL 25 RATCHET"
**Goal**: Place M at (23, 14) (Adjacent to Door) and P at (22, 16).
**Hypothesis**: Murkrow at (23, 14) counts as "at the door".

## Step 1: Navigate to Col 25
- **Current**: P(6, 15). M(5, 2) (Estimated).
- **Action**:
  - Right to (25, 15).
  - M mimics X: (5, 2) -> (25, 2).
  - *State*: P(25, 15), M(25, 2).

## Step 2: Ratchet M Down (Col 25)
- **Action**:
  - Push UP against Wall (25, 14) x14.
  - P blocked. M moves Down (2 -> 16).
  - *State*: P(25, 15), M(25, 16).

## Step 3: Re-align & Shift
- **Action**:
  - Down to (25, 16).
    - M moves Up to (25, 15).
  - Left to (22, 16).
    - P(22, 16).
    - M(25, 15) -> Left -> (23, 15) (Blocked by Wall 22, 15).
  - *State*: P(22, 16), M(23, 15).

## Step 4: Final Ratchet
- **Action**:
  - Push DOWN against Wall (22, 17).
  - M moves Up to (23, 14).
  - *State*: P(22, 16), M(23, 14).

## Step 5: Solve
- **Action**: Interact Up.