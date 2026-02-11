# Team Rocket HQ - Murkrow Puzzle

## STATUS: EXECUTING "COL 4 INVERT & STATUE DESYNC"
**Goal**: Open Boss Door at (22, 14).
**Strategy**: Invert Y on Col 4, Desync X using Statue at (6, 1).

## Step 1: Reach (4, 16) [DONE]
- Current State: P(4, 16), M(4, 1).

## Step 2: Invert Y (Col 4) [IN PROGRESS]
- **Action**: Up 15 to (4, 1).
  - M moves Down 15 to (4, 16).
  - *Expect*: Battles (Traps at 4,9/11/12/13).
  - *Target*: P(4, 1), M(4, 16).

## Step 3: Statue Desync (Row 1)
- **Action**:
  - Right 1 to (5, 1).
  - Push Right x24 against Statue (6, 1).
    - P blocked at (5, 1).
    - M moves Right on Row 16 to (29, 16).
  - *State*: P(5, 1), M(29, 16).

## Step 4: Align & Swap
- **Action**:
  - Down to (5, 2). M Up to (29, 15).
  - Right to (28, 2). M Right to (29, 15) -> (28, 15).
  - Down to (28, 13). M Up to (28, 4).
  - *State*: P(28, 13), M(28, 4).

## Step 5: Ratchet & Solve
- **Action**:
  - Left to (22, 13). M Left to (22, 4).
  - Push UP (22, 14) x8. M to (22, 12).
  - Interact.