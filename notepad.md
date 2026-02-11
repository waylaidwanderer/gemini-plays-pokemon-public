# Team Rocket HQ - Murkrow Puzzle

## STATUS: EXECUTING "THE ULTIMATE PLAN"
**Goal**: P(22, 13), M(22, 15).

## Plan: "Col 25 Deep Dive"
1. **Sync Left**: P(1, 2), M(1, 2). (Done)
2. **Col 26 Setup**:
   - Right to (26, 2). M->(26, 2).
   - Down to (26, 9). M->(26, 1).
   - Up to (26, 1). M->(26, 9).
     - *State*: P(26, 1), M(26, 9).
3. **Col 25 Dive**:
   - Left to (25, 1). M->(25, 9).
   - Down to (25, 16). M->(25, 2).
   - Up to (25, 1). M->(25, 16).
     - *State*: P(25, 1), M(25, 16).
4. **The Lock**:
   - Left to (22, 1). M->(22, 16).
   - Down to (22, 2). M->(22, 15).
   - Down to (22, 13). M->(22, 15) (Hits Door).
   - Interact.