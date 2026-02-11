# Murkrow Solution: The Corridor Flank

## Current State
- P(22, 16). M(22, 15) [Estimated].
- Goal: M(22, 14).

## Execution Plan
1. **Reset X**:
   - Move **Left x2** to (20, 16).
   - M moves to (20, 15).
   
2. **Move Up to Row 13**:
   - Move **Up** to (20, 15). M -> (20, 14).
   - Move **Up** to (20, 14). M -> (20, 13).

3. **X-Align (Grunt Bump)**:
   - Move **Right** (Bump Grunt). P stays (20, 14). M -> (21, 13).
   - Move **Right** (Bump Grunt). P stays (20, 14). M -> (22, 13).

4. **Delivery**:
   - Move **Down** to (20, 15). M -> (22, 14).
   - **Check Door**.