# Murkrow Puzzle: Jed's Ratchet & Flank Strategy

## Phase 1: Reset & Setup
1. **Reset**:
   - Go to P(3, 14). M resets to (7, 1).
2. **Jed Positioning**:
   - Move Right to P(14, 14). M(18, 1).
   - Move Up to P(14, 3). M(18, 11) [Hits Jed].
   - Move Right to P(15, 3). M(19, 11).
   - Move Up to P(15, 1). M(19, 13).
   - Move Left to P(14, 1). M(18, 13) [Below Jed].

## Phase 2: Vertical Ratchet
3. **Lock Y=13**:
   - Move Down to P(14, 14).
   - M tries Up (13->1). Blocked by Jed at 12.
   - Result: P(14, 14), M(18, 13).
4. **Target Y**:
   - Move Up to P(14, 13). M(18, 14).

## Phase 3: The Flank & Sync
5. **East Flank**:
   - Move Up to P(14, 12). M(18, 15).
   - Move Right to P(25, 12). M(29, 15).
   - Move Down to P(25, 13). M(29, 14).
6. **X-Sync (Right Wall)**:
   - Move Right to P(28, 13) [Adjust as needed].
   - M hits Wall 29 at (29, 14).
   - Align P and M to same X.
   - State: P(28, 13), M(28, 14).

## Phase 4: Delivery
7. **Final Approach**:
   - Move Left to P(22, 13). M(22, 14).
   - Interact.