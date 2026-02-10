# Team Rocket HQ - Murkrow Puzzle

## STATUS: RESET COMPLETE (Entering B2F)
- **Goal**: Execute "The 22-11 Ratchet" perfectly.
- **Murkrow**: Will be at (7, 2).
- **Player**: Will start at (27, 2) or (3, 14) depending on entry. (Souvenir Shop entry lands at 27, 2).

## THE SOLUTION (Step-by-Step)
1. **Sync X (West)**:
   - Go to P(1, 2). Murkrow hits West Wall at (1, 2).
   - **State**: P(1, 2), M(1, 2).
2. **Invert Y (Col 1)**:
   - Down 14 -> P(1, 16). M moves Up to (1, 1) (Blocked North).
   - Up 14 -> P(1, 2). M moves Down to (1, 15).
   - **State**: P(1, 2), M(1, 15).
3. **Move to Col 22**:
   - Right 21 -> P(22, 2). M(22, 15).
   - **State**: P(22, 2), M(22, 15).
4. **Ratchet M Up**:
   - Down 14 -> P(22, 16).
   - M(22, 15) -> Up 14 -> Blocked at 10 -> M(22, 11).
   - **State**: P(22, 16), M(22, 11).
5. **Converge**:
   - Up 4 -> P(22, 12). M(22, 15) (Wait, M moves Down).
   - M(22, 11) -> Down 4 -> Hits Wall(22, 14)? 
   - No, (22, 14) is the Door. If locked, it's solid.
   - If (22, 14) is solid, M stops at (22, 13).
   - **State**: P(22, 12), M(22, 13).
6. **Interact**:
   - Face Down. Press A.