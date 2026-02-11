# Murkrow Solution: The Flanking Maneuver

## Current State
- P(22, 16). M(24, 16) [Estimated].
- Goal: Route M to (22, 14) via Row 13 to avoid Grunt.

## Execution Plan
1. **Reset X & Move to Row 13**:
   - Move **Left x4** to (18, 16). M -> (20, 16).
   - Move **Up x3** to (18, 13). M -> (20, 13).
   - State: P(18, 13), M(20, 13).

2. **Position M**:
   - Move **Right x2** to (20, 13). M -> (22, 13).
   - Move **Down** to (20, 14). M -> (22, 14) [TARGET].

3. **Verify & Enter**:
   - Move **Down** to (20, 15). M blocked at (22, 15). Stays.
   - Move **Down** to (20, 16). M blocked. Stays.
   - Move **Right** to (23, 16). Check Door.