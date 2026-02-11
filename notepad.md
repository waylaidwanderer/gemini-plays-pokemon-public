# Murkrow Puzzle: Col 25 Shimmy Strategy

## Phase 1: Setup & Alignment
1. **Initial State**: P(3, 14), M(7, 1).
2. **Right Shift**:
   - Move Right to P(25, 14).
   - M(7, 1) -> M(23, 1). (Blocked by Statue 24).
   - State: P(25, 14), M(23, 1).

## Phase 2: Vertical Align
3. **Upward Bound**:
   - Move Up to P(25, 1).
   - M(23, 1) -> Down to M(23, 14).
   - **Constraint**: M blocked at (23, 9) [Wall].
   - **Result**: P(25, 7), M(23, 8).

## Phase 3: Left Hook
4. **Shift Left**:
   - Move Left to P(21, 7).
   - M(23, 8) -> Left to M(19, 8).
   - State: P(21, 7), M(19, 8).
5. **Final Vertical**:
   - Move Up to P(21, 1).
   - M(19, 8) -> Down to M(19, 14).
   - **Constraint**: M blocked at (19, 13) [Wall 14].
   - **Result**: P(21, 2), M(19, 13).

## Phase 4: Delivery
6. **Positioning**:
   - Move Right to P(24, 2).
   - M(19, 13) -> Right to M(22, 13).
   - State: P(24, 2), M(22, 13).
7. **Trigger**:
   - Move Up to P(24, 1).
   - M(22, 13) -> Down to M(22, 14) [Plate].
   - **Door Opens**.