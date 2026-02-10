# Team Rocket HQ - Murkrow Puzzle

## SOLVED: The "Ratchet & Bridge" Strategy
Target State: P(22, 13), M(22, 14).

## Current Status (Turn 36390)
- **Player**: (19, 6).
- **Murkrow**: (19, 12).
- **Goal**: Navigate to P(1, 16) via Col 19 Passage.

## Execution Path
1. **Passage North**:
   - Up 4 -> P(19, 2). M(19, 13) [Blocked by Wall at 14].
2. **West Sync**:
   - Left 18 -> P(1, 2). M(1, 13).
3. **South Sync**:
   - Down 14 -> P(1, 16). M(1, 1) [Blocked by Wall at 1].
4. **Col 25 Swap**:
   - Right 24 -> P(25, 16). M(25, 1).
   - Up 14 -> P(25, 2). M(25, 15).
5. **Ratchet**:
   - Left 5 -> P(20, 2). M(20, 15).
   - Down 14 -> P(20, 16). M(20, 11) [Blocked at 10].
6. **Finish**:
   - Up 3, Right 2. Interact.