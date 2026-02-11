# Team Rocket HQ - Murkrow Puzzle

## STATUS: EXECUTING "THE ULTIMATE PLAN"
**Goal**: P(22, 13), M(22, 15).

## Step 1: Sync X (Right Wall)
- **Action**: Move Right to (28, 2) and bump wall.
- **Result**: P(28, 2), M(28, 2).

## Step 2: Top Ratchet (Col 26)
- **Action**:
  - Left to (26, 2). M->(26, 2).
  - Down to (26, 9). M->(26, 1) (Hits top wall).
  - *State*: P(26, 9), M(26, 1).

## Step 3: The Cross (Col 26)
- **Action**:
  - Up to (26, 1). M->(26, 9).
  - *State*: P(26, 1), M(26, 9).

## Step 4: The Swap (Col 28)
- **Action**:
  - Right to (28, 1). M->(28, 9).
  - Down to (28, 13). M->(28, 9) (Hits Wall 28,8).
  - *State*: P(28, 13), M(28, 9).

## Step 5: The Dive (Col 28)
- **Action**:
  - Up to (28, 7). M->(28, 15).
  - *State*: P(28, 7), M(28, 15).

## Step 6: The Lock (Col 25)
- **Action**:
  - Left to (25, 7). M->(25, 15).
  - Down to (25, 13). M->(25, 15) (Hits Wall 25,14).
  - *State*: P(25, 13), M(25, 15).

## Step 7: Finish
- **Action**:
  - Left to (22, 13). M->(22, 15).
  - Interact.