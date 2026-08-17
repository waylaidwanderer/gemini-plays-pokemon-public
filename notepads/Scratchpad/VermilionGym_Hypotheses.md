# Vermilion Gym - Trash Can Empirical Trial Log & Mechanics

## Root Cause Analysis (Verified Turn 2641)
- Multi-button sequences combining textbox dismissal (`B`) with movement and `A` resulted in dropped inputs (evidenced by consistent system warnings: 'You pressed 3 movement buttons, but visited 2 tiles').
- As a result, directional turns were misaligned and several cans were never actually interacted with.

## Strict Single-Action Verification Protocol
1. **Dismiss**: Press `B` alone to close textbox. Verify screen is clear of dialogue.
2. **Position**: Move to target tile in front of can. Verify coordinates on `<GameState>`.
3. **Inspect**: Face target can and press `A` alone. Verify resulting textbox text.
4. **Log**: Record exact outcome with turn number.

## Cumulative Sweep Log - Run #5 Verified Single-Action Checks
- (Position: (8, 11) facing Right at Turn 2641)
