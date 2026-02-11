# Team Rocket HQ - Murkrow Puzzle

## STATUS: RESETTING & RE-ENTERING
**Goal**: Re-enter Map 3_49 to reset Murkrow to (7, 2).
**Current**: Map 3_48 (7, 3). Moving to re-enter.

## Plan: "North Approach (Col 3 Variant)"
1. **Sync X (Col 3)**:
   - Start at (7, 2).
   - Left 4 to (3, 2).
   - *State*: P(3, 2), M(3, 2).
2. **Invert Y (Col 3)**:
   - Down to (3, 16).
   - *Note*: Avoids wall at (1, 5) and warp at (1, 4)?
   - *State*: P(3, 16), M(3, 1).
3. **Sync X (Col 1)**:
   - Left to (1, 16).
   - *State*: P(1, 16), M(1, 1).
4. **Swap Y**:
   - Up to (1, 1).
   - *State*: P(1, 1), M(1, 16).
5. **Traverse & Align**:
   - Right to (22, 1). M Right to (22, 16).
   - Down to (22, 13). M Up to (22, 4).
   - *State*: P(22, 13), M(22, 4).
6. **Ratchet**:
   - Push UP against Door/Wall (22, 14) x9.
   - M moves Down (4 -> 13).
   - *State*: P(22, 13), M(22, 13).
7. **Solve**:
   - Collision Squeeze or Interact.