# Murkrow Solution: The Grunt Bump

## Current State
- P(21, 13), M(21, 12).
- Plan: Use Grunt at (21, 14) and Wall at (21, 15) to desync.

## Execution
1. **Positioning**:
   - Move Left to (20, 13). P(20, 13), M moves to (20, 12) OR stays (21, 12).
   - Move Down to (20, 14). P(20, 14). M moves to (20, 13) OR (21, 13).
   - **Crucial**: M is now at Y=13, P is at Y=14.

2. **X-Desync (Grunt Bump)**:
   - Move Right (Bump Grunt). P stays (20, 14). M moves Right (X+1).
   - Move Right (Bump Grunt). P stays (20, 14). M moves Right (X+2).
   - Target M X: 22.

3. **Delivery**:
   - Move Down to (20, 15). P(20, 15). M moves Down to (22, 14).
   - Move Right (Bump Wall). P stays (20, 15). M moves Right to (23, 14) [Door].
   - **OPEN!**