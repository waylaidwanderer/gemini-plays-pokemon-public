# Game Corner Interior Empirical Testing Log

## Single-Stepping Tile Passability Protocol (Turn 51091)
- Current Position: (3, 7) facing Up in Celadon Game Corner.
- Goal: Systematically test tile passability 1 step at a time across Columns 3 through 9 to reach East Casino floor (x>=10).
- Rules: Never issue 'Down' while at y=7 (exit mat). Always verify tile passability before issuing multi-step macros.

## Verified Tile Log
- (3, 7) / (4, 7): Exit mats (warps outside if 'Down' is pressed).
- (3, 6) / (4, 6): Open carpet.
- (3, 5), (4, 5), (5, 5): Open carpet.
- (6, 5): Solid brown slot machine counter (bumped turn 51072).