# Team Rocket HQ - Murkrow Puzzle

## SOLVED: The "Pocket Ratchet" Strategy
Target State: P(22, 13), M(22, 14).

## Current Status (Turn 36395)
- **Player**: (12, 9) -> Moving to (3, 9).
- **Murkrow**: (19, 11) (Blocked West).

## Execution Path
1. **Setup Pocket**:
   - Left 9 -> P(3, 9). M(19, 11) [Blocked West].
   - Up 7 -> P(3, 2). M(19, 13) [Blocked South at 14].
   - Right 19 -> P(22, 2). M(22, 13).
2. **The "Pocket Ratchet"**:
   - Down 14 -> P(22, 16). M(22, 11) [Blocked Up at 10].
   - Up 4 -> P(22, 12). M(22, 14) [Blocked Down at 15].
   - Down 1 -> P(22, 13). M(22, 14) [Collision].
3. **Finish**:
   - Interact.