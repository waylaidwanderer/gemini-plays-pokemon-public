# Team Rocket HQ - Murkrow Puzzle

## STATUS: EXECUTING "THE ULTIMATE PLAN"
**Goal**: P(22, 13), M(22, 15).

## Plan: "The Col 4 Flip" (Verified)
1. **Vertical Flip (Col 4)**:
   - *Status*: Complete.
   - *Current State*: P(4, 1), M(4, 16).
2. **Horizontal Slide**:
   - *Status*: Complete.
   - *Current State*: P(22, 1), M(22, 16).
3. **The Door Ratchet & Detour**:
   - **Goal**: Go to (22, 13).
   - **Obstacle**: Wall at (22, 8).
   - **Logic**: 
     - M is in Row 15/16.
     - Row 14 is a Wall (Ratchet).
     - Any Down move by P (Up for M) keeps M pinned at Row 15.
     - Detouring Left/Right moves M Left/Right along Row 15.
   - **Action**: Use BFS to (22, 13).
     - Expected Path: (22,7)->(21,7)->(21,9)->(22,9)->(22,13).
     - *End State*: P(22, 13), M(22, 15).
4. **Interact**:
   - Press A (Facing Down).