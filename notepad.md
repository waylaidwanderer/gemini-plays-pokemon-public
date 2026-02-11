# Team Rocket HQ - Murkrow Puzzle

## STATUS: EXECUTING "LEFT-SIDE DOOR RATCHET"
**Goal**: Open Boss Door at (22, 14).
**Target State**: P(22, 15), M(22, 13).

## Strategy
1. **Sync X (Col 1)**:
   - P Left to (1, 2). M Left to (1, 2).
2. **Invert Y (Bottom)**:
   - P Down to (1, 16). M Up to (1, 1).
3. **Desync X (Use Grunt)**:
   - P Up to (1, 13). M Down to (1, 4).
   - P Right to (22, 13). M Blocked at (1, 4) by Grunt.
   - *State*: P(22, 13), M(1, 4).
4. **Ratchet Y (Drop M)**:
   - P Up to (22, 11). M Down to (1, 6).
   - P Push Up against Wall (22, 10). M Down to (1, 15).
   - *State*: P(22, 11), M(1, 15).
5. **Resync X (Right)**:
   - P Push Right against Wall (23, 11). M Right to (22, 15).
   - *State*: P(22, 11), M(22, 15).
6. **Convergence**:
   - P Down to (22, 13). M Up to (22, 13).
   - P Left -> (21, 13). M Left -> (21, 13).
   - P Down -> (21, 15). M Up -> (21, 11).
   - P Right -> (22, 15). M Right -> (22, 11).
7. **Solve**:
   - P Push Up (Door). M Down -> 12.
   - P Push Up (Door). M Down -> 13.
   - Interact (A).