# Murkrow Puzzle: Jed's Ratchet Strategy

## Phase 1: Setup & Alignment
1. **X-Sync (Left)**:
   - Move Left to P(3, 2). (M blocked at 6, stays 7).
   - Offset: P = M - 4.
2. **Y-Init**:
   - Move Down to P(3, 13). M stays 1 (blocked Up).
   - Move Up to P(3, 3). M moves to 11.
   - State: P(3, 3), M(7, 11).

## Phase 2: Crossing & X-Offset
3. **Cross Walls**:
   - Move Right to P(26, 3).
   - M moves to 25 (Blocked by Wall 26).
   - State: P(26, 3), M(25, 11).
   - Offset: P = M + 1.
4. **Position for Jed**:
   - Move Left to P(19, 3). M moves to 18.
   - Move Up to P(19, 1). M moves to 13.
   - State: P(19, 1), M(18, 13).

## Phase 3: The Jed Ratchet
5. **Ratchet**:
   - Move Down to P(19, 14).
   - M tries Up (13->12), Blocked by Jed(18, 12).
   - State: P(19, 14), M(18, 13).
6. **Y-Swap**:
   - Move Up to P(19, 13). M moves to 14.
   - State: P(19, 13), M(18, 14).

## Phase 4: Delivery
7. **X-Sync (Final)**:
   - Move Left to P(14, 13).
   - M moves Left to 14 (Blocked by Wall 13).
   - State: P(14, 13), M(14, 14).
8. **Finish**:
   - Move Right to P(22, 13). M moves to (22, 14).
   - Interact (A).