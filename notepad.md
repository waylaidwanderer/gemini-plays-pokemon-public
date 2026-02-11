# Murkrow Solution: Grunt Bump & Door Check

## Current Status
- **Verified**: P(17, 14), M(17, 13).
- **Rule**: Murkrow Mimics X and Mimics Y.
- **Offset**: M = (P.X, P.Y-1).

## Execution Plan
1. **Approach Grunt**:
   - Move **Right x3** to (20, 14). M -> (20, 13).
2. **X-Desync (Grunt Bump)**:
   - Move **Right** (Bump Grunt). P stays (20, 14). M -> (21, 13).
   - Move **Right** (Bump Grunt). P stays (20, 14). M -> (22, 13).
3. **Trigger Plate**:
   - Move **Down** to (20, 15). M -> (22, 14) [Plate].
   - **Check for Door Open sound/visual**.
4. **Enter Door (Attempt)**:
   - Move **Down** to (20, 16). M stays (22, 14) [Blocked by Wall 22,15].
   - Move **Right x3** to (23, 16). M stays (22, 14) [Blocked by Door 23,14?].
   - Move **Up x2** to (23, 14). M moves to (22, 12).
     - *Risk*: Door closes when M moves off.
     - *Hope*: Latched or M blocked.