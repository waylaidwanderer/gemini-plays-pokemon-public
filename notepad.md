# Murkrow Solution: The Wall Block

## Current State
- P(22, 16). M(22, 15) [Estimated].
- Goal: M(22, 14).

## Execution Plan
1. **Desync X (Wall at 21,15)**:
   - Move **Left x2** to (20, 16).
   - M tries to move Left but hits Wall at (21, 15).
   - M stays at (22, 15).
   - State: P(20, 16), M(22, 15).

2. **Position M**:
   - Move **Up** to (20, 15).
   - M (Mimic Y) moves Up to (22, 14).
   - **M is on Target**.

3. **Check Status**:
   - Look for "Click" or Door Opening.
   - If nothing, try moving to see door.