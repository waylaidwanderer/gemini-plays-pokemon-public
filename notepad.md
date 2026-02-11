# Team Rocket HQ - Murkrow Puzzle

## STATUS: EXECUTING COL 26 STRATEGY
**Goal**: Open Boss Door at (22, 14) from (22, 13).
**Condition**: M must be at (22, 15) when P is at (22, 13).

## Step 1: Navigate to Bottom Right
- **Current**: (3, 2).
- **Route**:
  1. Right to (26, 2).
  2. Down to (26, 9) (Blocked).
  3. Left to (22, 9).
  4. Down to (22, 16).
  5. Right to (26, 16).

## Step 2: Swap Y & Ratchet
- **Current Strategy**:
  1. **Swap Sides**: 
     - From (26, 16), go Right to Wall (Sync X), Left to 26.
     - Go Up to (26, 2). M goes Down to (26, 16).
     - *State*: P(26, 2), M(26, 16).
  2. **Ratchet Up**:
     - Go Down to (26, 9). M goes Up to (26, 12) (Blocked by Obstacle at 11).
     - *State*: P(26, 9), M(26, 12).
  3. **Align & Adjust**:
     - Left to (22, 9). M Left to (22, 12).
     - Up to (22, 6). M Down to (22, 15).
     - *State*: P(22, 6), M(22, 15).
  4. **Ratchet Door**:
     - Down to (22, 13). M Blocked Up by Door.
     - *State*: P(22, 13), M(22, 15).
     - INTERACT!