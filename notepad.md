# Murkrow Solution: The Double Ratchet (Desk & Ceiling)

## Current State
- P(20, 15), M(20, 14). Verified by sight.
- Goal: P(23, 14), M(22, 14).

## Execution Plan
1. **X-Ratchet (Desk)**:
   - Move Left to (19, 15).
   - Move Up to (19, 11). M(19, 10).
   - Move Right to (21, 11).
     - M tries (21, 10) [Desk], Blocked. Stays (20, 10).
     - State: P(21, 11), M(20, 10). (Offset: X+1, Y+1).

2. **Y-Ratchet (Desk 2)**:
   - Move Down to (21, 12). M(20, 11).
   - Move Right to (22, 12). M(21, 11).
   - Move Up to (22, 11).
     - M tries (21, 10) [Desk], Blocked. Stays (21, 11).
     - State: P(22, 11), M(21, 11). (Offset: X+1, Y+0).

3. **Delivery**:
   - Move Down to (22, 14). M(21, 14).
   - Move Right to (23, 14) [Door]. M(22, 14) [Plate].
   - **OPEN!**