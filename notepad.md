# Team Rocket HQ - Murkrow Puzzle

## STATUS: EXECUTING "THE ULTIMATE PLAN"
**Goal**: P(22, 13), M(22, 15).

## Plan: "The Col 4 Flip & Detour" (Refined)
1. **Setup**:
   - Current: P(1, 2), M(1, 2).
   - **Action**: Move to (4, 1).
   - Path: Right to (4, 2), Up to (4, 1).
     - M: (1,2)->(4,2)->(4,3).
     - *State*: P(4, 1), M(4, 3).
2. **Vertical Flip (Col 4)**:
   - **Action**: Down to (4, 16).
     - M: 3->2->1->0(Block)->1.
     - *State*: P(4, 16), M(4, 1).
   - **Action**: Up to (4, 1).
     - M: 1->16.
     - *State*: P(4, 1), M(4, 16).
3. **Horizontal Slide**:
   - **Action**: Right to (22, 1).
     - M: (4,16)->(22,16).
     - *State*: P(22, 1), M(22, 16).
4. **Ratchet & Detour (Via Col 19)**:
   - **Action**: Down to (22, 7).
     - M: 16->15->14(Block)->15.
     - *State*: P(22, 7), M(22, 15).
   - **Action**: Left to (19, 7).
     - M: (22,15)->(19,15).
   - **Action**: Down to (19, 9).
     - M: Blocked by Row 14, stays 15.
   - **Action**: Right to (22, 9).
     - M: (19,15)->(22,15).
5. **Finish**:
   - **Action**: Down to (22, 13).
     - M: Blocked by Door, stays 15.
   - **Action**: Interact (Face Down).