# Team Rocket HQ - Murkrow Puzzle

## STRATEGY: "The Col 4 Swap & 26 Ratchet"
Target: P(22, 13), M(22, 14).

## Current Status (Turn 36428)
- **Player**: (26, 16).
- **Murkrow**: (26, 2).

## Strategy: "The Col 28 Inversion"
1. **Move to Col 28**:
   - Right 2 -> P(28, 16). M(28, 2).
2. **Invert at Col 28**:
   - Up 14 -> P(28, 2).
   - M(28, 2) -> Down 14 -> M(28, 16).
   - State: P(28, 2), M(28, 16).
3. **Move to Col 26**:
   - Left 2 -> P(26, 2). M(26, 16).
4. **Ratchet at Col 26**:
   - Down 13 -> P(26, 15).
   - M(26, 16) -> Up 13 -> Blocked at 11 -> M(26, 12).
   - State: P(26, 15), M(26, 12).
5. **Adjust Y**:
   - Up 2 -> P(26, 13). M(26, 14).
6. **Finish**:
   - Left 4 -> P(22, 13). M(22, 14).
   - Interact.