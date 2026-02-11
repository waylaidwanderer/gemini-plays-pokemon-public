# Murkrow Solution: The Desk Ratchet

## Current State
- P(21, 13), M(21, 12).

## Execution
1. **X-Desync (Left Wall)**:
   - Move Left to (19, 13).
   - M blocked by Wall(20, 12). Stays (21, 12).
   - State: P(19, 13), M(21, 12).
2. **Y-Sync (Desk)**:
   - Move Up to (19, 11).
   - M moves to (21, 10) [Blocked by Desk]. Stays (21, 11).
   - State: P(19, 11), M(21, 11).
3. **Y-Reverse (P Above)**:
   - Move Up to (19, 10). M blocked. Stays (21, 11).
   - State: P(19, 10), M(21, 11).
4. **X-Adjust**:
   - Right to (20, 10). M(22, 11).
   - Down to (20, 11). M(22, 12).
   - Right to (21, 11). M blocked by Wall(23, 12). Stays (22, 12).
   - State: P(21, 11), M(22, 12).
5. **Finish**:
   - Down to (21, 13). M(22, 14) [Plate].
   - Walk Right to Open Door.