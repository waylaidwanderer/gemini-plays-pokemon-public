# Team Rocket HQ - Murkrow Puzzle

## Active Attempt: "The Col 22 Ratchet" (Mathematical Proof)
**Goal**: Sync P(22, 16), M(22, 11) -> Sum 27.
**Then**: P(22, 12), M(22, 13).

## Execution Steps
1. **Sync X (East Wall)**:
   - Move Down 7 -> P(24, 16). (Avoid Wall 23,9).
   - Move Right 5 -> P(29, 16).
   - **Pump Right 10x**: Ensures M is at Col 29.
   - State: P(29, 16), M(29, Y).
2. **Move to Col 22**:
   - Left 7 -> P(22, 16). M(22, Y).
3. **Reset Y (Top)**:
   - Up 14 -> P(22, 2). M(22, 16) (Hits Bottom).
   - State: P(22, 2), M(22, 16).
4. **Position for Ratchet**:
   - Down 5 -> P(22, 7). M(22, 11).
   - State: P(22, 7), M(22, 11).
5. **The Ratchet**:
   - Down 9 -> P(22, 16).
   - M(22, 11) -> Up 9 -> Hits Wall(22, 10). Stays at 11.
   - State: P(22, 16), M(22, 11).
6. **Converge**:
   - Up 4 -> P(22, 12).
   - M(22, 11) -> Down 4 -> Hits Wall(22, 14). Stays at 13.
   - State: P(22, 12), M(22, 13).
7. **Interact**:
   - Face Down. Press A.