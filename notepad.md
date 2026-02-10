# Team Rocket HQ - Murkrow Puzzle

## FINAL SOLUTION: "The Victory Lap" (Validated)
Target: M(22, 14).

## Current Status (Turn 36400)
- **Player**: (11, 11).
- **Murkrow**: (28, 16) (Assuming last ratchet worked).

## Execution Path
1. **Redundant Ratchet**:
   - Up 7 (Verify P blocked, M at 16).
2. **Horizontal Ratchet**:
   - Right 6 -> P(17, 11). M(28, 16).
3. **Align to Col 7/18**:
   - Left 10 -> P(7, 11). M(18, 16).
4. **Vertical Ratchet (Row 12)**:
   - Up 7 -> P(7, 5). M(18, 16).
   - Down 4 -> P(7, 9). M(18, 12).
5. **Cross to Col 11/22**:
   - Right 4 -> P(11, 9). M(22, 12).
6. **Final Ratchet to Door**:
   - Up 2 -> P(11, 9) [Blocked at 8]. M(22, 14).
7. **Interact**.

## Notes
- P blocked at Row 8 and Row 10/14 used to manipulate M.
- M crosses West->East on Row 12.
- M drops to Door on Col 22.