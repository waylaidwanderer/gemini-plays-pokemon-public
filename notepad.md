# Team Rocket HQ - Murkrow Puzzle

## FINAL SOLUTION: "The Col 26 Ratchet Loop"
Target: P(22, 13), M(22, 14).

## Current Status (Turn 36435)
- **Player**: (22, 16).
- **Murkrow**: (22, 5).

## Execution Path
1. **Invert Y (Col 25)**:
   - Right 3 -> P(25, 16). M(25, 5).
   - Up 11 -> P(25, 5). M(25, 16).
2. **Ratchet M Up (Col 26)**:
   - Right 1 -> P(26, 5). M(26, 16).
   - Down 11 -> P(26, 16).
   - M(26, 16) -> Up 11 -> Blocked at 10 -> M(26, 11).
   - State: P(26, 16), M(26, 11).
3. **Align Y**:
   - Up 3 -> P(26, 13). M(26, 14).
4. **Finish**:
   - Left 4 -> P(22, 13). M(22, 14).
   - Interact (Face Down).