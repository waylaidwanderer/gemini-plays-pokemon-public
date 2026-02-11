# Murkrow Solution: The Wall Bump (Corrected)

## Current State
- P(20, 15). M(21, 13) [Visual Confirmation].
- Obstacles:
  - Wall at (21, 15) [Right of Player].
  - Grunt at (21, 14).
  - Boss Door at (23, 14). Target M: (22, 14).

## Execution Plan
1. **X-Align (Wall Bump)**:
   - Input: **Right**.
   - P stays (20, 15) [Blocked].
   - M (Mimic X) moves to (22, 13).
   - State: P(20, 15), M(22, 13).

2. **Y-Align (Probe)**:
   - Input: **Up** (to 20, 14).
   - If Mirror Y: M moves Down to (22, 14). **SOLVED**.
   - If Mimic Y: M moves Up to (22, 12).
     - Correction: **Down, Down** (to 20, 16). M moves to (22, 14).

3. **Delivery**:
   - Walk to Door (23, 14).