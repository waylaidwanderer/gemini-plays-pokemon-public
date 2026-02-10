# Team Rocket HQ - Murkrow Puzzle

## Active Attempt: "The Col 4 Reset & 22 Ratchet"
**Current State**: P(24, 9). M(Unknown).
**Goal**: Reset Y-axis at Col 4, then Ratchet M to door at Col 22.

## The Master Plan
1. **Sync X (West)**:
   - Move Left to P(4, 9). M hits West Wall.
   - **State**: P(4, 9), M(4, 9) (Synced X).
2. **Reset Y (Col 4)**:
   - Move Up 7 -> P(4, 2). M(4, 16). (M hits bottom wall).
   - **State**: P(4, 2), M(4, 16).
3. **Setup Y (Col 4)**:
   - Move Down 10 -> P(4, 12). M Up 10 -> M(4, 6).
   - **State**: P(4, 12), M(4, 6).
4. **Move to Col 22**:
   - Right 18 -> P(22, 12). M(22, 6).
   - **State**: P(22, 12), M(22, 6).
5. **Ratchet M Down (Col 22)**:
   - Pump Up 10 times against Wall(22, 10).
   - P stays at (22, 11). M moves Down from 6 to 14 (Pinned).
   - **State**: P(22, 11), M(22, 14).
6. **Finish**:
   - Down 1 -> P(22, 12). M Up 1 -> M(22, 13).
   - Interact Down.