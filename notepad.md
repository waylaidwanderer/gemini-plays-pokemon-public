# Team Rocket HQ - Murkrow Puzzle

## STRATEGY: "The Col 1 Swap (Revised)"
Target: P(22, 13), M(22, 14).

## Current Status (Turn 36419)
- **Player**: (3, 2).
- **Murkrow**: (3, 3) (Calculated).

## Phase 1: The Swap (Col 1)
1. **Navigate to Col 1**:
   - Left 2 -> P(1, 2). M(1, 3).
2. **Vertical Separation**:
   - Down 14 -> P(1, 16).
   - M(1, 3) -> Up 14 -> Blocked at 1 -> M(1, 1).
   - State: P(1, 16), M(1, 1).
3. **Invert**:
   - Up 14 -> P(1, 2). M(1, 15).
   - State: P(1, 2), M(1, 15).

## Phase 2: The Ratchet (Col 26)
4. **Move to Col 26**:
   - Right 25 -> P(26, 2). M(26, 15).
5. **Ratchet M**:
   - Down 13 -> P(26, 15).
   - M(26, 15) -> Up 13 -> Blocked at 12 -> M(26, 12).
   - State: P(26, 15), M(26, 12).

## Phase 3: Finish (Col 22)
6. **Align**:
   - Left 4 -> P(22, 15). M(22, 12).
   - Up 2 -> P(22, 13). M(22, 14).
   - Interact.