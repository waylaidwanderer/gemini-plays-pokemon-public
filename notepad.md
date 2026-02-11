# Team Rocket HQ - Murkrow Puzzle

## STATUS: EXECUTING "THE ULTIMATE PLAN"
**Goal**: P(22, 13), M(22, 15).

## Plan: "The Col 4 Flip & Direct Approach" (Verified Simulation)
1. **Move to Col 4 (Left Side)**:
   - *Status*: Complete.
2. **Vertical Flip (Col 4)**:
   - *Status*: Complete.
   - *State*: P(4, 1), M(4, 16).
3. **Move to Col 22 (Direct)**:
   - **Action**: Right to (22, 1).
     - M moves Right to (22, 16).
     - *Sim Check*: M crosses Row 16. Safe from (5, 15) trap.
     - *Risk*: (22, 16) trap. Assuming M safe or trap false.
     - *State*: P(22, 1), M(22, 16).
4. **Approach Door**:
   - **Action**: Down to (22, 13).
     - M moves Up to (22, 16) -> (22, 15) -> Blocked?
     - Map Check: (22, 15) is `TYPE_2889` (Wall).
     - M blocked at (22, 15). Stays at (22, 16).
     - *State*: P(22, 13), M(22, 16).
5. **Finish**:
   - **Action**: Interact (Face Down).
   - **Contingency**: If fails, M might need to be at (21, 15).
     - To achieve M(21, 15):
     - From P(19, 1), M(19, 16).
     - Down to (19, 4). M Ratchets on (19, 14) Wall to (19, 15).
     - Right to (23, 4). M Blocked at (21, 15) (Wall at 22, 15).
     - Down to (23, 13). M Blocked at (21, 15).
     - Left to (22, 13). M Blocked at (21, 15)? (20, 15) is Floor.
     - M moves to (20, 15).
     - To keep M at (21, 15), P must not move Left.
     - P at (23, 13), M(21, 15). Interact? (Diagonal).
     - Worth testing if direct approach fails.