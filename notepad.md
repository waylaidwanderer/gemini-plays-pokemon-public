# Team Rocket HQ - Murkrow Puzzle

## STATUS: EXECUTING "THE ULTIMATE PLAN"
**Goal**: P(22, 13), M(22, 15).

## Plan: "Col 28 Dive" (Verified)
1. **Sync Left**:
   - Go Left to (1, 2). P(1, 2), M(1, 2).
2. **Setup Y-Split (Col 26)**:
   - Right to (26, 2). M(26, 2).
   - Down to (26, 9). M(26, 1) [Blocked by Wall 0].
   - Up to (26, 1). M(26, 9).
   - *State*: P(26, 1), M(26, 9).
3. **Move to Col 28**:
   - Right to (28, 1). M(28, 9).
   - *State*: P(28, 1), M(28, 9).
4. **The Dive (Col 28)**:
   - Down to (28, 7). M(28, 9) [Blocked Up by Wall 8].
   - Up to (28, 1). M(28, 15).
   - *State*: P(28, 1), M(28, 15).
5. **The Approach**:
   - Left to (22, 1). M(22, 15).
   - *State*: P(22, 1), M(22, 15).
6. **Unlock**:
   - Down to (22, 13). M(22, 15) [Blocked Up by Door 14].
   - Interact.