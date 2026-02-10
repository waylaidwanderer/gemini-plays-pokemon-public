# Team Rocket HQ - Murkrow Puzzle

## RECOVERY & SOLVE
Target: P(22, 13), M(22, 14).

## Current Status (Turn 36438)
- **Player**: (22, 16).
- **Murkrow**: (17, 5) (Estimated).

## Step 1: Sync to P(23, 5), M(18, 7)
1. **Move to (23, 16)**:
   - Right 1 -> P(23, 16). M(18, 5).
2. **Ratchet M Down (Col 18)**:
   - Up 11 -> P(23, 5).
   - M(18, 5) -> Down 11 -> M(18, 16).
   - Col 18 Blocked at 8. M stops at (18, 7).
   - State: P(23, 5), M(18, 7).

## Step 2: Move to Col 28
3. **Shift Right**:
   - Right 5 -> P(28, 5). M(23, 7).
4. **Align Y**:
   - Up 4 -> P(28, 1). M(23, 11).
5. **Ratchet M Up (Col 18)**:
   - Left 5 -> P(23, 1). M(18, 11).
   - Down 10 -> P(23, 11). M(18, 1).
   - Right 5 -> P(28, 11). M(23, 1).
   - Up 10 -> P(28, 1). M(23, 11).
   - (Wait, this loops).

## Alternate Step 2 (Direct to 28)
- From P(23, 1), M(18, 7).
- Right 10 -> P(28, 1). M(28, 7) (Clear).
- State: P(28, 1), M(28, 7).

## Step 3: The Col 22 Finish
- P Down 6 -> P(28, 7). M Up 6 -> M(28, 1).
- P Up 1 -> P(28, 6). M Down 1 -> M(28, 2).
- P Left 6 -> P(22, 6). M Left 6 -> M(22, 2).
- P Up 2 -> P(22, 4). M Down 2 -> M(22, 4).
- (Collision).
- From P(22, 6), M(22, 2).
- P Down 5 -> P(22, 11). M Up 5 -> M(22, 1) (Hits top).
- P Up 3 -> P(22, 8). M Down 3 -> M(22, 4).
- P Down 6 -> P(22, 14) [Blocked]. P(22, 13).
- M Up 6 -> M(22, 1).
- This assumes M was at 4. 4-6 = -2.
- **Problem**: P and M are too close on Y axis.
- Need to separate them.