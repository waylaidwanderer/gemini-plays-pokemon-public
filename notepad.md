# Murkrow Solution: The Grunt Bump & Test

## Current Status
- P(20, 14). M(20, 13) [Visual Confirmation].
- Grunt at (21, 14).

## Execution
1. **Align X (Grunt Bump)**:
   - Move **Right**. P stays (20, 14). M -> (21, 13).
   - Move **Right**. P stays (20, 14). M -> (22, 13).

2. **Test Y (Move Down)**:
   - Move **Down** to (20, 15).
   - **Check M**:
     - If M at (22, 14) [Plate]: **Mimic Y**.
     - If M at (22, 12): **Mirror Y**.
   - If Mimic Y: We have a problem (M leaves plate when P moves Up).
   - If Mirror Y: We are golden (M blocked by Wall 22,15 when P moves Up).

3. **Proceed**:
   - Navigate to Door based on Y behavior.