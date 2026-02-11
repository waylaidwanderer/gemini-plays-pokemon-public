# Murkrow Solution: The Desk Ratchet (Plan B)

## Current State
- P(20, 15). M(21, 13).
- Goal: M(22, 14).

## Execution Plan
1. **Setup**:
   - Move **Left** to (19, 15). M -> (20, 13).
   - Move **Up** to (19, 13). M -> (20, 11).
   - Move **Up** to (19, 11). M -> (20, 9).
   
2. **X-Ratchet (Desk at 21,10?)**:
   - Move **Right** to (22, 11). M -> (23, 9).
   - Move **Down** to (22, 12). M -> (23, 10).
   - Move **Left** to (20, 12).
     - M tries (21, 10).
     - If blocked: M stays (22, 10). **Desync Achieved**.
   
3. **Delivery**:
   - Move **Down** (x3) to (20, 15).
   - M moves Down (x3) to (22, 13).
   - Move **Down** to (20, 16).
   - M moves Down to (22, 14).
   - **SOLVED**.