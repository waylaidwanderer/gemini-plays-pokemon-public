# Team Rocket HQ - Murkrow Puzzle

## STATUS: EXECUTING "THE ULTIMATE PLAN"
**Goal**: P(22, 13), M(22, 15).

## Plan: "The Col 5 Flip & Slide" (Final Verified)
1. **Vertical Flip (Col 5)**:
   - Current: P(5,1), M(5,3).
   - **Action**: Down to (5,16).
     - M moves Up: 3->2->1->0(Wall)->Stay 1.
     - *State*: P(5,16), M(5,1).
   - **Action**: Up to (5,1).
     - M moves Down: 1->16.
     - *State*: P(5,1), M(5,16).
2. **Horizontal Slide**:
   - **Action**: Right to (22,1).
     - M moves Right: (5,16) -> (22,16).
     - *State*: P(22,1), M(22,16).
3. **The Door Ratchet**:
   - **Action**: Down to (22,13).
     - M moves Up: 16 -> 15 -> 14(Door Block) -> Stay 15.
     - *State*: P(22,13), M(22,15).
4. **Interact**:
   - Press A (Facing Up).