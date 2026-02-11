# Team Rocket HQ - Murkrow Puzzle

## STATUS: RESETTING FOR "COL 19 RUSH"
**Goal**: Open Boss Door at (22, 14).
**Strategy**: Reset M to (7, 2). Rush down Col 19 (Secret Passage). Ratchet from North.

## Step 1: Reset (Current)
- **Current**: P(19, 1) (Warped).
- **Action**:
  - Down to (19, 2).
  - Right to (27, 2) (Exit).
  - Re-enter at (7, 2).

## Step 2: Col 19 Rush
- **Action**:
  - Right to (19, 2).
    - M Right to (19, 2).
  - Down to (19, 11).
    - Passes through Secret Passage (19, 8).
    - P(19, 11). M moves Up (2 -> -7, blocked at 1).
    - *State*: P(19, 11), M(19, 1).

## Step 3: Align & Ratchet
- **Action**:
  - Right to (22, 11).
    - M Right to (22, 1).
  - Push UP against Wall (22, 10) x13.
    - P blocked at 11.
    - M moves Down (1 -> 14).
  - *State*: P(22, 11), M(22, 14).

## Step 4: Solve
- **Action**:
  - Down to (22, 13).
  - Interact Down.