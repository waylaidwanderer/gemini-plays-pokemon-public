# Team Rocket HQ - Murkrow Puzzle

## STATUS: RESETTING ROOM
**Goal**: Exit map via (27, 2) to reset Murkrow.
**Plan**: Execute "Right-Side Jed Ratchet".

## Strategy: "Right-Side Jed Ratchet"
1. **Reset**: Exit (27, 2) and Re-enter. Start P(7, 2).
2. **Sync X (Right Wall)**:
   - Move Right to Col 28 (Use Row 3 to avoid Exit).
   - *State*: P(28, 3), M(28, 3).
3. **Invert Y (Bottom Wall)**:
   - P Down to (28, 16). M Up to (28, 1).
   - *State*: P(28, 16), M(28, 1).
4. **Position for Ratchet**:
   - P Up to (28, 3). M Down to (28, 14).
   - *State*: P(28, 3), M(28, 14).
5. **Align Col 18**:
   - Left to (18, 3). M Left to (18, 14).
6. **The Jed Lock**:
   - P Down to (18, 15).
   - M tries Up -> Hits Jed (18, 12). Stuck at (18, 13).
   - *End State*: P(18, 15), M(18, 13).
7. **The Door Ratchet (Final Sync)**:
   - Move Right to 22. P(22, 15), M(22, 13).
   - Move Up (Push Door). P blocked. M Down -> 14.
   - *Final State*: P(22, 15), M(22, 14).
8. **Solve**: Interact (A).