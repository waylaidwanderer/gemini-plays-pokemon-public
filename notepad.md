# Team Rocket HQ - Murkrow Puzzle

## STRATEGY: "The Col 3 Swap & 26 Ratchet"
Target: P(22, 13), M(22, 14).

## Current Status (Turn 36418)
- **Player**: (1, 4) (Hit Wall).
- **Murkrow**: (1, 1).

## Phase 1: The Swap (Col 3)
1. **Navigate to Col 3**:
   - Up 2 -> P(1, 2). M(1, 1) [Blocked].
   - Right 2 -> P(3, 2). M(3, 1).
2. **Vertical Separation**:
   - Down 14 -> P(3, 16). M(3, 1) [Blocked Up].
   - State: P(3, 16), M(3, 1).
3. **Invert**:
   - Up 14 -> P(3, 2). M(3, 15).
   - State: P(3, 2), M(3, 15).

## Phase 2: The Ratchet (Col 26)
4. **Move to Col 26**:
   - Right 23 -> P(26, 2). M(26, 15).
5. **Ratchet M**:
   - Down 13 -> P(26, 15).
   - M(26, 15) -> Up 13 -> Blocked at 11 -> M(26, 12).
   - State: P(26, 15), M(26, 12).

## Phase 3: Finish (Col 22)
6. **Align**:
   - Left 4 -> P(22, 15). M(22, 12).
   - Up 2 -> P(22, 13). M(22, 14).
   - Interact.