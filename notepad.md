# Murkrow Solution: The Double Desk Ratchet (FINAL)

## Current Status
- P(17, 14), M(17, 13).
- Goal: P(23, 14), M(22, 14).

## Execution Path
1. **Positioning**:
   - Move **Right x3** to (20, 14). M -> (20, 13).
   - Move **Up x3** to (20, 11). M -> (20, 10).

2. **Ratchet 1 (X-Shift)**:
   - Move **Right** to (21, 11).
   - M tries (21, 10) [Desk]. Blocked. Stays (20, 10).
   - State: P(21, 11), M(20, 10).

3. **Ratchet 2 (Align)**:
   - Move **Down** to (21, 12). M -> (20, 11).
   - Move **Right** to (22, 12). M -> (21, 11).
   - Move **Up** to (22, 11).
   - M tries (21, 10) [Desk]. Blocked. Stays (21, 11).
   - State: P(22, 11), M(21, 11).

4. **Delivery**:
   - Move **Down x3** to (22, 14). M -> (21, 14).
   - Move **Right** to (23, 14) [Door]. M -> (22, 14) [Plate].
   - **ENTER!**