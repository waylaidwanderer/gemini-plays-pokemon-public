# Team Rocket HQ - Murkrow Puzzle

## STATUS: RESETTING ROOM
**Goal**: Re-enter Map 3_49 to reset Murkrow.
**Plan**: "Left-Side Door Ratchet".

## Strategy: "Left-Side Door Ratchet"
1. **Reset**: Re-enter 3_49. Start P(7, 2).
2. **Sync X (Left Wall)**:
   - Move Left to (1, 2).
   - *State*: P(1, 2), M(1, 2).
3. **Invert Y (Battle Path)**:
   - Move Down to (1, 16).
   - *Note*: Expect battles (Voltorb/Geodude). No warps.
   - *State*: P(1, 16), M(1, 1) (M blocked at Top).
4. **Position for Ratchet**:
   - Move Right to (22, 16).
   - *State*: P(22, 16), M(22, 1).
   - Move Up to (22, 15).
   - *State*: P(22, 15), M(22, 2).
5. **The Door Ratchet**:
   - Push UP against Boss Door (22, 14).
   - P blocked at (22, 15).
   - M moves Down (2->3->...->14).
   - Repeat until M is at (22, 14).
6. **Solve**: Interact (A).