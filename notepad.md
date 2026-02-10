# Team Rocket HQ - Murkrow Puzzle

## STRATEGY: "The Col 4 Swap & 26 Ratchet"
Target: P(22, 13), M(22, 14).

## Current Status (Turn 36424)
- **Player**: (4, 2).
- **Murkrow**: (4, 15) (Inverted).

## Phase 2: The Ratchet (Col 26)
4. **Move to Col 26**:
   - Right 22 -> P(26, 2). M(26, 15).
5. **Ratchet M**:
   - Down 13 -> P(26, 15).
   - M(26, 15) -> Up 13 -> Blocked at 11 -> M(26, 12).
   - State: P(26, 15), M(26, 12).

## Phase 3: Finish (Col 22)
6. **Align**:
   - Left 4 -> P(22, 15). M(22, 12).
7. **The Squeeze**:
   - Up 1 (Bump Door). M(22, 12) -> Down 1 -> M(22, 13).
   - State: P(22, 15), M(22, 13).
   - Up 2 -> P(22, 13). M(22, 13) (Collision).
   - Wait. M(22, 13) -> Up 1 -> P(22, 12). M(22, 14).
   - Interact.