# Murkrow Puzzle: Col 21 Ratchet Strategy

## Phase 1: Setup & Alignment (Col 3/7)
1. **X-Sync**:
   - Move Left to P(3, 2). M aligns to Col 7.
2. **Y-Init (Target P=16, M=9)**:
   - Move Down to P(3, 16). M stays at 1 (Blocked Row 0).
   - Move Up to P(3, 8). M moves to 9.
   - Move Down to P(3, 16). M stays at 9 (Blocked Row 8).
   - State: P(3, 16), M(7, 9).

## Phase 2: Crossing (Row 16/9)
3. **Cross**:
   - Move Right to P(21, 16). M moves to (21, 9).
   - Note: Avoid P(22, 16) Warp Trap.

## Phase 3: Ratchet (Col 21)
4. **Set Sum 27**:
   - Move Up to P(21, 14). M moves to 11.
   - Move Down to P(21, 16). M stays at 11 (Blocked Row 10).
   - State: P(21, 16), M(21, 11).

## Phase 4: Delivery
5. **Final Approach**:
   - Move Up to P(21, 13). M moves to 14.
   - Move Right to P(22, 13). M moves to (22, 14).
   - Interact (A).