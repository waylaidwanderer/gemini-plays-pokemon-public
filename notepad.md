# Team Rocket HQ - Murkrow Puzzle

## Active Attempt: "The High Road West"
**Target**: P(22, 12), M(22, 13).

## Current Status (Turn 36465)
- **Player**: (28, 13) (Deduced).
- **Murkrow**: (22, 9) (Deduced).

## Execution Path
1. **Lift M to Row 6**:
   - Down 3 -> P(28, 16). M(22, 9) -> Up 3 -> M(22, 6).
2. **Move M East to Col 28**:
   - Left 4 -> P(24, 16). M(22, 6) -> Left 4 -> M(18, 6).
   - Right 10 -> P(28, 16). M(18, 6) -> Right 10 -> M(28, 6).
   - *Constraint*: Assumes Col 24 Row 6 is walkable for M.
3. **Drop M to Row 14**:
   - Up 8 -> P(28, 8). M(28, 6) -> Down 8 -> M(28, 14).
4. **Move M West to Door**:
   - Left 6 -> P(22, 8). M(28, 14) -> Left 6 -> M(22, 14).
   - *Note*: M is pinned at (22, 14) by West Wall.
5. **Adjust & Finish**:
   - Down 4 -> P(22, 12). M(22, 11).
   - Down 1 -> P(22, 13). M(22, 11).
   - Up 3 -> P(22, 11). M(22, 14).
   - Down 1 -> P(22, 12). M(22, 13).
   - Interact.