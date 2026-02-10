# Team Rocket HQ - Murkrow Puzzle

## STRATEGY: "The Col 28 Inversion"
Target: M(22, 14).

## Current Status (Turn 36413)
- **Player**: (6, 2) -> Moving to (28, 2).
- **Murkrow**: (6, 2) (Synced).

## Step 1: Sync X at Col 28
- Move Right to P(28, 2). M(28, 2).
- (Col 28 is fully clear 1-16).

## Step 2: Vertical Separation
- Move Down 14 -> P(28, 16).
- M(28, 2) -> Up 14 -> Hits Wall at 0 -> M(28, 0). (Actually stops at 1).
- State: P(28, 16), M(28, 1).

## Step 3: Invert Positions
- Move Up 15 -> P(28, 1).
- M(28, 1) -> Down 15 -> M(28, 16). (Wait, is M clear? Yes).
- State: P(28, 1), M(28, 16). (Or 15, depending on boundary).

## Step 4: The Ratchet (Col 26)
- Left 2 -> P(26, 1), M(26, 16).
- Down 14 -> P(26, 15).
- M(26, 16) -> Up 14 -> Hits Wall at 11 -> M(26, 12).
- State: P(26, 15), M(26, 12).

## Step 5: Finish
- Left 4 -> P(22, 15), M(22, 12).
- Up 2 -> P(22, 13), M(22, 14).
- Interact.