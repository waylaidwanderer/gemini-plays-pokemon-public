# Team Rocket HQ - Murkrow Puzzle

## STATUS: EXECUTING "THE COL 26 RATCHET LOOP"
**Goal**: Sync X at 28, Invert Y, Ratchet at 26, Swap at 21.

## Current State (Turn 36495)
- **Player**: (27, 2).
- **Murkrow**: (7, 2).

## Step 1: Sync X (Col 28)
1. **Move Right 1**: P(28, 2). M(8, 2).
2. **Move Down 14**: P(28, 16). M(8, 16).
3. **Move Right 20**: P(28, 16). M(28, 16). (Sync X).
   - *Wait, P is at 28. P stays. M moves.*
   - P Bump Right x20. M moves 8->28.
   - **State**: P(28, 16), M(28, 16).

## Step 2: Invert Y (Col 28)
4. **Move Up 15**: P(28, 1). M(28, 1). (M hits top wall at 0).
   - Wait, M(28, 16) -> Up 15 -> M(28, 1).
   - Is (28, 1) clear? Yes.
   - **State**: P(28, 1), M(28, 1).
5. **Move Down 1**: P(28, 2). M(28, 0)?
   - P Down. M Up.
   - M(28, 1) -> Up -> M(28, 0).
   - (28, 0) is Wall. M stays 1.
   - **State**: P(28, 2), M(28, 1).
   - *This is not Inverted.*

   **Retry Invert**:
   - P(28, 16), M(28, 16).
   - P Up 1 -> P(28, 15). M Down 1 -> M(28, 17) (Wall). M stays 16.
   - P Up 13 -> P(28, 2). M Stays 16.
   - **State**: P(28, 2), M(28, 16).
   - *Perfect.*

## Step 3: Move to 26
6. **Left 2**: P(26, 2). M(26, 16).

## Step 4: Ratchet at 26
7. **Down 11**: P(26, 13).
   - M(26, 16) -> Up 11.
   - Path: 16->15->14->13->12->11(Block)->12...
   - M stops at 12.
   - **State**: P(26, 13), M(26, 12).

## Step 5: Finish
8. **Left 4**: P(22, 13). M(22, 12).
9. **Side-Step**:
   - Left 1 -> P(21, 13), M(21, 12).
   - Up 1 -> P(21, 12), M(21, 13).
   - Right 1 -> P(22, 12), M(22, 13).
10. **Interact**.