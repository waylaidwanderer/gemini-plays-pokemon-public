# Team Rocket HQ - Murkrow Puzzle

## FINAL SOLUTION: "West Sync & Ratchet"
Target State: P(22, 13), M(22, 14).

## Current Status (Turn 36398)
- **Player**: (12, 13) -> Moving to (1, 11).
- **Murkrow**: (24, 7) (Est).

## Execution Path
1. **Shift to Row 11**:
   - Up 2 -> P(12, 11). M(24, 9).
2. **Sync West (Col 1)**:
   - Left 20 -> P(1, 11). M(1, 9).
3. **Move to Col 22**:
   - Right 21 -> P(22, 11). M(22, 9).
4. **Position M at 11**:
   - Up 2 -> P(22, 9). M(22, 11).
5. **Ratchet P to 16**:
   - Down 7 -> P(22, 16). M(22, 11) [Blocked Up at 10].
6. **Finish**:
   - Up 3 -> P(22, 13). M(22, 14).
   - Interact.

## Mechanics
- **M moves**: Parallel X, Mirror Y.
- **Ratchet**: At (22, 11), M is blocked North by Wall (22, 10). Allows P to move South freely.