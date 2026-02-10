# Team Rocket HQ - Murkrow Puzzle

## STRATEGY: "The Col 4 Swap & 26 Ratchet"
Target: P(22, 13), M(22, 14).

## Current Status (Turn 36427)
- **Player**: (6, 16).
- **Murkrow**: (6, 1) (Synced).

## Strategy: "The Col 6 Swap"
1. **Swap Y**:
   - P(6, 16) -> Up (Blocked at 14). M(6, 1) -> Down -> M(6, 3).
   - State: P(6, 15), M(6, 3).
   - P(6, 15) -> Down 1 -> P(6, 16). M(6, 3) -> Up 1 -> M(6, 2).
   - State: P(6, 16), M(6, 2).

2. **Cross East**:
   - Right 20 -> P(26, 16). M(26, 2).

3. **Invert at Col 26**:
   - P(26, 16) -> Up 14 -> P(26, 2).
   - M(26, 2) -> Down 14 -> M(26, 16).

4. **Ratchet at Col 26**:
   - P(26, 2) -> Down 13 -> P(26, 15).
   - M(26, 16) -> Up 13 -> Blocked at 11 -> M(26, 12).

5. **Finish**:
   - Left 4 -> P(22, 15). M(22, 12).
   - Interact logic.