# Team Rocket HQ - Murkrow Puzzle

## Active Attempt: "The Mathematical Ratchet"
**Target State**: P(22, 13), M(22, 14).
**Ratchet Logic**: Sum(P_y + M_y) must equal 27. Currently ~23.
**Action**: Move P Down to force M Up against Wall(22, 10), increasing the sum.

## The Plan
1. **Align X (Col 22)**:
   - Left 1 -> P(26, 12). M moves to Col 22 (Expected).
   - **VISUAL CHECK**: M should be at (22, 11) or (22, 12).
2. **The Ratchet (Col 26)**:
   - Down 4 -> P(26, 16).
   - M moves Up. Hits Wall(22, 10) and stays at (22, 11).
   - State: P(26, 16), M(22, 11). (16+11 = 27).
3. **Position Y**:
   - Up 3 -> P(26, 13). M moves Down 3 -> M(22, 14).
4. **Approach**:
   - Left 4 -> P(22, 13). M Blocked West by Wall(21, 14). Stays (22, 14).
5. **Interact**:
   - Press A.